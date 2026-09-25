"""Exact-context tests with full-year fixtures and hand-checked outcomes."""

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal

from test_openings import fixtures
from pipeline.analysis.opening_data import build_observations

ROOT = Path(__file__).resolve().parents[1]


def year_fixtures() -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
    games, spring, outcomes = fixtures()
    spring = spring.filter(pl.col("phase_idx") == 0)
    rows = []
    for original in spring.iter_rows(named=True):
        if original["game_id"] == "late":
            rows.append(original)
            continue
        rows.append(original)
        # Only game b has a retreat phase; Austria has no retreat orders there.
        if original["game_id"] == "b":
            rows.append({**original, "phase_idx": 1, "phase_name": "S1901R",
                         "orders": ["A PAR R GAS"] if original["power"] == "FRANCE" else [],
                         "n_orders": 1 if original["power"] == "FRANCE" else 0})
        offset = int(original["game_id"] == "b")
        orders = sorted(original["orders"])
        if original["game_id"] == "e" and original["power"] == "ENGLAND":
            orders[0] = "A LVP - WAL"
        rows.append({**original, "phase_idx": 1 + offset, "phase_name": "F1901M", "orders": orders})
        winter = ["WAIVE", "WAIVE"] if original["power"] == "TURKEY" else []
        rows.append({**original, "phase_idx": 2 + offset, "phase_name": "W1901A",
                     "orders": winter, "n_orders": len(winter)})
        rows.append({**original, "phase_idx": 3 + offset, "phase_name": "S1902M",
                     "adjudicated": False, "orders": None, "n_orders": None})
    return games, pl.DataFrame(rows), outcomes


class ExactOpeningTests(unittest.TestCase):
    def data(self):
        from pipeline.analysis.exact_data import build_exact_data

        games, phases, outcomes = year_fixtures()
        spring, counts = build_observations(games.lazy(), phases.lazy(), outcomes.lazy())
        return build_exact_data(spring, phases.lazy()), counts

    def test_cli_publishes_all_four_views_and_supports_exact_lookup(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, df in zip(["games", "phases", "game_outcomes"], year_fixtures()):
                df.write_parquet(root / f"{name}.parquet")
            cmd = [sys.executable, "-m", "pipeline.exact_openings"]
            run = subprocess.run(cmd + ["build", "--data-dir", str(root), "--output-dir", str(root / "out"), "--top-n", "2"], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            out = root / "out"
            obs = pl.read_parquet(out / "opening_exact_observations.parquet")
            self.assertEqual(obs.height, 70)
            rates = pl.read_parquet(out / "opening_exact_own_rates.parquet")
            singleton = rates.filter(pl.col("n_games") == 1)
            for column in ["solo_rate", "draw_rate", "survival_rate", "solo_ci_low", "solo_ci_high"]:
                self.assertTrue(singleton[column].is_null().all(), column)
            self.assertTrue(singleton["n_draws"].is_not_null().all())
            self.assertTrue(singleton["n_survived"].is_not_null().all())
            manifest = json.loads((out / "opening_exact_manifest.json").read_text())
            for entry in manifest["outputs"]:
                self.assertEqual(hashlib.sha256((out / entry["name"]).read_bytes()).hexdigest(), entry["sha256"])
            profile = obs.filter((pl.col("game_id") == "a") & (pl.col("horizon") == "spring1901"))["joint_id"][0]
            query = subprocess.run(cmd + ["lookup", "--data-dir", str(out), "--horizon", "spring1901", "--context", "all", "--pattern-id", profile, "--press-level", "no_press"], capture_output=True, text=True)
            self.assertEqual(query.returncode, 0, query.stderr)
            result = json.loads(query.stdout)
            self.assertEqual(result["n_matches"], 2)
            self.assertEqual(result["game_ids"], ["a", "b"])
            report = (out / "opening_exact.md").read_text()
            for label in ["Own Spring", "Own full 1901", "All countries, Spring", "All countries, full 1901"]:
                self.assertIn(label, report)
            spring_section = report.split("## Own Spring\n", 1)[1].split("## Own full 1901\n", 1)[0]
            self.assertIn("A BUD H", spring_section)

    def test_optional_empty_phases_do_not_split_own_histories(self) -> None:
        (obs, sequences, profiles), _ = self.data()
        own = obs.filter((pl.col("horizon") == "year1901") & (pl.col("power") == "austria") & pl.col("game_id").is_in(["a", "b"]))
        self.assertEqual(own["sequence_id"].n_unique(), 1)
        self.assertEqual(own["joint_id"].n_unique(), 2)
        turkey = obs.filter((pl.col("horizon") == "year1901") & (pl.col("power") == "turkey"))["sequence_id"][0]
        history = json.loads(sequences.filter(pl.col("sequence_id") == turkey)["sequence_json"].item())
        self.assertEqual(history[-1], {"phase": "W1901A", "orders": ["WAIVE", "WAIVE"]})
        self.assertEqual(profiles.select(pl.struct("horizon", "joint_id").n_unique()).item(), profiles.height)

    def test_missing_or_duplicate_year_data_fails(self) -> None:
        from pipeline.analysis.exact_data import build_exact_data

        games, phases, outcomes = year_fixtures()
        spring, _ = build_observations(games.lazy(), phases.lazy(), outcomes.lazy())
        bad = [
            phases.filter(~((pl.col("game_id") == "a") & (pl.col("phase_name") == "F1901M"))),
            phases.filter(pl.col("phase_name") != "S1902M"),
            pl.concat([phases, phases.head(1)]),
            phases.with_columns(pl.when(pl.col("phase_name") == "W1901A").then(None).otherwise(pl.col("orders")).alias("orders")),
            phases.with_columns(pl.col("phase_idx").replace({0: 1, 1: 0})),
        ]
        for frame in bad:
            with self.subTest(rows=frame.height), self.assertRaises(ValueError):
                build_exact_data(spring, frame.lazy())

    def test_lookups_return_observed_counts_without_fallbacks(self) -> None:
        from pipeline.analysis.exact_query import lookup_exact

        (obs, _, _), _ = self.data()
        pattern = obs.filter((pl.col("game_id") == "a") & (pl.col("horizon") == "spring1901"))["joint_id"][0]
        result = lookup_exact(obs.lazy(), horizon="spring1901", context="all", pattern_id=pattern, press_level="no_press")
        self.assertEqual(result["n_matches"], 2)
        self.assertEqual(result["game_ids"], ["a", "b"])
        austria = next(r for r in result["outcomes"] if r["power"] == "austria")
        self.assertEqual(austria["n_solos"], 1)
        self.assertEqual(austria["observed_solo_rate"], 0.5)
        self.assertEqual(austria["mean_sos"], 0.5)
        single = lookup_exact(obs.lazy(), horizon="spring1901", context="all", pattern_id=pattern, press_level="no_press", quality_group="tier_1")
        self.assertEqual(single["status"], "single_historical_game")
        self.assertTrue(all(r["observed_solo_rate"] is None for r in single["outcomes"]))
        missing = lookup_exact(obs.lazy(), horizon="year1901", context="all", pattern_id="unseen")
        self.assertEqual(missing["status"], "no_exact_matches")
        self.assertEqual(missing["outcomes"], [])
        self.assertEqual(missing["game_ids"], [])
        with self.assertRaises(ValueError):
            lookup_exact(obs.lazy(), horizon="spring1901", context="own", pattern_id=pattern)

    def test_spring_identity_remains_compatible_and_no_future_orders_leak(self) -> None:
        from pipeline.analysis.exact_data import build_exact_data

        games, phases, outcomes = year_fixtures()
        spring, _ = build_observations(games.lazy(), phases.lazy(), outcomes.lazy())
        obs, _, _ = build_exact_data(spring, phases.lazy())
        reordered = phases.reverse().with_columns(pl.col("orders").list.reverse())
        assert_frame_equal(obs, build_exact_data(spring, reordered.lazy())[0])
        coasts = phases.with_columns(pl.col("orders").list.eval(pl.element().str.replace("STP/SC", "STP/NC")))
        different_coasts = build_exact_data(spring, coasts.lazy())[0]
        russia_year = (pl.col("power") == "russia") & (pl.col("horizon") == "year1901")
        self.assertNotEqual(obs.filter(russia_year)["sequence_id"].to_list(), different_coasts.filter(russia_year)["sequence_id"].to_list())
        joined = obs.filter(pl.col("horizon") == "spring1901").join(spring, on=["game_id", "power"])
        self.assertTrue(joined.select((pl.col("sequence_id") == pl.col("opening_id")).all()).item())
        changed = phases.with_columns(pl.when(pl.col("phase_name") == "W1901A").then(pl.lit(["WAIVE"])).otherwise(pl.col("orders")).alias("orders")).with_columns(pl.col("orders").list.len().alias("n_orders"))
        other, _, _ = build_exact_data(spring, changed.lazy())
        left = obs.filter(pl.col("horizon") == "spring1901").sort("game_id", "power")
        right = other.filter(pl.col("horizon") == "spring1901").sort("game_id", "power")
        self.assertEqual(left["joint_id"].to_list(), right["joint_id"].to_list())


if __name__ == "__main__":
    unittest.main()
