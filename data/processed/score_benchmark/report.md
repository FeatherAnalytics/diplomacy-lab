# Expected-score benchmark

Offline experiment. The explorer shows exact historical results by default; its optional estimated-score toggle uses the own-country models evaluated here.

Split seed: 1901. Whole games are assigned once to approximately 70% training, 15% validation and 15% test. The same split applies to every country, horizon and quality cohort. Strength is selected on validation MSE, then models are refit on training + validation before scoring the held-out test games.

All press settings are pooled. Tier 1 is the primary analysis; Tiers 1–3 is an overlapping sensitivity analysis. One-country contexts use that country's complete order set. Pair contexts cover all 21 pairs and predict both members. All-country contexts require all seven histories. Full 1901 estimates use only 1901 orders, but are not Spring forecasts.

Baseline = the country's mean final score in fitting games. Exact = mean among fitting games with the same orders. Shrinkage = (matching score sum + k × baseline) / (match count + k). Unseen orders use the baseline only for shrinkage; raw exact estimates are unavailable. The baseline includes the matched fitting games, making this a simple regularized estimator rather than a full Bayesian model.

Validation grid: 0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, baseline. The baseline candidate ignores orders. Ties prefer greater shrinkage. k = 0 uses raw exact means where available and the baseline elsewhere.

Errors use final scores on the 0–1 scale. Lower RMSE is better; MSE reduction is relative to the country baseline. Coverage is the share of test country/context cases with at least one exact match in training + validation. All-case metrics weight games equally. Matched/support subsets weight retained country/context cases equally, so games may contribute different numbers of cases. Pair cases are correlated, not additional independent games.

## Primary: Tier 1

Games: 10,148 training, 2,169 validation, 2,219 test.

### All test cases

Raw exact estimates abstain on unseen histories; the next table compares all three methods on the same matched subset.

| Window | Context | Exact coverage | Selected k | Baseline RMSE | Shrinkage RMSE | MSE reduction |
|---|---|---:|---:|---:|---:|---:|
| Spring 1901 | One country | 99.5% | 10 | 0.2916 | 0.2902 | +1.02% |
| Spring 1901 | Country pairs | 94.5% | 50 | 0.2916 | 0.2902 | +0.99% |
| Spring 1901 | All seven countries | 5.5% | 10 | 0.2916 | 0.2916 | -0.01% |
| Full 1901 | One country | 77.6% | 20 | 0.2916 | 0.2881 | +2.39% |
| Full 1901 | Country pairs | 15.7% | 10 | 0.2916 | 0.2914 | +0.14% |
| Full 1901 | All seven countries | 0.0% | baseline | 0.2916 | 0.2916 | +0.00% |

### Identical subset: exact matches available

These errors must not be compared directly with the full-test errors above; the case mix differs.

| Window | Context | Cases | Baseline RMSE | Exact RMSE | Shrinkage RMSE |
|---|---|---:|---:|---:|---:|
| Spring 1901 | One country | 15,450 | 0.2920 | 0.2909 | 0.2905 |
| Spring 1901 | Country pairs | 88,086 | 0.2927 | 0.2980 | 0.2912 |
| Spring 1901 | All seven countries | 861 | 0.2865 | 0.3588 | 0.2868 |
| Full 1901 | One country | 12,048 | 0.2991 | 0.3129 | 0.2947 |
| Full 1901 | Country pairs | 14,624 | 0.2967 | 0.3614 | 0.2954 |
| Full 1901 | All seven countries | 0 | — | — | — |

### Paired MSE differences

Negative favors shrinkage. Brackets are approximate pointwise 95% intervals clustered by game, not by country/context case. They are not adjusted for multiple comparisons and do not account for repeated players or dataset selection.

| Window | Context | Shrinkage − baseline, all cases | Shrinkage − exact, matched cases |
|---|---|---|---|
| Spring 1901 | One country | -0.000864 [-0.001152, -0.000575] | -0.000214 [-0.000330, -0.000098] |
| Spring 1901 | Country pairs | -0.000843 [-0.001042, -0.000644] | -0.003972 [-0.004390, -0.003554] |
| Spring 1901 | All seven countries | +0.000008 [-0.000074, +0.000090] | -0.046507 [-0.058905, -0.034110] |
| Full 1901 | One country | -0.002030 [-0.002496, -0.001565] | -0.011049 [-0.012741, -0.009358] |
| Full 1901 | Country pairs | -0.000118 [-0.000209, -0.000027] | -0.043307 [-0.046473, -0.040141] |
| Full 1901 | All seven countries | +0.000000 [+0.000000, +0.000000] | — |

## Sensitivity: Tiers 1–3

Games: 26,072 training, 5,519 validation, 5,611 test.

### All test cases

Raw exact estimates abstain on unseen histories; the next table compares all three methods on the same matched subset.

| Window | Context | Exact coverage | Selected k | Baseline RMSE | Shrinkage RMSE | MSE reduction |
|---|---|---:|---:|---:|---:|---:|
| Spring 1901 | One country | 99.7% | 10 | 0.3026 | 0.2997 | +1.91% |
| Spring 1901 | Country pairs | 96.4% | 20 | 0.3026 | 0.2997 | +1.93% |
| Spring 1901 | All seven countries | 5.9% | 20 | 0.3026 | 0.3026 | +0.02% |
| Full 1901 | One country | 83.5% | 10 | 0.3026 | 0.2963 | +4.17% |
| Full 1901 | Country pairs | 20.5% | 10 | 0.3026 | 0.3019 | +0.50% |
| Full 1901 | All seven countries | 0.0% | baseline | 0.3026 | 0.3026 | +0.00% |

### Identical subset: exact matches available

These errors must not be compared directly with the full-test errors above; the case mix differs.

| Window | Context | Cases | Baseline RMSE | Exact RMSE | Shrinkage RMSE |
|---|---|---:|---:|---:|---:|
| Spring 1901 | One country | 39,174 | 0.3029 | 0.3001 | 0.2999 |
| Spring 1901 | Country pairs | 227,234 | 0.3039 | 0.3054 | 0.3009 |
| Spring 1901 | All seven countries | 2,303 | 0.2979 | 0.3739 | 0.2975 |
| Full 1901 | One country | 32,786 | 0.3093 | 0.3146 | 0.3018 |
| Full 1901 | Country pairs | 48,230 | 0.3069 | 0.3630 | 0.3032 |
| Full 1901 | All seven countries | 0 | — | — | — |

### Paired MSE differences

Negative favors shrinkage. Brackets are approximate pointwise 95% intervals clustered by game, not by country/context case. They are not adjusted for multiple comparisons and do not account for repeated players or dataset selection.

| Window | Context | Shrinkage − baseline, all cases | Shrinkage − exact, matched cases |
|---|---|---|---|
| Spring 1901 | One country | -0.001750 [-0.001958, -0.001542] | -0.000067 [-0.000138, +0.000003] |
| Spring 1901 | Country pairs | -0.001765 [-0.001956, -0.001575] | -0.002688 [-0.002899, -0.002477] |
| Spring 1901 | All seven countries | -0.000014 [-0.000048, +0.000020] | -0.051285 [-0.059445, -0.043125] |
| Full 1901 | One country | -0.003822 [-0.004249, -0.003395] | -0.007926 [-0.008785, -0.007068] |
| Full 1901 | Country pairs | -0.000455 [-0.000536, -0.000375] | -0.039842 [-0.041580, -0.038103] |
| Full 1901 | All seven countries | +0.000000 [+0.000000, +0.000000] | — |

## Interpretation limits

This measures generalization within the same historical snapshot, not future-platform performance. The dataset has no usable player identities or original game dates for player-disjoint or chronological validation. Only games with detectable endings are included. Strength selection and these intervals do not remove that selection bias.

The benchmark covers complete own, pair and all-country histories. It does not establish accuracy for arbitrary partial-turn combinations, individual orders, third countries outside a selected pair, or other press/quality filters. Selected simultaneous orders are treated as known; this is not a model of opponents' unknown choices. A lower prediction error does not establish that changing an order causes a higher score or that a move-ranking policy works.

results.json includes validation curves, MAE, per-country results and support-count breakdowns. split_assignments.parquet preserves every game's split; manifest.json records source/input hashes, configuration and timings.
