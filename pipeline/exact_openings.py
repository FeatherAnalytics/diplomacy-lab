"""Build or query exact Spring/full-1901 histories. No generalized estimates."""

import argparse
import json
import platform
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

import polars as pl

from .analysis.artifacts import fingerprint, load_exact_snapshot, require_unchanged
from .analysis.exact_data import build_exact_data
from .analysis.exact_query import lookup_exact
from .analysis.exact_report import render_exact_report
from .analysis.exact_pairs import summarize_pairs
from .analysis.exact_pair_report import render_pair_report
from .analysis.opening_data import build_observations
from .analysis.opening_stats import summarize_openings

MANIFEST = "opening_exact_manifest.json"
OBSERVATIONS = "opening_exact_observations.parquet"


def own_rate_table(observations: pl.DataFrame, min_games: int) -> pl.DataFrame:
    rate_frames = []
    for horizon in ("spring1901", "year1901"):
        group = observations.filter(pl.col("horizon") == horizon).drop("joint_id", "horizon").rename({"sequence_id": "opening_id"})
        rate_frames.append(summarize_openings(group, min_games).rename({"opening_id": "sequence_id"}).with_columns(pl.lit(horizon).alias("horizon")))
    return pl.concat(rate_frames).with_columns(
        # Recover the integer event counts before suppressing singleton fractions.
        (pl.col("draw_rate") * pl.col("n_games")).round().cast(pl.UInt32).alias("n_draws"),
        (pl.col("survival_rate") * pl.col("n_games")).round().cast(pl.UInt32).alias("n_survived"),
    ).with_columns(
        *[pl.when(pl.col("n_games") > 1).then(pl.col(column)).alias(column)
          for column in ("solo_rate", "draw_rate", "survival_rate", "solo_ci_low", "solo_ci_high")],
        pl.when(pl.col("cohort_games") > 1).then(pl.col("baseline_solo_rate")).alias("baseline_solo_rate"),
    ).sort("horizon", "quality_group", "press_level", "power", "sequence_id")


def publish(output_dir: Path, tables: dict[str, pl.DataFrame], reports: dict[str, str], manifest: dict) -> None:
    """Stage every output, then replace them with the manifest last as the completion marker."""
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".exact-openings-", dir=output_dir) as tmp:
        stage = Path(tmp)
        for name, table in tables.items():
            table.write_parquet(stage / name, compression="zstd", row_group_size=8192)
        for name, text in reports.items():
            (stage / name).write_text(text, encoding="utf-8")
        names = [*tables, *reports]
        manifest["outputs"] = [fingerprint(stage / name) for name in names]
        (stage / MANIFEST).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        for name in [*names, MANIFEST]:
            (stage / name).replace(output_dir / name)


def build(data_dir: Path, output_dir: Path, min_games: int = 200, top_n: int = 5) -> dict:
    if min_games < 2 or top_n < 1:
        raise ValueError("min_games must be at least 2 and top_n must be positive")
    start = perf_counter()
    paths = [data_dir / name for name in ("games.parquet", "phases.parquet", "game_outcomes.parquet")]
    inputs = [fingerprint(path) for path in paths]
    spring, counts = build_observations(*(pl.scan_parquet(path) for path in paths))
    observations, sequences, profiles = build_exact_data(spring, pl.scan_parquet(paths[1]))
    extract_seconds = perf_counter() - start
    own_rates = own_rate_table(observations, min_games)
    report = render_exact_report(observations, sequences, profiles, own_rates, top_n)
    pair_start = perf_counter()
    pair_coverage, pair_examples = summarize_pairs(observations, min_games, top_n)
    pair_report = render_pair_report(pair_coverage, pair_examples, sequences)
    pair_seconds = perf_counter() - pair_start
    require_unchanged(paths, inputs)
    tables = {
        OBSERVATIONS: observations,
        "opening_exact_sequences.parquet": sequences,
        "opening_exact_profiles.parquet": profiles,
        "opening_exact_own_rates.parquet": own_rates,
        "opening_exact_pair_coverage.parquet": pair_coverage,
        "opening_exact_pair_examples.parquet": pair_examples,
    }
    manifest = {
        "schema_version": 1,
        "built_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(), "polars_version": pl.__version__,
        "config": {"matching": "exact_only", "min_games": min_games, "top_n": top_n},
        "counts": {**counts, "exact_observations": observations.height,
                   "sequence_patterns": sequences.height, "joint_profiles": profiles.height,
                   "own_rate_rows": own_rates.height, "pair_coverage_rows": pair_coverage.height,
                   "pair_example_rows": pair_examples.height},
        "inputs": inputs,
        "sources": [fingerprint(path) for path in [Path(__file__), *sorted((Path(__file__).parent / "analysis").glob("*.py"))]],
        "outputs": None,
        "schemas": {name: {column: str(dtype) for column, dtype in table.schema.items()} for name, table in tables.items()},
        "timings_seconds": {"extract_with_fingerprints": round(extract_seconds, 4),
                            "pair_summary_and_report": round(pair_seconds, 4),
                            "total_before_publish": round(perf_counter() - start, 4)},
    }
    publish(output_dir, tables, {"opening_exact.md": report, "opening_exact_pairs.md": pair_report}, manifest)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    builder = commands.add_parser("build")
    builder.add_argument("--data-dir", type=Path, default=Path("data/processed"))
    builder.add_argument("--output-dir", type=Path, default=Path("data/processed"))
    builder.add_argument("--min-games", type=int, default=200)
    builder.add_argument("--top-n", type=int, default=5)
    query = commands.add_parser("lookup")
    query.add_argument("--data-dir", type=Path, default=Path("data/processed"))
    query.add_argument("--horizon", choices=["spring1901", "year1901"], required=True)
    query.add_argument("--context", choices=["own", "all", "selected"], required=True)
    query.add_argument("--pattern-id")
    query.add_argument("--select", action="append", default=[], metavar="COUNTRY=SEQUENCE_ID",
                       help="Repeat for each country whose orders must match (selected context only)")
    query.add_argument("--power")
    query.add_argument("--press-level", default="all")
    query.add_argument("--quality-group", default="tiers_1_3")
    query.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    if args.command == "build":
        manifest = build(args.data_dir, args.output_dir, args.min_games, args.top_n)
        print(json.dumps({"counts": manifest["counts"], "timings_seconds": manifest["timings_seconds"]}, indent=2))
    else:
        selections = {}
        for selection in args.select:
            country, separator, sequence = selection.partition("=")
            if not separator or not country or not sequence:
                parser.error("--select requires COUNTRY=SEQUENCE_ID")
            if country in selections:
                parser.error(f"Duplicate country selection: {country}")
            selections[country] = sequence
        _, _, (observations,) = load_exact_snapshot(args.data_dir, (OBSERVATIONS,))
        try:
            result = lookup_exact(observations.lazy(), horizon=args.horizon, context=args.context,
                                  selections=selections or None, pattern_id=args.pattern_id, power=args.power,
                                  press_level=args.press_level, quality_group=args.quality_group, limit=args.limit)
        except ValueError as error:
            parser.error(str(error))
        print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
