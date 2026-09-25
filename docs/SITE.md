# How the site works

The site in `web/` is fully static: HTML, CSS, plain ES modules, self-hosted fonts and a compact data snapshot. It runs locally with `make serve` and deploys to GitHub Pages at `/diplomacy-lab/`. There is no server, build step or runtime dependency; every query runs in the browser.

## Data snapshot

`pipeline/web_export.py` converts the verified exact-match build (`opening_exact_*.parquet`, `game_outcomes.parquet` and the optional benchmark) into three files in `web/data/`:

| File | Size | Contents |
|---|---|---|
| `meta.json` | ~2 KB | Build ID, counts, array layout, per-country offsets and benchmark model settings |
| `catalog.json.gz` | ~360 KB | Distinct order strings, Spring openings and full-1901 turns, each with a short content-hash ID |
| `games.bin.gz` | ~1.1 MB | Little-endian typed arrays, one row per game (37,202 games × 7 countries) |

Design choices behind that size — about 1.4 MB compressed versus 15 MB of source Parquet:

- **Dictionary encoding** — the 67-character hash on every observation becomes a 16-bit index. Countries never exceed 17,137 distinct full-year histories, so `uint16` suffices, and 2,069 distinct order strings cover all 26,570 turns.
- **Derive, don't store** — each game keeps its 7 final center counts (`uint8`) instead of 7 float scores. The browser recomputes sum-of-squares scores exactly, and the exporter refuses to write if any recomputed score or outcome flag disagrees with the snapshot.
- **Packed flags** — press setting, quality tier, benchmark split and draw ending share one byte per game.
- **Full-year histories as turn tuples** — each distinct 1901 history is five turn indexes, so selecting any subset of turns is an integer comparison.
- **gzip plus `DecompressionStream`** — no decompression library. The loader checks the gzip magic bytes, so it works whether a host serves `.gz` raw or decodes it with `Content-Encoding`.
- **Cache busting** — `meta.json` is fetched with `no-cache`; the data files are requested with `?v=<build_id>`, so a deploy can never pair new metadata with stale data.

IDs are the first 12 hex characters of the build's content hashes (`o1_…` openings, `p1_…` turns), stable across rebuilds of the same data. The exporter fails if any shortened ID collides. Output is byte-identical for identical inputs.

Decoding takes about 15 ms. An explorer query takes about 3 ms and a matchup about 4 ms.

## Code

| Module | Responsibility |
|---|---|
| `web/js/dataset.js` | Fetch, decompress and decode the snapshot; precompute scores and outcomes; cohort filters |
| `web/js/explore.js` | Exact-match explorer queries over full 1901: turn selections, alternatives, baselines, sorting, search and paging |
| `web/js/estimates.js` | Optional shrinkage estimates fitted from benchmark training + validation games |
| `web/js/game-theory.js` | Matchup payoff tables, best replies, pure equilibria and historical-mix gains |
| `web/js/scenario.js` | Shareable explorer URLs (contract version 3) |
| `web/js/app.js`, `web/js/matchup.js` | Page rendering and controls |
| `web/js/theme.js` | Light/dark theme, loaded before first paint |

Pages render with text nodes only. A `<meta>` content security policy allows only same-origin scripts, styles, fonts and data.

## Using the explorer

The explorer always covers full 1901. Choose a communication setting and game quality (defaults: All press settings and Tier 1 only), browse a country's orders for any of the five turns (Spring movement, Spring retreats, Fall movement, Fall retreats, Winter adjustments), and select one to narrow the matching games. Add other countries or turns to require their orders in the same games. Selecting only the Spring movement turn answers the classic opening question. Unselected countries and turns may vary. "No recorded orders" matches an empty order set; it is not a wildcard.

Three game counts appear:

- **Filtered games** — all games under the communication and quality filters.
- **Matching games** — games satisfying every selection; these supply the outcomes table.
- **Eligible games** — games satisfying every selection except the choice being browsed. Card frequency uses this denominator.

Outcomes are mutually exclusive: **Solo** (18+ centers), **In draw** (held centers in a game classified as a draw), **Survived** (held centers when another country soloed) and **Eliminated**. In each numeric column a solid neutral cell marks the best value and crimson the worst; Eliminated is lower-is-better.

In a solo the winner scores 1 and everyone else 0. In a draw each country scores its final centers squared divided by the sum of squares. The baseline is the browsing country's game-weighted mean over eligible games, including the current choice. Differences are descriptive, not causal.

Mean-score sorting puts choices with at least `min_games` (200) games first unless "Allow sparse samples at the top" is on.

## Estimated scores

"Show estimated scores (experimental)" is off by default. It blends a choice's exact mean with the country's average, `(score_sum + k × baseline) / (fitting_matches + k)`, fitted on the benchmark's training and validation games; held-out test games are never used. The strength `k` per window and quality filter comes from the benchmark results in `meta.json`. Supported contexts are All press settings and one country's complete 1901 history: select the other four turns and each card estimates the full year. See [benchmark methodology](SCORE_BENCHMARK.md).

## Matchups

The Matchups page restricts to games where both chosen countries played one of their top 2–5 Spring openings, ranked by frequency or by mean score among openings with at least `min_games` games. Each cell's payoffs are both countries' mean scores. A best reply is a country's highest payoff against the other's opening; one within an approximate 95% noise band of the runner-up is marked △. A pure equilibrium is a cell where both openings are best replies. The historical-mix gain assumes the other country keeps choosing openings at their observed frequencies.

## Scenario URLs

The explorer URL records every nondefault setting plus turn selections such as `france.S1901M=p1_…`. The query starts with `v=3`. Changing defaults or ID formats requires a new version, so saved links never silently change meaning. Unknown, repeated or invalid parameters show an error instead of dropping constraints. The matchup page keeps its settings in the URL as well.

## Verification

- `tests/web/*.test.js` — hand-counted fixtures for explorer queries, full-year turns, estimates, the matchup solver and the URL contract (`npm test`).
- `tests/test_web_export.py` — export round trip, determinism and rejection of scores that disagree with final centers.
- Before the Python server was retired, the JavaScript engine matched it on 17 explorer and 7 matchup queries over the full dataset, to a relative tolerance of 1e-9.
