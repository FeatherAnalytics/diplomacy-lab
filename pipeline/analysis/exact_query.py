"""Exact historical lookup. No smoothing, similarity search, or fallback model."""

from collections.abc import Mapping
from dataclasses import dataclass

import polars as pl

from .cohorts import POWERS, REPORT_PRESS_LEVELS

HORIZONS = ("spring1901", "year1901")
QUALITY_GROUPS = ("tiers_1_3", "tier_1")
LOOKUP_CHOICES = {
    "horizon": HORIZONS, "context": ("own", "all", "selected"), "power": (None, *POWERS),
    "press_level": (*REPORT_PRESS_LEVELS, "all"), "quality_group": QUALITY_GROUPS,
}


def filter_cohort(observations: pl.LazyFrame, horizon: str, press_level: str, quality_group: str) -> pl.LazyFrame:
    cohort = observations.filter(pl.col("horizon") == horizon)
    if press_level != "all":
        cohort = cohort.filter(pl.col("press_level") == press_level)
    if quality_group == "tier_1":
        cohort = cohort.filter(pl.col("quality_tier") == 1)
    return cohort


def match_selections(observations: pl.LazyFrame, selections: Mapping[str, str]) -> pl.LazyFrame:
    """Intersect validated country constraints within games in one filtered horizon."""
    if not selections:
        return observations
    requested = pl.DataFrame({"power": list(selections), "sequence_id": list(selections.values())}).lazy()
    games = observations.join(requested, on=["power", "sequence_id"], how="semi").group_by("game_id").agg(
        pl.col("power").n_unique().alias("matched_countries")
    ).filter(pl.col("matched_countries") == len(selections)).select("game_id")
    return observations.join(games, on="game_id", how="semi")


@dataclass
class ExactLookup:
    horizon: str
    context: str
    pattern_id: str | None = None
    selections: Mapping[str, str] | None = None
    power: str | None = None
    press_level: str = "all"
    quality_group: str = "tiers_1_3"
    limit: int = 10

    def __post_init__(self) -> None:
        for name, allowed in LOOKUP_CHOICES.items():
            if getattr(self, name) not in allowed:
                raise ValueError(f"Unsupported {name}")
        if self.limit < 1:
            raise ValueError("limit must be positive")
        if self.context == "own" and self.power is None:
            raise ValueError("Own-country lookup requires power")
        if self.context == "selected":
            self._normalize_selections()
        elif self.selections is not None or not self.pattern_id:
            raise ValueError("Own/all context requires pattern_id and no selections")

    def _normalize_selections(self) -> None:
        if self.pattern_id is not None or not self.selections:
            raise ValueError("Selected context requires country selections and no pattern_id")
        if not all(p in POWERS and isinstance(s, str) and s.strip() for p, s in self.selections.items()):
            raise ValueError("Selections require known countries and nonempty sequence IDs")
        self.selections = dict(sorted(self.selections.items()))

    def describe(self) -> dict:
        described = {"horizon": self.horizon, "context": self.context, "pattern_id": self.pattern_id,
                     "power": self.power, "press_level": self.press_level, "quality_group": self.quality_group}
        return described | ({"selections": self.selections} if self.context == "selected" else {})


def lookup_exact(observations: pl.LazyFrame, **options) -> dict:
    """Return counts/outcomes and a bounded list of matching game IDs; options are ExactLookup fields.

    A singleton exposes its observed counts/score, with rate fields null. Zero
    matches return an explicit empty result, never a zero win probability.
    """
    lookup = ExactLookup(**options)
    query = filter_cohort(observations, lookup.horizon, lookup.press_level, lookup.quality_group)
    if lookup.context == "selected":
        # Find games satisfying EVERY country/sequence constraint before filtering
        # the outcome country. The latter may be outside the selected countries.
        query = match_selections(query, lookup.selections)
    else:
        pattern_column = "sequence_id" if lookup.context == "own" else "joint_id"
        query = query.filter(pl.col(pattern_column) == lookup.pattern_id)
    if lookup.power:
        query = query.filter(pl.col("power") == lookup.power)
    matches = query.select("game_id", "power", "solo", "survived", "draw_vote", "sos_score").collect()
    return {**summarize_matches(matches, lookup.limit), "query": lookup.describe()}


def summarize_matches(matches: pl.DataFrame, limit: int = 10) -> dict:
    """Observed outcomes for validated game/power rows; limit only the game list."""
    n_matches = matches["game_id"].n_unique()
    outcomes = matches.group_by("power").agg(
        pl.len().alias("n_games"), pl.col("solo").sum().alias("n_solos"),
        pl.col("draw_vote").sum().alias("n_draws"), pl.col("survived").sum().alias("n_survived"),
        pl.col("sos_score").mean().alias("mean_sos"),
    ).with_columns(
        pl.when(pl.col("n_games") > 1).then(pl.col("n_solos") / pl.col("n_games")).alias("observed_solo_rate"),
        pl.when(pl.col("n_games") > 1).then(pl.col("n_draws") / pl.col("n_games")).alias("observed_draw_rate"),
    ).sort("power")
    return {
        "status": "no_exact_matches" if n_matches == 0 else "single_historical_game" if n_matches == 1 else "exact_matches",
        "n_matches": n_matches,
        "game_ids": matches["game_id"].unique().sort().head(limit).to_list(),
        "game_ids_truncated": n_matches > limit,
        "outcomes": outcomes.to_dicts(),
    }
