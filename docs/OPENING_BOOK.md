# Opening-book data contract and architecture

The Spring artifacts documented here remain available. The
[exact-history extension](EXACT_OPENINGS.md) adds own-country full 1901 and
all-country Spring/full-1901 matching, with a self-contained four-view report.

## Purpose and boundaries

This pipeline measures recorded Spring 1901 openings and their eventual outcomes.
The reports and [site](SITE.md) use this analysis and its exact-history
extension. Results describe historical matches, without a predictive model or
causal interpretation.

Processing is separated into selection/validation, aggregation, presentation and
publication. Pure analysis functions accept Polars tables and do not write files.
The CLI owns paths and build metadata. Analysis does not depend on a web
framework or storage service.

```text
games.parquet ──────────┐
phases.parquet ─────────┼─ select and validate ─ openings_observations.parquet
game_outcomes.parquet ──┘                              │
                                               group and estimate
                                                      │
                                              openings_own.parquet
                                                      │
                                                 render report
                                                      │
                                                openings_own.md
```

`openings_manifest.json` describes the build and all three output files.

## Cohort and validation

- Use `games.in_scope` and the shared source allowlist: `no_press`,
  `press_with_msgs`, `public_press`. The `press` source is excluded because almost
  none of its draws are detected.
- Require first phase `S1901M`, index zero and adjudicated. One of the 37,203
  otherwise eligible games starts at `S1902M`, leaving 37,202 games.
- Join on game ID and lowercase power. Require unique keys and exactly seven
  known powers per admitted game on both sides of the join. Missing matches fail
  the build rather than silently changing the denominator.
- Require matching outcome/game communication and quality metadata, finite scores
  in [0,1], and scores summing to one per game. Reject overlapping solo/draw flags.
- Require nonempty orders, matching stored order counts, and exactly one order
  origin per starting unit. Duplicate, missing or malformed origins fail the build.
  This is a structural check, not an adjudicator or legal-move validator.
- Do not exclude failed orders: bounced moves and cut supports are observations
  of legitimate attempted openings.

The existing global scope and dropout thresholds remain unchanged. No records
are deleted from upstream files. The manifest records the additional start-phase
exclusion; invalid inputs produce an error and leave a previous publication intact.

## Artifact contracts, version 1

All rates, scores and frequencies in Parquet are numeric fractions on [0,1].
Presentation alone turns them into percentages. Null uncertainty values mean
unavailable, not zero uncertainty. Schema changes require an explicit manifest
schema-version change; opening-identity changes require a new ID prefix.

### `openings_observations.parquet`

One row per `(game_id, power)`, sorted by those keys. Current snapshot: 260,414
rows, approximately 2.1 MiB compressed.

| Fields | Meaning |
|---|---|
| `game_id`, `power` | Historical game ID and lowercase country |
| `press_level`, `quality_tier` | Original source setting and quality label |
| `opening_id` | Stable country/opening identifier |
| `orders` | Sorted exact order strings, including coasts and `VIA` |
| `solo`, `survived`, `draw_vote`, `sos_score` | Labels from the corrected game-outcome table |

The stored `survived` flag means final centers > 0, including solo winners and
draw participants. The explorer's displayed Survived category excludes both.

The identity is `o1_` followed by SHA-256 of compact JSON containing the lowercase
power and sorted order list. It is independent of row order, Python hash seeds,
communication settings and final outcome. A unique catalog is hashed once and
joined back to observations. Actual order strings remain available to consumers.

### `openings_own.parquet`

One row per `(quality_group, press_level, power, opening_id)`. Current snapshot:
8,417 rows and approximately 334 KiB. Sparse openings are retained.

| Fields | Meaning |
|---|---|
| `quality_group` | `tiers_1_3` or `tier_1`; these are overlapping cohorts |
| `press_level` | Original setting, or `all` for the pooled cohort |
| `power`, `opening_id`, `orders` | Country and canonical opening |
| `n_games`, `cohort_games`, `frequency` | Opening count, same-country cohort denominator, and their ratio |
| `n_solos`, `solo_rate`, `survival_rate`, `draw_rate` | Observed outcome counts/rates |
| `mean_sos`, `sos_se` | Mean score and sample standard deviation divided by sqrt(n) |
| `sos_ci_low`, `sos_ci_high` | Approximate pointwise 95% mean-score interval |
| `solo_ci_low`, `solo_ci_high` | Pointwise 95% Wilson solo-rate interval |
| `baseline_mean_sos`, `baseline_solo_rate` | Same-country, same-press, same-quality baseline |
| `sos_lift` | Mean score minus the matched baseline |
| `sparse` | Whether `n_games` is below the configured threshold, default 200 |

Do not sum across quality groups or combine `all` with individual press settings:
these rows overlap. Within a single power/press/quality cohort, counts sum to the
denominator and opening frequencies sum to one. The Markdown report separates
press settings and shows the most frequent openings, not a score leaderboard.

### `openings_manifest.json`

Records schema version, Python/Polars versions, UTC build timestamp, thresholds,
cohort counts, per-stage timings, input/source/output SHA-256 hashes and byte sizes,
and the Parquet column types. Hashes identify actual data and code without relying
on version control. Dependency versions are also recorded in `uv.lock`.

The CLI computes and validates results before publication. Files are staged in a
temporary directory under the destination and replaced individually; the manifest
is replaced last as the completion marker. This is not a multi-file filesystem
transaction. A consumer reading during a build must verify output hashes against
one manifest and retry if they disagree. A future deployed website should publish
an immutable build directory and switch its serving pointer after validation.

## Statistical interpretation

The score is 1 for a solo and 0 for other powers in that game. In a non-solo game
it is final centers squared divided by the sum of squared final centers across countries. This supplies a
common retrospective metric; it does not imply players were pursuing that scoring
rule during play.

Mean-score intervals use `mean ± 1.959963984540054 × SE`, clipped to [0,1]. SE uses
sample variance (`ddof=1`). With fewer than two observations or zero observed
variance, mean-score intervals are null. Wilson intervals avoid falsely reporting
zero uncertainty for a solo rate with no observed wins.

These are analytic, pointwise intervals. They are inexpensive to compute and
deterministic without bootstrap resampling. They assume independent observations;
repeated players cannot be identified in this source. Normal intervals are less
reliable for sparse groups. No multiple-comparison correction or significance
claim is made. The baseline includes the opening itself; lift has no separate
confidence interval and is not an independent-samples hypothesis test.

All results are conditional on detectable endings and the scope rules. Skill,
negotiation and opponent choices are not controlled for. Hold orders can include
filled-in missed turns. Tier 1 means no *detected* dropout, not proof that everyone
played every turn. These limitations carry into any future presentation.

## Performance and extension points

- Polars lazy scans push row filters and column selection into Parquet reads. Only
  admitted first-turn observations are materialized; raw JSONL is not reread.
- Validation and aggregation operate on the compact observation table, not the
  33-million-row phase table. Grouped calculations are vectorized. Opening hashes
  run only on the 1,873 distinct order sets.
- Analytic intervals avoid repeated full-data resampling. Existing Polars worker
  threads are used; the build does not create another process pool.
- A full local run measured about 2.4 seconds, including full input fingerprints;
  this is a local observation, not a cross-machine performance guarantee. The
  manifest records each run's actual timings. Fingerprinting reads all input bytes
  sequentially; analysis itself uses the filtered Parquet scans.
- Parquet uses Zstandard compression. Reports use precomputed aggregates; the
  explorer computes conditional summaries from compact observations in memory.
  Neither needs raw histories per request. Country, press setting, quality group
  and opening ID provide the query keys.
- The renderer accepts only aggregates and counts. Reports can be regenerated
  from those artifacts without rescanning the phase data.
- Neighbor-opening analysis can self-join observations on `game_id` and add
  pair-specific grouping without repeating raw extraction. Do not reuse an own-
  opening baseline for pair-specific comparisons without defining that cohort.
- Future ML work should select feature columns explicitly, keep outcome labels
  separate, split at game level before fitting (all seven country rows stay
  together), and record split/feature/model versions and evaluation metrics.
  Opening IDs are keys, not evidence that two situations share the same payoff.

## Verification

```sh
uv run python -m unittest discover -s tests -v
uv run python -m pipeline.openings
```

Tests use hand-checkable games, not production-derived expected values. They cover
coast-preserving IDs, reordered orders, missing/duplicate keys, metadata conflicts,
malformed inputs, cohort filtering, matched baselines, sparse and zero-variance
cases, large-sample interval arithmetic, report escaping, repeated builds, output
hashes and preserving the previous publication when validation fails.
