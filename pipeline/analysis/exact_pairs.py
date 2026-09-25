"""Pair coverage and bounded examples from validated exact observations."""

from itertools import combinations

import polars as pl

from .cohorts import POWERS, comparison_cohorts

COHORT = ["horizon", "quality_group", "press_level"]


def summarize_pairs(
    observations: pl.DataFrame, min_games: int = 200, top_n: int = 5,
) -> tuple[pl.DataFrame, pl.DataFrame]:
    """Summarize all 21 pairs, retaining only top_n examples per pair/cohort.

    Input is the validated complete observation table from build_exact_data.
    Pattern counts are computed before truncation. No combination of three or
    more countries is materialized; the lookup handles those on demand.
    """
    if min_games < 2 or top_n < 1:
        raise ValueError("min_games must be at least 2 and top_n must be positive")
    keys = ["horizon", "game_id", "press_level", "quality_tier"]
    values = ["sequence_id", "solo", "draw_vote", "survived", "sos_score"]
    countries = {p: observations.filter(pl.col("power") == p).select(*keys, *values) for p in POWERS}
    summaries, examples = [], []
    for a, b in combinations(POWERS, 2):
        pair = countries[a].rename({c: f"{c}_a" for c in values}).join(
            countries[b].rename({c: f"{c}_b" for c in values}), on=keys, validate="1:1")
        cohorts = comparison_cohorts(pair)
        patterns = cohorts.group_by(*COHORT, "sequence_id_a", "sequence_id_b").agg(
            pl.len().alias("n_games"),
            *[expr for side in ("a", "b") for expr in (
                pl.col(f"solo_{side}").sum().alias(f"n_solos_{side}"),
                pl.col(f"draw_vote_{side}").sum().alias(f"n_draws_{side}"),
                pl.col(f"survived_{side}").sum().alias(f"n_survived_{side}"),
                pl.col(f"sos_score_{side}").mean().alias(f"mean_sos_{side}"),
            )],
        )
        coverage = patterns.group_by(*COHORT).agg(
            pl.col("n_games").sum().alias("cohort_games"), pl.len().alias("n_patterns"),
            (pl.col("n_games") == 1).sum().alias("singleton_patterns"),
            pl.col("n_games").filter(pl.col("n_games") > 1).sum().alias("games_in_repeated_patterns"),
            (pl.col("n_games") >= min_games).sum().alias("patterns_at_threshold"),
            pl.col("n_games").filter(pl.col("n_games") >= min_games).sum().alias("games_at_threshold"),
            pl.col("n_games").max().alias("max_matches"),
        ).with_columns(pl.lit(a).alias("power_a"), pl.lit(b).alias("power_b"),
                       pl.lit(min_games).alias("min_games"))
        top = patterns.sort([*COHORT, "n_games", "sequence_id_a", "sequence_id_b"],
            descending=[False, False, False, True, False, False]).group_by(*COHORT, maintain_order=True).head(top_n)
        top = top.with_columns(
            pl.lit(a).alias("power_a"), pl.lit(b).alias("power_b"),
            (pl.col("n_games") < min_games).alias("sparse"),
            *[pl.when(pl.col("n_games") > 1).then(pl.col(f"n_{event}_{side}") / pl.col("n_games")).alias(f"{rate}_rate_{side}")
              for side in ("a", "b") for event, rate in [("solos", "solo"), ("draws", "draw"), ("survived", "survival")]],
        )
        summaries.append(coverage)
        examples.append(top)
    return (
        pl.concat(summaries).sort(*COHORT, "power_a", "power_b"),
        pl.concat(examples).sort([*COHORT, "power_a", "power_b", "n_games", "sequence_id_a", "sequence_id_b"],
                               descending=[False] * 5 + [True, False, False]),
    )
