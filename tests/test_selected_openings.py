"""Hand-counted tests for intersecting country histories within a game."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import polars as pl

from pipeline.analysis.cohorts import POWERS
from pipeline.analysis.exact_query import lookup_exact


def observations() -> pl.DataFrame:
    rows = []
    for horizon in ("spring1901", "year1901"):
        for game in "abcdef":
            for power in POWERS:
                variant = int((game, power) in [("b", "france"), ("c", "england"), ("d", "austria")])
                rows.append(dict(horizon=horizon, game_id=game, power=power,
                    sequence_id=f"{horizon}:{power}:{variant}", joint_id=f"{horizon}:{game}",
                    press_level="public_press" if game == "e" else "no_press",
                    quality_tier=2 if game == "f" else 1,
                    solo=game == "a" and power == "austria", survived=True,
                    draw_vote=game != "a", sos_score=float(power == "austria") if game == "a" else 1/7))
    return pl.DataFrame(rows)


class SelectedOpeningTests(unittest.TestCase):
    def query(self, **options):
        settings = dict(horizon="spring1901", context="selected",
                        selections={p: f"spring1901:{p}:0" for p in ("austria", "england")},
                        press_level="no_press")
        return lookup_exact(observations().lazy(), **(settings | options))

    def test_intersection_ignores_unselected_moves_and_keeps_all_outcomes(self):
        result = self.query(limit=1)
        self.assertEqual(result["n_matches"], 3)
        self.assertEqual(result["game_ids"], ["a"])
        self.assertTrue(result["game_ids_truncated"])
        self.assertEqual(len(result["outcomes"]), 7)
        austria = result["outcomes"][0]
        self.assertEqual(austria["n_solos"], 1)
        self.assertAlmostEqual(austria["observed_solo_rate"], 1/3)
        self.assertEqual(self.query(quality_group="tier_1")["game_ids"], ["a", "b"])
        outside = self.query(power="france")
        self.assertEqual(outside["n_matches"], 3)
        self.assertEqual([r["power"] for r in outside["outcomes"]], ["france"])
        self.assertEqual(self.query(press_level="all")["n_matches"], 4)

    def test_zero_singleton_one_country_and_seven_countries(self):
        one = self.query(press_level="public_press")
        self.assertEqual(one["status"], "single_historical_game")
        self.assertTrue(all(r["observed_solo_rate"] is None for r in one["outcomes"]))
        missing = self.query(selections={"austria": "unseen"})
        self.assertEqual((missing["n_matches"], missing["outcomes"]), (0, []))
        own = self.query(selections={"austria": "spring1901:austria:0"}, power="austria")
        old = lookup_exact(observations().lazy(), horizon="spring1901", context="own",
                           pattern_id="spring1901:austria:0", power="austria", press_level="no_press")
        self.assertEqual(own["outcomes"], old["outcomes"])
        self.assertEqual(own["game_ids"], old["game_ids"])
        all_powers = {p: f"year1901:{p}:0" for p in POWERS}
        result = self.query(horizon="year1901", selections=all_powers, quality_group="tier_1")
        self.assertEqual(result["game_ids"], ["a"])
        reverse = self.query(horizon="year1901", selections=dict(reversed(list(all_powers.items()))), quality_group="tier_1")
        self.assertEqual(result, reverse)

    def test_invalid_or_ambiguous_selectors_fail(self):
        for options in [dict(selections={}), dict(selections={"unknown": "id"}),
                        dict(selections={"austria": ""}), dict(pattern_id="id"),
                        dict(context="all", pattern_id="id")]:
            with self.subTest(options=options), self.assertRaises(ValueError):
                self.query(**options)

    def test_pair_summary_counts_games_not_power_rows(self):
        from pipeline.analysis.exact_pairs import summarize_pairs

        coverage, examples = summarize_pairs(observations(), min_games=3, top_n=1)
        row = coverage.filter((pl.col("horizon") == "spring1901") &
            (pl.col("press_level") == "no_press") & (pl.col("quality_group") == "tiers_1_3") &
            (pl.col("power_a") == "austria") & (pl.col("power_b") == "england")).row(0, named=True)
        self.assertEqual(row["cohort_games"], 5)
        self.assertEqual(row["n_patterns"], 3)
        self.assertEqual(row["singleton_patterns"], 2)
        self.assertEqual(row["games_in_repeated_patterns"], 3)
        self.assertEqual(row["patterns_at_threshold"], 1)
        self.assertEqual(row["games_at_threshold"], 3)
        self.assertEqual(row["max_matches"], 3)
        sample = examples.filter((pl.col("horizon") == "spring1901") &
            (pl.col("press_level") == "no_press") & (pl.col("quality_group") == "tiers_1_3") &
            (pl.col("power_a") == "austria") & (pl.col("power_b") == "england")).row(0, named=True)
        self.assertEqual(sample["n_games"], 3)
        self.assertEqual(sample["n_solos_a"], 1)
        self.assertEqual(sample["n_draws_b"], 2)
        self.assertAlmostEqual(sample["solo_rate_a"], 1/3)
        self.assertTrue(examples.filter(pl.col("n_games") == 1)["solo_rate_a"].is_null().all())
        self.assertEqual(coverage.filter((pl.col("horizon") == "year1901") &
            (pl.col("press_level") == "all") & (pl.col("quality_group") == "tier_1")).height, 21)

    def test_cli_build_report_and_selected_lookup(self):
        from test_exact_openings import year_fixtures

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, frame in zip(("games", "phases", "game_outcomes"), year_fixtures()):
                frame.write_parquet(root / f"{name}.parquet")
            cmd = [sys.executable, "-m", "pipeline.exact_openings"]
            built = subprocess.run(cmd + ["build", "--data-dir", tmp, "--output-dir", tmp, "--top-n", "1"], capture_output=True, text=True)
            self.assertEqual(built.returncode, 0, built.stderr)
            self.assertTrue((root / "opening_exact_pairs.md").exists())
            report = (root / "opening_exact_pairs.md").read_text()
            self.assertIn("Austria / England", report)
            self.assertIn("Spring 1901", report)
            self.assertIn("Full 1901", report)
            self.assertIn("A BUD H", report)
            obs = pl.read_parquet(root / "opening_exact_observations.parquet")
            selection = dict(obs.filter((pl.col("game_id") == "a") & (pl.col("horizon") == "spring1901") & pl.col("power").is_in(["austria", "england"])).select("power", "sequence_id").iter_rows())
            args = ["lookup", "--data-dir", tmp, "--horizon", "spring1901", "--context", "selected", "--press-level", "no_press", "--power", "france"]
            for power, sequence in selection.items():
                args += ["--select", f"{power}={sequence}"]
            queried = subprocess.run(cmd + args, capture_output=True, text=True)
            self.assertEqual(queried.returncode, 0, queried.stderr)
            self.assertEqual(json.loads(queried.stdout)["n_matches"], 2)
            duplicate = subprocess.run(cmd + args + ["--select", f"austria={selection['austria']}"], capture_output=True, text=True)
            self.assertNotEqual(duplicate.returncode, 0)
            self.assertIn("Duplicate", duplicate.stderr)
