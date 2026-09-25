"""Vectorized opening aggregates and analytic uncertainty, without presentation."""

import polars as pl

from .cohorts import comparison_cohorts

Z_95 = 1.959963984540054
GROUP = ["quality_group", "press_level", "power"]


def summarize_openings(observations: pl.DataFrame, min_games: int = 200) -> pl.DataFrame:
    """Aggregate each press mode plus pooled data, for tiers 1-3 and tier 1.

    Mean-score intervals use the normal approximation to the sample mean, clipped
    to [0,1]. They are null for singleton/zero-variance samples, where that method
    cannot estimate uncertainty. Solo-rate intervals use Wilson's formula, which
    remains non-degenerate at zero wins. Both are pointwise, not simultaneous.
    """
    if min_games < 2:
        raise ValueError("min_games must be at least 2")
    if observations.is_empty():
        raise ValueError("No opening observations")
    cohorts = comparison_cohorts(observations)
    stats = cohorts.group_by(*GROUP, "opening_id").agg(
        *([pl.col("orders").first()] if "orders" in observations.columns else []),
        pl.len().alias("n_games"),
        pl.col("solo").sum().alias("n_solos"),
        pl.col("solo").mean().alias("solo_rate"),
        pl.col("survived").mean().alias("survival_rate"),
        pl.col("draw_vote").mean().alias("draw_rate"),
        pl.col("sos_score").mean().alias("mean_sos"),
        pl.col("sos_score").std(ddof=1).alias("sos_std"),
    )
    baseline = cohorts.group_by(GROUP).agg(
        pl.len().alias("cohort_games"),
        pl.col("sos_score").mean().alias("baseline_mean_sos"),
        pl.col("solo").mean().alias("baseline_solo_rate"),
    )
    stats = stats.join(baseline, on=GROUP, validate="m:1").with_columns(
        (pl.col("n_games") / pl.col("cohort_games")).alias("frequency"),
        (pl.col("mean_sos") - pl.col("baseline_mean_sos")).alias("sos_lift"),
        (pl.col("sos_std") / pl.col("n_games").sqrt()).alias("sos_se"),
        (pl.col("n_games") < min_games).alias("sparse"),
    )
    # Convert n before squaring: UInt32 overflows beyond 65,535 observations.
    # Current cohorts are smaller; retain this contract for larger future corpora.
    n, p = pl.col("n_games").cast(pl.Float64), pl.col("solo_rate")
    denominator = 1 + Z_95**2 / n
    center = (p + Z_95**2 / (2 * n)) / denominator
    radius = Z_95 * (p * (1 - p) / n + Z_95**2 / (4 * n**2)).sqrt() / denominator
    estimable = (pl.col("n_games") > 1) & (pl.col("sos_std") > 0)
    return stats.with_columns(
        pl.when(estimable).then((pl.col("mean_sos") - Z_95 * pl.col("sos_se")).clip(0, 1)).alias("sos_ci_low"),
        pl.when(estimable).then((pl.col("mean_sos") + Z_95 * pl.col("sos_se")).clip(0, 1)).alias("sos_ci_high"),
        (center - radius).clip(0, 1).alias("solo_ci_low"),
        (center + radius).clip(0, 1).alias("solo_ci_high"),
    ).drop("sos_std").sort(*GROUP, "n_games", "opening_id", descending=[False, False, False, True, False])
