"""Extract and validate compact, reusable game/power opening observations."""

import hashlib
import json

import polars as pl

from .cohorts import POWERS, outcome_cohort

KEY = ["game_id", "power"]


def opening_id(power: str, orders: list[str]) -> str:
    """Stable identity v1: lowercase power + sorted exact orders, including coasts."""
    payload = json.dumps([power.lower(), sorted(orders)], separators=(",", ":"))
    return "o1_" + hashlib.sha256(payload.encode("utf-8")).hexdigest()


def require_unique(df: pl.DataFrame, keys: list[str], label: str) -> None:
    if df.select(pl.any_horizontal(pl.col(keys).is_null()).any()).item():
        raise ValueError(f"{label}: null key in {keys}")
    if df.select(pl.struct(keys).n_unique()).item() != df.height:
        raise ValueError(f"{label}: duplicate key in {keys}")


def build_observations(
    games: pl.LazyFrame, phases: pl.LazyFrame, outcomes: pl.LazyFrame,
) -> tuple[pl.DataFrame, dict[str, int]]:
    """Push selection into Parquet scans; materialize only the opening cohort.

    Missing/duplicate power rows and inconsistent metadata fail loudly. Non-S1901M
    starts are the only additional game exclusion, and are counted explicitly.
    Orders are checked for completeness and unique unit origins, not adjudicated
    for legality: failed moves and supports remain legitimate opening observations.
    """
    cohort = games.filter(outcome_cohort()).select(
        "game_id", "press_level", "quality_tier", "first_phase",
    ).collect()
    require_unique(cohort, ["game_id"], "games")
    if cohort.select(pl.any_horizontal(pl.all().is_null()).any()).item():
        raise ValueError("games: null cohort metadata")
    if not cohort["quality_tier"].is_in([1, 2, 3]).all():
        raise ValueError("games: in_scope contains an invalid quality tier")
    admitted = cohort.filter(pl.col("first_phase") == "S1901M").drop("first_phase")
    if admitted.is_empty():
        raise ValueError("No eligible S1901M games")
    ids = admitted.lazy().select("game_id")
    first = (
        phases.filter(pl.col("phase_idx") == 0)
        .join(ids, on="game_id", how="semi")
        .select("game_id", pl.col("power").str.to_lowercase(), "phase_name",
                "adjudicated", "orders", "units", "n_orders")
        .collect()
    )
    scores = (
        outcomes.join(ids, on="game_id", how="semi")
        .select("game_id", pl.col("power").str.to_lowercase(), "press_level",
                "quality_tier", "solo", "survived", "draw_vote", "sos_score")
        .collect()
    )
    for label, frame in [("phases", first), ("outcomes", scores)]:
        require_unique(frame, KEY, label)
        if frame.height != admitted.height * len(POWERS) or not frame["power"].is_in(POWERS).all():
            raise ValueError(f"{label}: expected exactly seven powers per admitted game")
        if frame.select(pl.any_horizontal(pl.all().is_null()).any()).item():
            raise ValueError(f"{label}: null required value")
    if not first.select(((pl.col("phase_name") == "S1901M") & pl.col("adjudicated")).all()).item():
        raise ValueError("phases: first phase must be adjudicated S1901M")

    checked = first.with_columns(
        pl.col("orders").list.eval(
            pl.element().str.extract(r"^([AF] [A-Z]{3}(?:/[NSEW]C)?) (?:H$|- |S |C )", 1)
        ).alias("origins")
    )
    invalid_orders = checked.filter(
        (pl.col("orders").list.len() == 0)
        | (pl.col("orders").list.len() != pl.col("n_orders"))
        | pl.col("origins").list.eval(pl.element().is_null()).list.any()
        | (pl.col("origins").list.n_unique() != pl.col("origins").list.len())
        | (pl.col("origins").list.sort() != pl.col("units").list.sort())
    )
    if invalid_orders.height:
        raise ValueError(f"phases: {invalid_orders.height} incomplete or malformed opening order sets")

    metadata = scores.join(admitted, on="game_id", suffix="_game", validate="m:1")
    if metadata.filter(
        (pl.col("press_level") != pl.col("press_level_game"))
        | (pl.col("quality_tier") != pl.col("quality_tier_game"))
    ).height:
        raise ValueError("outcomes: cohort metadata disagrees with games")
    if scores.filter(
        ~pl.col("sos_score").is_finite() | ~pl.col("sos_score").is_between(0, 1)
        | (pl.col("solo") & pl.col("draw_vote"))
    ).height:
        raise ValueError("outcomes: invalid score or conflicting ending flags")
    if scores.group_by("game_id").agg(pl.col("sos_score").sum()).filter(
        (pl.col("sos_score") - 1).abs() > 1e-9
    ).height:
        raise ValueError("outcomes: scores must sum to one per game")

    first = first.select(*KEY, pl.col("orders").list.sort())
    # Hash only distinct openings, not every observation; Python hashes are not stable.
    catalog = first.select("power", "orders").unique().with_columns(
        pl.struct("power", "orders").map_elements(
            lambda row: opening_id(row["power"], row["orders"]), return_dtype=pl.String,
        ).alias("opening_id")
    )
    require_unique(catalog, ["opening_id"], "opening identities")
    observations = (
        first.join(scores, on=KEY, validate="1:1")
        .join(catalog, on=["power", "orders"], validate="m:1")
        .select(*KEY, "press_level", "quality_tier", "opening_id", "orders",
                "solo", "survived", "draw_vote", "sos_score")
        .sort(KEY)
    )
    if observations.height != admitted.height * len(POWERS):
        raise ValueError("opening join lost game/power observations")
    return observations, {
        "candidate_games": cohort.height,
        "excluded_non_s1901_games": cohort.height - admitted.height,
        "included_games": admitted.height,
        "observations": observations.height,
        "distinct_openings": catalog.height,
    }
