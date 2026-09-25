"""Markdown presentation of precomputed opening statistics; no data scanning."""

from html import escape

import polars as pl

from .cohorts import POWERS, REPORT_PRESS_LEVELS

PRESS_LABELS = {
    "no_press": "No press",
    "press_with_msgs": "Private messages",
    "public_press": "Public press",
}


def interval(value: float, low: float | None, high: float | None, scale: float = 1) -> str:
    def fmt(x: float) -> str:
        return f"{x:.3f}" if scale == 1 else f"{x * scale:.1f}%"
    if low is None or high is None:
        return fmt(value) + " [unavailable]"
    return f"{fmt(value)} [{fmt(low)}, {fmt(high)}]"


def render_report(
    stats: pl.DataFrame, counts: dict[str, int], min_games: int = 200, top_n: int = 10,
) -> str:
    """Select common openings for display; keep all estimates in the data artifact."""
    if top_n < 1:
        raise ValueError("top_n must be positive")
    lines = [
        "# Spring 1901 opening book",
        f"{counts['included_games']:,} games; {counts['observations']:,} country/game observations. "
        f"Games excluded for not starting in Spring 1901: {counts['excluded_non_s1901_games']:,}.",
        "The cohort uses standard-map in-scope games from no_press, press_with_msgs, and public_press. "
        "Unknown endings and press_without_msgs are excluded. Results describe recorded play in this selected "
        "historical sample; they do not establish the effect of an opening or an optimal strategy. "
        "Player skill and negotiation are not controlled for.",
        f"Each table shows up to {top_n} openings ordered by frequency, with exact orders and preserved coasts. "
        f"Sparse means fewer than {min_games} games in that table's cohort. All openings, including sparse ones, "
        "are retained in openings_own.parquet. The minimum count is a display flag, not proof of reliability.",
        "In a solo game, score is 1 for the winner and 0 for everyone else, including survivors. "
        "In a draw, score is final centers squared divided by the sum of squared final centers across "
        "all powers. Lift is the opening's mean score minus the same country's baseline in that press/quality "
        "cohort. The baseline includes the opening; lift is descriptive, not a significance test.",
        "Brackets show approximate pointwise 95% intervals: Wilson for solo rates, normal mean ± 1.96 standard "
        "errors for scores, clipped to [0,1]. Score intervals are unavailable with fewer than two observations "
        "or zero observed variance; this does not mean the true score is certain. Normal intervals can be "
        "unreliable in sparse groups. Intervals assume independent game observations, are not adjusted for "
        "comparing many openings, and do not account for repeated players or selection bias.",
        "Tier 1 repeats the analysis for games without detected dropout; detection uses terminal all-hold "
        "streaks, so this does not guarantee uninterrupted play. Its baseline is recalculated separately. "
        "Pooled estimates are available as press_level=all in the Parquet, but press modes are separated here.",
    ]
    for power in POWERS:
        lines.append(f"## {power.title()}")
        for press in REPORT_PRESS_LEVELS:
            for quality, label in [("tiers_1_3", "Tiers 1–3"), ("tier_1", "Tier 1")]:
                group = stats.filter(
                    (pl.col("power") == power) & (pl.col("press_level") == press)
                    & (pl.col("quality_group") == quality)
                ).sort(["n_games", "opening_id"], descending=[True, False])
                lines.append(f"### {PRESS_LABELS[press]} — {label}")
                if group.is_empty():
                    lines.append("No observations in this cohort.")
                    continue
                lines += cohort_section(group, min_games, top_n)
    return "\n\n".join(lines) + "\n"


def cohort_section(group: pl.DataFrame, min_games: int, top_n: int) -> list[str]:
    baseline = group.row(0, named=True)
    table = [
        "| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in group.head(top_n).iter_rows(named=True):
        orders = "; ".join(escape(order).replace("|", "&#124;") for order in row["orders"])
        solo = interval(row["solo_rate"], row["solo_ci_low"], row["solo_ci_high"], 100)
        score = interval(row["mean_sos"], row["sos_ci_low"], row["sos_ci_high"])
        evidence = "Sparse" if row["sparse"] else f"n ≥ {min_games}"
        table.append(
            f"| {orders} | {row['n_games']:,} | {row['frequency'] * 100:.1f}% | "
            f"{solo} | {score} | {row['sos_lift']:+.3f} | {evidence} |"
        )
    return [
        f"{baseline['cohort_games']:,} games. Country baseline: "
        f"{baseline['baseline_mean_sos']:.3f} score; {baseline['baseline_solo_rate'] * 100:.1f}% solo.",
        "\n".join(table),
    ]
