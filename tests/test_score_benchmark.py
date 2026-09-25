"""Hand-counted estimator checks and end-to-end leakage regression."""

import unittest
import contextlib
import hashlib
import io
import json
import tempfile
from pathlib import Path

import polars as pl

from pipeline.analysis.score_benchmark import (
    STRENGTHS, assign_splits, attach_estimates, choose_strength, context_frames,
    evaluate, predict, run_experiment,
)
from pipeline.analysis.cohorts import POWERS
from pipeline.score_benchmark import load_observations, run


def rows(games):
    return pl.DataFrame([
        dict(game_id=game, power=power, sequence_id=pattern, joint_id=f"joint-{game}",
             horizon="spring1901", quality_tier=1, press_level="no_press", sos_score=score)
        for game, entries in games.items() for power, pattern, score in entries
    ])


class ScoreBenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.train = rows({
            "a": [("france", "bur", 1.), ("england", "nth", 0.)],
            "b": [("france", "bur", .2), ("england", "eng", .8)],
            "c": [("france", "pic", 0.), ("england", "nth", 1.)],
        })
        self.test = rows({
            "x": [("france", "bur", .3), ("england", "unknown", .7)],
        })

    def test_splits_follow_game_not_country_horizon_or_order(self):
        data = pl.concat([self.train, self.train.with_columns(pl.lit("year1901").alias("horizon"))])
        a = assign_splits(data, seed=1901)
        b = assign_splits(data.reverse(), seed=1901)
        self.assertEqual(a.sort("game_id").to_dicts(), b.sort("game_id").to_dicts())
        self.assertEqual(a.height, 3)
        self.assertEqual(a["game_id"].n_unique(), 3)

    def test_estimates_use_only_training_scores_and_weight_games(self):
        training = next(context_frames(self.train, "own"))
        test = next(context_frames(self.test, "own"))
        frame = attach_estimates(training, test)
        france = frame.filter(pl.col("power") == "france")
        self.assertAlmostEqual(france["baseline"].item(), .4)
        self.assertEqual(france["support"].item(), 2)
        self.assertAlmostEqual(france["exact"].item(), .6)
        self.assertAlmostEqual(france.select(predict(2)).item(), .5)
        self.assertAlmostEqual(france.select(predict(0)).item(), .6)
        self.assertAlmostEqual(france.select(predict("baseline")).item(), .4)
        changed = test.with_columns((1 - pl.col("sos_score")).alias("sos_score"))
        self.assertEqual(frame.drop("sos_score").to_dicts(), attach_estimates(training, changed).drop("sos_score").to_dicts())
        england = frame.filter(pl.col("power") == "england")
        self.assertIsNone(england["exact"].item())
        self.assertEqual(england["support"].item(), 0)
        self.assertAlmostEqual(england.select(predict(2)).item(), .6)

    def test_overlap_is_rejected(self):
        frame = next(context_frames(self.train, "own"))
        with self.assertRaisesRegex(ValueError, "overlap"):
            attach_estimates(frame, frame)

    def test_pairs_require_both_countries_in_the_same_game(self):
        pair = list(context_frames(self.train, "pairs"))
        self.assertEqual(len(pair), 1)
        self.assertEqual(pair[0].height, 6)
        self.assertEqual(pair[0]["pattern"].n_unique(), 3)
        joint = next(context_frames(self.train, "all"))
        self.assertEqual(joint["pattern"].n_unique(), 3)

    def test_validation_selects_strength_and_ties_prefer_baseline(self):
        training = next(context_frames(self.train, "own"))
        validation = next(context_frames(rows({"v": [("france", "bur", .4)]}), "own"))
        strength, curve = choose_strength([attach_estimates(training, validation)])
        self.assertEqual(strength, "baseline")
        self.assertEqual(len(curve), len(STRENGTHS))
        unknown = validation.with_columns(pl.lit("missing").alias("pattern"))
        self.assertEqual(choose_strength([attach_estimates(training, unknown)])[0], "baseline")

    def test_metrics_compare_identical_cases_and_expose_abstentions(self):
        training = next(context_frames(self.train, "own"))
        test = next(context_frames(self.test, "own"))
        frame = attach_estimates(training, test).with_columns(predict(2).alias("shrinkage"))
        result = evaluate(frame)
        self.assertEqual(result["all"]["n_cases"], 2)
        self.assertEqual(result["all"]["n_games"], 1)
        self.assertEqual(result["exact_coverage"], .5)
        self.assertIsNone(result["all"]["exact"])
        self.assertAlmostEqual(result["all"]["baseline"]["mse"], .01)
        self.assertAlmostEqual(result["all"]["shrinkage"]["mse"], .025)
        self.assertAlmostEqual(result["matched"]["exact"]["mse"], .09)
        self.assertAlmostEqual(result["matched"]["shrinkage"]["mse"], .04)
        self.assertIsNone(result["paired_mse"]["shrinkage_vs_baseline_all"]["ci_low"])

    def test_test_labels_cannot_change_tuning_or_predictions(self):
        validation = rows({"v": [("france", "bur", .4), ("england", "nth", .6)]})
        data = pl.concat([self.train, validation, self.test])
        splits = pl.DataFrame({"game_id": ["a", "b", "c", "v", "x"], "split": ["train"] * 3 + ["validation", "test"]})
        a = run_experiment(data, splits, "own")
        changed = data.with_columns(pl.when(pl.col("game_id") == "x").then(1 - pl.col("sos_score")).otherwise(pl.col("sos_score")).alias("sos_score"))
        b = run_experiment(changed, splits, "own")
        self.assertEqual(a["strength"], b["strength"])
        self.assertEqual(a["validation"], b["validation"])
        self.assertNotEqual(a["test"]["all"]["baseline"]["mse"], b["test"]["all"]["baseline"]["mse"])
        self.assertEqual(a["fit_games"], 4)

    def test_paired_interval_does_not_treat_repeated_game_rows_as_independent(self):
        frame = pl.DataFrame({"game_id": ["a", "b"], "power": ["france"] * 2,
            "sos_score": [0., 1.], "support": [1, 1], "baseline": [.5, .5],
            "exact": [0., 1.], "shrinkage": [.25, .5]})
        a = evaluate(frame)["paired_mse"]
        b = evaluate(pl.concat([frame] * 6))["paired_mse"]
        self.assertEqual(a, b)
        comparison = a["shrinkage_vs_baseline_all"]
        self.assertAlmostEqual(comparison["difference"], -.09375)
        self.assertAlmostEqual(comparison["ci_low"], -.2775)
        self.assertAlmostEqual(comparison["ci_high"], .09)

    def test_verified_pipeline_and_manifest_reject_modified_input(self):
        data = pl.DataFrame([dict(game_id=f"game-{game}", power=power,
            sequence_id=f"{power}-{game % 3}", joint_id=f"joint-{game % 3}", horizon=horizon,
            quality_tier=1 if game % 2 else 2, press_level="no_press",
            sos_score=float(index == game % 7))
            for game in range(80) for horizon in ("spring1901", "year1901")
            for index, power in enumerate(POWERS)])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "opening_exact_observations.parquet"
            data.write_parquet(path)
            (root / "opening_exact_manifest.json").write_text(json.dumps({"schema_version": 1,
                "built_at_utc": "2026-09-25", "outputs": [{"name": path.name,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}]}))
            self.assertEqual(load_observations(root)[0].height, 1120)
            with contextlib.redirect_stdout(io.StringIO()):
                manifest = run(root, root / "benchmark")
            self.assertEqual(len(json.loads((root / "benchmark/results.json").read_text())), 12)
            for entry in manifest["outputs"]:
                self.assertEqual(hashlib.sha256((root / "benchmark" / entry["name"]).read_bytes()).hexdigest(), entry["sha256"])
            splits = pl.read_parquet(root / "benchmark/split_assignments.parquet")
            self.assertEqual(splits.height, 80)
            self.assertEqual(splits["game_id"].n_unique(), 80)
            path.write_bytes(b"tampered")
            with self.assertRaisesRegex(ValueError, "manifest"):
                load_observations(root)


if __name__ == "__main__":
    unittest.main()
