"""Canonical own and seven-country histories for exact historical matching."""

import hashlib
import json

import polars as pl

from .cohorts import POWERS
from .opening_data import KEY, require_unique

PHASES = ("S1901M", "S1901R", "F1901M", "F1901R", "W1901A", "S1902M")
LABELS = ["press_level", "quality_tier", "solo", "survived", "draw_vote", "sos_score"]


def year_id(power: str, sequence_json: str) -> str:
    return "y1_" + hashlib.sha256((power.lower() + "\n" + sequence_json).encode("utf-8")).hexdigest()


def joint_id(horizon: str, sequence_ids: list[str]) -> str:
    """Sequence IDs must follow the fixed alphabetical POWERS order."""
    encoded = json.dumps([horizon, sequence_ids], separators=(",", ":"))
    return "j1_" + hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def build_exact_data(
    spring: pl.DataFrame, phases: pl.LazyFrame,
) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
    """Build observation links plus normalized own/joint pattern catalogs.

    Spring observations must come from build_observations. The next Spring's
    pre-adjudication boundary establishes that the whole year is recorded. Empty
    optional own phases do not split identities, while movement phases remain.
    Orders are matched as recorded, not checked for strategic or legal validity.
    """
    ids = spring.select("game_id").unique()
    history = (
        phases.filter(pl.col("phase_name").is_in(PHASES))
        .join(ids.lazy(), on="game_id", how="semi")
        .select("game_id", "phase_idx", "phase_name", "adjudicated",
                pl.col("power").str.to_lowercase(), "orders", "n_orders")
        .collect()
    )
    require_unique(history, ["game_id", "phase_idx", "power"], "year phases")
    require_unique(history, ["game_id", "phase_name", "power"], "year phase names")
    if not history["power"].is_in(POWERS).all():
        raise ValueError("year phases: unknown power")
    headers = history.group_by("game_id", "phase_idx").agg(
        pl.col("phase_name").first(), pl.col("phase_name").n_unique().alias("names"),
        pl.len().alias("rows"),
    ).sort("game_id", "phase_idx")
    if headers.filter((pl.col("names") != 1) | (pl.col("rows") != 7)).height:
        raise ValueError("year phases: inconsistent headers or missing power rows")
    coverage = headers.group_by("game_id").agg(
        pl.col("phase_name").filter(pl.col("phase_name").is_in(["S1901M", "F1901M", "S1902M"])).n_unique().alias("required"),
        pl.col("phase_idx").min().alias("first_idx"),
        pl.col("phase_idx").max().alias("last_idx"), pl.len().alias("phases"),
    )
    if coverage.height != ids.height or coverage.filter(
        (pl.col("required") != 3) | (pl.col("first_idx") != 0)
        | (pl.col("last_idx") != pl.col("phases") - 1)
    ).height:
        raise ValueError("year phases: incomplete 1901 history or missing Spring 1902 boundary")
    ordered = headers.with_columns(pl.col("phase_name").replace_strict(dict(zip(PHASES, range(6)))).alias("rank"))
    if ordered.with_columns(pl.col("rank").diff().over("game_id").alias("step")).filter(pl.col("step") <= 0).height:
        raise ValueError("year phases: invalid chronology")
    year = history.filter(pl.col("phase_name") != "S1902M")
    if year.select(pl.any_horizontal(pl.all().is_null()).any()).item():
        raise ValueError("year phases: null orders or metadata")
    if not year["adjudicated"].all():
        raise ValueError("year phases: unadjudicated 1901 phase")
    if year.filter(
        (pl.col("orders").list.len() != pl.col("n_orders"))
        | pl.col("orders").list.eval(pl.element().is_null() | (pl.element() == "")).list.any()
    ).height:
        raise ValueError("year phases: missing order text or mismatched order count")

    # JSON is the explicit, portable ordered-event representation of a sequence.
    own = (
        year.filter(pl.col("phase_name").str.ends_with("M") | (pl.col("orders").list.len() > 0))
        .with_columns(pl.struct(pl.col("phase_name").alias("phase"), pl.col("orders").list.sort()).struct.json_encode().alias("event"))
        .sort("game_id", "power", "phase_idx")
        .group_by(KEY, maintain_order=True).agg(pl.col("event").str.join(",").alias("events"))
        .with_columns(pl.concat_str(pl.lit("["), "events", pl.lit("]")).alias("sequence_json"))
        .drop("events")
    )
    year_catalog = own.select("power", "sequence_json").unique().with_columns(
        pl.struct("power", "sequence_json").map_elements(
            lambda row: year_id(row["power"], row["sequence_json"]), return_dtype=pl.String,
        ).alias("sequence_id"), pl.lit("year1901").alias("horizon"),
    )
    spring_catalog = spring.select("power", "opening_id", "orders").unique().with_columns(
        pl.concat_str(pl.lit("["), pl.struct(pl.lit("S1901M").alias("phase"), "orders").struct.json_encode(), pl.lit("]")).alias("sequence_json"),
        pl.lit("spring1901").alias("horizon"),
    ).rename({"opening_id": "sequence_id"})
    catalog_cols = ["horizon", "power", "sequence_id", "sequence_json"]
    sequences = pl.concat([spring_catalog.select(catalog_cols), year_catalog.select(catalog_cols)]).sort("horizon", "power", "sequence_id")
    require_unique(sequences, ["sequence_id"], "sequence catalog")

    year_rows = own.join(year_catalog, on=["power", "sequence_json"], validate="m:1").join(
        spring.select(*KEY, *LABELS), on=KEY, validate="1:1",
    )
    spring_rows = spring.rename({"opening_id": "sequence_id"}).with_columns(pl.lit("spring1901").alias("horizon"))
    columns = ["horizon", *KEY, "sequence_id", *LABELS]
    observations = pl.concat([spring_rows.select(columns), year_rows.select(columns)])
    if observations.height != spring.height * 2:
        raise ValueError("year history join lost observations")
    profiles_by_game = observations.group_by("horizon", "game_id").agg(
        pl.col("sequence_id").sort_by("power").alias("sequence_ids"),
    )
    profiles = profiles_by_game.select("horizon", "sequence_ids").unique().with_columns(
        pl.struct("horizon", "sequence_ids").map_elements(
            lambda row: joint_id(row["horizon"], row["sequence_ids"]), return_dtype=pl.String,
        ).alias("joint_id"),
    ).sort("horizon", "joint_id")
    require_unique(profiles, ["joint_id"], "joint catalog")
    links = profiles_by_game.join(profiles, on=["horizon", "sequence_ids"], validate="m:1").select("horizon", "game_id", "joint_id")
    observations = observations.join(links, on=["horizon", "game_id"], validate="m:1").sort("horizon", "joint_id", "game_id", "power")
    return observations, sequences, profiles
