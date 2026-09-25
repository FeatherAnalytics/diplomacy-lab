"""Offline score estimators and game-grouped evaluation; no serving dependencies."""

import hashlib
import math
from itertools import combinations
from typing import Iterator, Literal

import polars as pl

Strength = int | Literal["baseline"]
STRENGTHS: tuple[Strength, ...] = (0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, "baseline")


def assign_splits(observations: pl.DataFrame, seed: int = 1901) -> pl.DataFrame:
    """Stable 70/15/15 split by game ID, shared by every country and horizon."""
    rows = []
    for game in sorted(observations["game_id"].unique()):
        fraction = int.from_bytes(hashlib.sha256(f"{seed}\0{game}".encode()).digest()[:8], "big") / 2**64
        rows.append((game, "train" if fraction < .70 else "validation" if fraction < .85 else "test"))
    return pl.DataFrame(rows, schema=["game_id", "split"], orient="row")


def context_frames(frame: pl.DataFrame, family: str) -> Iterator[pl.DataFrame]:
    """Yield one context at a time, avoiding a persistent sixfold pair expansion."""
    if family in ("own", "all"):
        column = "sequence_id" if family == "own" else "joint_id"
        yield frame.with_columns(pl.col(column).alias("pattern"), pl.lit(family).alias("context"))
    elif family == "pairs":
        wide = frame.pivot(on="power", index="game_id", values="sequence_id")
        for a, b in combinations(sorted(frame["power"].unique()), 2):
            patterns = wide.select("game_id", pl.concat_str(a, b, separator=":").alias("pattern"))
            yield frame.filter(pl.col("power").is_in([a, b])).join(patterns, on="game_id", validate="m:1").with_columns(
                pl.lit(f"{a}+{b}").alias("context"))
    else:
        raise ValueError(f"Unknown context family: {family}")


def attach_estimates(training: pl.DataFrame, target: pl.DataFrame) -> pl.DataFrame:
    """Fit solely on training rows; unseen exact patterns have no exact estimate."""
    if training["game_id"].is_in(target["game_id"].implode()).any():
        raise ValueError("Training and target games overlap")
    baseline = training.group_by("power").agg(pl.col("sos_score").mean().alias("baseline"))
    groups = training.group_by("power", "pattern").agg(
        pl.len().alias("support"), pl.col("sos_score").sum().alias("score_sum"),
        pl.col("sos_score").mean().alias("exact"))
    result = target.join(baseline, on="power", how="left", validate="m:1").join(
        groups, on=["power", "pattern"], how="left", validate="m:1").with_columns(
            pl.col("support").fill_null(0), pl.col("score_sum").fill_null(0.))
    if result["baseline"].null_count():
        raise ValueError("A target country has no training baseline")
    return result


def predict(strength: Strength) -> pl.Expr:
    if strength == "baseline":
        return pl.col("baseline")
    if strength < 0:
        raise ValueError("Shrinkage strength must be nonnegative")
    return pl.when(pl.col("support") > 0).then(
        (pl.col("score_sum") + strength * pl.col("baseline")) / (pl.col("support") + strength)
    ).otherwise(pl.col("baseline"))


def choose_strength(validation_frames: list[pl.DataFrame]) -> tuple[Strength, list[dict]]:
    n = sum(frame.height for frame in validation_frames)
    if not n:
        raise ValueError("No validation cases")
    errors = {str(k): 0. for k in STRENGTHS}
    for frame in validation_frames:
        sums = frame.select([(predict(k) - pl.col("sos_score")).pow(2).sum().alias(str(k)) for k in STRENGTHS]).row(0, named=True)
        for key, value in sums.items():
            errors[key] += value
    curve = [{"strength": k, "mse": errors[str(k)] / n} for k in STRENGTHS]
    best = min(row["mse"] for row in curve)
    # Conservative tie break, including the no-exact-matches case.
    chosen = [row["strength"] for row in curve if row["mse"] <= best + 1e-12][-1]
    return chosen, curve


def metrics(frame: pl.DataFrame) -> dict:
    result = {"n_cases": frame.height, "n_games": frame["game_id"].n_unique()}
    for name in ("baseline", "exact", "shrinkage"):
        if frame.is_empty() or frame[name].null_count():
            result[name] = None
        else:
            error = pl.col(name) - pl.col("sos_score")
            mse, mae = frame.select(error.pow(2).mean().alias("mse"), error.abs().mean().alias("mae")).row(0)
            result[name] = {"mse": mse, "rmse": math.sqrt(mse), "mae": mae}
    return result


def paired_mse(frame: pl.DataFrame, reference: str) -> dict:
    """Paired loss difference with a game-clustered, approximate 95% interval."""
    if frame.is_empty():
        return {"difference": None, "ci_low": None, "ci_high": None, "n_games": 0}
    delta = (pl.col("shrinkage") - pl.col("sos_score")).pow(2) - (pl.col(reference) - pl.col("sos_score")).pow(2)
    games = frame.group_by("game_id").agg(delta.sum().alias("delta_sum"), pl.len().alias("cases"))
    difference = games["delta_sum"].sum() / frame.height
    radius = None
    if games.height > 1:
        residual_sum = games.select((pl.col("delta_sum") - difference * pl.col("cases")).pow(2).sum()).item()
        radius = 1.96 * math.sqrt(games.height / (games.height - 1) * residual_sum) / frame.height
    return {"difference": difference, "ci_low": difference - radius if radius is not None else None,
            "ci_high": difference + radius if radius is not None else None, "n_games": games.height}


def evaluate(frame: pl.DataFrame) -> dict:
    matched = frame.filter(pl.col("support") > 0)
    buckets = frame.with_columns(pl.when(pl.col("support") == 0).then(pl.lit("0"))
        .when(pl.col("support") == 1).then(pl.lit("1"))
        .when(pl.col("support") < 10).then(pl.lit("2–9"))
        .when(pl.col("support") < 50).then(pl.lit("10–49"))
        .when(pl.col("support") < 200).then(pl.lit("50–199"))
        .otherwise(pl.lit("200+")).alias("bucket"))
    return {
        "exact_coverage": matched.height / frame.height if frame.height else None,
        "all": metrics(frame), "matched": metrics(matched),
        "by_support": {key: metrics(buckets.filter(pl.col("bucket") == key)) for key in ("0", "1", "2–9", "10–49", "50–199", "200+")},
        "by_power": {power: metrics(frame.filter(pl.col("power") == power)) for power in sorted(frame["power"].unique())},
        "paired_mse": {
            "shrinkage_vs_baseline_all": paired_mse(frame, "baseline"),
            "shrinkage_vs_exact_matched": paired_mse(matched, "exact"),
        },
    }


def run_experiment(observations: pl.DataFrame, splits: pl.DataFrame, family: str) -> dict:
    frame = observations.join(splits, on="game_id", how="left", validate="m:1")
    if frame["split"].null_count() or set(frame["split"].unique()) != {"train", "validation", "test"}:
        raise ValueError("Experiment requires nonempty train, validation and test splits")
    validation = []
    for context in context_frames(frame, family):
        validation.append(attach_estimates(context.filter(pl.col("split") == "train"),
                                           context.filter(pl.col("split") == "validation")))
    strength, curve = choose_strength(validation)
    del validation
    predictions = []
    for context in context_frames(frame, family):
        estimates = attach_estimates(context.filter(pl.col("split") != "test"), context.filter(pl.col("split") == "test"))
        predictions.append(estimates.with_columns(predict(strength).alias("shrinkage")).select(
            "game_id", "power", "context", "sos_score", "support", "baseline", "exact", "shrinkage"))
    return {"strength": strength, "validation": curve,
            "split_games": {part: frame.filter(pl.col("split") == part)["game_id"].n_unique() for part in ("train", "validation", "test")},
            "fit_games": frame.filter(pl.col("split") != "test")["game_id"].n_unique(),
            "test": evaluate(pl.concat(predictions))}
