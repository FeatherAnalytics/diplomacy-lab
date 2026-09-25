"""Fetch webDiplomacy's public finished-games listing and parse it into one row per classic game.

Usage: uv run python -m pipeline.scrape_webdip_finished fetch [max_pages]
       uv run python -m pipeline.scrape_webdip_finished parse

fetch caches each listing page under data/raw/webdip_finished/pages/ and skips pages already on
disk, so an interrupted run can be resumed. It is not incremental: games that finish later land
on page numbers already cached, so a refresh needs an empty pages directory. parse reads every
cached page and writes data/processed/webdip_finished.parquet plus a verification report on stdout.
"""

import html
import re
import sys
import time
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import polars as pl

# Sorted by processTime ascending so already-finished games keep their position while new
# games finish during the run. The Finished tab excludes bot-only games (playerTypes <> 'MemberVsBots').
URL = "https://webdiplomacy.net/gamelistings.php?gamelistType=Finished&sortCol=processTime&sortType=asc&pagenum={}"
USER_AGENT = "diplomacy-game-theory research scraper (one pass over the public finished-games listing, 1 request per 1.5 s)"
DELAY_SECONDS = 1.5
PAGES_DIR = Path("data/raw/webdip_finished/pages")
LOG = Path("data/raw/webdip_finished/fetch_log.txt")
OUT = Path("data/processed/webdip_finished.parquet")

COUNTRIES = ["England", "France", "Italy", "Germany", "Austria", "Turkey", "Russia"]
PANEL_START = '<div class="gamePanel variant'
LISTING_MARKER = "Showing results"  # present on every real listing page, including the empty one past the end
TAG_RE = re.compile(r"<[^>]+>")
RETRIES = 3
RETRY_WAIT_SECONDS = 15
# Some old finished games carry processTime 2000000000 (2033) instead of a real finish time.
PLACEHOLDER_TIME = 2_000_000_000


def log(msg: str) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    print(msg, file=sys.stderr, flush=True)
    with LOG.open("a") as f:
        f.write(f"{stamp} {msg}\n")


def fetch_page(page: int) -> str:
    """Return the listing HTML, retrying transient failures; exits the process if the page never loads."""
    req = urllib.request.Request(URL.format(page), headers={"User-Agent": USER_AGENT})
    for attempt in range(1, RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read().decode("utf-8", "replace")
            if LISTING_MARKER in body:
                return body
            log(f"page {page} attempt {attempt}: response is not a listing page")
        except Exception as e:
            log(f"page {page} attempt {attempt}: {e}")
        time.sleep(RETRY_WAIT_SECONDS * attempt)
    log(f"giving up at page {page}")
    sys.exit(1)


def fetch(max_pages: int) -> None:
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    for page in range(1, max_pages + 1):
        path = PAGES_DIR / f"page_{page:05d}.html"
        if path.exists():
            continue
        body = fetch_page(page)
        if PANEL_START not in body:
            log(f"page {page} has no games; last page is {page - 1}")
            return
        tmp = path.with_suffix(".tmp")
        tmp.write_text(body, encoding="utf-8")
        tmp.rename(path)
        if page % 100 == 0:
            log(f"fetched page {page}")
        time.sleep(DELAY_SECONDS)
    log(f"reached max_pages={max_pages}")


def text(fragment: str | None) -> str:
    return html.unescape(TAG_RE.sub("", fragment or "")).strip()


def first(pattern: str, s: str) -> str | None:
    m = re.search(pattern, s)
    return m.group(1) if m else None


def parse_members(members_html: str) -> list[dict]:
    rows = re.findall(
        r'<span class="country\d+ memberStatus(\w+)">(\w+)</span>(.*?)</tr>', members_html
    )
    return [
        {
            "country": country,
            "status": status,
            "user_id": int(uid) if (uid := first(r"userID=(\d+)", rest)) else None,
            "sc": int(sc) if (sc := first(r"<em>(\d+)</em> supply-centers", rest)) else 0,
        }
        for status, country, rest in rows
    ]


def parse_settings(settings: str) -> dict:
    """The comma-joined game options line, e.g. 'Classic, No messaging, Anonymous players, Draw-Size Scoring'."""
    scoring = first(r"(Draw-Size|Sum-of-Squares|Survivors-Win|Points-per-supply-center) Scoring", settings)
    return {
        "settings": settings,
        "press_type": first(r"(No messaging|Public messaging only|Rulebook press)", settings) or "Regular",
        "scoring": scoring or ("Unranked" if "Unranked" in settings else None),
        "anon": "Anonymous players" in settings,
        "hidden_draw_votes": "Hidden draw votes" in settings,
        "fill_with_bots": "Fill with Bots" in settings,
    }


def finish_time(unixtime: int) -> int | None:
    return None if unixtime == PLACEHOLDER_TIME else unixtime


def game_status(notice: str) -> str:
    if notice.startswith("Game won by"):
        return "won"
    if notice == "Game drawn":
        return "drawn"
    return notice


def parse_panel(panel: str) -> dict:
    members_html, _, cd_html = panel.partition("Civil Disorders</div>")
    notice = text(first(r'<div class="bar gameNoticeBar[^"]*">(.*?)</div>', panel))
    season, year = re.search(r'<span class="gameDate">(\w+), (\d+)</span>', panel).groups()
    members = parse_members(members_html)
    by_country = {m["country"]: m for m in members}
    statuses = [m["status"] for m in members]

    row = {
        "game_id": int(first(r"board\.php\?gameID=(\d+)", panel)),
        "game_name": text(first(r'<span class="gameName">(.*?)</span>', panel)),
        "variant": first(r'^(\w+)"', panel),
        **parse_settings(text(first(r'<span class="gamePotType">(.*?)</span>', panel))),
        "phase_length": text(first(r'<span class="gameHoursPerPhase">(.*?)</span>', panel)),
        "pot": int(first(r'<span class="gamePot">(\d+)', panel)),
        "last_season": season,
        "last_year": int(year),
        "finished_unixtime": finish_time(int(first(r'unixtime="(\d+)"', panel))),
        "excused_missed_turns": int(first(r'<span class="excusedNMRs">(\d+)</span>', panel) or 0),
        "status": game_status(notice),
        "winner_country": next((m["country"] for m in members if m["status"] == "Won"), None),
        "n_members": len(members),
        "n_won": statuses.count("Won"),
        "n_drawn": statuses.count("Drawn"),
        "n_survived": statuses.count("Survived"),
        "n_defeated": statuses.count("Defeated"),
        "n_resigned": statuses.count("Resigned"),
        "n_left": statuses.count("Left"),
        "n_civil_disorder": cd_html.count('<tr class="member'),
    }
    for c in COUNTRIES:
        m = by_country.get(c, {})
        row[f"result_{c.lower()}"] = m.get("status")
        row[f"sc_{c.lower()}"] = m.get("sc")
        row[f"user_id_{c.lower()}"] = m.get("user_id")
    return row


def parse_page(path: Path, variant_counts: Counter) -> list[dict]:
    """Parse only Classic panels; other variants are counted for the completeness check and skipped."""
    flat = re.sub(r"\s+", " ", path.read_text(encoding="utf-8"))
    panels = flat.split(PANEL_START)[1:]
    variant_counts.update(first(r'^(\w+)"', p) for p in panels)
    return [parse_panel(p) for p in panels if p.startswith('Classic"')]


def listing_total(path: Path) -> int:
    """The 'of N total results' figure the site prints, all variants."""
    return int(first(r"of ([\d,]+) total results", path.read_text(encoding="utf-8")).replace(",", ""))


def verify(df: pl.DataFrame, variant_counts: Counter, listing_total: int) -> None:
    checks = {
        "duplicate classic game_ids": df.height - df["game_id"].n_unique(),
        "classic games without exactly 7 members": df.filter(pl.col("n_members") != 7).height,
        "won games without exactly one Won member": df.filter((pl.col("status") == "won") & (pl.col("n_won") != 1)).height,
        "drawn games with fewer than 2 Drawn members": df.filter((pl.col("status") == "drawn") & (pl.col("n_drawn") < 2)).height,
        "classic games with status neither won nor drawn": df.filter(~pl.col("status").is_in(["won", "drawn"])).height,
        "games with placeholder finish time": df["finished_unixtime"].null_count(),
    }
    print(f"pages parsed: {len(list(PAGES_DIR.glob('page_*.html')))}")
    print(f"panels seen, all variants: {sum(variant_counts.values())}; site total at fetch time: {listing_total}")
    print(f"classic panels: {variant_counts['Classic']}; unique classic game_ids: {df['game_id'].n_unique()}")
    for name, n in checks.items():
        print(f"{name}: {n}")
    print(dict(variant_counts.most_common()))


def parse() -> None:
    pages = sorted(PAGES_DIR.glob("page_*.html"))
    if not pages:
        sys.exit(f"No cached pages in {PAGES_DIR}; run fetch first")
    variant_counts: Counter = Counter()
    rows = [row for path in pages for row in parse_page(path, variant_counts)]
    df = pl.DataFrame(rows, infer_schema_length=None)
    verify(df, variant_counts, listing_total(pages[0]))
    classic = df.unique("game_id", keep="first").sort("game_id")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    classic.write_parquet(OUT)
    print(f"wrote {classic.height} classic games to {OUT}")


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "fetch":
        fetch(int(sys.argv[2]) if len(sys.argv) > 2 else 10_000)
    elif cmd == "parse":
        parse()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
