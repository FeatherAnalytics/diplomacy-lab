"""Shared source selection for analyses requiring detectable endings."""

import polars as pl

REPORT_PRESS_LEVELS = ("no_press", "press_with_msgs", "public_press")
POWERS = ("austria", "england", "france", "germany", "italy", "russia", "turkey")


def outcome_cohort() -> pl.Expr:
    """Apply to games.parquet; retain the existing in_scope definition."""
    return pl.col("in_scope") & pl.col("press_level").is_in(REPORT_PRESS_LEVELS)


def comparison_cohorts(observations: pl.DataFrame) -> pl.DataFrame:
    """Expand validated observations into overlapping press and quality cohorts."""
    tiers = pl.concat([
        observations.with_columns(pl.lit("tiers_1_3").alias("quality_group")),
        observations.filter(pl.col("quality_tier") == 1).with_columns(pl.lit("tier_1").alias("quality_group")),
    ])
    return pl.concat([tiers, tiers.with_columns(pl.lit("all").alias("press_level"))])
