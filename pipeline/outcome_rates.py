"""Per-power outcome rates and sum-of-squares scores from games.parquet.

Usage: uv run python -m pipeline.outcome_rates [data/processed] [data/raw/playdiplomacy/diplomacy-data.csv]

Writes game_outcomes.parquet for all in-scope games and outcome_rates.md for
the three sources with detectable draws, including a tier-1 sensitivity table.
"""

import sys
from pathlib import Path

import polars as pl

from .analysis.cohorts import POWERS, REPORT_PRESS_LEVELS

SOLO_CENTERS = 18

# Sum-of-squares scoring: a power with SOLO_CENTERS or more scores 1 and everyone else 0;
# otherwise each power scores centers^2 / sum(centers^2). Scores in a game sum to 1.


def game_outcomes(games: pl.DataFrame) -> pl.DataFrame:
    index = ["game_id", "press_level", "quality_tier", "ending"]
    long = (
        games.select(*index, *[f"centers_{p}" for p in POWERS])
        .unpivot(index=index, variable_name="power", value_name="final_centers")
        .with_columns(pl.col("power").str.strip_prefix("centers_"))
    )
    centers = pl.col("final_centers")
    solo = centers >= SOLO_CENTERS
    sq = centers.pow(2)
    return long.with_columns(
        survived=centers > 0,
        solo=solo,
        draw_vote=(centers > 0) & (pl.col("ending") == "draw_vote"),
        sos_score=pl.when(solo.any().over("game_id")).then(solo.cast(pl.Float64)).otherwise(sq / sq.sum().over("game_id")),
    ).drop("ending")


def md_table(df: pl.DataFrame) -> str:
    lines = ["| " + " | ".join(df.columns) + " |", "|---" * df.width + "|"]
    lines += ["| " + " | ".join(str(v) for v in row) + " |" for row in df.iter_rows()]
    return "\n".join(lines)


def pct(expr: pl.Expr) -> pl.Expr:
    return (expr.mean() * 100).round(1)


def rates_table(outcomes: pl.DataFrame) -> str:
    agg = outcomes.group_by("power").agg(
        pl.len().alias("games"),
        pct(pl.col("solo")).alias("solo %"),
        pct(pl.col("draw_vote")).alias("in draw vote %"),
        pct(pl.col("survived") & ~pl.col("solo")).alias("finished with centers (excluding solos) %"),
        pct(~pl.col("survived")).alias("eliminated %"),
        pl.col("final_centers").mean().round(2).alias("mean final SC"),
        pl.col("sos_score").mean().round(3).alias("mean SoS score"),
    )
    return md_table(agg.sort("power"))


def by_press_table(outcomes: pl.DataFrame, metric: pl.Expr) -> str:
    wide = (
        outcomes.group_by("press_level", "power").agg(pct(metric).alias("v"))
        .pivot(on="power", index="press_level", values="v")
        .select("press_level", *POWERS)
    )
    return md_table(wide.sort("press_level"))


def playdip_table(path: Path) -> str:
    df = pl.read_csv(path)
    draw_cols = [c for c in df.columns if c.endswith("Draw")]
    total = pl.sum_horizontal("Lost", "Won", *draw_cols)
    out = df.select(
        pl.col("Country").str.to_lowercase().alias("power"),
        total.cast(pl.Int64).alias("games"),
        (pl.col("Won") / total * 100).round(1).alias("solo %"),
        (pl.sum_horizontal(*draw_cols) / total * 100).round(1).alias("draw %"),
        (pl.col("Lost") / total * 100).round(1).alias("lost %"),
    )
    return md_table(out.sort("power"))


def main() -> None:
    out_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "data/processed")
    playdip = Path(sys.argv[2] if len(sys.argv) > 2 else "data/raw/playdiplomacy/diplomacy-data.csv")

    games = pl.read_parquet(out_dir / "games.parquet").filter(pl.col("in_scope"))
    outcomes = game_outcomes(games)
    outcomes.write_parquet(out_dir / "game_outcomes.parquet")

    report_games = games.filter(pl.col("press_level").is_in(REPORT_PRESS_LEVELS))
    report_outcomes = outcomes.filter(pl.col("press_level").is_in(REPORT_PRESS_LEVELS))
    clean_outcomes = report_outcomes.filter(pl.col("quality_tier") == 1)
    n_clean = report_games.filter(pl.col("quality_tier") == 1).height

    sections = [
        "# Country outcome rates",
        f"Report cohort: {report_games.height} games from no_press, press_with_msgs, and public_press, "
        "filtered to in_scope (standard map, quality tiers 1-3, ended by solo or draw vote, standard build rules, ended by 1930). "
        "The press_without_msgs source is excluded from these comparisons because its draws are almost never detected, "
        "making its eligible sample almost entirely solos. Unknown endings remain excluded in the other sources too; "
        "these are descriptive rates among games with detectable endings, not population or causal estimates. "
        f"game_outcomes.parquet retains all {games.height} in-scope games across all four sources.",
        "Solo = 18+ centers at the end. 'In draw vote' = survived a game classified as ending == draw_vote; "
        "solo games are excluded even when their terminal orders are empty. Draw votes are inferred from empty orders, "
        "not confirmed site outcomes. "
        "Finished with centers (excluding solos) includes draw participants, so these report columns overlap. "
        "The explorer's Survived category excludes both solos and draws. "
        "In a solo game, SoS score is 1 for the winner and 0 for everyone else, including survivors. "
        "In a draw, score is centers^2 / sum(centers^2) across the seven powers.",
        "## All included press levels",
        rates_table(report_outcomes),
        "## Solo % by press level",
        by_press_table(report_outcomes, pl.col("solo")),
        "## Eliminated % by press level",
        by_press_table(report_outcomes, ~pl.col("survived")),
        "## Mean SoS score x 100 by press level",
        by_press_table(report_outcomes, pl.col("sos_score")),
        f"## Sensitivity: Tier 1 only ({n_clean} games)",
        "Same three sources, restricted to games with no detected dropout. The main tables retain tiers 1-3, "
        "including major dropouts. Tier 1 uses the all-hold-streak heuristic and does not guarantee uninterrupted play.",
        rates_table(clean_outcomes),
        "## Reference: playdiplomacy finished standard games (outcomes only, different platform)",
        playdip_table(playdip),
    ]
    (out_dir / "outcome_rates.md").write_text("\n\n".join(sections) + "\n")
    print(rates_table(report_outcomes))


if __name__ == "__main__":
    main()
