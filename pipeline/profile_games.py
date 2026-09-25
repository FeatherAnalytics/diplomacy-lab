"""Stream DipNet JSONL files and emit one row per game plus a quality summary.

Usage: uv run python -m pipeline.profile_games [data/raw/dipnet] [data/processed]
"""

import json
import re
import sys
from pathlib import Path

import polars as pl

POWERS = ["AUSTRIA", "ENGLAND", "FRANCE", "GERMANY", "ITALY", "RUSSIA", "TURKEY"]
POWER_BY_CODE = {p[:3]: p for p in POWERS}

FILES = {
    "standard_no_press.jsonl": "no_press",
    "standard_press_without_msgs.jsonl": "press",
    "standard_press_with_msgs.jsonl": "press_with_msgs",
    "standard_public_press.jsonl": "public_press",
}

# Outcome: the only end-of-game marker in the data is a final phase named COMPLETED whose
# state.note reads "Victory by: XXX". Games that ended in a draw, were abandoned, or were
# still running when scraped all just stop at an ordinary phase, so they are "no_solo".
#
# Dropout: state.civil_disorder is 0 everywhere and missing orders were filled in as holds when
# the dataset was built, so a dropped player shows up as a power whose every unit holds in
# every movement phase from some point until it is eliminated or the record ends. A power that
# all-holds for a while and then moves again is not counted. A movement phase where *every*
# surviving power has [] orders is how games end by draw or cancel vote; it is flagged as
# ended_by_vote and skipped. The final phase of a no_solo game is unadjudicated and skipped.
#
# Quality tiers (copied verbatim into data/DICTIONARY.md):
#   1 clean:         last_year >= 1904 and no dropout (no power all-held its last 3+ movement phases)
#   2 minor dropout: last_year >= 1904 and every dropout began with the power holding <= 2 centers
#   3 major dropout: last_year >= 1904 and some dropout began with the power holding >= 3 centers
#   4 short:         last_year < 1904
#
# in_scope (copied verbatim into data/DICTIONARY.md): map == "standard" and quality_tier <= 3
# and ending != "unknown" and "BUILD_ANY" not in rules and last_year <= 1930 and not
# (ending == "solo" and the winner's final centers < 18).
MIN_YEAR_FOR_QUALITY = 1904
DROPOUT_STREAK = 3
MINOR_DROPOUT_MAX_CENTERS = 2
MAX_QUALITY_TIER = 3
MAX_LAST_YEAR = 1930
SOLO_CENTERS = 18
EXCLUDED_RULE = "BUILD_ANY"

PHASE_RE = re.compile(r"^[SFW](\d{4})[MRA]$")
VICTORY_RE = re.compile(r"Victory by: (\w{3})")


def phase_year(name: str) -> int | None:
    m = PHASE_RE.match(name)
    return int(m.group(1)) if m else None


def center_counts(state: dict) -> dict[str, int]:
    return {p: len(state["centers"].get(p, [])) for p in POWERS}


def ended_by_vote(movement_phases: list[dict]) -> bool:
    """Every surviving power submitted [] in the last adjudicated movement phase."""
    if not movement_phases:
        return False
    last = movement_phases[-1]
    alive = [p for p in POWERS if last["state"]["units"].get(p)]
    return bool(alive) and not any(last["orders"].get(p) for p in alive)


def all_hold(orders: list[str] | None) -> bool:
    return bool(orders) and all(o.endswith(" H") for o in orders)


def dropout_stats(movement_phases: list[dict]) -> dict:
    """Powers whose final DROPOUT_STREAK+ movement phases were all holds, and their size."""
    run = dict.fromkeys(POWERS, 0)
    centers_at_start = dict.fromkeys(POWERS, 0)
    year_at_start = dict.fromkeys(POWERS, None)
    n_cd = 0
    for ph in movement_phases:
        n_cd += any(ph["state"]["civil_disorder"].values())
        centers = center_counts(ph["state"])
        for p in POWERS:
            if not ph["state"]["units"].get(p):
                continue  # eliminated: keep the streak it ended with
            if not all_hold(ph["orders"].get(p)):
                run[p] = 0
                continue
            if run[p] == 0:
                centers_at_start[p] = centers[p]
                year_at_start[p] = phase_year(ph["name"])
            run[p] += 1
    dropped = [p for p in POWERS if run[p] >= DROPOUT_STREAK]
    return {
        "n_phases_with_cd": n_cd,
        "n_powers_dropout": len(dropped),
        "first_dropout_year": min((year_at_start[p] for p in dropped), default=None),
        "max_centers_of_dropout_power": max((centers_at_start[p] for p in dropped), default=0),
    }


def quality_tier(last_year: int, stats: dict) -> int:
    if last_year < MIN_YEAR_FOR_QUALITY:
        return 4
    if stats["n_powers_dropout"] == 0:
        return 1
    if stats["max_centers_of_dropout_power"] <= MINOR_DROPOUT_MAX_CENTERS:
        return 2
    return 3


def winner(note: str) -> str | None:
    m = VICTORY_RE.search(note)
    return POWER_BY_CODE[m.group(1)] if m else None


def game_ending(is_solo: bool, vote: bool) -> str:
    if is_solo:
        return "solo"
    return "draw_vote" if vote else "unknown"


def in_scope(row: dict) -> bool:
    winner_centers = row[f"centers_{row['winner'].lower()}"] if row["winner"] else 0
    return (
        row["map"] == "standard"
        and row["quality_tier"] <= MAX_QUALITY_TIER
        and row["ending"] != "unknown"
        and EXCLUDED_RULE not in row["rules"]
        and row["last_year"] <= MAX_LAST_YEAR
        and (row["ending"] != "solo" or winner_centers >= SOLO_CENTERS)
    )


def profile_game(game: dict, source_file: str) -> dict:
    phases = game["phases"]
    last = phases[-1]
    is_solo = last["name"] == "COMPLETED"
    final_centers = center_counts(last["state"])
    # A COMPLETED phase carries the final state; the last phase of a no_solo game is
    # the pending, never-adjudicated one. Either way the last phase holds no play.
    adjudicated = phases[:-1]
    movement = [ph for ph in adjudicated if ph["name"].endswith("M")]
    vote = ended_by_vote(movement)
    stats = dropout_stats(movement[:-1] if vote else movement)
    last_year = phase_year((adjudicated or phases)[-1]["name"])

    row = {
        "game_id": game["id"],
        "source_file": source_file,
        "press_level": FILES[source_file],
        "map": game["map"],
        "rules": ",".join(game["rules"]),
        "n_phases": len(phases),
        "n_movement_phases": len(movement),
        "first_phase": phases[0]["name"],
        "last_phase": last["name"],
        "last_year": last_year,
        "outcome_type": "solo" if is_solo else "no_solo",
        "ending": game_ending(is_solo, vote),
        "winner": winner(last["state"]["note"]),
        "ended_by_vote": vote,
        "n_alive_at_end": sum(c > 0 for c in final_centers.values()),
        "n_messages": sum(len(ph["messages"] or []) for ph in phases),
        **stats,
        "quality_tier": quality_tier(last_year, stats),
        **{f"centers_{p.lower()}": final_centers[p] for p in POWERS},
    }
    row["in_scope"] = in_scope(row)
    return row


def profile_file(path: Path) -> list[dict]:
    rows = []
    with path.open() as f:
        for line in f:
            rows.append(profile_game(json.loads(line), path.name))
            if len(rows) % 5000 == 0:
                print(f"{path.name}: {len(rows)} games", file=sys.stderr, flush=True)
    return rows


def pct_table(df: pl.DataFrame, col: str, by: str = "press_level") -> str:
    counts = (
        df.group_by(by, col)
        .len()
        .join(df.group_by(by).len().rename({"len": "total"}), on=by)
        .with_columns((pl.col("len") / pl.col("total") * 100).round(1).alias("pct"))
        .sort(by, col)
    )
    lines = [f"| {by} | {col} | games | pct |", "|---|---|---|---|"]
    lines += [f"| {r[by]} | {r[col]} | {r['len']} | {r['pct']} |" for r in counts.iter_rows(named=True)]
    return "\n".join(lines)


def write_summary(df: pl.DataFrame, out: Path) -> None:
    std = df.filter(pl.col("map") == "standard")
    years = std["last_year"]
    sections = [
        "# DipNet standard-map games: quality summary",
        f"Total games: {df.height}. Solo: {(df['outcome_type'] == 'solo').sum()}. "
        "Draws are not marked in the data; no_solo mixes draws, abandoned, and in-progress games. "
        f"ended_by_vote (all surviving powers submitted [] in the last movement phase): {df['ended_by_vote'].sum()}.",
        "## Map by press level (all maps)",
        pct_table(df, "map"),
        "## Outcome by press level (standard map only)",
        pct_table(std, "outcome_type"),
        "## Quality tier by press level (standard map only)",
        pct_table(std, "quality_tier"),
        "## ended_by_vote by press level (no_solo, standard map)",
        pct_table(std.filter(pl.col("outcome_type") == "no_solo"), "ended_by_vote"),
        "## Quality tier by outcome (standard map only)",
        pct_table(std, "quality_tier", by="outcome_type"),
        "## Ending by press level (standard map only)",
        pct_table(std, "ending"),
        f"In scope: {std['in_scope'].sum()} of {std.height} standard-map games "
        f"({std['in_scope'].mean() * 100:.1f}%). in_scope = tier <= {MAX_QUALITY_TIER}, ending != unknown, "
        f"no {EXCLUDED_RULE}, last_year <= {MAX_LAST_YEAR}, solo winner has >= {SOLO_CENTERS} centers.",
        "## Last year (standard map only)",
        f"min {years.min()}, p25 {years.quantile(0.25)}, median {years.median()}, p75 {years.quantile(0.75)}, max {years.max()}",
    ]
    out.write_text("\n\n".join(sections) + "\n")


def main() -> None:
    raw_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "data/raw/dipnet")
    out_dir = Path(sys.argv[2] if len(sys.argv) > 2 else "data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pl.DataFrame([row for name in FILES for row in profile_file(raw_dir / name)])
    df.write_parquet(out_dir / "games.parquet")
    write_summary(df, out_dir / "quality_summary.md")
    print(df.group_by("source_file").len().sort("source_file"))


if __name__ == "__main__":
    main()
