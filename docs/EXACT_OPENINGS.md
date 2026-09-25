# Exact opening histories

This extension supports four historical questions for every country:

| Horizon | Context | Matching condition |
|---|---|---|
| `spring1901` | `own` | That country's Spring orders |
| `year1901` | `own` | That country's orders throughout 1901 |
| `spring1901` | `all` | All seven countries' Spring orders |
| `year1901` | `all` | All seven countries' orders throughout 1901 |
| Either | `selected` | Every selected country's sequence, in the same game; other countries may vary |

Results describe observed outcomes among exact matches. There is no model,
smoothing, similar-position search or fallback estimate. A missing match is an
empty result, not a zero chance of winning. One match exposes its historical
counts and score, with outcome-rate fields null. Two or more matches expose
empirical fractions; a small sample remains a small sample.

## Build and query

```sh
uv run python -m pipeline.exact_openings build
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context own --power austria --pattern-id y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --press-level no_press
```

`build` accepts `--data-dir`, `--output-dir`, `--min-games` (default 200) and
`--top-n` (default 5). The sparse threshold annotates aggregates; it does not
remove patterns. The report shows frequent histories and a few joint examples;
the Parquet catalogs retain all observed patterns.

`lookup` accepts `--data-dir` pointing to the output directory, `--horizon`,
`--context`, `--pattern-id`, optional `--power`, `--press-level` (default `all`),
`--quality-group` (`tiers_1_3` or `tier_1`) and `--limit` (default 10). Own context
requires a country; all-country context returns seven country outcomes unless
a target country is supplied. The limit bounds returned game IDs, not the sample
used for aggregation. Pattern IDs are available in the report and catalogs.
For `--context selected`, replace `--pattern-id` with repeated
`--select COUNTRY=SEQUENCE_ID` arguments, one per selected country. One to seven
countries are supported. Duplicate country arguments, empty selections and
mixing pattern IDs with selections are errors. A sequence from the wrong horizon
or country cannot match. Country names are lowercase. `--power` chooses the
outcome country independently of the selected countries; omit it for all seven.
The query response records the selections in sorted country order. The pair
report contains ready-to-run examples with both sequence IDs and cohort filters.

The CLI accepts IDs. The [site](SITE.md) lets you select recorded
orders by country and turn. Free-form order entry and external game import are
not implemented.

The JSON response contains `status`, the query, `n_matches`, matching `game_ids`,
`game_ids_truncated`, and per-country `outcomes`. Status is `no_exact_matches`,
`single_historical_game` or `exact_matches`. Each outcome includes `n_games`,
`n_solos`, `n_draws`, `n_survived`, `mean_sos`, `observed_solo_rate` and
`observed_draw_rate`. Draw counts mean country participation in detected draws.
`n_survived` counts every country with centers at the end, including solo winners
and draw participants. Reports label this count “Finished with centers”; the
explorer subtracts solos and draws for its separate “Survived” category.

## Cohort and identity

The build reuses the original [Spring validation and cohort](OPENING_BOOK.md):
37,202 games from the three draw-detectable sources, with tiers 1–3 and a
separate tier-1 view. No upstream scope or dropout rules change.

Full 1901 includes Spring and Fall movements, any retreats, and Winter
adjustments. Validation requires all seven powers, unique phase/power keys,
chronological contiguous phase indices, adjudicated 1901 phases, nonnull orders
and consistent order counts. Required movement phases and the Spring 1902
boundary must exist. The boundary establishes that 1901 ended; its orders and
outcomes do not enter the history key. Later orders receive structural checks,
not legal-move adjudication. Failed attempted orders remain part of the history.

Canonical histories are chronological JSON arrays of objects with `phase` and
sorted `orders`. Sorting preserves coasts, `VIA`, and duplicate strings such as
multiple `WAIVE` orders. Empty optional retreat/adjustment phases are omitted
from each country's identity: another country's retreat should not split an
unchanged own-country history. Missing and explicitly empty optional phases
therefore represent the same absence of orders for that country. Raw phases
remain available upstream.

- Spring sequence IDs retain the original `o1_` identity.
- Full-year IDs are `y1_` plus SHA-256 of lowercase power, a newline, and canonical
  compact history JSON. Phase order is significant.
- Joint IDs are `j1_` plus SHA-256 of compact JSON containing the horizon and
  seven sequence IDs ordered Austria, England, France, Germany, Italy, Russia,
  Turkey. They do not depend on outcome, source setting or quality tier.

Identity changes require a new prefix. Schema changes require a new manifest
schema version.

## Artifacts, schema version 1

All files are written under the chosen output directory.

| File | Grain and contents |
|---|---|
| `opening_exact_observations.parquet` | One row per `(horizon, game_id, power)`: `sequence_id`, `joint_id`, `press_level`, `quality_tier`, `solo`, `survived`, `draw_vote`, `sos_score` |
| `opening_exact_sequences.parquet` | One row per `(horizon, power, sequence_id)`: canonical `sequence_json` |
| `opening_exact_profiles.parquet` | One row per `(horizon, joint_id)`: `sequence_ids`, a list of seven IDs in the country order above |
| `opening_exact_own_rates.parquet` | One row per `(horizon, quality_group, press_level, power, sequence_id)`: own-country counts and statistics |
| `opening_exact.md` | Self-contained report covering all four views |
| `opening_exact_pair_coverage.parquet` | One row per `(horizon, quality_group, press_level, power_a, power_b)`: repetition and sample-size coverage for each pair |
| `opening_exact_pair_examples.parquet` | Up to `top_n` most frequent exact patterns per pair/cohort, with both sequence IDs and the two countries' outcomes |
| `opening_exact_pairs.md` | Pair coverage tables and the most frequent pattern for each pair, separately by communication setting and quality cohort |
| `opening_exact_manifest.json` | Schemas, configuration, versions, input/code/output hashes, counts and timings |

Own rates reuse the original [aggregate fields and interval definitions](OPENING_BOOK.md),
replacing `opening_id` with `sequence_id`, adding `horizon`, `n_draws` and
`n_survived`, and keeping descriptions in the sequence catalog. Exact exports
set singleton `solo_rate`, `draw_rate`, `survival_rate` and Wilson bounds to null.
`baseline_solo_rate` is null for a singleton baseline cohort. Counts, observed
mean score and descriptive score lift remain available. The original Spring
artifacts retain their original contract. Cohort baselines include the history
itself; pooled press and tier cohorts overlap and must not be summed together.

Current counts are 520,828 observations, 63,202 country sequences, 72,944 joint
profiles and 215,167 own-rate rows. There are 35,742 Spring joint profiles;
34,885 occur once, and the largest has 18 games. All 37,202 full-year joint
histories occur once. Own-country full-year histories have many repeated matches.
Full-year decisions respond to earlier adjudication and negotiation, so matching
them describes a realized history, not the value of committing to a Spring plan.

### Pair coverage and examples

All 21 unordered country pairs are included, with `power_a` alphabetically before
`power_b`. Coverage is computed across every observed pair pattern before examples
are truncated. Fields are `cohort_games`, `n_patterns`, `singleton_patterns`,
`games_in_repeated_patterns`, `patterns_at_threshold`, `games_at_threshold`,
`max_matches`, and `min_games`. Repeated means at least two matches in that exact
cohort; the configurable threshold defaults to 200. Each game belongs to one
pattern for a given pair, so covered games are counted once within that pair.
Different pairs and overlapping cohorts must not be summed together. Empty
cohorts have no artifact rows and display as no observations in the report.

Examples contain `sequence_id_a`, `sequence_id_b`, `n_games`, `sparse`, and, for
each suffix `_a` and `_b`, `n_solos`, `n_draws`, `n_survived`, `mean_sos`,
`solo_rate`, `draw_rate`, and `survival_rate`. Singleton rate fields are null.
Ties are resolved by sequence IDs, making example selection deterministic.
The examples are bounded extracts, not an exhaustive pair catalog. Any observed
or unobserved combination can still be submitted to exact lookup.

The current build adds 336 coverage rows and 1,680 examples at the default
`top_n=5`. The report shows one example per pair/cohort; the Parquet retains up
to five. In no-press tiers 1–3, the most frequent England/France Spring combination
has 1,275 games, and the most frequent full-year combination has 104. Repetition
measures available evidence, not strategic quality or causality.

## Performance and website integration

The offline build filters the existing Parquet phase table, normalizes distinct
histories once, and joins compact IDs back to observations. It does not reread
raw JSONL or enumerate possible combinations. A local full-data build measured
roughly four seconds including input fingerprints; timings vary by machine.
Including pair summaries and their report measured roughly five seconds locally,
with about one second for the added pair work and about 330 KB of added outputs.

Own-country summaries are precomputed. Joint lookups filter compact observations
and aggregate only matching rows through `pipeline/analysis/exact_query.py`. This
avoids publishing mostly redundant aggregate rows for unique joint histories.
The observation Parquet is sorted by horizon and joint ID with bounded row
groups to support filtered reads. Descriptions are stored once in catalogs.

Selected-country queries first intersect requested `(power, sequence_id)` matches
by game within the horizon and cohort, then retrieve outcome rows for those
games. The outcome-country filter is applied after this intersection. Counts and
rates use all matching games; only the returned game-ID list is limited. Pair
aggregation works on one pair at a time and keeps compact coverage plus bounded
examples. No cross product of possible orders or enumeration of all larger
country subsets is stored.

The static site does not read these Parquet files. `pipeline/web_export.py`
re-encodes the verified observations and catalogs as compact typed arrays, and
the browser runs the same exact-match semantics; see [how the site works](SITE.md).
The CLI verifies the observation file's manifest hash on each invocation.

Publication stages all outputs, replaces files individually, and replaces the
manifest last. It is not a multi-file transaction. Consumers must verify hashes
and retry if reading across a build; deployment should use immutable build
directories and switch its serving pointer after verification.

## Verification

```sh
uv run python -m unittest discover -s tests -v
uv run python -m pipeline.exact_openings build
```

Deterministic fixtures cover all four views, exact counts and empty/singleton
results, phase chronology, coast-sensitive IDs, repeated waives, optional empty
phases, missing/duplicate data, Spring isolation from later orders, manifest
hashes, and a standalone report with actual orders for both horizons.
Selected-country fixtures also cover within-game intersections, unselected
countries varying, target countries outside the selection, one/all-seven
constraints, press and quality filters, bounded game lists, zero/singleton
results, duplicate CLI selectors, and hand-counted pair coverage and outcomes.
