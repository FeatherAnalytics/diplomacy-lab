"""Small shared provenance helpers for offline builds."""

import hashlib
import io
import json
from pathlib import Path

import polars as pl


def fingerprint(path: Path) -> dict:
    stat = path.stat()
    with path.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    return {"name": path.name, "size_bytes": stat.st_size, "mtime_ns": stat.st_mtime_ns, "sha256": digest}


def require_unchanged(paths: list[Path], inputs: list[dict]) -> None:
    """Refuse to publish if an upstream build changed an input while it was read."""
    for path, original in zip(paths, inputs):
        stat = path.stat()
        if (stat.st_size, stat.st_mtime_ns) != (original["size_bytes"], original["mtime_ns"]):
            raise ValueError(f"Input changed during build: {path}")


def load_exact_snapshot(data_dir: Path, names: tuple[str, ...]) -> tuple[bytes, dict, list[pl.DataFrame]]:
    """Hash and decode the same bytes, so a concurrent rebuild cannot mix data."""
    manifest_bytes = (data_dir / "opening_exact_manifest.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    if manifest["schema_version"] != 1:
        raise ValueError("Unsupported exact-match artifact version")
    expected = {entry["name"]: entry["sha256"] for entry in manifest["outputs"]}
    tables = []
    for name in names:
        raw = (data_dir / name).read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected.get(name):
            raise ValueError(f"{name} does not match its build manifest; rebuild or retry")
        tables.append(pl.read_parquet(io.BytesIO(raw)))
    return manifest_bytes, manifest, tables
