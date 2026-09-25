"""Report exact-pair repetition separately from historical outcome examples."""

import polars as pl

from .cohorts import REPORT_PRESS_LEVELS
from .exact_report import describe


def render_pair_report(coverage: pl.DataFrame, examples: pl.DataFrame, sequences: pl.DataFrame) -> str:
    descriptions = dict(sequences.select("sequence_id", "sequence_json").iter_rows())
    lines = ["# Exact matches for country pairs",
        "Each match requires both countries' recorded orders in the same game. The other five countries may vary. "
        "All 21 pairs are included for Spring and full 1901. Selected-country lookup also supports any larger "
        "combination and can return outcomes for any country, including an unselected one.",
        "Coverage measures how often exact patterns repeat, not whether a pair is strategically good. "
        "The threshold is a configurable sample-size flag, not proof of reliability. "
        "Games in repeated patterns means games whose pattern appears at least twice within that same cohort. "
        "Each pair partitions its cohort; rows for different pairs overlap and must not be added together.",
        "The existing scope, detectable-ending sources and quality filters apply. Tier 1 means no detected "
        "terminal dropout. Outcomes are descriptive; skill and negotiation are not controlled for. "
        "Full-year histories include adaptive Fall, retreat and Winter decisions. Exact orders need not imply identical board states.",
        "Each pair's most frequent pattern is shown below its coverage table, with counts and observed rates. "
        "A single match is one historical outcome, with rate fields unavailable. Unseen patterns return no exact matches. "
        "The examples Parquet contains the configured top N patterns per pair/cohort; lookup retains access to every pattern. "
        "Pooled-source summaries are available in Parquet; this report separates communication settings.",
        "Mean score averages final sum-of-squares scores: a solo gives the winner 1 and everyone else 0. "
        "In a draw, each country scores its final centers squared divided by the sum of those squares. "
        "Finished with centers includes solo winners and draw participants; it is broader than the explorer's Survived category. "
        "Dataset game IDs are not WebDiplomacy game IDs."]
    for horizon, label in [("spring1901", "Spring 1901"), ("year1901", "Full 1901")]:
        lines.append(f"## {label}")
        for press in REPORT_PRESS_LEVELS:
            for quality, title in [("tiers_1_3", "Tiers 1–3"), ("tier_1", "Tier 1")]:
                condition = ((pl.col("horizon") == horizon) & (pl.col("press_level") == press) & (pl.col("quality_group") == quality))
                group = coverage.filter(condition).sort(["games_at_threshold", "games_in_repeated_patterns", "power_a", "power_b"], descending=[True, True, False, False])
                lines.append(f"### {press} — {title}")
                if group.is_empty():
                    lines.append("No observations.")
                    continue
                threshold = group["min_games"][0]
                lines.append(f"{group['cohort_games'][0]:,} games in this cohort. Threshold: {threshold:,} matches.")
                table = [f"| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ {threshold} | Games ≥ {threshold} | Largest match count |",
                         "|---|---:|---:|---:|---:|---:|---:|"]
                for row in group.iter_rows(named=True):
                    table.append(f"| {row['power_a'].title()} / {row['power_b'].title()} | {row['n_patterns']:,} | {row['singleton_patterns']:,} | {row['games_in_repeated_patterns']:,} | {row['patterns_at_threshold']:,} | {row['games_at_threshold']:,} | {row['max_matches']:,} |")
                lines.append("\n".join(table))
                cohort_examples = examples.filter(condition)
                for pair in group.iter_rows(named=True):
                    row = cohort_examples.filter((pl.col("power_a") == pair["power_a"]) & (pl.col("power_b") == pair["power_b"])).row(0, named=True)
                    lines.append(f"#### {row['power_a'].title()} / {row['power_b'].title()} — {row['n_games']:,} matches")
                    if row["n_games"] == 1:
                        lines.append("One historical game; outcome rates are unavailable.")
                    elif row["sparse"]:
                        lines.append("Below the sample-size threshold; these are observed fractions from a sparse sample.")
                    result = ["| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |",
                              "|---|---|---:|---:|---:|---:|---:|---:|"]
                    for side in ("a", "b"):
                        solo = row[f"solo_rate_{side}"]
                        draw = row[f"draw_rate_{side}"]
                        solo_text = "—" if solo is None else f"{solo:.1%}"
                        draw_text = "—" if draw is None else f"{draw:.1%}"
                        result.append(f"| {row[f'power_{side}'].title()} | {describe(descriptions[row[f'sequence_id_{side}']])} | {row[f'n_solos_{side}']} | {solo_text} | {row[f'n_draws_{side}']} | {draw_text} | {row[f'n_survived_{side}']} | {row[f'mean_sos_{side}']:.3f} |")
                    lines.append("\n".join(result))
                    lines.append("```sh\nuv run python -m pipeline.exact_openings lookup "
                        f"--horizon {horizon} --context selected --press-level {press} --quality-group {quality} "
                        f"--select {row['power_a']}={row['sequence_id_a']} --select {row['power_b']}={row['sequence_id_b']}\n```")
    return "\n\n".join(lines) + "\n"
