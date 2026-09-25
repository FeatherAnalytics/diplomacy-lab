"""Human-readable exact-match reports, with counts and historical outcomes."""

import json
from html import escape

import polars as pl

from .cohorts import POWERS, REPORT_PRESS_LEVELS
from .exact_query import lookup_exact


def describe(sequence_json: str) -> str:
    parts = [f"{step['phase']}: {', '.join(step['orders']) or '(no orders)'}" for step in json.loads(sequence_json)]
    return escape("; ".join(parts)).replace("|", "&#124;")


def render_exact_report(
    observations: pl.DataFrame, sequences: pl.DataFrame, profiles: pl.DataFrame,
    own_rates: pl.DataFrame, top_n: int = 5,
) -> str:
    descriptions = dict(sequences.select("sequence_id", "sequence_json").iter_rows())
    n_games = observations["game_id"].n_unique()
    lines = [
        "# Exact opening histories",
        f"{n_games:,} games. Every number comes from games matching the recorded orders exactly. "
        "There is no smoothing, similarity matching or predictive model. Unseen histories return no exact matches. "
        "One matching game is one historical outcome, not an estimated win probability.",
        "Full 1901 includes Spring and Fall movements plus actual retreat and Winter adjustment orders. "
        "Order within a phase is ignored; phase chronology and coasts are preserved. Empty optional own phases "
        "are omitted; repeated WAIVE orders are preserved. These are recorded adaptive histories, not strategies "
        "committed to before Spring. Same own orders can produce different board positions.",
        "The existing in-scope and source filters apply. Results are conditional on detectable endings. "
        "Tier 1 means no detected terminal dropout; skill and negotiation are not controlled for. "
        "Tables are ordered by match count, not by winning percentage.",
        "The data tables retain every observed sequence. This report shows common sequences "
        "by country, press setting and quality cohort. Use sequence IDs with the lookup command to find matching games. "
        "Game IDs identify dataset records, not WebDiplomacy games.",
        "Mean score averages final sum-of-squares scores: a solo gives the winner 1 and everyone else 0. "
        "In a draw, each country scores its final centers squared divided by the sum of those squares. "
        "Score lift is the difference from the same country's press/quality baseline, which includes the opening. "
        "Finished with centers counts all countries with centers at the end, including solo winners and draw participants. "
        "This is broader than the explorer's Survived category, which excludes Solo and In draw.",
    ]
    for horizon, heading in [("spring1901", "Own Spring"), ("year1901", "Own full 1901")]:
        lines.append(f"## {heading}")
        window = own_rates.filter(pl.col("horizon") == horizon)
        for power in POWERS:
            lines.append(f"### {power.title()}")
            for press in REPORT_PRESS_LEVELS:
                for quality, label in [("tiers_1_3", "Tiers 1–3"), ("tier_1", "Tier 1")]:
                    group = window.filter((pl.col("power") == power) & (pl.col("press_level") == press) & (pl.col("quality_group") == quality))
                    lines.append(f"#### {press} — {label}")
                    if group.is_empty():
                        lines.append("No observations.")
                        continue
                    rows = group.sort(["n_games", "sequence_id"], descending=[True, False]).head(top_n)
                    base = rows.row(0, named=True)
                    lines.append(f"{base['cohort_games']:,} games; country mean-score baseline {base['baseline_mean_sos']:.3f}.")
                    table = ["| Sequence ID | Recorded orders | Matches | Solos | Mean score | Score lift | Evidence |",
                             "|---|---|---:|---:|---:|---:|---|"]
                    for row in rows.iter_rows(named=True):
                        evidence = "One historical game" if row["n_games"] == 1 else "Sparse" if row["sparse"] else "Repeated matches"
                        table.append(f"| {row['sequence_id']} | {describe(descriptions[row['sequence_id']])} | {row['n_games']:,} | {row['n_solos']} | {row['mean_sos']:.3f} | {row['sos_lift']:+.3f} | {evidence} |")
                    lines.append("\n".join(table))

    for horizon, label in [("spring1901", "All countries, Spring"), ("year1901", "All countries, full 1901")]:
        lines.append(f"## {label}")
        game_profiles = observations.filter(pl.col("horizon") == horizon).select("game_id", "joint_id", "press_level").unique()
        counts = game_profiles.group_by("joint_id").len()
        lines.append(f"Across the pooled sources: {counts.height:,} exact profiles; {(counts['len'] == 1).sum():,} appear once; "
                     f"largest match count {counts['len'].max()}. The following examples are separated by press setting. "
                     "All profiles are retained for exact lookup, even when only one game matches.")
        for press in REPORT_PRESS_LEVELS:
            top = game_profiles.filter(pl.col("press_level") == press).group_by("joint_id").len().sort(["len", "joint_id"], descending=[True, False])
            # One example suffices when every history is unique; the catalog retains all.
            shown = 1 if top.height and top["len"].max() == 1 else min(top_n, 3)
            for pattern in top.head(shown).iter_rows(named=True):
                pid = pattern["joint_id"]
                lines.append(f"### {press}: {pid}")
                result = lookup_exact(observations.lazy(), horizon=horizon, context="all", pattern_id=pid, press_level=press)
                lines.append(f"{result['n_matches']} exact matches (tiers 1–3). Example game IDs: {', '.join(result['game_ids'])}.")
                if result["n_matches"] == 1:
                    lines.append("One historical game: the following counts and scores are its observed outcome, not win probabilities.")
                sequence_ids = profiles.filter(pl.col("joint_id") == pid)["sequence_ids"][0].to_list()
                outcome_map = {row["power"]: row for row in result["outcomes"]}
                table = ["| Country | Recorded orders | Solos | Draw participation | Finished with centers | Mean score |",
                         "|---|---|---:|---:|---:|---:|"]
                for power, sid in zip(POWERS, sequence_ids):
                    row = outcome_map[power]
                    table.append(f"| {power.title()} | {describe(descriptions[sid])} | {row['n_solos']} | {row['n_draws']} | {row['n_survived']} | {row['mean_sos']:.3f} |")
                lines.append("\n".join(table))
                clean = lookup_exact(observations.lazy(), horizon=horizon, context="all", pattern_id=pid, press_level=press, quality_group="tier_1")
                lines.append(f"Tier 1 exact matches for this same profile: {clean['n_matches']}. Use the lookup's tier_1 filter for those outcomes.")
    return "\n\n".join(lines) + "\n"
