# Offline expected-score benchmark

Run from the project root:

```sh
uv run python -m pipeline.score_benchmark
```

Outputs are separate from the explorer's artifacts, under
`data/processed/score_benchmark/`: `report.md`, `results.json`,
`split_assignments.parquet` and `manifest.json`. Optional arguments are
`--data-dir`, `--output-dir` and `--seed`. No API key or new dependency is needed.
The site's optional estimated-score toggle uses the own-country strengths selected
here, refitted in the browser on the same training and validation games.

## Fixed evaluation design

The protocol was chosen before evaluating the held-out games:

- Primary cohort: Tier 1, all three included press settings pooled. Tiers 1–3
  provide a sensitivity analysis, not an independent replication.
- Evaluate Spring 1901 and completed Full 1901 separately. Spring features
  contain no Fall/Winter orders. Full-year results describe a forecast after
  the year's orders are known, not a pre-Spring strategy.
- Contexts: each country's own orders; all 21 country pairs, predicting both
  members; all seven countries' orders, predicting each country's score.
- Assign whole games to approximately 70% training, 15% validation and 15% test
  using SHA-256 of `seed + NUL + game_id`. Default seed: 1901. The first 8 bytes
  interpreted as an unsigned big-endian integer, divided by 2^64, select the
  split using thresholds 0.70 and 0.85. Every country and horizon shares its
  game's split. Input ordering does not affect assignment.
- Select one strength per cohort/horizon/context family using validation MSE.
  Refit on training plus validation, then evaluate the test set once. Neither
  test scores nor test error select a strength.

## Estimators

**Country baseline:** mean score for the country in the fitting games.

**Raw exact mean:** mean score for that country among fitting games with the
same order history and context. It abstains when no exact match exists.

**Shrinkage:** `(matching score sum + k × country baseline) / (match count + k)`.
On unseen histories, it returns the country baseline and supplies no
opening-specific evidence. The baseline includes the matched fitting games.
This is a regularized mean, not a fully fitted hierarchical Bayesian model.

The fixed strength grid is 0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000 and
baseline-only. Ties within 1e-12 MSE prefer greater shrinkage. Zero strength
uses raw exact means where available and the baseline elsewhere. Validation
uses every case; the fallback policy is the same for every numeric strength.

Final scores use the existing sum-of-squares metric, from 0 to 1. A solo gives
the winner 1 and everyone else 0. Otherwise, each country scores its squared
final center count divided by the sum of those squares across countries.

## Metrics and limits

Report RMSE, MSE and MAE. MSE is the selection metric because the target is a
conditional mean; MAE is a secondary description. Report exact-match coverage,
and compare all three estimators on the identical subset with observed exact
matches. Compare baseline and shrinkage across all test cases separately.

Each game contributes seven own/all-country cases or 42 pair cases, so full
test metrics weight games equally. Matched subsets can contain varying numbers
of retained cases per game. Paired MSE differences use their case-weighted mean
and an approximate 95% interval clustered by game. Countries/pairs within one
game are not treated as independent observations. These are pointwise intervals,
without multiple-comparison correction or player-level clustering.

The JSON also records per-country errors and errors by exact fitting support:
0, 1, 2–9, 10–49, 50–199 and 200+. Support counts refer to training + validation,
not the full explorer dataset.

This is random holdout evaluation within a historical snapshot. Player IDs and
original game dates are unavailable, so it does not test new-player or future-era
performance. Unknown endings are excluded. Simultaneous orders are treated as
known; opponent-choice prediction is outside this experiment. Accuracy on these
contexts does not establish accuracy for arbitrary partial-turn selections or
individual orders, or that choosing a higher-scoring move causes a better result.

## Implementation and reproducibility

`pipeline/analysis/score_benchmark.py` contains the estimators and evaluation functions.
`pipeline/score_benchmark.py` verifies the exact observations against the existing
manifest, validates their grain and scores, runs the experiment and publishes
the reports. It hashes and decodes the same bytes to avoid mixed input reads.

Only the compact observation table is read; no raw replays or phase scans are
needed. Each pair is processed separately; only its small validation/test frames
are retained. Predictions are not added to live tables. Outputs are staged and
the manifest is replaced last. The manifest records input and source hashes,
split rules, grid, library versions and elapsed time. The split assignments are
saved so the test set can remain untouched during any subsequent development.

Regression tests cover game-level splitting, training-only estimates, unseen
histories, within-game pairs, conservative tuning ties, matched-case metrics,
clustered uncertainty, test-label isolation and artifact integrity.

## First run

The primary Tier 1 test set contains 2,219 games. Compared with the country
baseline, shrinkage reduced MSE by 1.02% for own Spring openings and 2.39% for
own Full 1901 histories. Exact-match coverage was 99.5% and 77.6%, respectively.
Spring pairs improved 0.99%; full-year pairs improved 0.14%, with only 15.7%
coverage. Full-year own histories are a later-information task, not evidence
that a Spring-only forecast could achieve the same result.

All-country Spring coverage was 5.5%, with no clear improvement over baseline.
All-country Full 1901 coverage was zero; validation selected baseline-only.
Shrinkage substantially reduced the poor predictions from sparse raw exact
means, but its advantage over the simpler country baseline was modest.

The Tiers 1–3 sensitivity run showed the same broad pattern, with 1.91% and
4.17% MSE reductions for own Spring and full-year histories. These samples
overlap the primary analysis and are not independent confirmation.

The run took about 2.9 seconds locally. These results support further offline
work on an optional estimated-score view, particularly for own-country
histories. They do not establish a reliable move recommendation system or
justify modeled scores for arbitrary explorer selections yet.
