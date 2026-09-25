"""Build the opening book offline: uv run python -m pipeline.openings [--help]."""

import argparse
import json
import platform
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

import polars as pl

from .analysis.artifacts import fingerprint, require_unchanged
from .analysis.opening_data import build_observations
from .analysis.opening_report import render_report
from .analysis.opening_stats import summarize_openings

SCHEMA_VERSION = 1
INPUTS = ("games.parquet", "phases.parquet", "game_outcomes.parquet")


def build(data_dir: Path, output_dir: Path, min_games: int = 200, top_n: int = 10) -> dict:
    """Compute validated artifacts, stage them, and publish their manifest last.

    No website or database runtime dependency: downstream consumers can read the
    small aggregates, while pair analyses reuse observations. Manifest hashes let
    consumers verify that all output files belong to the same completed build.
    """
    if min_games < 2 or top_n < 1:
        raise ValueError("min_games must be at least 2 and top_n must be positive")
    start = perf_counter()
    input_paths = [data_dir / name for name in INPUTS]
    inputs = [fingerprint(path) for path in input_paths]
    fingerprint_seconds = perf_counter() - start
    phase_start = perf_counter()
    observations, counts = build_observations(*(pl.scan_parquet(path) for path in input_paths))
    extract_seconds = perf_counter() - phase_start
    phase_start = perf_counter()
    stats = summarize_openings(observations, min_games=min_games)
    aggregate_seconds = perf_counter() - phase_start
    report = render_report(stats, counts, min_games=min_games, top_n=top_n)

    require_unchanged(input_paths, inputs)
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".openings-", dir=output_dir) as temporary:
        stage = Path(temporary)
        observations.write_parquet(stage / "openings_observations.parquet", compression="zstd")
        stats.write_parquet(stage / "openings_own.parquet", compression="zstd")
        (stage / "openings_own.md").write_text(report, encoding="utf-8")
        outputs = [fingerprint(stage / name) for name in (
            "openings_observations.parquet", "openings_own.parquet", "openings_own.md",
        )]
        source_paths = [Path(__file__), *sorted((Path(__file__).parent / "analysis").glob("*.py"))]
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "built_at_utc": datetime.now(timezone.utc).isoformat(),
            "polars_version": pl.__version__,
            "python_version": platform.python_version(),
            "config": {"min_games": min_games, "top_n": top_n, "confidence_level": 0.95},
            "counts": {**counts, "aggregate_rows": stats.height},
            "inputs": inputs,
            "sources": [fingerprint(path) for path in source_paths],
            "outputs": outputs,
            "schemas": {
                "observations": {name: str(dtype) for name, dtype in observations.schema.items()},
                "aggregates": {name: str(dtype) for name, dtype in stats.schema.items()},
            },
            "intervals": {"solo": "wilson_95", "mean_sos": "normal_95_clipped; null for n<2 or zero variance"},
            "timings_seconds": {
                "input_fingerprints": round(fingerprint_seconds, 4),
                "extract_validate": round(extract_seconds, 4),
                "aggregate": round(aggregate_seconds, 4),
                "total_before_publish": round(perf_counter() - start, 4),
            },
        }
        (stage / "openings_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        # Individual replacements are atomic; the manifest is the completion marker.
        for output in outputs:
            (stage / output["name"]).replace(output_dir / output["name"])
        (stage / "openings_manifest.json").replace(output_dir / "openings_manifest.json")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path("data/processed"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/processed"))
    parser.add_argument("--min-games", type=int, default=200, help="Sparse-sample flag threshold; retain all openings")
    parser.add_argument("--top-n", type=int, default=10, help="Common openings per report table")
    args = parser.parse_args()
    manifest = build(args.data_dir, args.output_dir, args.min_games, args.top_n)
    print(json.dumps({"counts": manifest["counts"], "timings_seconds": manifest["timings_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
