"""Run the offline score benchmark: python -m pipeline.score_benchmark."""

import argparse
import hashlib
import json
import platform
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

import polars as pl

from .analysis.artifacts import fingerprint, load_exact_snapshot
from .analysis.cohorts import POWERS, REPORT_PRESS_LEVELS
from .analysis.score_benchmark import STRENGTHS, assign_splits, run_experiment

OBSERVATIONS = "opening_exact_observations.parquet"
FAMILIES = {"own": "One country", "pairs": "Country pairs", "all": "All seven countries"}
HORIZONS = {"spring1901": "Spring 1901", "year1901": "Full 1901"}


def load_observations(data_dir: Path) -> tuple[pl.DataFrame, dict]:
    """Never scan the raw replay files."""
    manifest_bytes, manifest, (frame,) = load_exact_snapshot(data_dir, (OBSERVATIONS,))
    digest = next(item["sha256"] for item in manifest["outputs"] if item["name"] == OBSERVATIONS)
    required = ["game_id", "horizon", "power", "sequence_id", "joint_id", "quality_tier", "press_level", "sos_score"]
    frame = frame.select(required)
    if frame.is_empty() or sum(frame.null_count().row(0)):
        raise ValueError("Empty or null benchmark observations")
    if frame.select("game_id", "horizon", "power").is_duplicated().any():
        raise ValueError("Duplicate game/horizon/country observations")
    if (set(frame["power"].unique()) != set(POWERS) or set(frame["horizon"].unique()) != set(HORIZONS)
            or not set(frame["press_level"].unique()) <= set(REPORT_PRESS_LEVELS)
            or not set(frame["quality_tier"].unique()) <= {1, 2, 3}
            or not frame.select((pl.col("sos_score").is_finite() & pl.col("sos_score").is_between(0, 1)).all()).item()):
        raise ValueError("Unexpected cohort, country, horizon or score")
    games = frame.group_by("game_id", "horizon").agg(pl.len().alias("n"), pl.col("sos_score").sum().alias("score"))
    if games.filter((pl.col("n") != 7) | ((pl.col("score") - 1).abs() > 1e-9)).height:
        raise ValueError("Games must contain seven countries with scores summing to one")
    if frame.group_by("game_id").agg(pl.col("quality_tier").n_unique().alias("quality"),
            pl.col("press_level").n_unique().alias("press"), pl.len().alias("n")).filter(
                (pl.col("quality") != 1) | (pl.col("press") != 1) | (pl.col("n") != 14)).height:
        raise ValueError("Game metadata or horizon coverage is inconsistent")
    return frame, {"observations_sha256": digest, "exact_manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
                   "exact_built_at": manifest["built_at_utc"], "n_games": frame["game_id"].n_unique()}


def render_report(results: list[dict], seed: int) -> str:
    def value(metric, field="rmse"):
        return "—" if metric is None else f"{metric[field]:.4f}"

    def improvement(test):
        baseline = test["all"]["baseline"]["mse"]
        return f"{100 * (1 - test['all']['shrinkage']['mse'] / baseline):+.2f}%" if baseline else "—"

    def interval(comparison):
        if comparison["difference"] is None:
            return "—"
        bounds = "unavailable" if comparison["ci_low"] is None else f"{comparison['ci_low']:+.6f}, {comparison['ci_high']:+.6f}"
        return f"{comparison['difference']:+.6f} [{bounds}]"

    lines = ["# Expected-score benchmark",
        "Offline experiment. The explorer shows exact historical results by default; its optional estimated-score toggle uses the own-country models evaluated here.",
        f"Split seed: {seed}. Whole games are assigned once to approximately 70% training, 15% validation and 15% test. "
        "The same split applies to every country, horizon and quality cohort. Strength is selected on validation MSE, "
        "then models are refit on training + validation before scoring the held-out test games.",
        "All press settings are pooled. Tier 1 is the primary analysis; Tiers 1–3 is an overlapping sensitivity analysis. "
        "One-country contexts use that country's complete order set. Pair contexts cover all 21 pairs and predict both members. "
        "All-country contexts require all seven histories. Full 1901 estimates use only 1901 orders, but are not Spring forecasts.",
        "Baseline = the country's mean final score in fitting games. Exact = mean among fitting games with the same orders. "
        "Shrinkage = (matching score sum + k × baseline) / (match count + k). "
        "Unseen orders use the baseline only for shrinkage; raw exact estimates are unavailable. "
        "The baseline includes the matched fitting games, making this a simple regularized estimator rather than a full Bayesian model.",
        f"Validation grid: {', '.join(map(str, STRENGTHS))}. The baseline candidate ignores orders. "
        "Ties prefer greater shrinkage. k = 0 uses raw exact means where available and the baseline elsewhere.",
        "Errors use final scores on the 0–1 scale. Lower RMSE is better; MSE reduction is relative to the country baseline. "
        "Coverage is the share of test country/context cases with at least one exact match in training + validation. "
        "All-case metrics weight games equally. Matched/support subsets weight retained country/context cases equally, "
        "so games may contribute different numbers of cases. Pair cases are correlated, not additional independent games."]
    for quality, heading in (("tier_1", "Primary: Tier 1"), ("tiers_1_3", "Sensitivity: Tiers 1–3")):
        subset = [row for row in results if row["quality_group"] == quality]
        counts = subset[0]["split_games"]
        lines += [f"## {heading}", f"Games: {counts['train']:,} training, {counts['validation']:,} validation, {counts['test']:,} test.",
            "### All test cases", "Raw exact estimates abstain on unseen histories; the next table compares all three methods on the same matched subset.",
            "| Window | Context | Exact coverage | Selected k | Baseline RMSE | Shrinkage RMSE | MSE reduction |",
            "|---|---|---:|---:|---:|---:|---:|"]
        for row in subset:
            test = row["test"]
            lines.append(f"| {HORIZONS[row['horizon']]} | {FAMILIES[row['family']]} | {test['exact_coverage']:.1%} | {row['strength']} | "
                         f"{value(test['all']['baseline'])} | {value(test['all']['shrinkage'])} | {improvement(test)} |")
        lines += ["### Identical subset: exact matches available", "These errors must not be compared directly with the full-test errors above; the case mix differs.",
            "| Window | Context | Cases | Baseline RMSE | Exact RMSE | Shrinkage RMSE |", "|---|---|---:|---:|---:|---:|"]
        for row in subset:
            matched = row["test"]["matched"]
            lines.append(f"| {HORIZONS[row['horizon']]} | {FAMILIES[row['family']]} | {matched['n_cases']:,} | "
                         f"{value(matched['baseline'])} | {value(matched['exact'])} | {value(matched['shrinkage'])} |")
        lines += ["### Paired MSE differences", "Negative favors shrinkage. Brackets are approximate pointwise 95% intervals clustered by game, not by country/context case. "
                  "They are not adjusted for multiple comparisons and do not account for repeated players or dataset selection.",
            "| Window | Context | Shrinkage − baseline, all cases | Shrinkage − exact, matched cases |", "|---|---|---|---|"]
        for row in subset:
            comparisons = row["test"]["paired_mse"]
            lines.append(f"| {HORIZONS[row['horizon']]} | {FAMILIES[row['family']]} | {interval(comparisons['shrinkage_vs_baseline_all'])} | "
                         f"{interval(comparisons['shrinkage_vs_exact_matched'])} |")
    lines += ["## Interpretation limits",
        "This measures generalization within the same historical snapshot, not future-platform performance. "
        "The dataset has no usable player identities or original game dates for player-disjoint or chronological validation. "
        "Only games with detectable endings are included. Strength selection and these intervals do not remove that selection bias.",
        "The benchmark covers complete own, pair and all-country histories. It does not establish accuracy for arbitrary partial-turn combinations, "
        "individual orders, third countries outside a selected pair, or other press/quality filters. "
        "Selected simultaneous orders are treated as known; this is not a model of opponents' unknown choices. "
        "A lower prediction error does not establish that changing an order causes a higher score or that a move-ranking policy works.",
        "results.json includes validation curves, MAE, per-country results and support-count breakdowns. "
        "split_assignments.parquet preserves every game's split; manifest.json records source/input hashes, configuration and timings."]
    report = lines[0]
    for previous, line in zip(lines, lines[1:]):
        report += ("\n" if previous.startswith("|") and line.startswith("|") else "\n\n") + line
    return report + "\n"


def run(data_dir: Path, output_dir: Path, seed: int = 1901) -> dict:
    start = perf_counter()
    observations, provenance = load_observations(data_dir)
    splits = assign_splits(observations, seed)
    results = []
    for quality in ("tier_1", "tiers_1_3"):
        for horizon in HORIZONS:
            cohort = observations.filter(pl.col("horizon") == horizon)
            if quality == "tier_1":
                cohort = cohort.filter(pl.col("quality_tier") == 1)
            for family in FAMILIES:
                result = {"quality_group": quality, "horizon": horizon, "family": family,
                          **run_experiment(cohort, splits, family)}
                results.append(result)
                print(f"Evaluated {quality}, {horizon}, {family}", flush=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".score-benchmark-", dir=output_dir) as tmp:
        stage = Path(tmp)
        (stage / "results.json").write_text(json.dumps(results, indent=2, allow_nan=False) + "\n")
        (stage / "report.md").write_text(render_report(results, seed))
        splits.write_parquet(stage / "split_assignments.parquet", compression="zstd")
        names = ["results.json", "report.md", "split_assignments.parquet"]
        manifest = {"schema_version": 1, "built_at_utc": datetime.now(timezone.utc).isoformat(),
            "input": provenance, "config": {"seed": seed, "split": [0.70, 0.15, 0.15], "strength_grid": STRENGTHS,
                "families": list(FAMILIES), "horizons": list(HORIZONS), "press_level": "all", "quality_groups": ["tier_1", "tiers_1_3"],
                "selection_metric": "validation_mse", "refit": "train_plus_validation", "test_evaluations_per_model": 1},
            "python_version": platform.python_version(), "polars_version": pl.__version__,
            "sources": [fingerprint(Path(__file__)), fingerprint(Path(__file__).parent / "analysis" / "score_benchmark.py")],
            "outputs": [fingerprint(stage / name) for name in names], "elapsed_seconds": round(perf_counter() - start, 3)}
        (stage / "manifest.json").write_text(json.dumps(manifest, indent=2, allow_nan=False) + "\n")
        for name in [*names, "manifest.json"]:
            (stage / name).replace(output_dir / name)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path("data/processed"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/processed/score_benchmark"))
    parser.add_argument("--seed", type=int, default=1901)
    args = parser.parse_args()
    manifest = run(args.data_dir, args.output_dir, args.seed)
    print(f"Report: {args.output_dir / 'report.md'} ({manifest['elapsed_seconds']:.2f}s)")


if __name__ == "__main__":
    main()
