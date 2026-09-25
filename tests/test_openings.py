"""Opening-book fixtures and regression tests; no downloaded data required."""

import json
import hashlib
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal

ROOT = Path(__file__).resolve().parents[1]
UNITS = {
    "austria": ["A BUD", "A VIE", "F TRI"],
    "england": ["A LVP", "F EDI", "F LON"],
    "france": ["A MAR", "A PAR", "F BRE"],
    "germany": ["A BER", "A MUN", "F KIE"],
    "italy": ["A ROM", "A VEN", "F NAP"],
    "russia": ["A MOS", "A WAR", "F SEV", "F STP/SC"],
    "turkey": ["A CON", "A SMY", "F ANK"],
}


def fixtures() -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
    games, phases, outcomes = [], [], []
    specs = [
        ("a", "no_press", 1, "solo", "austria"),
        ("b", "no_press", 3, "solo", "france"),
        ("c", "no_press", 1, "draw_vote", None),
        ("d", "press_with_msgs", 1, "solo", "austria"),
        ("e", "public_press", 1, "solo", "england"),
        ("selected", "press", 1, "solo", "austria"),
        ("excluded", "no_press", 4, "solo", "austria"),
        ("late", "no_press", 1, "solo", "austria"),
    ]
    for game_id, press, tier, ending, winner in specs:
        first = "S1902M" if game_id == "late" else "S1901M"
        games.append({"game_id": game_id, "press_level": press, "quality_tier": tier,
                      "in_scope": game_id != "excluded", "first_phase": first})
        for power, units in UNITS.items():
            orders = [unit + " H" for unit in units]
            if power == "austria" and game_id == "c":
                orders[0] = "A BUD - SER"
            if game_id == "b":
                orders.reverse()
            phases.append({"game_id": game_id, "phase_idx": 0, "phase_name": first,
                           "adjudicated": True, "power": power.upper(), "units": units,
                           "orders": orders, "n_orders": len(orders)})
            score = float(power == winner) if winner else (0.5 if power in ("austria", "england") else 0.0)
            outcomes.append({"game_id": game_id, "power": power, "press_level": press,
                             "quality_tier": tier, "solo": power == winner,
                             "survived": score > 0, "draw_vote": ending == "draw_vote" and score > 0,
                             "sos_score": score})
    # Later phases must never be admitted, even with a misleading phase_name.
    phases.append({**phases[0], "phase_idx": 1, "orders": ["A BUD - RUM", "A VIE H", "F TRI H"]})
    return pl.DataFrame(games), pl.DataFrame(phases), pl.DataFrame(outcomes)


class OpeningBookTests(unittest.TestCase):
    def test_cli_builds_reusable_artifacts_from_the_correct_cohort(self) -> None:
        games, phases, outcomes = fixtures()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, df in [("games", games), ("phases", phases), ("game_outcomes", outcomes)]:
                df.write_parquet(root / f"{name}.parquet")
            cmd = [sys.executable, "-m", "pipeline.openings", "--data-dir", str(root),
                   "--output-dir", str(root / "book"), "--min-games", "2", "--top-n", "2"]
            run = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            book = root / "book"
            observations = pl.read_parquet(book / "openings_observations.parquet")
            aggregate = pl.read_parquet(book / "openings_own.parquet")
            manifest = json.loads((book / "openings_manifest.json").read_text())
            report = (book / "openings_own.md").read_text()
            self.assertEqual(observations.height, 35)
            self.assertEqual(set(observations["game_id"]), {"a", "b", "c", "d", "e"})
            self.assertEqual(manifest["counts"]["excluded_non_s1901_games"], 1)
            self.assertEqual(manifest["counts"]["included_games"], 5)
            self.assertNotIn("press", aggregate["press_level"].to_list())
            for power in UNITS:
                self.assertIn(f"## {power.title()}", report)
            self.assertIn("Sparse", report)
            self.assertIn("Tier 1", report)
            for output in manifest["outputs"]:
                self.assertEqual(hashlib.sha256((book / output["name"]).read_bytes()).hexdigest(), output["sha256"])
            # A second build yields the same data regardless of timing metadata.
            second = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(second.returncode, 0, second.stderr)
            assert_frame_equal(aggregate, pl.read_parquet(book / "openings_own.parquet"))
            # Invalid upstream data must not replace a previously good publication.
            published = {p.name: p.read_bytes() for p in book.iterdir() if p.is_file()}
            outcomes.slice(1).write_parquet(root / "game_outcomes.parquet")
            broken = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(broken.returncode, 0)
            self.assertEqual(published, {p.name: p.read_bytes() for p in book.iterdir() if p.is_file()})

    def test_join_normalizes_power_and_canonicalizes_orders(self) -> None:
        from pipeline.analysis.opening_data import build_observations

        games, phases, outcomes = fixtures()
        observations, counts = build_observations(games.lazy(), phases.lazy(), outcomes.lazy())
        self.assertEqual(counts["included_games"], 5)
        a = observations.filter((pl.col("power") == "austria") & pl.col("game_id").is_in(["a", "b"]))
        self.assertEqual(a["opening_id"].n_unique(), 1)
        self.assertEqual(a["orders"].to_list(), [["A BUD H", "A VIE H", "F TRI H"]] * 2)

    def test_identity_preserves_coasts_and_is_independent_of_order_sequence(self) -> None:
        from pipeline.analysis.opening_data import opening_id

        orders = ["F STP/SC H", "A MOS H"]
        self.assertEqual(opening_id("russia", orders), opening_id("russia", orders[::-1]))
        self.assertNotEqual(opening_id("russia", orders), opening_id("russia", ["F STP/NC H", "A MOS H"]))
        self.assertNotEqual(opening_id("russia", orders), opening_id("turkey", orders))

    def test_missing_duplicate_or_inconsistent_inputs_fail_before_aggregation(self) -> None:
        from pipeline.analysis.opening_data import build_observations

        games, phases, outcomes = fixtures()
        cases = [
            (games, phases, outcomes.slice(1)),
            (games, pl.concat([phases, phases.head(1)]), outcomes),
            (pl.concat([games, games.head(1)]), phases, outcomes),
            (games, phases, pl.concat([outcomes, outcomes.head(1)])),
            (games, phases, outcomes.with_columns(pl.when(pl.col("game_id") == "a").then(pl.lit("public_press")).otherwise(pl.col("press_level")).alias("press_level"))),
            (games, phases.with_columns(pl.when((pl.col("game_id") == "a") & (pl.col("power") == "AUSTRIA")).then(pl.lit([], dtype=pl.List(pl.String))).otherwise(pl.col("orders")).alias("orders")), outcomes),
            (games, phases.with_columns(pl.lit(False).alias("adjudicated")), outcomes),
            (games, phases, outcomes.with_columns(pl.lit(float("nan")).alias("sos_score"))),
            (games, phases, outcomes.with_columns(pl.lit(0.0).alias("sos_score"))),
            (games.with_columns(pl.lit(False).alias("in_scope")), phases, outcomes),
            (games, phases.with_columns(pl.when((pl.col("game_id") == "a") & (pl.col("power") == "AUSTRIA")).then(pl.lit(["A BUD H", "A BUD - SER", "F TRI H"])).otherwise(pl.col("orders")).alias("orders")), outcomes),
        ]
        for inputs in cases:
            with self.subTest(inputs=[df.height for df in inputs]):
                with self.assertRaises(ValueError):
                    build_observations(*(df.lazy() for df in inputs))

    def test_statistics_use_matching_baselines_and_preserve_sparse_openings(self) -> None:
        from pipeline.analysis.opening_data import build_observations
        from pipeline.analysis.opening_stats import summarize_openings

        observations, _ = build_observations(*(df.lazy() for df in fixtures()))
        stats = summarize_openings(observations, min_games=2)
        rows = stats.filter((pl.col("power") == "austria") & (pl.col("press_level") == "no_press") & (pl.col("quality_group") == "tiers_1_3"))
        common = rows.filter(pl.col("n_games") == 2).row(0, named=True)
        self.assertAlmostEqual(common["frequency"], 2 / 3)
        self.assertEqual(common["solo_rate"], 0.5)
        self.assertEqual(common["mean_sos"], 0.5)
        self.assertAlmostEqual(common["sos_se"], 0.5)
        self.assertEqual(common["baseline_mean_sos"], 0.5)
        self.assertEqual(common["sos_lift"], 0)
        self.assertEqual(common["sos_ci_low"], 0)
        self.assertEqual(common["sos_ci_high"], 1)
        self.assertFalse(common["sparse"])
        self.assertAlmostEqual(common["solo_ci_low"], 0.0945312057, places=7)
        self.assertAlmostEqual(common["solo_ci_high"], 0.9054687943, places=7)
        singleton = rows.filter(pl.col("n_games") == 1).row(0, named=True)
        self.assertTrue(singleton["sparse"])
        self.assertIsNone(singleton["sos_se"])
        self.assertIsNone(singleton["sos_ci_low"])
        clean = stats.filter((pl.col("power") == "austria") & (pl.col("press_level") == "no_press") & (pl.col("quality_group") == "tier_1"))
        self.assertEqual(clean["baseline_mean_sos"].to_list(), [0.75, 0.75])
        private = stats.filter((pl.col("power") == "austria") & (pl.col("press_level") == "press_with_msgs"))
        self.assertEqual(set(private["baseline_mean_sos"]), {1.0})
        sums = stats.group_by("power", "press_level", "quality_group").agg(pl.col("frequency").sum())
        self.assertTrue(all(math.isclose(v, 1) for v in sums["frequency"]))

    def test_intervals_remain_honest_at_boundaries(self) -> None:
        from pipeline.analysis.opening_data import build_observations
        from pipeline.analysis.opening_stats import summarize_openings

        observations, _ = build_observations(*(df.lazy() for df in fixtures()))
        rows = summarize_openings(observations, min_games=2).filter(pl.col("power") == "germany")
        self.assertTrue(all(v > 0 for v in rows["solo_ci_high"]))
        self.assertTrue(rows["sos_ci_low"].is_null().all())
        self.assertTrue(rows["sos_ci_high"].is_null().all())

    def test_large_samples_do_not_overflow_interval_arithmetic(self) -> None:
        from pipeline.analysis.opening_stats import summarize_openings

        count = 70_000
        observations = pl.DataFrame({"game_id": [str(i) for i in range(count)]}).with_columns(
            pl.lit("germany").alias("power"), pl.lit("no_press").alias("press_level"),
            pl.lit(1).alias("quality_tier"), pl.lit("example").alias("opening_id"),
            pl.lit(["A BER H", "A MUN H", "F KIE H"]).alias("orders"),
            pl.lit(False).alias("solo"), pl.lit(False).alias("survived"),
            pl.lit(False).alias("draw_vote"), pl.lit(0.0).alias("sos_score"),
        )
        stats = summarize_openings(observations)
        self.assertEqual(stats["n_games"].to_list(), [count] * 4)
        for upper in stats["solo_ci_high"]:
            self.assertGreater(upper, 0.0000548)
            self.assertLess(upper, 0.0000550)

    def test_report_handles_absent_tier_one_and_escapes_order_text(self) -> None:
        from pipeline.analysis.opening_data import build_observations
        from pipeline.analysis.opening_stats import summarize_openings
        from pipeline.analysis.opening_report import render_report

        games, phases, outcomes = fixtures()
        games = games.with_columns(pl.lit(3).alias("quality_tier"))
        outcomes = outcomes.with_columns(pl.lit(3).alias("quality_tier"))
        observations, counts = build_observations(games.lazy(), phases.lazy(), outcomes.lazy())
        stats = summarize_openings(observations).with_columns(pl.lit(["<script>|bad</script>"]).alias("orders"))
        report = render_report(stats, counts)
        self.assertIn("No observations in this cohort.", report)
        self.assertNotIn("<script>", report)
        self.assertIn("&lt;script&gt;&#124;bad&lt;/script&gt;", report)

    def test_percentage_intervals_use_the_same_units_as_the_value(self) -> None:
        from pipeline.analysis.opening_report import interval

        self.assertEqual(interval(0.101, 0.09233, 0.10934, 100), "10.1% [9.2%, 10.9%]")

    def test_invalid_build_options_fail_without_writing(self) -> None:
        from pipeline.openings import build

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for minimum, top in [(1, 10), (200, 0)]:
                with self.subTest(minimum=minimum, top=top), self.assertRaises(ValueError):
                    build(root, root / "output", minimum, top)
            self.assertFalse((root / "output").exists())

    def test_statistics_can_keep_descriptions_in_a_separate_catalog(self) -> None:
        from pipeline.analysis.opening_data import build_observations
        from pipeline.analysis.opening_stats import summarize_openings

        observations, _ = build_observations(*(df.lazy() for df in fixtures()))
        expected = summarize_openings(observations).drop("orders")
        actual = summarize_openings(observations.drop("orders"))
        assert_frame_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
