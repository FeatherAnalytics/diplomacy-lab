"""Export the exact-match snapshot as compact, gzip-compressed files for the static site.

Usage: uv run python -m pipeline.web_export [--data-dir data/processed] [--output-dir web/data]

Hash IDs become small integer indexes, and each game stores final centers instead of
scores; the browser recomputes scores exactly. Output is byte-identical for the same
inputs, so re-running is safe.
"""

import argparse
import gzip
import hashlib
import json
import sys
import tempfile
from array import array
from pathlib import Path

import polars as pl

from .analysis.artifacts import load_exact_snapshot
from .analysis.cohorts import POWERS
from .analysis.exact_data import PHASES
from .analysis.score_benchmark import STRENGTHS

YEAR_PHASES = PHASES[:-1]
PRESS_CODES = {"no_press": 0, "press_with_msgs": 1, "public_press": 2}
SPLIT_CODES = {"train": 0, "validation": 1, "test": 2}
NO_SPLIT = 3
SOLO_CENTERS = 18
ID_HEX = 12
OBSERVATIONS = "opening_exact_observations.parquet"
SEQUENCES = "opening_exact_sequences.parquet"


def short_id(prefix: str, digest: str) -> str:
    return prefix + digest[:ID_HEX]


def turn_id(power: str, phase: str, orders: list[str]) -> str:
    payload = json.dumps([power, phase, orders], separators=(",", ":"))
    return short_id("p1_", hashlib.sha256(payload.encode()).hexdigest())


def year_history(sequence_json: str) -> list[list[str]]:
    """Every full-year turn, with empty optional turns filled in, in chronological order."""
    history = {step["phase"]: step["orders"] for step in json.loads(sequence_json)}
    return [sorted(history.get(phase, [])) for phase in YEAR_PHASES]


def order_texts(spring: pl.DataFrame, year: pl.DataFrame) -> set[str]:
    texts = {order for s in spring["sequence_json"] for step in json.loads(s) for order in step["orders"]}
    return texts | {order for s in year["sequence_json"] for turn in year_history(s) for order in turn}


class Catalog:
    """Deterministic integer indexes for order text, Spring openings, turns and full-year histories."""

    def __init__(self, sequences: pl.DataFrame):
        spring = sequences.filter(pl.col("horizon") == "spring1901").sort("sequence_id")
        year = sequences.filter(pl.col("horizon") == "year1901").sort("sequence_id")
        self.orders = sorted(order_texts(spring, year))
        self.order_index = {text: i for i, text in enumerate(self.orders)}
        self.turns = {p: {phase: {} for phase in YEAR_PHASES} for p in POWERS}
        self.spring, self.spring_index = self.index(spring, self.spring_entry)
        self.year, self.year_index = self.index(year, self.year_entry)
        require_unique_ids(self)

    @staticmethod
    def index(frame: pl.DataFrame, entry) -> tuple[dict[str, list], dict[str, int]]:
        lists, positions = {p: [] for p in POWERS}, {}
        for power, sid, text in frame.select("power", "sequence_id", "sequence_json").iter_rows():
            positions[sid] = len(lists[power])
            lists[power].append(entry(power, sid, text))
        return lists, positions

    def spring_entry(self, power: str, sid: str, text: str) -> list:
        return [short_id("o1_", sid.removeprefix("o1_")), self.encode(json.loads(text)[0]["orders"])]

    def year_entry(self, power: str, sid: str, text: str) -> list[int]:
        return [self.turn(power, phase, orders) for phase, orders in zip(YEAR_PHASES, year_history(text))]

    def encode(self, orders: list[str]) -> list[int]:
        return [self.order_index[order] for order in sorted(orders)]

    def turn(self, power: str, phase: str, orders: list[str]) -> int:
        entries = self.turns[power][phase]
        key = tuple(orders)
        if key not in entries:
            entries[key] = len(entries)
        return entries[key]

    def turn_lists(self) -> dict:
        return {p: {phase: [[turn_id(p, phase, list(orders)), self.encode(list(orders))] for orders in entries]
                    for phase, entries in phases.items()} for p, phases in self.turns.items()}

    def to_json(self) -> dict:
        return {"orders": self.orders, "spring": self.spring, "turns": self.turn_lists()}


def require_unique_ids(catalog: Catalog) -> None:
    spring = [entry[0] for entries in catalog.spring.values() for entry in entries]
    turns = [entry[0] for phases in catalog.turn_lists().values() for entries in phases.values() for entry in entries]
    for label, ids in (("opening", spring), ("turn", turns)):
        if len(set(ids)) != len(ids):
            raise ValueError(f"Shortened {label} IDs collide; increase ID_HEX")


def game_table(observations: pl.DataFrame, outcomes: pl.DataFrame, splits: pl.DataFrame | None) -> pl.DataFrame:
    """One row per game in fixed order, with packed flags and final centers per power."""
    spring = observations.filter(pl.col("horizon") == "spring1901")
    games = spring.group_by("game_id").agg(
        pl.col("press_level").first(), pl.col("quality_tier").first(), pl.col("draw_vote").any().alias("draw_ending"),
    ).sort("game_id").with_row_index("game")
    split = splits.select("game_id", pl.col("split").replace_strict(SPLIT_CODES)) if splits is not None else None
    games = games.join(split, on="game_id", how="left") if split is not None else games.with_columns(split=None)
    flags = (pl.col("press_level").replace_strict(PRESS_CODES) + pl.col("quality_tier").cast(pl.UInt8) * 4
             + pl.col("split").fill_null(NO_SPLIT) * 16 + pl.col("draw_ending").cast(pl.UInt8) * 64)
    centers = outcomes.join(games.select("game_id"), on="game_id", how="semi").pivot(
        on="power", index="game_id", values="final_centers")
    return games.with_columns(flags.cast(pl.UInt8).alias("flags")).join(centers, on="game_id", validate="1:1").sort("game")


def verify_outcomes(observations: pl.DataFrame, games: pl.DataFrame) -> None:
    """Scores and flags recomputed from centers must equal the snapshot, since the browser relies on it."""
    long = games.unpivot(index=["game_id", "draw_ending"], on=list(POWERS), variable_name="power", value_name="centers")
    solo = pl.col("centers") >= SOLO_CENTERS
    squares = pl.col("centers").cast(pl.Float64).pow(2)
    derived = long.with_columns(
        pl.when(solo.any().over("game_id")).then(solo.cast(pl.Float64)).otherwise(squares / squares.sum().over("game_id")).alias("score"),
        solo.alias("solo_d"), (pl.col("centers") > 0).alias("survived_d"),
        ((pl.col("centers") > 0) & pl.col("draw_ending")).alias("draw_d"))
    checked = observations.filter(pl.col("horizon") == "spring1901").join(derived, on=["game_id", "power"], validate="1:1")
    mismatched = checked.filter(((pl.col("score") - pl.col("sos_score")).abs() > 1e-12) | (pl.col("solo") != pl.col("solo_d"))
                                | (pl.col("survived") != pl.col("survived_d")) | (pl.col("draw_vote") != pl.col("draw_d")))
    if checked.height != observations.height // 2 or mismatched.height:
        raise ValueError(f"{mismatched.height} observations disagree with scores derived from final centers")


def sequence_matrix(observations: pl.DataFrame, games: pl.DataFrame, horizon: str, index: dict[str, int]) -> list[int]:
    rows = observations.filter(pl.col("horizon") == horizon).join(games.select("game_id", "game"), on="game_id", validate="m:1")
    rows = rows.with_columns(
        (pl.col("game") * len(POWERS) + pl.col("power").replace_strict({p: i for i, p in enumerate(POWERS)})).alias("slot"),
        pl.col("sequence_id").replace_strict(index).alias("index")).sort("slot")
    if rows["slot"].to_list() != list(range(games.height * len(POWERS))):
        raise ValueError(f"{horizon}: every game needs exactly one history per country")
    return rows["index"].to_list()


def load_benchmark(folder: Path, observations_sha: str, manifest_sha: str) -> tuple[pl.DataFrame, dict, str] | None:
    """Splits and selected strengths for the optional estimate toggle; None when absent or stale."""
    try:
        raw_manifest = (folder / "manifest.json").read_bytes()
    except FileNotFoundError:
        return None
    manifest = json.loads(raw_manifest)
    if not benchmark_matches(manifest, observations_sha, manifest_sha):
        print("Skipping estimates: benchmark does not match this snapshot", file=sys.stderr)
        return None
    files = verified_files(folder, manifest, ("results.json", "split_assignments.parquet"))
    models = own_models(json.loads(files["results.json"]))
    return pl.read_parquet(files["split_assignments.parquet"]), models, hashlib.sha256(raw_manifest).hexdigest()[:16]


def benchmark_matches(manifest: dict, observations_sha: str, manifest_sha: str) -> bool:
    return (manifest["schema_version"] == 1 and manifest["input"]["observations_sha256"] == observations_sha
            and manifest["input"]["exact_manifest_sha256"] == manifest_sha
            and manifest["config"]["refit"] == "train_plus_validation")


def verified_files(folder: Path, manifest: dict, names: tuple[str, ...]) -> dict[str, bytes]:
    expected = {entry["name"]: entry["sha256"] for entry in manifest["outputs"]}
    files = {name: (folder / name).read_bytes() for name in names}
    for name, data in files.items():
        if hashlib.sha256(data).hexdigest() != expected.get(name):
            raise ValueError(f"{name} does not match its benchmark manifest")
    return files


def own_models(results: list[dict]) -> dict:
    models = {}
    for row in (r for r in results if r["family"] == "own"):
        strength = row["strength"]
        if not (type(strength) is int or strength == "baseline") or strength not in STRENGTHS:
            raise ValueError("Unsupported shrinkage strength")
        models.setdefault(row["horizon"], {})[row["quality_group"]] = {"strength": strength, "fit_games": row["fit_games"]}
    return models


def verify_fit_games(games: pl.DataFrame, models: dict) -> None:
    fitting = games.filter(pl.col("flags") // 16 % 4 < 2)
    for quality, frame in (("tiers_1_3", fitting), ("tier_1", fitting.filter(pl.col("quality_tier") == 1))):
        for horizon, groups in models.items():
            if groups[quality]["fit_games"] != frame.height:
                raise ValueError(f"Benchmark fitting population differs for {horizon}/{quality}")


def pack(arrays: list[tuple[str, str, list[int]]]) -> tuple[bytes, list[dict]]:
    """Concatenate typed arrays little-endian, 16-bit arrays first so every view stays aligned."""
    blob, layout = bytearray(), []
    for name, code, values in arrays:
        data = array(code, values)
        if sys.byteorder != "little":
            data.byteswap()
        layout.append({"name": name, "type": {"H": "uint16", "B": "uint8"}[code], "offset": len(blob), "length": len(values)})
        blob += data.tobytes()
    return bytes(blob), layout


def benchmark_parts(benchmark: tuple[pl.DataFrame, dict, str] | None) -> tuple[pl.DataFrame | None, dict | None]:
    if benchmark is None:
        return None, None
    splits, models, model_id = benchmark
    return splits, {"model_id": model_id, "models": models}


def year_offsets(catalog: Catalog) -> dict[str, int]:
    """Where each country's full-year histories start in the shared year_turns array."""
    offsets, start = {}, 0
    for power in POWERS:
        offsets[power] = start
        start += len(catalog.year[power])
    return offsets


def build(data_dir: Path) -> tuple[dict, bytes, bytes]:
    manifest_bytes, manifest, (observations, sequences) = load_exact_snapshot(data_dir, (OBSERVATIONS, SEQUENCES))
    observations_sha = next(e["sha256"] for e in manifest["outputs"] if e["name"] == OBSERVATIONS)
    benchmark = load_benchmark(data_dir / "score_benchmark", observations_sha, hashlib.sha256(manifest_bytes).hexdigest())
    catalog = Catalog(sequences)
    outcomes = pl.read_parquet(data_dir / "game_outcomes.parquet").select("game_id", "power", "final_centers")
    splits, estimates = benchmark_parts(benchmark)
    games = game_table(observations, outcomes, splits)
    verify_outcomes(observations, games)
    if estimates:
        verify_fit_games(games, estimates["models"])
    year_turns = [turn for power in POWERS for entry in catalog.year[power] for turn in entry]
    blob, layout = pack([
        ("spring", "H", sequence_matrix(observations, games, "spring1901", catalog.spring_index)),
        ("year", "H", sequence_matrix(observations, games, "year1901", catalog.year_index)),
        ("year_turns", "H", year_turns),
        ("centers", "B", [c for row in games.select(POWERS).iter_rows() for c in row]),
        ("flags", "B", games["flags"].to_list()),
    ])
    meta = {
        "schema_version": 1, "build_id": hashlib.sha256(manifest_bytes).hexdigest()[:16],
        "built_at": manifest["built_at_utc"], "n_games": games.height, "min_games": manifest["config"]["min_games"],
        "powers": list(POWERS), "year_phases": list(YEAR_PHASES), "press_levels": list(PRESS_CODES),
        "arrays": layout, "year_offsets": year_offsets(catalog), "bytes": len(blob),
        "estimates": estimates,
    }
    catalog_bytes = json.dumps(catalog.to_json(), separators=(",", ":"), ensure_ascii=False).encode()
    return meta, catalog_bytes, blob


def write(output_dir: Path, meta: dict, catalog_bytes: bytes, blob: bytes) -> dict:
    files = {"catalog.json.gz": gzip.compress(catalog_bytes, 9, mtime=0), "games.bin.gz": gzip.compress(blob, 9, mtime=0)}
    meta = meta | {"files": {name: len(data) for name, data in files.items()}}
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".web-export-", dir=output_dir) as tmp:
        stage = Path(tmp)
        for name, data in files.items():
            (stage / name).write_bytes(data)
        (stage / "meta.json").write_text(json.dumps(meta, indent=1) + "\n", encoding="utf-8")
        # meta.json goes last: it names the build the other files belong to.
        for name in [*files, "meta.json"]:
            (stage / name).replace(output_dir / name)
    return meta


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data-dir", type=Path, default=Path("data/processed"))
    parser.add_argument("--output-dir", type=Path, default=Path("web/data"))
    args = parser.parse_args()
    meta = write(args.output_dir, *build(args.data_dir))
    print(json.dumps({"n_games": meta["n_games"], "raw_bytes": meta["bytes"], "files": meta["files"]}, indent=2))


if __name__ == "__main__":
    main()
