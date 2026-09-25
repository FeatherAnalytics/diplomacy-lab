"""Regression checks: python -m unittest discover -s tests -v."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import polars as pl

from pipeline.outcome_rates import POWERS, game_outcomes

ROOT = Path(__file__).resolve().parents[1]


def game(game_id: str, press_level: str, ending: str, tier: int = 1) -> dict:
    centers = [18, 10, 6, 0, 0, 0, 0] if ending == "solo" else [0, 17, 17, 0, 0, 0, 0]
    return {
        "game_id": game_id,
        "press_level": press_level,
        "quality_tier": tier,
        "ending": ending,
        "ended_by_vote": True,
        "in_scope": True,
        **{f"centers_{power}": count for power, count in zip(POWERS, centers)},
    }


class OutcomeRatesTests(unittest.TestCase):
    def test_solo_with_empty_terminal_orders_has_no_draw_participants(self) -> None:
        outcomes = game_outcomes(pl.DataFrame([game("solo", "no_press", "solo")]))
        self.assertEqual(outcomes["draw_vote"].sum(), 0)
        self.assertEqual(outcomes["solo"].sum(), 1)
        self.assertEqual(outcomes["survived"].sum(), 3)
        self.assertEqual(outcomes.filter(pl.col("power") == "austria")["sos_score"].item(), 1)
        self.assertEqual(outcomes["sos_score"].sum(), 1)

    def test_draw_participation_requires_survival_and_scores_are_normalized(self) -> None:
        outcomes = game_outcomes(pl.DataFrame([game("draw", "no_press", "draw_vote")]))
        participants = outcomes.filter("draw_vote").sort("power")
        self.assertEqual(participants["power"].to_list(), ["england", "france"])
        self.assertEqual(participants["sos_score"].to_list(), [0.5, 0.5])
        self.assertEqual(outcomes["solo"].sum(), 0)
        self.assertEqual(outcomes["sos_score"].sum(), 1)

    def test_cli_restricts_report_but_preserves_all_eligible_scores(self) -> None:
        rows = [
            game("gunboat", "no_press", "draw_vote"),
            game("messages", "press_with_msgs", "solo", tier=3),
            game("public", "public_press", "solo"),
            game("selected", "press", "solo"),
            game("excluded", "no_press", "solo"),
        ]
        rows[-1]["in_scope"] = False
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            pl.DataFrame(rows).write_parquet(out / "games.parquet")
            reference = out / "reference.csv"
            pl.DataFrame({"Country": POWERS, "Lost": [1] * 7, "Won": [1] * 7, "2-way Draw": [1] * 7}).write_csv(reference)
            result = subprocess.run(
                [sys.executable, "-m", "pipeline.outcome_rates", str(out), str(reference)],
                check=True, capture_output=True, text=True,
            )
            outcomes = pl.read_parquet(out / "game_outcomes.parquet")
            report = (out / "outcome_rates.md").read_text()
        self.assertEqual(outcomes.height, 28)
        self.assertEqual(set(outcomes["game_id"]), {"gunboat", "messages", "public", "selected"})
        self.assertIn("Report cohort: 3 games", report)
        self.assertNotIn("| press |", report)
        self.assertIn("| austria | 3 | 66.7 |", report)
        self.assertIn("| austria | 3 | 66.7 |", result.stdout)
        self.assertIn("Tier 1 only (2 games)", report)
        self.assertIn("| austria | 2 | 50.0 |", report)


if __name__ == "__main__":
    unittest.main()
