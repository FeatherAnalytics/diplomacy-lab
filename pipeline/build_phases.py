"""Build phases.parquet: one row per game, phase, and power for standard-map DipNet games.

Usage: uv run python -m pipeline.build_phases [data/raw/dipnet] [data/processed] [--sample N]

Every phase is included. The trailing phase (adjudicated == False) is the final board state:
either the pending never-adjudicated phase or the COMPLETED marker after a solo. Its
orders-derived columns are null because whatever orders sit there were never adjudicated,
so phases_from_end == 0 is the end position and phases_from_end == 1 is the last phase played.
Scope (quality, ending) is not applied here; join to games.parquet and filter in_scope.
"""

import argparse
import json
import shutil
import sys
import tempfile
from multiprocessing import Pool
from pathlib import Path

import polars as pl

from .profile_games import FILES, PHASE_RE, POWERS, all_hold, phase_year

GAMES_PER_CHUNK = 2000

SCHEMA = {
    "game_id": pl.Utf8,
    "phase_idx": pl.Int32,
    "phases_from_end": pl.Int32,
    "phase_name": pl.Utf8,
    "year": pl.Int16,
    "season": pl.Utf8,
    "phase_type": pl.Utf8,
    "adjudicated": pl.Boolean,
    "power": pl.Utf8,
    "n_centers": pl.Int8,
    "n_units": pl.Int8,
    "centers": pl.List(pl.Utf8),
    "units": pl.List(pl.Utf8),
    "orders": pl.List(pl.Utf8),
    "n_orders": pl.Int8,
    "n_failed": pl.Int8,
    "all_hold": pl.Boolean,
}

NO_ORDERS = {"orders": None, "n_orders": None, "n_failed": None, "all_hold": None}


def order_failed(order: str, results: dict) -> bool:
    # results is keyed by unit ("A PAR"); malformed NO_CHECK orders are keyed by their own text
    # and marked void. A missing key in a non-empty results dict is treated as failed.
    # Successes are [] or [""] (builds); an explicit disband's "disband" is its intended outcome.
    if order == "WAIVE":
        return False
    unit = " ".join(order.split()[:2])
    outcome = results.get(unit, results.get(order, ["void"]))
    return any(r for r in outcome if not (r == "disband" and order.endswith(" D")))


def order_fields(orders: list[str], results: dict) -> dict:
    return {
        "orders": orders,
        "n_orders": len(orders),
        "n_failed": sum(order_failed(o, results) for o in orders),
        "all_hold": all_hold(orders),
    }


def power_row(ph: dict, power: str, adjudicated: bool) -> dict:
    units = ph["state"]["units"].get(power, [])
    centers = ph["state"]["centers"].get(power, [])
    orders = ph["orders"].get(power) or []
    return {
        "power": power,
        "n_centers": len(centers),
        "n_units": len(units),
        "centers": centers,
        "units": units,
        **(order_fields(orders, ph["results"]) if adjudicated else NO_ORDERS),
    }


def game_rows(game: dict) -> list[dict]:
    phases = game["phases"]
    rows = []
    for idx, ph in enumerate(phases):
        name = ph["name"]
        season, phase_type = (name[0], name[-1]) if PHASE_RE.match(name) else (None, None)
        adjudicated = idx < len(phases) - 1
        head = {
            "game_id": game["id"],
            "phase_idx": idx,
            "phases_from_end": len(phases) - 1 - idx,
            "phase_name": name,
            "year": phase_year(name),
            "season": season,
            "phase_type": phase_type,
            "adjudicated": adjudicated,
        }
        rows += [head | power_row(ph, p, adjudicated) for p in POWERS]
    return rows


def write_chunk(rows: list[dict], chunk_dir: Path, stem: str, n: int) -> None:
    pl.DataFrame(rows, schema=SCHEMA).write_parquet(chunk_dir / f"{stem}_{n:05d}.parquet")


def build_file(args: tuple[Path, Path, int | None]) -> int:
    path, chunk_dir, sample = args
    rows, n_games, n_chunks = [], 0, 0
    with path.open() as f:
        for line in f:
            game = json.loads(line)
            if game["map"] != "standard":
                continue
            rows += game_rows(game)
            n_games += 1
            if n_games % 5000 == 0:
                print(f"{path.name}: {n_games} standard-map games", file=sys.stderr, flush=True)
            if n_games % GAMES_PER_CHUNK == 0:
                write_chunk(rows, chunk_dir, path.stem, n_chunks)
                rows, n_chunks = [], n_chunks + 1
            if sample and n_games >= sample:
                break
    if rows:
        write_chunk(rows, chunk_dir, path.stem, n_chunks)
    return n_games


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("raw_dir", nargs="?", default="data/raw/dipnet", type=Path)
    ap.add_argument("out_dir", nargs="?", default="data/processed", type=Path)
    ap.add_argument("--sample", type=int, help="standard-map games per file; writes phases_sample.parquet")
    a = ap.parse_args()

    a.out_dir.mkdir(parents=True, exist_ok=True)
    chunk_dir = Path(tempfile.mkdtemp(dir=a.out_dir, prefix="phases_chunks_"))
    jobs = [(a.raw_dir / name, chunk_dir, a.sample) for name in FILES]
    with Pool(len(jobs)) as pool:
        counts = pool.map(build_file, jobs)
    print(f"standard-map games: {dict(zip(FILES, counts))}", file=sys.stderr)

    out = a.out_dir / ("phases_sample.parquet" if a.sample else "phases.parquet")
    pl.scan_parquet(chunk_dir / "*.parquet").sink_parquet(out)
    shutil.rmtree(chunk_dir)
    print(f"wrote {out}: {pl.scan_parquet(out).select(pl.len()).collect().item()} rows")


if __name__ == "__main__":
    main()
