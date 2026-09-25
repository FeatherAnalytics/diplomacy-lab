"""Web export round trip on the full-year fixtures."""

import gzip
import json
import struct
import tempfile
import unittest
from pathlib import Path

import polars as pl

from pipeline.analysis.cohorts import POWERS
from pipeline.exact_openings import build as build_exact
from pipeline.web_export import build, write
from test_exact_openings import year_fixtures


class WebExportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        games, phases, outcomes = year_fixtures()
        # Fixture scores are solos (1 for 18 centers) or two-way draws (0.5 each at 5 centers).
        centers = pl.when(pl.col("sos_score") == 1).then(18).when(pl.col("sos_score") == .5).then(5).otherwise(0)
        outcomes = outcomes.with_columns(centers.alias("final_centers"))
        for name, frame in zip(["games", "phases", "game_outcomes"], (games, phases, outcomes)):
            frame.write_parquet(self.root / f"{name}.parquet")
        build_exact(self.root, self.root, top_n=1)

    def test_indexes_decode_to_recorded_orders_and_rebuilds_are_identical(self):
        meta, catalog_bytes, blob = build(self.root)
        catalog = json.loads(catalog_bytes)
        layout = {array["name"]: array for array in meta["arrays"]}
        spring = struct.unpack_from(f"<{layout['spring']['length']}H", blob, layout["spring"]["offset"])
        observations = pl.read_parquet(self.root / "opening_exact_observations.parquet").filter(pl.col("horizon") == "spring1901")
        texts = dict(pl.read_parquet(self.root / "opening_exact_sequences.parquet").select("sequence_id", "sequence_json").iter_rows())
        first_game = observations["game_id"].sort()[0]
        for p, power in enumerate(POWERS):
            sid = observations.filter((pl.col("game_id") == first_game) & (pl.col("power") == power))["sequence_id"][0]
            recorded = json.loads(texts[sid])[0]["orders"]
            _, order_indexes = catalog["spring"][power][spring[p]]
            self.assertEqual([catalog["orders"][i] for i in order_indexes], sorted(recorded))
        first = write(self.root / "web", meta, catalog_bytes, blob)
        second = write(self.root / "web", *build(self.root))
        self.assertEqual(first, second)
        self.assertEqual(len(gzip.decompress((self.root / "web" / "games.bin.gz").read_bytes())), meta["bytes"])

    def test_scores_that_disagree_with_final_centers_are_rejected(self):
        outcomes = pl.read_parquet(self.root / "game_outcomes.parquet")
        outcomes.with_columns(pl.col("final_centers") + 1).write_parquet(self.root / "game_outcomes.parquet")
        with self.assertRaisesRegex(ValueError, "disagree"):
            build(self.root)


if __name__ == "__main__":
    unittest.main()
