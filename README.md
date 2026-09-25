# Diplomacy Lab

**What happens after an opening, measured across 37,202 online Diplomacy games.** An exact-match opening explorer, a game-theory view of opening matchups, and the reproducible pipeline behind them.

**Live site:** [featheranalytics.dev/diplomacy-lab](https://www.featheranalytics.dev/diplomacy-lab/)

- **Opening explorer** — pick any country's recorded 1901 orders turn by turn, from Spring movement through Winter adjustments, add other countries to narrow the sample, and see how those exact games ended for all seven countries.
- **Opening matchups** — treat two countries' most common openings as a two-player game with observed payoffs, and see best replies, pure equilibria and how much each side could gain against the historical mix.
- **Reports** — opening books, exact-match repetition, country outcome rates and an expected-score benchmark, all rebuilt from raw data by one command.

Everything is descriptive. Results come from recorded games with detectable endings; they don't control for player skill or negotiation, and they aren't a claim that choosing an opening causes a better result.

## Data

The source is the [DipNet dataset](https://github.com/diplomacy/research) (Paquette et al., 2019): 156,468 games scraped from webDiplomacy and playdiplomacy, with every phase's orders and board state.

- **Scope** — standard map, quality tiers 1–3 (a turn resolved in 1904 or later), a solo or a detectable draw vote, standard build rules, ended by 1930.
- **Sources with detectable draws** — no press, private messages and public press; 37,202 games. The press-without-messages file is excluded from outcome comparisons because its draws are almost never detectable.
- **Quality tiers** — Tier 1 has no detected terminal dropout. The [data dictionary](data/DICTIONARY.md) has every field, filter and inference rule.

The DipNet dataset doesn't state a license. This repository publishes code, aggregated reports and a compact per-game export (openings and final supply-center counts) for research use. It doesn't republish the raw game records; `make fetch` downloads them from the original source.

## Reports

- [Exact country pairs](data/processed/opening_exact_pairs.md) — repetition across all 21 country pairs, with outcomes and lookup commands.
- [Exact opening histories](data/processed/opening_exact.md) — own-country and all-country matches for Spring and full 1901.
- [Spring 1901 opening book](data/processed/openings_own.md) — common openings per country and communication setting, with uncertainty intervals.
- [Expected-score benchmark](data/processed/score_benchmark/report.md) — country baselines vs exact means vs shrinkage on held-out games ([methodology](docs/SCORE_BENCHMARK.md)).
- [Country outcome rates](data/processed/outcome_rates.md) and the [data quality summary](data/processed/quality_summary.md).
- [Analysis backlog](IDEAS.md).

## Repository layout

| Path | Contents |
|---|---|
| `pipeline/` | Python package: profiling, phase table, outcomes, opening books, exact matching, benchmark and web export |
| `pipeline/analysis/` | Pure transforms and report rendering, independent of the CLIs |
| `web/` | The static site: HTML, CSS, ES modules, self-hosted fonts and the exported `web/data/` snapshot |
| `tests/` | Python tests on small hand-checked fixtures; `tests/web/` holds Node tests for the browser engine |
| `data/` | `DICTIONARY.md`, committed reports and manifests; raw data and large tables are gitignored |
| `docs/` | Data contracts and design notes for each stage |
| `scripts/` | Raw dataset downloads |

## Run the site locally

Requires [uv](https://docs.astral.sh/uv/) and Node 20 or newer (tests only; the site has no build step or dependencies).

```sh
make setup   # uv sync
make serve   # http://localhost:8000
make test    # Python and web tests
```

The site is static. `pipeline/web_export.py` turns the exact-match snapshot into about 1.4 MB of gzip-compressed typed arrays and catalogs, and the browser answers every query in a few milliseconds. See [how the site works](docs/SITE.md).

## Rebuild the data

```sh
make fetch      # raw datasets into data/raw (about 16 GB unpacked)
make data       # every table, report and web/data from raw
make reports    # opening, exact-match and benchmark outputs from existing tables
make site-data  # only re-export web/data
```

Each build validates its inputs, stages outputs and publishes a manifest last, so an interrupted run never leaves a mixed snapshot. The export is byte-identical for identical inputs.

The exact-match CLI answers ad hoc lookups. This one requires both England's and France's Spring orders to match within each game:

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press \
  --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 \
  --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36
```

Any one to seven countries can be selected; add `--power germany` for another country's outcomes in those games. See the [exact-history contract](docs/EXACT_OPENINGS.md) and the [opening-book contract](docs/OPENING_BOOK.md).

## License

Code is [MIT](LICENSE). Data comes from the DipNet dataset under its own terms.
