# Spring 1901 opening book

37,202 games; 260,414 country/game observations. Games excluded for not starting in Spring 1901: 1.

The cohort uses standard-map in-scope games from no_press, press_with_msgs, and public_press. Unknown endings and press_without_msgs are excluded. Results describe recorded play in this selected historical sample; they do not establish the effect of an opening or an optimal strategy. Player skill and negotiation are not controlled for.

Each table shows up to 10 openings ordered by frequency, with exact orders and preserved coasts. Sparse means fewer than 200 games in that table's cohort. All openings, including sparse ones, are retained in openings_own.parquet. The minimum count is a display flag, not proof of reliability.

In a solo game, score is 1 for the winner and 0 for everyone else, including survivors. In a draw, score is final centers squared divided by the sum of squared final centers across all powers. Lift is the opening's mean score minus the same country's baseline in that press/quality cohort. The baseline includes the opening; lift is descriptive, not a significance test.

Brackets show approximate pointwise 95% intervals: Wilson for solo rates, normal mean ± 1.96 standard errors for scores, clipped to [0,1]. Score intervals are unavailable with fewer than two observations or zero observed variance; this does not mean the true score is certain. Normal intervals can be unreliable in sparse groups. Intervals assume independent game observations, are not adjusted for comparing many openings, and do not account for repeated players or selection bias.

Tier 1 repeats the analysis for games without detected dropout; detection uses terminal all-hold streaks, so this does not guarantee uninterrupted play. Its baseline is recalculated separately. Pooled estimates are available as press_level=all in the Parquet, but press modes are separated here.

## Austria

### No press — Tiers 1–3

15,333 games. Country baseline: 0.107 score; 6.6% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BUD - SER; A VIE - GAL; F TRI - ALB | 4,805 | 31.3% | 10.1% [9.2%, 10.9%] | 0.164 [0.155, 0.173] | +0.057 | n ≥ 200 |
| A BUD - SER; A VIE - TRI; F TRI - ALB | 2,203 | 14.4% | 7.7% [6.7%, 8.9%] | 0.117 [0.105, 0.129] | +0.010 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI - VEN | 1,361 | 8.9% | 4.8% [3.8%, 6.1%] | 0.075 [0.063, 0.087] | -0.032 | n ≥ 200 |
| A BUD H; A VIE H; F TRI H | 835 | 5.4% | 1.6% [0.9%, 2.6%] | 0.024 [0.015, 0.033] | -0.083 | n ≥ 200 |
| A BUD - SER; A VIE - BUD; F TRI - ALB | 785 | 5.1% | 6.8% [5.2%, 8.7%] | 0.125 [0.105, 0.144] | +0.018 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI H | 526 | 3.4% | 4.8% [3.2%, 6.9%] | 0.088 [0.068, 0.108] | -0.019 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI S A VEN | 371 | 2.4% | 7.8% [5.5%, 11.0%] | 0.121 [0.092, 0.150] | +0.014 | n ≥ 200 |
| A BUD - SER; A VIE - TYR; F TRI - ALB | 297 | 1.9% | 6.7% [4.4%, 10.2%] | 0.097 [0.067, 0.127] | -0.010 | n ≥ 200 |
| A BUD - RUM; A VIE - TRI; F TRI - ALB | 283 | 1.8% | 4.6% [2.7%, 7.7%] | 0.063 [0.037, 0.089] | -0.044 | n ≥ 200 |
| A BUD - SER; A VIE - BUD; F TRI H | 280 | 1.8% | 2.1% [1.0%, 4.6%] | 0.047 [0.027, 0.067] | -0.060 | n ≥ 200 |

### No press — Tier 1

7,106 games. Country baseline: 0.112 score; 6.4% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BUD - SER; A VIE - GAL; F TRI - ALB | 2,595 | 36.5% | 9.4% [8.3%, 10.5%] | 0.161 [0.149, 0.173] | +0.049 | n ≥ 200 |
| A BUD - SER; A VIE - TRI; F TRI - ALB | 1,025 | 14.4% | 7.1% [5.7%, 8.9%] | 0.115 [0.098, 0.132] | +0.003 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI - VEN | 627 | 8.8% | 3.3% [2.2%, 5.1%] | 0.061 [0.045, 0.077] | -0.050 | n ≥ 200 |
| A BUD - SER; A VIE - BUD; F TRI - ALB | 387 | 5.4% | 6.7% [4.6%, 9.7%] | 0.133 [0.105, 0.161] | +0.021 | n ≥ 200 |
| A BUD H; A VIE H; F TRI H | 231 | 3.3% | 1.7% [0.7%, 4.4%] | 0.030 [0.012, 0.049] | -0.081 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI H | 213 | 3.0% | 3.3% [1.6%, 6.6%] | 0.075 [0.046, 0.104] | -0.036 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI S A VEN | 187 | 2.6% | 8.6% [5.3%, 13.4%] | 0.118 [0.077, 0.159] | +0.007 | Sparse |
| A BUD - SER; A VIE - TYR; F TRI - ALB | 133 | 1.9% | 8.3% [4.7%, 14.2%] | 0.116 [0.067, 0.165] | +0.005 | Sparse |
| A BUD - GAL; A VIE - TRI; F TRI - ALB | 124 | 1.7% | 5.6% [2.8%, 11.2%] | 0.106 [0.061, 0.151] | -0.006 | Sparse |
| A BUD - RUM; A VIE - TRI; F TRI - ALB | 120 | 1.7% | 5.0% [2.3%, 10.5%] | 0.071 [0.030, 0.113] | -0.040 | Sparse |

### Private messages — Tiers 1–3

20,951 games. Country baseline: 0.113 score; 7.6% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BUD - SER; A VIE - TRI; F TRI - ALB | 3,977 | 19.0% | 9.9% [9.0%, 10.9%] | 0.145 [0.135, 0.155] | +0.032 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI - ALB | 3,227 | 15.4% | 12.4% [11.3%, 13.6%] | 0.189 [0.177, 0.201] | +0.076 | n ≥ 200 |
| A BUD - SER; A VIE - BUD; F TRI - ALB | 2,482 | 11.8% | 9.7% [8.6%, 10.9%] | 0.148 [0.136, 0.160] | +0.035 | n ≥ 200 |
| A BUD H; A VIE H; F TRI H | 1,569 | 7.5% | 1.0% [0.6%, 1.6%] | 0.017 [0.012, 0.022] | -0.096 | n ≥ 200 |
| A BUD - SER; A VIE - BUD; F TRI H | 925 | 4.4% | 6.4% [5.0%, 8.1%] | 0.093 [0.076, 0.110] | -0.021 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI - VEN | 793 | 3.8% | 7.7% [6.0%, 9.8%] | 0.122 [0.102, 0.141] | +0.008 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI H | 765 | 3.7% | 4.3% [3.1%, 6.0%] | 0.076 [0.060, 0.092] | -0.037 | n ≥ 200 |
| A BUD - SER; A VIE H; F TRI - ALB | 538 | 2.6% | 7.6% [5.7%, 10.2%] | 0.117 [0.094, 0.141] | +0.004 | n ≥ 200 |
| A BUD - RUM; A VIE - TRI; F TRI - ALB | 497 | 2.4% | 8.5% [6.3%, 11.2%] | 0.109 [0.084, 0.134] | -0.004 | n ≥ 200 |
| A BUD - SER; A VIE - TRI; F TRI - ADR | 467 | 2.2% | 6.9% [4.9%, 9.5%] | 0.090 [0.067, 0.114] | -0.023 | n ≥ 200 |

### Private messages — Tier 1

7,116 games. Country baseline: 0.115 score; 6.5% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BUD - SER; A VIE - TRI; F TRI - ALB | 1,350 | 19.0% | 8.9% [7.5%, 10.5%] | 0.147 [0.131, 0.163] | +0.032 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI - ALB | 1,249 | 17.6% | 9.1% [7.7%, 10.9%] | 0.174 [0.157, 0.191] | +0.059 | n ≥ 200 |
| A BUD - SER; A VIE - BUD; F TRI - ALB | 865 | 12.2% | 8.3% [6.7%, 10.4%] | 0.151 [0.132, 0.171] | +0.036 | n ≥ 200 |
| A BUD H; A VIE H; F TRI H | 369 | 5.2% | 1.4% [0.6%, 3.1%] | 0.023 [0.010, 0.036] | -0.092 | n ≥ 200 |
| A BUD - SER; A VIE - BUD; F TRI H | 320 | 4.5% | 5.6% [3.6%, 8.7%] | 0.089 [0.062, 0.116] | -0.026 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI - VEN | 312 | 4.4% | 7.7% [5.2%, 11.2%] | 0.125 [0.094, 0.156] | +0.010 | n ≥ 200 |
| A BUD - SER; A VIE - GAL; F TRI H | 248 | 3.5% | 2.4% [1.1%, 5.2%] | 0.062 [0.040, 0.085] | -0.053 | n ≥ 200 |
| A BUD - SER; A VIE H; F TRI - ALB | 183 | 2.6% | 4.9% [2.6%, 9.1%] | 0.110 [0.074, 0.145] | -0.005 | Sparse |
| A BUD - RUM; A VIE - GAL; F TRI - ALB | 168 | 2.4% | 3.6% [1.6%, 7.6%] | 0.072 [0.041, 0.103] | -0.043 | Sparse |
| A BUD - SER; A VIE - TYR; F TRI - ALB | 157 | 2.2% | 8.3% [4.9%, 13.7%] | 0.127 [0.081, 0.172] | +0.012 | Sparse |

### Public press — Tiers 1–3

918 games. Country baseline: 0.100 score; 4.9% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BUD - SER; A VIE - GAL; F TRI - ALB | 198 | 21.6% | 5.1% [2.8%, 9.0%] | 0.126 [0.090, 0.162] | +0.026 | Sparse |
| A BUD - SER; A VIE - TRI; F TRI - ALB | 157 | 17.1% | 5.1% [2.6%, 9.7%] | 0.123 [0.083, 0.163] | +0.023 | Sparse |
| A BUD - SER; A VIE - BUD; F TRI - ALB | 63 | 6.9% | 12.7% [6.6%, 23.1%] | 0.182 [0.099, 0.265] | +0.082 | Sparse |
| A BUD - SER; A VIE - GAL; F TRI - VEN | 54 | 5.9% | 1.9% [0.3%, 9.8%] | 0.073 [0.021, 0.124] | -0.027 | Sparse |
| A BUD H; A VIE H; F TRI H | 51 | 5.6% | 3.9% [1.1%, 13.2%] | 0.050 [0.000, 0.107] | -0.050 | Sparse |
| A BUD - SER; A VIE - GAL; F TRI H | 43 | 4.7% | 4.7% [1.3%, 15.5%] | 0.084 [0.016, 0.152] | -0.016 | Sparse |
| A BUD - SER; A VIE - BUD; F TRI H | 41 | 4.5% | 7.3% [2.5%, 19.4%] | 0.108 [0.025, 0.192] | +0.009 | Sparse |
| A BUD - SER; A VIE - TYR; F TRI - ALB | 28 | 3.1% | 10.7% [3.7%, 27.2%] | 0.115 [0.000, 0.232] | +0.015 | Sparse |
| A BUD - RUM; A VIE - TRI; F TRI - ALB | 26 | 2.8% | 3.8% [0.7%, 18.9%] | 0.063 [0.000, 0.144] | -0.037 | Sparse |
| A BUD - SER; A VIE - TRI; F TRI - ADR | 19 | 2.1% | 0.0% [0.0%, 16.8%] | 0.033 [0.000, 0.098] | -0.067 | Sparse |

### Public press — Tier 1

314 games. Country baseline: 0.094 score; 3.2% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BUD - SER; A VIE - GAL; F TRI - ALB | 77 | 24.5% | 3.9% [1.3%, 10.8%] | 0.129 [0.072, 0.185] | +0.035 | Sparse |
| A BUD - SER; A VIE - TRI; F TRI - ALB | 52 | 16.6% | 0.0% [0.0%, 6.9%] | 0.089 [0.042, 0.136] | -0.005 | Sparse |
| A BUD - SER; A VIE - BUD; F TRI - ALB | 27 | 8.6% | 14.8% [5.9%, 32.5%] | 0.215 [0.081, 0.349] | +0.122 | Sparse |
| A BUD - SER; A VIE - BUD; F TRI H | 19 | 6.1% | 0.0% [0.0%, 16.8%] | 0.026 [0.000, 0.060] | -0.068 | Sparse |
| A BUD - SER; A VIE - GAL; F TRI H | 17 | 5.4% | 0.0% [0.0%, 18.4%] | 0.045 [0.000, 0.095] | -0.049 | Sparse |
| A BUD - SER; A VIE - GAL; F TRI - VEN | 15 | 4.8% | 0.0% [0.0%, 20.4%] | 0.047 [0.000, 0.127] | -0.047 | Sparse |
| A BUD - SER; A VIE - TRI; F TRI - ADR | 9 | 2.9% | 0.0% [0.0%, 29.9%] | 0.070 [0.000, 0.207] | -0.024 | Sparse |
| A BUD - SER; A VIE - TYR; F TRI - ALB | 9 | 2.9% | 0.0% [0.0%, 29.9%] | 0.026 [0.000, 0.074] | -0.068 | Sparse |
| A BUD - RUM; A VIE - TRI; F TRI - ALB | 9 | 2.9% | 0.0% [0.0%, 29.9%] | 0.000 [unavailable] | -0.094 | Sparse |
| A BUD - SER; A VIE - TYR; F TRI H | 8 | 2.5% | 0.0% [0.0%, 32.4%] | 0.011 [0.000, 0.028] | -0.083 | Sparse |

## England

### No press — Tiers 1–3

15,333 games. Country baseline: 0.119 score; 7.1% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A LVP - YOR; F EDI - NWG; F LON - NTH | 4,786 | 31.2% | 7.5% [6.8%, 8.3%] | 0.128 [0.120, 0.136] | +0.009 | n ≥ 200 |
| A LVP - EDI; F EDI - NWG; F LON - NTH | 3,948 | 25.7% | 9.0% [8.2%, 10.0%] | 0.154 [0.145, 0.164] | +0.036 | n ≥ 200 |
| A LVP - YOR; F EDI - NTH; F LON - ENG | 3,364 | 21.9% | 6.8% [6.0%, 7.7%] | 0.103 [0.094, 0.112] | -0.016 | n ≥ 200 |
| A LVP - WAL; F EDI - NTH; F LON - ENG | 1,188 | 7.7% | 7.2% [5.9%, 8.9%] | 0.111 [0.095, 0.126] | -0.008 | n ≥ 200 |
| A LVP H; F EDI H; F LON H | 762 | 5.0% | 1.7% [1.0%, 2.9%] | 0.036 [0.026, 0.047] | -0.082 | n ≥ 200 |
| A LVP - EDI; F EDI - NTH; F LON - ENG | 254 | 1.7% | 7.9% [5.2%, 11.8%] | 0.115 [0.080, 0.150] | -0.004 | n ≥ 200 |
| A LVP - WAL; F EDI - NWG; F LON - NTH | 215 | 1.4% | 3.7% [1.9%, 7.2%] | 0.067 [0.039, 0.094] | -0.052 | n ≥ 200 |
| A LVP - EDI; F EDI - NWG; F LON - ENG | 121 | 0.8% | 5.8% [2.8%, 11.5%] | 0.088 [0.043, 0.133] | -0.031 | Sparse |
| A LVP - YOR; F EDI - NWG; F LON - ENG | 107 | 0.7% | 1.9% [0.5%, 6.6%] | 0.056 [0.025, 0.087] | -0.063 | Sparse |
| A LVP - WAL; F EDI - NWG; F LON - ENG | 75 | 0.5% | 1.3% [0.2%, 7.2%] | 0.063 [0.024, 0.101] | -0.056 | Sparse |

### No press — Tier 1

7,106 games. Country baseline: 0.121 score; 6.7% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A LVP - YOR; F EDI - NWG; F LON - NTH | 2,326 | 32.7% | 6.7% [5.8%, 7.8%] | 0.123 [0.113, 0.134] | +0.002 | n ≥ 200 |
| A LVP - EDI; F EDI - NWG; F LON - NTH | 1,947 | 27.4% | 8.5% [7.3%, 9.8%] | 0.157 [0.144, 0.170] | +0.036 | n ≥ 200 |
| A LVP - YOR; F EDI - NTH; F LON - ENG | 1,508 | 21.2% | 6.1% [5.0%, 7.4%] | 0.097 [0.084, 0.110] | -0.024 | n ≥ 200 |
| A LVP - WAL; F EDI - NTH; F LON - ENG | 575 | 8.1% | 7.0% [5.2%, 9.3%] | 0.115 [0.093, 0.137] | -0.006 | n ≥ 200 |
| A LVP H; F EDI H; F LON H | 231 | 3.3% | 2.6% [1.2%, 5.5%] | 0.067 [0.044, 0.091] | -0.054 | n ≥ 200 |
| A LVP - EDI; F EDI - NTH; F LON - ENG | 97 | 1.4% | 6.2% [2.9%, 12.8%] | 0.102 [0.050, 0.154] | -0.019 | Sparse |
| A LVP - WAL; F EDI - NWG; F LON - NTH | 92 | 1.3% | 3.3% [1.1%, 9.2%] | 0.082 [0.039, 0.124] | -0.039 | Sparse |
| A LVP - EDI; F EDI - NWG; F LON - ENG | 57 | 0.8% | 7.0% [2.8%, 16.7%] | 0.103 [0.032, 0.174] | -0.018 | Sparse |
| A LVP - YOR; F EDI - NWG; F LON - ENG | 49 | 0.7% | 0.0% [0.0%, 7.3%] | 0.049 [0.018, 0.080] | -0.072 | Sparse |
| A LVP - WAL; F EDI - NWG; F LON - ENG | 34 | 0.5% | 2.9% [0.5%, 14.9%] | 0.051 [0.000, 0.113] | -0.070 | Sparse |

### Private messages — Tiers 1–3

20,951 games. Country baseline: 0.138 score; 8.6% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A LVP - YOR; F EDI - NWG; F LON - NTH | 7,246 | 34.6% | 9.6% [8.9%, 10.3%] | 0.155 [0.148, 0.162] | +0.017 | n ≥ 200 |
| A LVP - EDI; F EDI - NWG; F LON - NTH | 4,147 | 19.8% | 11.1% [10.2%, 12.1%] | 0.177 [0.167, 0.187] | +0.040 | n ≥ 200 |
| A LVP - YOR; F EDI - NTH; F LON - ENG | 3,563 | 17.0% | 9.5% [8.6%, 10.5%] | 0.141 [0.132, 0.151] | +0.004 | n ≥ 200 |
| A LVP - WAL; F EDI - NTH; F LON - ENG | 2,132 | 10.2% | 8.8% [7.7%, 10.1%] | 0.144 [0.131, 0.156] | +0.006 | n ≥ 200 |
| A LVP H; F EDI H; F LON H | 1,489 | 7.1% | 2.0% [1.4%, 2.9%] | 0.037 [0.030, 0.045] | -0.100 | n ≥ 200 |
| A LVP - WAL; F EDI - NWG; F LON - NTH | 465 | 2.2% | 5.8% [4.0%, 8.3%] | 0.087 [0.065, 0.109] | -0.051 | n ≥ 200 |
| A LVP - EDI; F EDI - NTH; F LON - ENG | 253 | 1.2% | 10.7% [7.4%, 15.1%] | 0.154 [0.115, 0.193] | +0.016 | n ≥ 200 |
| A LVP - YOR; F EDI - NTH; F LON H | 167 | 0.8% | 1.8% [0.6%, 5.1%] | 0.055 [0.029, 0.080] | -0.083 | Sparse |
| A LVP - YOR; F EDI - NWG; F LON - ENG | 141 | 0.7% | 2.8% [1.1%, 7.1%] | 0.065 [0.033, 0.096] | -0.073 | Sparse |
| A LVP - WAL; F EDI - NWG; F LON - ENG | 139 | 0.7% | 2.9% [1.1%, 7.2%] | 0.059 [0.028, 0.091] | -0.078 | Sparse |

### Private messages — Tier 1

7,116 games. Country baseline: 0.146 score; 7.9% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A LVP - YOR; F EDI - NWG; F LON - NTH | 2,562 | 36.0% | 8.9% [7.8%, 10.0%] | 0.160 [0.149, 0.172] | +0.014 | n ≥ 200 |
| A LVP - EDI; F EDI - NWG; F LON - NTH | 1,487 | 20.9% | 9.1% [7.7%, 10.6%] | 0.176 [0.160, 0.191] | +0.030 | n ≥ 200 |
| A LVP - YOR; F EDI - NTH; F LON - ENG | 1,199 | 16.8% | 7.9% [6.5%, 9.6%] | 0.136 [0.120, 0.152] | -0.010 | n ≥ 200 |
| A LVP - WAL; F EDI - NTH; F LON - ENG | 760 | 10.7% | 8.3% [6.5%, 10.5%] | 0.157 [0.137, 0.178] | +0.012 | n ≥ 200 |
| A LVP H; F EDI H; F LON H | 367 | 5.2% | 2.2% [1.1%, 4.2%] | 0.047 [0.031, 0.064] | -0.098 | n ≥ 200 |
| A LVP - WAL; F EDI - NWG; F LON - NTH | 145 | 2.0% | 6.9% [3.8%, 12.2%] | 0.116 [0.072, 0.159] | -0.030 | Sparse |
| A LVP - EDI; F EDI - NTH; F LON - ENG | 74 | 1.0% | 10.8% [5.6%, 19.9%] | 0.149 [0.078, 0.221] | +0.004 | Sparse |
| A LVP - YOR; F EDI - NTH; F LON H | 55 | 0.8% | 3.6% [1.0%, 12.3%] | 0.091 [0.031, 0.151] | -0.055 | Sparse |
| A LVP - WAL; F EDI - NWG; F LON - ENG | 48 | 0.7% | 6.2% [2.1%, 16.8%] | 0.096 [0.025, 0.168] | -0.049 | Sparse |
| A LVP - YOR; F EDI - NWG; F LON - ENG | 44 | 0.6% | 0.0% [0.0%, 8.0%] | 0.051 [0.020, 0.081] | -0.095 | Sparse |

### Public press — Tiers 1–3

918 games. Country baseline: 0.139 score; 6.6% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A LVP - YOR; F EDI - NWG; F LON - NTH | 320 | 34.9% | 5.6% [3.6%, 8.7%] | 0.141 [0.113, 0.168] | +0.002 | n ≥ 200 |
| A LVP - EDI; F EDI - NWG; F LON - NTH | 192 | 20.9% | 12.0% [8.1%, 17.3%] | 0.220 [0.174, 0.267] | +0.082 | Sparse |
| A LVP - YOR; F EDI - NTH; F LON - ENG | 178 | 19.4% | 7.3% [4.3%, 12.1%] | 0.150 [0.109, 0.191] | +0.012 | Sparse |
| A LVP - WAL; F EDI - NTH; F LON - ENG | 54 | 5.9% | 7.4% [2.9%, 17.6%] | 0.119 [0.044, 0.193] | -0.020 | Sparse |
| A LVP H; F EDI H; F LON H | 52 | 5.7% | 1.9% [0.3%, 10.1%] | 0.025 [0.000, 0.063] | -0.114 | Sparse |
| A LVP - WAL; F EDI - NWG; F LON - NTH | 31 | 3.4% | 0.0% [0.0%, 11.0%] | 0.052 [0.015, 0.089] | -0.087 | Sparse |
| A LVP - EDI; F EDI - NTH; F LON - ENG | 14 | 1.5% | 0.0% [0.0%, 21.5%] | 0.021 [0.000, 0.057] | -0.117 | Sparse |
| A LVP - YOR; F EDI - NTH; F LON - NTH | 11 | 1.2% | 0.0% [0.0%, 25.9%] | 0.024 [0.000, 0.066] | -0.114 | Sparse |
| A LVP - EDI; F EDI - NWG; F LON - ENG | 9 | 1.0% | 22.2% [6.3%, 54.7%] | 0.298 [0.026, 0.570] | +0.160 | Sparse |
| A LVP - WAL; F EDI - NWG; F LON - ENG | 9 | 1.0% | 0.0% [0.0%, 29.9%] | 0.000 [unavailable] | -0.139 | Sparse |

### Public press — Tier 1

314 games. Country baseline: 0.157 score; 6.1% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A LVP - YOR; F EDI - NWG; F LON - NTH | 124 | 39.5% | 2.4% [0.8%, 6.9%] | 0.135 [0.099, 0.171] | -0.022 | Sparse |
| A LVP - EDI; F EDI - NWG; F LON - NTH | 72 | 22.9% | 12.5% [6.7%, 22.1%] | 0.243 [0.165, 0.322] | +0.086 | Sparse |
| A LVP - YOR; F EDI - NTH; F LON - ENG | 55 | 17.5% | 10.9% [5.1%, 21.8%] | 0.206 [0.123, 0.290] | +0.049 | Sparse |
| A LVP H; F EDI H; F LON H | 15 | 4.8% | 0.0% [0.0%, 20.4%] | 0.018 [0.000, 0.036] | -0.139 | Sparse |
| A LVP - WAL; F EDI - NTH; F LON - ENG | 11 | 3.5% | 9.1% [1.6%, 37.7%] | 0.193 [0.000, 0.399] | +0.035 | Sparse |
| A LVP - WAL; F EDI - NWG; F LON - NTH | 7 | 2.2% | 0.0% [0.0%, 35.4%] | 0.053 [0.000, 0.135] | -0.104 | Sparse |
| A LVP - EDI; F EDI - NTH; F LON - ENG | 5 | 1.6% | 0.0% [0.0%, 43.4%] | 0.005 [0.000, 0.014] | -0.153 | Sparse |
| A LVP - EDI; F EDI - NWG; F LON - ENG | 4 | 1.3% | 0.0% [0.0%, 49.0%] | 0.171 [0.021, 0.321] | +0.014 | Sparse |
| A LVP - YOR; F EDI - NTH; F LON - NTH | 3 | 1.0% | 0.0% [0.0%, 56.1%] | 0.000 [unavailable] | -0.157 | Sparse |
| A LVP - YOR; F EDI - NTH; F LON - WAL | 3 | 1.0% | 0.0% [0.0%, 56.1%] | 0.000 [unavailable] | -0.157 | Sparse |

## France

### No press — Tiers 1–3

15,333 games. Country baseline: 0.178 score; 12.1% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - MAO | 3,848 | 25.1% | 16.9% [15.8%, 18.1%] | 0.240 [0.228, 0.252] | +0.061 | n ≥ 200 |
| A MAR - SPA; A PAR - BUR; F BRE - MAO | 2,621 | 17.1% | 10.5% [9.4%, 11.7%] | 0.161 [0.149, 0.173] | -0.018 | n ≥ 200 |
| A MAR - SPA; A PAR - PIC; F BRE - MAO | 1,176 | 7.7% | 7.1% [5.7%, 8.7%] | 0.118 [0.102, 0.133] | -0.061 | n ≥ 200 |
| A MAR - BUR; A PAR - PIC; F BRE - MAO | 931 | 6.1% | 13.6% [11.6%, 16.0%] | 0.216 [0.194, 0.239] | +0.038 | n ≥ 200 |
| A MAR - SPA; A PAR - BUR; F BRE - ENG | 922 | 6.0% | 12.8% [10.8%, 15.1%] | 0.172 [0.150, 0.194] | -0.006 | n ≥ 200 |
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - ENG | 846 | 5.5% | 15.8% [13.5%, 18.5%] | 0.211 [0.186, 0.235] | +0.032 | n ≥ 200 |
| A MAR H; A PAR H; F BRE H | 742 | 4.8% | 3.4% [2.3%, 4.9%] | 0.062 [0.048, 0.076] | -0.117 | n ≥ 200 |
| A MAR - BUR; A PAR - GAS; F BRE - MAO | 652 | 4.3% | 18.3% [15.5%, 21.4%] | 0.263 [0.234, 0.292] | +0.085 | n ≥ 200 |
| A MAR - SPA; A PAR - PIC; F BRE - ENG | 546 | 3.6% | 9.2% [7.0%, 11.9%] | 0.133 [0.108, 0.158] | -0.045 | n ≥ 200 |
| A MAR - SPA; A PAR - GAS; F BRE - MAO | 330 | 2.2% | 10.0% [7.2%, 13.7%] | 0.152 [0.119, 0.185] | -0.027 | n ≥ 200 |

### No press — Tier 1

7,106 games. Country baseline: 0.185 score; 12.0% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - MAO | 1,894 | 26.7% | 16.4% [14.8%, 18.1%] | 0.245 [0.229, 0.261] | +0.060 | n ≥ 200 |
| A MAR - SPA; A PAR - BUR; F BRE - MAO | 1,195 | 16.8% | 10.4% [8.8%, 12.2%] | 0.165 [0.148, 0.183] | -0.020 | n ≥ 200 |
| A MAR - SPA; A PAR - PIC; F BRE - MAO | 540 | 7.6% | 7.2% [5.3%, 9.7%] | 0.130 [0.107, 0.153] | -0.055 | n ≥ 200 |
| A MAR - BUR; A PAR - PIC; F BRE - MAO | 459 | 6.5% | 11.1% [8.6%, 14.3%] | 0.190 [0.161, 0.220] | +0.005 | n ≥ 200 |
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - ENG | 406 | 5.7% | 15.0% [11.9%, 18.8%] | 0.203 [0.168, 0.237] | +0.017 | n ≥ 200 |
| A MAR - SPA; A PAR - BUR; F BRE - ENG | 384 | 5.4% | 12.2% [9.3%, 15.9%] | 0.170 [0.137, 0.203] | -0.015 | n ≥ 200 |
| A MAR - BUR; A PAR - GAS; F BRE - MAO | 357 | 5.0% | 18.2% [14.5%, 22.5%] | 0.264 [0.225, 0.302] | +0.078 | n ≥ 200 |
| A MAR - SPA; A PAR - PIC; F BRE - ENG | 237 | 3.3% | 8.4% [5.5%, 12.7%] | 0.143 [0.106, 0.180] | -0.042 | n ≥ 200 |
| A MAR H; A PAR H; F BRE H | 220 | 3.1% | 1.4% [0.5%, 3.9%] | 0.054 [0.036, 0.072] | -0.131 | n ≥ 200 |
| A MAR - SPA; A PAR - GAS; F BRE - MAO | 187 | 2.6% | 11.8% [7.9%, 17.2%] | 0.173 [0.126, 0.220] | -0.012 | Sparse |

### Private messages — Tiers 1–3

20,951 games. Country baseline: 0.166 score; 11.1% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MAR - SPA; A PAR - BUR; F BRE - MAO | 3,875 | 18.5% | 11.9% [11.0%, 13.0%] | 0.171 [0.161, 0.182] | +0.006 | n ≥ 200 |
| A MAR - SPA; A PAR - PIC; F BRE - MAO | 3,449 | 16.5% | 10.8% [9.8%, 11.9%] | 0.164 [0.154, 0.175] | -0.001 | n ≥ 200 |
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - MAO | 2,221 | 10.6% | 15.6% [14.2%, 17.2%] | 0.233 [0.218, 0.248] | +0.068 | n ≥ 200 |
| A MAR H; A PAR H; F BRE H | 1,438 | 6.9% | 2.9% [2.1%, 3.8%] | 0.051 [0.042, 0.061] | -0.114 | n ≥ 200 |
| A MAR - SPA; A PAR - PIC; F BRE - ENG | 1,425 | 6.8% | 11.8% [10.2%, 13.6%] | 0.169 [0.152, 0.186] | +0.003 | n ≥ 200 |
| A MAR - SPA; A PAR - BUR; F BRE - ENG | 1,061 | 5.1% | 13.6% [11.6%, 15.8%] | 0.185 [0.164, 0.206] | +0.020 | n ≥ 200 |
| A MAR - BUR; A PAR - PIC; F BRE - MAO | 853 | 4.1% | 14.8% [12.5%, 17.3%] | 0.218 [0.194, 0.242] | +0.052 | n ≥ 200 |
| A MAR - SPA; A PAR - BUR; F BRE - PIC | 807 | 3.9% | 10.5% [8.6%, 12.8%] | 0.139 [0.118, 0.161] | -0.026 | n ≥ 200 |
| A MAR H; A PAR - PIC; F BRE - MAO | 784 | 3.7% | 12.8% [10.6%, 15.3%] | 0.192 [0.168, 0.215] | +0.026 | n ≥ 200 |
| A MAR - SPA; A PAR - GAS; F BRE - MAO | 531 | 2.5% | 8.1% [6.1%, 10.7%] | 0.148 [0.124, 0.172] | -0.018 | n ≥ 200 |

### Private messages — Tier 1

7,116 games. Country baseline: 0.166 score; 9.6% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MAR - SPA; A PAR - BUR; F BRE - MAO | 1,298 | 18.2% | 10.8% [9.2%, 12.6%] | 0.172 [0.155, 0.189] | +0.006 | n ≥ 200 |
| A MAR - SPA; A PAR - PIC; F BRE - MAO | 1,166 | 16.4% | 8.6% [7.1%, 10.3%] | 0.155 [0.138, 0.172] | -0.011 | n ≥ 200 |
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - MAO | 810 | 11.4% | 12.0% [9.9%, 14.4%] | 0.215 [0.192, 0.237] | +0.048 | n ≥ 200 |
| A MAR - SPA; A PAR - PIC; F BRE - ENG | 489 | 6.9% | 11.7% [9.1%, 14.8%] | 0.182 [0.153, 0.211] | +0.016 | n ≥ 200 |
| A MAR H; A PAR H; F BRE H | 354 | 5.0% | 5.1% [3.2%, 7.9%] | 0.084 [0.059, 0.108] | -0.083 | n ≥ 200 |
| A MAR - BUR; A PAR - PIC; F BRE - MAO | 339 | 4.8% | 10.0% [7.3%, 13.7%] | 0.199 [0.165, 0.232] | +0.032 | n ≥ 200 |
| A MAR - SPA; A PAR - BUR; F BRE - ENG | 332 | 4.7% | 12.3% [9.2%, 16.3%] | 0.179 [0.143, 0.216] | +0.013 | n ≥ 200 |
| A MAR H; A PAR - PIC; F BRE - MAO | 258 | 3.6% | 12.8% [9.3%, 17.4%] | 0.193 [0.152, 0.234] | +0.027 | n ≥ 200 |
| A MAR - SPA; A PAR - BUR; F BRE - PIC | 231 | 3.2% | 10.0% [6.7%, 14.5%] | 0.151 [0.111, 0.191] | -0.015 | n ≥ 200 |
| A MAR - SPA; A PAR - GAS; F BRE - MAO | 195 | 2.7% | 6.2% [3.6%, 10.4%] | 0.151 [0.114, 0.188] | -0.015 | Sparse |

### Public press — Tiers 1–3

918 games. Country baseline: 0.161 score; 8.9% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MAR - SPA; A PAR - BUR; F BRE - MAO | 197 | 21.5% | 10.7% [7.1%, 15.7%] | 0.187 [0.143, 0.231] | +0.026 | Sparse |
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - MAO | 160 | 17.4% | 14.4% [9.8%, 20.6%] | 0.239 [0.185, 0.293] | +0.078 | Sparse |
| A MAR - SPA; A PAR - PIC; F BRE - MAO | 119 | 13.0% | 4.2% [1.8%, 9.5%] | 0.121 [0.080, 0.163] | -0.040 | Sparse |
| A MAR - SPA; A PAR - BUR; F BRE - ENG | 64 | 7.0% | 12.5% [6.5%, 22.8%] | 0.196 [0.113, 0.279] | +0.035 | Sparse |
| A MAR H; A PAR H; F BRE H | 54 | 5.9% | 1.9% [0.3%, 9.8%] | 0.051 [0.005, 0.097] | -0.110 | Sparse |
| A MAR - BUR; A PAR - PIC; F BRE - MAO | 37 | 4.0% | 8.1% [2.8%, 21.3%] | 0.136 [0.045, 0.228] | -0.025 | Sparse |
| A MAR - SPA; A PAR - PIC; F BRE - ENG | 34 | 3.7% | 11.8% [4.7%, 26.6%] | 0.168 [0.057, 0.280] | +0.007 | Sparse |
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - ENG | 29 | 3.2% | 24.1% [12.2%, 42.1%] | 0.309 [0.156, 0.463] | +0.148 | Sparse |
| A MAR H; A PAR - PIC; F BRE - MAO | 27 | 2.9% | 7.4% [2.1%, 23.4%] | 0.137 [0.035, 0.239] | -0.024 | Sparse |
| A MAR - SPA; A PAR - GAS; F BRE - ENG | 26 | 2.8% | 7.7% [2.1%, 24.1%] | 0.156 [0.046, 0.267] | -0.005 | Sparse |

### Public press — Tier 1

314 games. Country baseline: 0.140 score; 5.4% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MAR - SPA; A PAR - BUR; F BRE - MAO | 75 | 23.9% | 6.7% [2.9%, 14.7%] | 0.170 [0.111, 0.230] | +0.031 | Sparse |
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - MAO | 59 | 18.8% | 6.8% [2.7%, 16.2%] | 0.153 [0.087, 0.219] | +0.013 | Sparse |
| A MAR - SPA; A PAR - PIC; F BRE - MAO | 39 | 12.4% | 2.6% [0.5%, 13.2%] | 0.121 [0.060, 0.181] | -0.019 | Sparse |
| A MAR - SPA; A PAR - BUR; F BRE - ENG | 21 | 6.7% | 9.5% [2.7%, 28.9%] | 0.173 [0.038, 0.308] | +0.033 | Sparse |
| A MAR - SPA; A PAR - PIC; F BRE - ENG | 13 | 4.1% | 7.7% [1.4%, 33.3%] | 0.181 [0.018, 0.344] | +0.041 | Sparse |
| A MAR S A PAR - BUR; A PAR - BUR; F BRE - ENG | 12 | 3.8% | 0.0% [0.0%, 24.2%] | 0.039 [0.000, 0.091] | -0.101 | Sparse |
| A MAR H; A PAR - PIC; F BRE - MAO | 11 | 3.5% | 0.0% [0.0%, 25.9%] | 0.071 [0.010, 0.131] | -0.069 | Sparse |
| A MAR - BUR; A PAR - GAS; F BRE - MAO | 10 | 3.2% | 0.0% [0.0%, 27.8%] | 0.187 [0.048, 0.327] | +0.047 | Sparse |
| A MAR - BUR; A PAR - PIC; F BRE - MAO | 9 | 2.9% | 11.1% [2.0%, 43.5%] | 0.158 [0.000, 0.373] | +0.018 | Sparse |
| A MAR H; A PAR H; F BRE H | 8 | 2.5% | 0.0% [0.0%, 32.4%] | 0.022 [0.000, 0.060] | -0.118 | Sparse |

## Germany

### No press — Tiers 1–3

15,333 games. Country baseline: 0.155 score; 10.3% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BER - KIE; A MUN - RUH; F KIE - DEN | 5,732 | 37.4% | 12.0% [11.2%, 12.9%] | 0.182 [0.173, 0.190] | +0.027 | n ≥ 200 |
| A BER - KIE; A MUN - RUH; F KIE - HOL | 2,606 | 17.0% | 11.0% [9.8%, 12.2%] | 0.157 [0.145, 0.169] | +0.002 | n ≥ 200 |
| A BER - KIE; A MUN - BUR; F KIE - DEN | 2,395 | 15.6% | 12.4% [11.1%, 13.7%] | 0.184 [0.171, 0.198] | +0.030 | n ≥ 200 |
| A BER - KIE; A MUN - BUR; F KIE - HOL | 869 | 5.7% | 9.3% [7.6%, 11.4%] | 0.134 [0.114, 0.154] | -0.021 | n ≥ 200 |
| A BER H; A MUN H; F KIE H | 751 | 4.9% | 1.2% [0.6%, 2.3%] | 0.027 [0.018, 0.036] | -0.128 | n ≥ 200 |
| A BER - KIE; A MUN H; F KIE - DEN | 294 | 1.9% | 7.1% [4.7%, 10.7%] | 0.116 [0.084, 0.147] | -0.039 | n ≥ 200 |
| A BER - KIE; A MUN H; F KIE - HOL | 224 | 1.5% | 2.7% [1.2%, 5.7%] | 0.069 [0.044, 0.095] | -0.085 | n ≥ 200 |
| A BER - KIE; A MUN - TYR; F KIE - DEN | 202 | 1.3% | 11.4% [7.7%, 16.5%] | 0.182 [0.137, 0.227] | +0.027 | n ≥ 200 |
| A BER - MUN; A MUN - RUH; F KIE - DEN | 199 | 1.3% | 12.1% [8.2%, 17.3%] | 0.209 [0.162, 0.256] | +0.054 | Sparse |
| A BER - SIL; A MUN - RUH; F KIE - DEN | 185 | 1.2% | 6.5% [3.7%, 11.0%] | 0.107 [0.069, 0.145] | -0.048 | Sparse |

### No press — Tier 1

7,106 games. Country baseline: 0.153 score; 9.6% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BER - KIE; A MUN - RUH; F KIE - DEN | 2,876 | 40.5% | 11.2% [10.1%, 12.4%] | 0.179 [0.167, 0.191] | +0.026 | n ≥ 200 |
| A BER - KIE; A MUN - RUH; F KIE - HOL | 1,183 | 16.6% | 9.6% [8.0%, 11.4%] | 0.143 [0.126, 0.160] | -0.010 | n ≥ 200 |
| A BER - KIE; A MUN - BUR; F KIE - DEN | 1,099 | 15.5% | 10.3% [8.6%, 12.2%] | 0.170 [0.151, 0.188] | +0.017 | n ≥ 200 |
| A BER - KIE; A MUN - BUR; F KIE - HOL | 389 | 5.5% | 8.2% [5.9%, 11.4%] | 0.132 [0.103, 0.160] | -0.022 | n ≥ 200 |
| A BER H; A MUN H; F KIE H | 208 | 2.9% | 1.0% [0.3%, 3.4%] | 0.033 [0.016, 0.050] | -0.121 | n ≥ 200 |
| A BER - KIE; A MUN H; F KIE - DEN | 139 | 2.0% | 9.4% [5.5%, 15.3%] | 0.124 [0.074, 0.174] | -0.029 | Sparse |
| A BER - KIE; A MUN - TYR; F KIE - DEN | 104 | 1.5% | 12.5% [7.5%, 20.2%] | 0.189 [0.124, 0.254] | +0.036 | Sparse |
| A BER - MUN; A MUN - RUH; F KIE - DEN | 90 | 1.3% | 12.2% [7.0%, 20.6%] | 0.211 [0.139, 0.282] | +0.057 | Sparse |
| A BER - KIE; A MUN S A PAR - BUR; F KIE - DEN | 87 | 1.2% | 17.2% [10.7%, 26.5%] | 0.246 [0.168, 0.324] | +0.093 | Sparse |
| A BER - KIE; A MUN H; F KIE - HOL | 84 | 1.2% | 3.6% [1.2%, 10.0%] | 0.083 [0.039, 0.128] | -0.070 | Sparse |

### Private messages — Tiers 1–3

20,951 games. Country baseline: 0.134 score; 9.1% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BER - KIE; A MUN - RUH; F KIE - DEN | 6,419 | 30.6% | 11.7% [11.0%, 12.6%] | 0.175 [0.167, 0.183] | +0.041 | n ≥ 200 |
| A BER - KIE; A MUN - RUH; F KIE - HOL | 3,726 | 17.8% | 10.3% [9.4%, 11.4%] | 0.150 [0.140, 0.160] | +0.015 | n ≥ 200 |
| A BER - KIE; A MUN - BUR; F KIE - DEN | 1,876 | 9.0% | 12.3% [10.9%, 13.9%] | 0.182 [0.167, 0.197] | +0.048 | n ≥ 200 |
| A BER H; A MUN H; F KIE H | 1,587 | 7.6% | 1.4% [1.0%, 2.2%] | 0.025 [0.018, 0.031] | -0.110 | n ≥ 200 |
| A BER - KIE; A MUN - BUR; F KIE - HOL | 1,362 | 6.5% | 10.1% [8.6%, 11.8%] | 0.149 [0.133, 0.166] | +0.015 | n ≥ 200 |
| A BER - KIE; A MUN H; F KIE - HOL | 719 | 3.4% | 4.7% [3.4%, 6.5%] | 0.076 [0.059, 0.092] | -0.059 | n ≥ 200 |
| A BER - KIE; A MUN H; F KIE - DEN | 711 | 3.4% | 7.9% [6.1%, 10.1%] | 0.125 [0.104, 0.146] | -0.009 | n ≥ 200 |
| A BER - SIL; A MUN - RUH; F KIE - DEN | 397 | 1.9% | 8.1% [5.8%, 11.2%] | 0.121 [0.093, 0.149] | -0.014 | n ≥ 200 |
| A BER - KIE; A MUN - TYR; F KIE - DEN | 252 | 1.2% | 10.3% [7.1%, 14.7%] | 0.143 [0.105, 0.181] | +0.008 | n ≥ 200 |
| A BER - KIE; A MUN - TYR; F KIE - HOL | 204 | 1.0% | 6.9% [4.1%, 11.2%] | 0.107 [0.070, 0.143] | -0.028 | n ≥ 200 |

### Private messages — Tier 1

7,116 games. Country baseline: 0.128 score; 7.0% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BER - KIE; A MUN - RUH; F KIE - DEN | 2,350 | 33.0% | 9.1% [8.0%, 10.3%] | 0.164 [0.152, 0.176] | +0.036 | n ≥ 200 |
| A BER - KIE; A MUN - RUH; F KIE - HOL | 1,235 | 17.4% | 8.3% [6.9%, 9.9%] | 0.139 [0.123, 0.155] | +0.011 | n ≥ 200 |
| A BER - KIE; A MUN - BUR; F KIE - DEN | 719 | 10.1% | 7.9% [6.2%, 10.1%] | 0.158 [0.137, 0.179] | +0.030 | n ≥ 200 |
| A BER - KIE; A MUN - BUR; F KIE - HOL | 476 | 6.7% | 7.1% [5.2%, 9.8%] | 0.133 [0.109, 0.158] | +0.005 | n ≥ 200 |
| A BER H; A MUN H; F KIE H | 379 | 5.3% | 0.3% [0.0%, 1.5%] | 0.020 [0.011, 0.028] | -0.108 | n ≥ 200 |
| A BER - KIE; A MUN H; F KIE - DEN | 228 | 3.2% | 7.0% [4.4%, 11.1%] | 0.141 [0.105, 0.177] | +0.013 | n ≥ 200 |
| A BER - KIE; A MUN H; F KIE - HOL | 216 | 3.0% | 1.4% [0.5%, 4.0%] | 0.054 [0.034, 0.075] | -0.073 | n ≥ 200 |
| A BER - SIL; A MUN - RUH; F KIE - DEN | 138 | 1.9% | 7.2% [4.0%, 12.8%] | 0.123 [0.077, 0.169] | -0.005 | Sparse |
| A BER - KIE; A MUN - TYR; F KIE - DEN | 97 | 1.4% | 8.2% [4.2%, 15.4%] | 0.143 [0.086, 0.201] | +0.016 | Sparse |
| A BER - PRU; A MUN - SIL; F KIE - DEN | 73 | 1.0% | 8.2% [3.8%, 16.8%] | 0.140 [0.073, 0.207] | +0.012 | Sparse |

### Public press — Tiers 1–3

918 games. Country baseline: 0.133 score; 7.2% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BER - KIE; A MUN - RUH; F KIE - DEN | 327 | 35.6% | 8.0% [5.5%, 11.4%] | 0.157 [0.126, 0.188] | +0.024 | n ≥ 200 |
| A BER - KIE; A MUN - RUH; F KIE - HOL | 167 | 18.2% | 9.6% [6.0%, 15.0%] | 0.165 [0.119, 0.212] | +0.032 | Sparse |
| A BER - KIE; A MUN - BUR; F KIE - DEN | 98 | 10.7% | 9.2% [4.9%, 16.5%] | 0.169 [0.109, 0.229] | +0.036 | Sparse |
| A BER H; A MUN H; F KIE H | 64 | 7.0% | 1.6% [0.3%, 8.3%] | 0.045 [0.006, 0.084] | -0.089 | Sparse |
| A BER - KIE; A MUN - BUR; F KIE - HOL | 55 | 6.0% | 7.3% [2.9%, 17.3%] | 0.122 [0.050, 0.193] | -0.012 | Sparse |
| A BER - KIE; A MUN H; F KIE - HOL | 30 | 3.3% | 6.7% [1.8%, 21.3%] | 0.099 [0.004, 0.193] | -0.035 | Sparse |
| A BER - KIE; A MUN H; F KIE - DEN | 23 | 2.5% | 0.0% [0.0%, 14.3%] | 0.087 [0.029, 0.145] | -0.046 | Sparse |
| A BER - SIL; A MUN - RUH; F KIE - DEN | 17 | 1.9% | 0.0% [0.0%, 18.4%] | 0.097 [0.014, 0.180] | -0.037 | Sparse |
| A BER - KIE; A MUN - SIL; F KIE - DEN | 12 | 1.3% | 8.3% [1.5%, 35.4%] | 0.118 [0.000, 0.283] | -0.016 | Sparse |
| A BER - PRU; A MUN - RUH; F KIE - DEN | 11 | 1.2% | 0.0% [0.0%, 25.9%] | 0.026 [0.000, 0.066] | -0.108 | Sparse |

### Public press — Tier 1

314 games. Country baseline: 0.156 score; 7.3% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A BER - KIE; A MUN - RUH; F KIE - DEN | 123 | 39.2% | 9.8% [5.7%, 16.3%] | 0.202 [0.148, 0.256] | +0.046 | Sparse |
| A BER - KIE; A MUN - RUH; F KIE - HOL | 63 | 20.1% | 6.3% [2.5%, 15.2%] | 0.146 [0.082, 0.210] | -0.010 | Sparse |
| A BER - KIE; A MUN - BUR; F KIE - DEN | 28 | 8.9% | 3.6% [0.6%, 17.7%] | 0.145 [0.060, 0.231] | -0.011 | Sparse |
| A BER - KIE; A MUN - BUR; F KIE - HOL | 18 | 5.7% | 5.6% [1.0%, 25.8%] | 0.115 [0.000, 0.231] | -0.042 | Sparse |
| A BER H; A MUN H; F KIE H | 16 | 5.1% | 0.0% [0.0%, 19.4%] | 0.063 [0.000, 0.132] | -0.093 | Sparse |
| A BER - KIE; A MUN H; F KIE - DEN | 9 | 2.9% | 0.0% [0.0%, 29.9%] | 0.099 [0.005, 0.193] | -0.057 | Sparse |
| A BER - KIE; A MUN - RUH; F KIE - HEL | 6 | 1.9% | 16.7% [3.0%, 56.4%] | 0.211 [0.000, 0.532] | +0.055 | Sparse |
| A BER - KIE; A MUN H; F KIE - HOL | 6 | 1.9% | 0.0% [0.0%, 39.0%] | 0.039 [0.000, 0.101] | -0.117 | Sparse |
| A BER - KIE; A MUN - SIL; F KIE - DEN | 4 | 1.3% | 0.0% [0.0%, 49.0%] | 0.076 [0.000, 0.226] | -0.080 | Sparse |
| A BER - SIL; A MUN - RUH; F KIE - DEN | 4 | 1.3% | 0.0% [0.0%, 49.0%] | 0.132 [0.000, 0.336] | -0.024 | Sparse |

## Italy

### No press — Tiers 1–3

15,333 games. Country baseline: 0.116 score; 7.3% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A ROM - VEN; A VEN - TYR; F NAP - ION | 3,807 | 24.8% | 11.5% [10.6%, 12.6%] | 0.160 [0.150, 0.171] | +0.045 | n ≥ 200 |
| A ROM - APU; A VEN H; F NAP - ION | 2,104 | 13.7% | 7.3% [6.2%, 8.5%] | 0.124 [0.113, 0.136] | +0.009 | n ≥ 200 |
| A ROM - APU; A VEN S F TRI; F NAP - ION | 1,360 | 8.9% | 8.8% [7.4%, 10.4%] | 0.144 [0.129, 0.160] | +0.029 | n ≥ 200 |
| A ROM - VEN; A VEN - PIE; F NAP - ION | 1,288 | 8.4% | 6.8% [5.5%, 8.3%] | 0.107 [0.093, 0.122] | -0.008 | n ≥ 200 |
| A ROM H; A VEN H; F NAP H | 804 | 5.2% | 1.5% [0.9%, 2.6%] | 0.034 [0.025, 0.044] | -0.082 | n ≥ 200 |
| A ROM - VEN; A VEN - TRI; F NAP - ION | 708 | 4.6% | 10.3% [8.3%, 12.8%] | 0.144 [0.120, 0.167] | +0.028 | n ≥ 200 |
| A ROM - APU; A VEN - TRI; F NAP - ION | 595 | 3.9% | 6.9% [5.1%, 9.2%] | 0.115 [0.093, 0.136] | -0.001 | n ≥ 200 |
| A ROM - APU; A VEN - PIE; F NAP - ION | 584 | 3.8% | 4.3% [2.9%, 6.2%] | 0.105 [0.086, 0.124] | -0.010 | n ≥ 200 |
| A ROM - NAP; A VEN H; F NAP - ION | 554 | 3.6% | 3.2% [2.1%, 5.1%] | 0.068 [0.051, 0.085] | -0.048 | n ≥ 200 |
| A ROM - VEN; A VEN - PIE; F NAP - TYS | 343 | 2.2% | 4.1% [2.4%, 6.7%] | 0.079 [0.056, 0.103] | -0.037 | n ≥ 200 |

### No press — Tier 1

7,106 games. Country baseline: 0.110 score; 6.5% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A ROM - VEN; A VEN - TYR; F NAP - ION | 1,622 | 22.8% | 10.7% [9.3%, 12.3%] | 0.149 [0.134, 0.165] | +0.040 | n ≥ 200 |
| A ROM - APU; A VEN H; F NAP - ION | 1,030 | 14.5% | 6.8% [5.4%, 8.5%] | 0.123 [0.107, 0.139] | +0.013 | n ≥ 200 |
| A ROM - APU; A VEN S F TRI; F NAP - ION | 712 | 10.0% | 8.0% [6.2%, 10.2%] | 0.138 [0.117, 0.159] | +0.028 | n ≥ 200 |
| A ROM - VEN; A VEN - PIE; F NAP - ION | 592 | 8.3% | 6.4% [4.7%, 8.7%] | 0.104 [0.083, 0.125] | -0.005 | n ≥ 200 |
| A ROM - APU; A VEN - PIE; F NAP - ION | 347 | 4.9% | 2.9% [1.6%, 5.2%] | 0.092 [0.070, 0.114] | -0.017 | n ≥ 200 |
| A ROM - VEN; A VEN - TRI; F NAP - ION | 330 | 4.6% | 10.6% [7.7%, 14.4%] | 0.156 [0.121, 0.190] | +0.046 | n ≥ 200 |
| A ROM - APU; A VEN - TRI; F NAP - ION | 299 | 4.2% | 4.7% [2.8%, 7.7%] | 0.096 [0.069, 0.123] | -0.014 | n ≥ 200 |
| A ROM - NAP; A VEN H; F NAP - ION | 274 | 3.9% | 2.2% [1.0%, 4.7%] | 0.064 [0.041, 0.086] | -0.046 | n ≥ 200 |
| A ROM H; A VEN H; F NAP H | 254 | 3.6% | 0.0% [0.0%, 1.5%] | 0.024 [0.015, 0.032] | -0.086 | n ≥ 200 |
| A ROM - APU; A VEN - TYR; F NAP - ION | 199 | 2.8% | 6.0% [3.5%, 10.2%] | 0.089 [0.054, 0.123] | -0.021 | Sparse |

### Private messages — Tiers 1–3

20,951 games. Country baseline: 0.093 score; 5.9% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A ROM - VEN; A VEN - TYR; F NAP - ION | 3,997 | 19.1% | 9.8% [8.9%, 10.8%] | 0.141 [0.132, 0.151] | +0.048 | n ≥ 200 |
| A ROM - APU; A VEN H; F NAP - ION | 3,788 | 18.1% | 6.9% [6.1%, 7.7%] | 0.114 [0.105, 0.122] | +0.021 | n ≥ 200 |
| A ROM H; A VEN H; F NAP H | 1,655 | 7.9% | 1.9% [1.4%, 2.7%] | 0.030 [0.023, 0.037] | -0.063 | n ≥ 200 |
| A ROM - NAP; A VEN H; F NAP - ION | 1,522 | 7.3% | 3.5% [2.7%, 4.6%] | 0.066 [0.056, 0.076] | -0.027 | n ≥ 200 |
| A ROM - VEN; A VEN - PIE; F NAP - ION | 1,522 | 7.3% | 6.1% [5.0%, 7.4%] | 0.091 [0.078, 0.103] | -0.002 | n ≥ 200 |
| A ROM - APU; A VEN - TRI; F NAP - ION | 864 | 4.1% | 9.5% [7.7%, 11.6%] | 0.146 [0.125, 0.166] | +0.053 | n ≥ 200 |
| A ROM - VEN; A VEN - TRI; F NAP - ION | 761 | 3.6% | 8.4% [6.6%, 10.6%] | 0.120 [0.100, 0.141] | +0.027 | n ≥ 200 |
| A ROM - VEN; A VEN - PIE; F NAP - TYS | 650 | 3.1% | 4.6% [3.3%, 6.5%] | 0.070 [0.053, 0.087] | -0.023 | n ≥ 200 |
| A ROM - APU; A VEN - PIE; F NAP - ION | 543 | 2.6% | 5.2% [3.6%, 7.4%] | 0.092 [0.072, 0.112] | -0.001 | n ≥ 200 |
| A ROM - TUS; A VEN - PIE; F NAP - TYS | 479 | 2.3% | 5.2% [3.6%, 7.6%] | 0.078 [0.057, 0.099] | -0.015 | n ≥ 200 |

### Private messages — Tier 1

7,116 games. Country baseline: 0.092 score; 5.0% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A ROM - APU; A VEN H; F NAP - ION | 1,470 | 20.7% | 4.8% [3.8%, 6.0%] | 0.100 [0.088, 0.112] | +0.007 | n ≥ 200 |
| A ROM - VEN; A VEN - TYR; F NAP - ION | 1,330 | 18.7% | 8.1% [6.8%, 9.7%] | 0.133 [0.118, 0.149] | +0.041 | n ≥ 200 |
| A ROM - NAP; A VEN H; F NAP - ION | 521 | 7.3% | 2.7% [1.6%, 4.5%] | 0.067 [0.051, 0.083] | -0.025 | n ≥ 200 |
| A ROM - VEN; A VEN - PIE; F NAP - ION | 469 | 6.6% | 4.9% [3.3%, 7.3%] | 0.084 [0.064, 0.105] | -0.008 | n ≥ 200 |
| A ROM H; A VEN H; F NAP H | 397 | 5.6% | 2.3% [1.2%, 4.3%] | 0.037 [0.021, 0.052] | -0.056 | n ≥ 200 |
| A ROM - APU; A VEN - TRI; F NAP - ION | 344 | 4.8% | 8.7% [6.2%, 12.2%] | 0.145 [0.114, 0.176] | +0.052 | n ≥ 200 |
| A ROM - VEN; A VEN - TRI; F NAP - ION | 262 | 3.7% | 6.1% [3.8%, 9.7%] | 0.114 [0.083, 0.145] | +0.021 | n ≥ 200 |
| A ROM - APU; A VEN - PIE; F NAP - ION | 233 | 3.3% | 3.9% [2.0%, 7.2%] | 0.083 [0.056, 0.110] | -0.009 | n ≥ 200 |
| A ROM - VEN; A VEN - PIE; F NAP - TYS | 220 | 3.1% | 4.1% [2.2%, 7.6%] | 0.065 [0.037, 0.092] | -0.028 | n ≥ 200 |
| A ROM - TUS; A VEN - PIE; F NAP - TYS | 161 | 2.3% | 3.7% [1.7%, 7.9%] | 0.071 [0.039, 0.103] | -0.022 | Sparse |

### Public press — Tiers 1–3

918 games. Country baseline: 0.100 score; 5.6% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A ROM - VEN; A VEN - TYR; F NAP - ION | 220 | 24.0% | 8.2% [5.2%, 12.6%] | 0.128 [0.090, 0.166] | +0.028 | n ≥ 200 |
| A ROM - APU; A VEN H; F NAP - ION | 164 | 17.9% | 6.7% [3.8%, 11.6%] | 0.129 [0.088, 0.170] | +0.029 | Sparse |
| A ROM - VEN; A VEN - PIE; F NAP - ION | 70 | 7.6% | 4.3% [1.5%, 11.9%] | 0.087 [0.036, 0.138] | -0.012 | Sparse |
| A ROM H; A VEN H; F NAP H | 60 | 6.5% | 3.3% [0.9%, 11.4%] | 0.051 [0.003, 0.098] | -0.049 | Sparse |
| A ROM - NAP; A VEN H; F NAP - ION | 49 | 5.3% | 4.1% [1.1%, 13.7%] | 0.083 [0.024, 0.142] | -0.017 | Sparse |
| A ROM - APU; A VEN - TRI; F NAP - ION | 36 | 3.9% | 5.6% [1.5%, 18.1%] | 0.115 [0.030, 0.200] | +0.015 | Sparse |
| A ROM - VEN; A VEN - TRI; F NAP - ION | 33 | 3.6% | 6.1% [1.7%, 19.6%] | 0.111 [0.024, 0.197] | +0.011 | Sparse |
| A ROM - VEN; A VEN - PIE; F NAP - TYS | 29 | 3.2% | 3.4% [0.6%, 17.2%] | 0.046 [0.000, 0.115] | -0.054 | Sparse |
| A ROM - APU; A VEN S F TRI; F NAP - ION | 23 | 2.5% | 8.7% [2.4%, 26.8%] | 0.145 [0.022, 0.267] | +0.045 | Sparse |
| A ROM - APU; A VEN - TYR; F NAP - ION | 21 | 2.3% | 0.0% [0.0%, 15.5%] | 0.062 [0.006, 0.118] | -0.038 | Sparse |

### Public press — Tier 1

314 games. Country baseline: 0.098 score; 4.5% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A ROM - VEN; A VEN - TYR; F NAP - ION | 70 | 22.3% | 2.9% [0.8%, 9.8%] | 0.091 [0.045, 0.137] | -0.007 | Sparse |
| A ROM - APU; A VEN H; F NAP - ION | 63 | 20.1% | 4.8% [1.6%, 13.1%] | 0.113 [0.053, 0.173] | +0.016 | Sparse |
| A ROM - VEN; A VEN - PIE; F NAP - ION | 21 | 6.7% | 4.8% [0.8%, 22.7%] | 0.102 [0.001, 0.203] | +0.004 | Sparse |
| A ROM - NAP; A VEN H; F NAP - ION | 19 | 6.1% | 0.0% [0.0%, 16.8%] | 0.038 [0.004, 0.071] | -0.060 | Sparse |
| A ROM - APU; A VEN - TRI; F NAP - ION | 13 | 4.1% | 15.4% [4.3%, 42.2%] | 0.206 [0.005, 0.406] | +0.108 | Sparse |
| A ROM H; A VEN H; F NAP H | 12 | 3.8% | 8.3% [1.5%, 35.4%] | 0.122 [0.000, 0.290] | +0.024 | Sparse |
| A ROM - APU; A VEN - PIE; F NAP - ION | 11 | 3.5% | 9.1% [1.6%, 37.7%] | 0.181 [0.009, 0.354] | +0.084 | Sparse |
| A ROM - VEN; A VEN - PIE; F NAP - TYS | 9 | 2.9% | 0.0% [0.0%, 29.9%] | 0.007 [0.000, 0.021] | -0.090 | Sparse |
| A ROM - VEN; A VEN - TRI; F NAP - ION | 9 | 2.9% | 0.0% [0.0%, 29.9%] | 0.107 [0.003, 0.211] | +0.009 | Sparse |
| A ROM - APU; A VEN - TYR; F NAP - ION | 8 | 2.5% | 0.0% [0.0%, 32.4%] | 0.098 [0.000, 0.236] | +0.001 | Sparse |

## Russia

### No press — Tiers 1–3

15,333 games. Country baseline: 0.119 score; 8.2% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 7,140 | 46.6% | 9.0% [8.4%, 9.7%] | 0.132 [0.125, 0.139] | +0.013 | n ≥ 200 |
| A MOS - STP; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 882 | 5.8% | 10.3% [8.5%, 12.5%] | 0.146 [0.126, 0.167] | +0.027 | n ≥ 200 |
| A MOS - STP; A WAR - UKR; F SEV - BLA; F STP/SC - BOT | 881 | 5.7% | 11.4% [9.4%, 13.6%] | 0.150 [0.129, 0.171] | +0.031 | n ≥ 200 |
| A MOS H; A WAR H; F SEV H; F STP/SC H | 750 | 4.9% | 1.7% [1.0%, 2.9%] | 0.029 [0.019, 0.039] | -0.090 | n ≥ 200 |
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - FIN | 675 | 4.4% | 10.8% [8.7%, 13.4%] | 0.160 [0.136, 0.184] | +0.040 | n ≥ 200 |
| A MOS - UKR; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 663 | 4.3% | 7.2% [5.5%, 9.5%] | 0.112 [0.091, 0.133] | -0.007 | n ≥ 200 |
| A MOS - UKR; A WAR H; F SEV - BLA; F STP/SC - BOT | 324 | 2.1% | 5.2% [3.3%, 8.2%] | 0.098 [0.071, 0.126] | -0.021 | n ≥ 200 |
| A MOS - UKR; A WAR H; F SEV - RUM; F STP/SC - BOT | 263 | 1.7% | 5.7% [3.5%, 9.2%] | 0.094 [0.064, 0.124] | -0.025 | n ≥ 200 |
| A MOS - SEV; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 249 | 1.6% | 5.2% [3.1%, 8.7%] | 0.072 [0.043, 0.101] | -0.047 | n ≥ 200 |
| A MOS - STP; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 219 | 1.4% | 10.0% [6.7%, 14.7%] | 0.130 [0.089, 0.171] | +0.011 | n ≥ 200 |

### No press — Tier 1

7,106 games. Country baseline: 0.124 score; 8.2% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 3,480 | 49.0% | 8.6% [7.7%, 9.6%] | 0.131 [0.122, 0.141] | +0.007 | n ≥ 200 |
| A MOS - STP; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 414 | 5.8% | 9.7% [7.2%, 12.9%] | 0.146 [0.117, 0.175] | +0.022 | n ≥ 200 |
| A MOS - STP; A WAR - UKR; F SEV - BLA; F STP/SC - BOT | 366 | 5.2% | 10.7% [7.9%, 14.2%] | 0.143 [0.111, 0.176] | +0.019 | n ≥ 200 |
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - FIN | 361 | 5.1% | 10.2% [7.5%, 13.8%] | 0.161 [0.129, 0.193] | +0.037 | n ≥ 200 |
| A MOS - UKR; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 318 | 4.5% | 6.3% [4.1%, 9.5%] | 0.103 [0.074, 0.131] | -0.022 | n ≥ 200 |
| A MOS H; A WAR H; F SEV H; F STP/SC H | 182 | 2.6% | 1.6% [0.6%, 4.7%] | 0.045 [0.023, 0.068] | -0.079 | Sparse |
| A MOS - UKR; A WAR H; F SEV - BLA; F STP/SC - BOT | 128 | 1.8% | 8.6% [4.9%, 14.7%] | 0.162 [0.109, 0.214] | +0.037 | Sparse |
| A MOS - UKR; A WAR H; F SEV - RUM; F STP/SC - BOT | 111 | 1.6% | 8.1% [4.3%, 14.7%] | 0.114 [0.061, 0.166] | -0.011 | Sparse |
| A MOS - STP; A WAR - UKR; F SEV - RUM; F STP/SC - BOT | 108 | 1.5% | 13.0% [7.9%, 20.6%] | 0.156 [0.092, 0.220] | +0.032 | Sparse |
| A MOS - SEV; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 107 | 1.5% | 2.8% [1.0%, 7.9%] | 0.049 [0.014, 0.084] | -0.075 | Sparse |

### Private messages — Tiers 1–3

20,951 games. Country baseline: 0.173 score; 13.5% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 4,647 | 22.2% | 17.6% [16.6%, 18.8%] | 0.228 [0.217, 0.239] | +0.056 | n ≥ 200 |
| A MOS - UKR; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 1,796 | 8.6% | 15.6% [14.0%, 17.4%] | 0.192 [0.175, 0.209] | +0.019 | n ≥ 200 |
| A MOS - STP; A WAR - UKR; F SEV - BLA; F STP/SC - BOT | 1,547 | 7.4% | 18.6% [16.7%, 20.6%] | 0.238 [0.219, 0.258] | +0.066 | n ≥ 200 |
| A MOS H; A WAR H; F SEV H; F STP/SC H | 1,521 | 7.3% | 1.9% [1.3%, 2.7%] | 0.026 [0.019, 0.033] | -0.147 | n ≥ 200 |
| A MOS - UKR; A WAR H; F SEV - BLA; F STP/SC - BOT | 834 | 4.0% | 10.8% [8.9%, 13.1%] | 0.146 [0.124, 0.167] | -0.027 | n ≥ 200 |
| A MOS - UKR; A WAR H; F SEV - RUM; F STP/SC - BOT | 780 | 3.7% | 8.2% [6.5%, 10.3%] | 0.107 [0.087, 0.127] | -0.065 | n ≥ 200 |
| A MOS - STP; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 752 | 3.6% | 19.7% [17.0%, 22.7%] | 0.240 [0.212, 0.268] | +0.067 | n ≥ 200 |
| A MOS - STP; A WAR - UKR; F SEV - RUM; F STP/SC - BOT | 626 | 3.0% | 17.3% [14.5%, 20.4%] | 0.208 [0.178, 0.237] | +0.035 | n ≥ 200 |
| A MOS - STP; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 616 | 2.9% | 15.1% [12.5%, 18.1%] | 0.190 [0.161, 0.218] | +0.017 | n ≥ 200 |
| A MOS - SEV; A WAR - UKR; F SEV - BLA; F STP/SC - BOT | 534 | 2.5% | 19.5% [16.3%, 23.0%] | 0.255 [0.222, 0.289] | +0.083 | n ≥ 200 |

### Private messages — Tier 1

7,116 games. Country baseline: 0.171 score; 12.2% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 1,768 | 24.8% | 15.6% [14.0%, 17.4%] | 0.218 [0.201, 0.235] | +0.047 | n ≥ 200 |
| A MOS - UKR; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 631 | 8.9% | 14.1% [11.6%, 17.0%] | 0.190 [0.162, 0.217] | +0.019 | n ≥ 200 |
| A MOS - STP; A WAR - UKR; F SEV - BLA; F STP/SC - BOT | 542 | 7.6% | 15.9% [13.0%, 19.2%] | 0.216 [0.185, 0.247] | +0.045 | n ≥ 200 |
| A MOS H; A WAR H; F SEV H; F STP/SC H | 368 | 5.2% | 2.2% [1.1%, 4.2%] | 0.033 [0.017, 0.049] | -0.138 | n ≥ 200 |
| A MOS - UKR; A WAR H; F SEV - BLA; F STP/SC - BOT | 280 | 3.9% | 8.6% [5.8%, 12.4%] | 0.136 [0.101, 0.171] | -0.035 | n ≥ 200 |
| A MOS - STP; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 256 | 3.6% | 19.1% [14.8%, 24.4%] | 0.248 [0.200, 0.296] | +0.077 | n ≥ 200 |
| A MOS - UKR; A WAR H; F SEV - RUM; F STP/SC - BOT | 249 | 3.5% | 7.2% [4.6%, 11.1%] | 0.111 [0.077, 0.145] | -0.060 | n ≥ 200 |
| A MOS - STP; A WAR - UKR; F SEV - RUM; F STP/SC - BOT | 205 | 2.9% | 13.7% [9.6%, 19.0%] | 0.185 [0.138, 0.233] | +0.015 | n ≥ 200 |
| A MOS - SEV; A WAR - UKR; F SEV - RUM; F STP/SC - BOT | 204 | 2.9% | 15.2% [10.9%, 20.8%] | 0.207 [0.158, 0.257] | +0.036 | n ≥ 200 |
| A MOS - STP; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 192 | 2.7% | 12.0% [8.1%, 17.3%] | 0.178 [0.131, 0.225] | +0.007 | Sparse |

### Public press — Tiers 1–3

918 games. Country baseline: 0.151 score; 10.1% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 296 | 32.2% | 14.9% [11.3%, 19.4%] | 0.210 [0.170, 0.251] | +0.059 | n ≥ 200 |
| A MOS - UKR; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 67 | 7.3% | 11.9% [6.2%, 21.8%] | 0.172 [0.092, 0.252] | +0.021 | Sparse |
| A MOS - STP; A WAR - UKR; F SEV - BLA; F STP/SC - BOT | 61 | 6.6% | 14.8% [8.0%, 25.7%] | 0.253 [0.163, 0.343] | +0.101 | Sparse |
| A MOS H; A WAR H; F SEV H; F STP/SC H | 57 | 6.2% | 0.0% [0.0%, 6.3%] | 0.032 [0.007, 0.057] | -0.120 | Sparse |
| A MOS - STP; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 49 | 5.3% | 6.1% [2.1%, 16.5%] | 0.128 [0.052, 0.203] | -0.024 | Sparse |
| A MOS - STP; A WAR - UKR; F SEV - RUM; F STP/SC - BOT | 33 | 3.6% | 21.2% [10.7%, 37.8%] | 0.224 [0.084, 0.364] | +0.073 | Sparse |
| A MOS - UKR; A WAR H; F SEV - BLA; F STP/SC - BOT | 31 | 3.4% | 6.5% [1.8%, 20.7%] | 0.090 [0.000, 0.181] | -0.061 | Sparse |
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - FIN | 23 | 2.5% | 8.7% [2.4%, 26.8%] | 0.140 [0.016, 0.263] | -0.012 | Sparse |
| A MOS - UKR; A WAR H; F SEV - RUM; F STP/SC - BOT | 22 | 2.4% | 4.5% [0.8%, 21.8%] | 0.073 [0.000, 0.167] | -0.078 | Sparse |
| A MOS - STP; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 22 | 2.4% | 9.1% [2.5%, 27.8%] | 0.154 [0.022, 0.285] | +0.002 | Sparse |

### Public press — Tier 1

314 games. Country baseline: 0.148 score; 8.9% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 105 | 33.4% | 14.3% [8.9%, 22.2%] | 0.208 [0.141, 0.276] | +0.060 | Sparse |
| A MOS - STP; A WAR - UKR; F SEV - BLA; F STP/SC - BOT | 20 | 6.4% | 20.0% [8.1%, 41.6%] | 0.303 [0.133, 0.472] | +0.155 | Sparse |
| A MOS - UKR; A WAR - GAL; F SEV - RUM; F STP/SC - BOT | 20 | 6.4% | 10.0% [2.8%, 30.1%] | 0.181 [0.045, 0.317] | +0.033 | Sparse |
| A MOS - STP; A WAR - GAL; F SEV - BLA; F STP/SC - BOT | 19 | 6.1% | 5.3% [0.9%, 24.6%] | 0.143 [0.023, 0.263] | -0.005 | Sparse |
| A MOS - STP; A WAR - UKR; F SEV - RUM; F STP/SC - BOT | 17 | 5.4% | 11.8% [3.3%, 34.3%] | 0.132 [0.000, 0.289] | -0.016 | Sparse |
| A MOS H; A WAR H; F SEV H; F STP/SC H | 15 | 4.8% | 0.0% [0.0%, 20.4%] | 0.005 [0.000, 0.011] | -0.144 | Sparse |
| A MOS - UKR; A WAR H; F SEV - BLA; F STP/SC - BOT | 10 | 3.2% | 10.0% [1.8%, 40.4%] | 0.123 [0.000, 0.317] | -0.025 | Sparse |
| A MOS - UKR; A WAR - SIL; F SEV - BLA; F STP/SC - BOT | 9 | 2.9% | 0.0% [0.0%, 29.9%] | 0.080 [0.000, 0.193] | -0.068 | Sparse |
| A MOS - UKR; A WAR - GAL; F SEV - BLA; F STP/SC - FIN | 9 | 2.9% | 0.0% [0.0%, 29.9%] | 0.065 [0.000, 0.193] | -0.083 | Sparse |
| A MOS - UKR; A WAR H; F SEV - RUM; F STP/SC - BOT | 8 | 2.5% | 0.0% [0.0%, 32.4%] | 0.073 [0.000, 0.166] | -0.076 | Sparse |

## Turkey

### No press — Tiers 1–3

15,333 games. Country baseline: 0.206 score; 13.8% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A CON - BUL; A SMY - CON; F ANK - BLA | 8,832 | 57.6% | 14.2% [13.5%, 15.0%] | 0.219 [0.212, 0.227] | +0.013 | n ≥ 200 |
| A CON - BUL; A SMY - ARM; F ANK - BLA | 3,503 | 22.8% | 17.1% [15.9%, 18.4%] | 0.233 [0.220, 0.246] | +0.027 | n ≥ 200 |
| A CON - BUL; A SMY - ANK; F ANK - CON | 800 | 5.2% | 11.5% [9.5%, 13.9%] | 0.178 [0.155, 0.201] | -0.028 | n ≥ 200 |
| A CON H; A SMY H; F ANK H | 751 | 4.9% | 4.3% [3.0%, 6.0%] | 0.075 [0.059, 0.091] | -0.131 | n ≥ 200 |
| A CON - BUL; A SMY - ARM; F ANK - CON | 316 | 2.1% | 10.8% [7.8%, 14.7%] | 0.158 [0.122, 0.194] | -0.048 | n ≥ 200 |
| A CON - BUL; A SMY H; F ANK - CON | 284 | 1.9% | 9.2% [6.3%, 13.1%] | 0.167 [0.131, 0.204] | -0.039 | n ≥ 200 |
| A CON - BUL; A SMY - CON; F ANK H | 170 | 1.1% | 10.6% [6.8%, 16.1%] | 0.146 [0.098, 0.193] | -0.061 | Sparse |
| A CON - BUL; A SMY - ANK; F ANK - BLA | 109 | 0.7% | 7.3% [3.8%, 13.8%] | 0.127 [0.074, 0.180] | -0.079 | Sparse |
| A CON - BUL; A SMY - CON; F ANK - ARM | 94 | 0.6% | 13.8% [8.3%, 22.2%] | 0.180 [0.109, 0.251] | -0.026 | Sparse |
| A CON - BUL; A SMY H; F ANK - BLA | 81 | 0.5% | 13.6% [7.8%, 22.7%] | 0.179 [0.102, 0.255] | -0.027 | Sparse |

### No press — Tier 1

7,106 games. Country baseline: 0.195 score; 12.0% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A CON - BUL; A SMY - CON; F ANK - BLA | 4,160 | 58.5% | 11.3% [10.3%, 12.3%] | 0.197 [0.187, 0.207] | +0.002 | n ≥ 200 |
| A CON - BUL; A SMY - ARM; F ANK - BLA | 1,554 | 21.9% | 16.0% [14.3%, 17.9%] | 0.226 [0.208, 0.245] | +0.031 | n ≥ 200 |
| A CON - BUL; A SMY - ANK; F ANK - CON | 466 | 6.6% | 11.2% [8.6%, 14.3%] | 0.179 [0.149, 0.209] | -0.016 | n ≥ 200 |
| A CON H; A SMY H; F ANK H | 196 | 2.8% | 6.1% [3.5%, 10.4%] | 0.103 [0.067, 0.139] | -0.092 | Sparse |
| A CON - BUL; A SMY - ARM; F ANK - CON | 180 | 2.5% | 7.8% [4.7%, 12.6%] | 0.133 [0.090, 0.176] | -0.062 | Sparse |
| A CON - BUL; A SMY H; F ANK - CON | 163 | 2.3% | 6.7% [3.8%, 11.7%] | 0.151 [0.108, 0.194] | -0.044 | Sparse |
| A CON - BUL; A SMY - CON; F ANK H | 75 | 1.1% | 14.7% [8.4%, 24.4%] | 0.182 [0.102, 0.263] | -0.013 | Sparse |
| A CON - BUL; A SMY - ANK; F ANK - BLA | 49 | 0.7% | 8.2% [3.2%, 19.2%] | 0.132 [0.051, 0.213] | -0.063 | Sparse |
| A CON - BUL; A SMY - CON; F ANK - ARM | 43 | 0.6% | 11.6% [5.1%, 24.5%] | 0.166 [0.068, 0.265] | -0.029 | Sparse |
| A CON - BUL; A SMY H; F ANK - BLA | 40 | 0.6% | 20.0% [10.5%, 34.8%] | 0.245 [0.119, 0.371] | +0.050 | Sparse |

### Private messages — Tiers 1–3

20,951 games. Country baseline: 0.183 score; 12.5% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A CON - BUL; A SMY - CON; F ANK - BLA | 10,452 | 49.9% | 14.7% [14.0%, 15.4%] | 0.213 [0.207, 0.220] | +0.030 | n ≥ 200 |
| A CON - BUL; A SMY - ARM; F ANK - BLA | 3,573 | 17.1% | 14.0% [12.9%, 15.2%] | 0.205 [0.193, 0.217] | +0.022 | n ≥ 200 |
| A CON H; A SMY H; F ANK H | 1,506 | 7.2% | 3.1% [2.3%, 4.1%] | 0.048 [0.039, 0.057] | -0.135 | n ≥ 200 |
| A CON - BUL; A SMY H; F ANK - CON | 1,498 | 7.2% | 10.9% [9.5%, 12.6%] | 0.159 [0.143, 0.175] | -0.024 | n ≥ 200 |
| A CON - BUL; A SMY - ANK; F ANK - CON | 1,401 | 6.7% | 10.7% [9.2%, 12.4%] | 0.166 [0.150, 0.183] | -0.017 | n ≥ 200 |
| A CON - BUL; A SMY - CON; F ANK H | 829 | 4.0% | 7.8% [6.2%, 9.9%] | 0.127 [0.108, 0.147] | -0.056 | n ≥ 200 |
| A CON - BUL; A SMY - ARM; F ANK - CON | 382 | 1.8% | 10.7% [8.0%, 14.2%] | 0.167 [0.135, 0.199] | -0.016 | n ≥ 200 |
| A CON - BUL; A SMY - ANK; F ANK - BLA | 225 | 1.1% | 11.6% [8.0%, 16.4%] | 0.187 [0.144, 0.230] | +0.004 | n ≥ 200 |
| A CON - BUL; A SMY H; F ANK - BLA | 193 | 0.9% | 7.3% [4.4%, 11.8%] | 0.119 [0.081, 0.157] | -0.064 | Sparse |
| A CON - BUL; A SMY - CON; F ANK - ARM | 173 | 0.8% | 13.9% [9.5%, 19.8%] | 0.165 [0.113, 0.217] | -0.018 | Sparse |

### Private messages — Tier 1

7,116 games. Country baseline: 0.182 score; 11.0% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A CON - BUL; A SMY - CON; F ANK - BLA | 3,600 | 50.6% | 12.7% [11.6%, 13.8%] | 0.206 [0.195, 0.217] | +0.025 | n ≥ 200 |
| A CON - BUL; A SMY - ARM; F ANK - BLA | 1,207 | 17.0% | 12.2% [10.5%, 14.1%] | 0.196 [0.177, 0.214] | +0.014 | n ≥ 200 |
| A CON - BUL; A SMY - ANK; F ANK - CON | 533 | 7.5% | 8.3% [6.2%, 10.9%] | 0.159 [0.134, 0.183] | -0.023 | n ≥ 200 |
| A CON - BUL; A SMY H; F ANK - CON | 533 | 7.5% | 9.6% [7.4%, 12.4%] | 0.160 [0.133, 0.186] | -0.022 | n ≥ 200 |
| A CON H; A SMY H; F ANK H | 364 | 5.1% | 3.8% [2.3%, 6.4%] | 0.064 [0.043, 0.085] | -0.118 | n ≥ 200 |
| A CON - BUL; A SMY - CON; F ANK H | 290 | 4.1% | 6.6% [4.2%, 10.0%] | 0.126 [0.095, 0.157] | -0.056 | n ≥ 200 |
| A CON - BUL; A SMY - ARM; F ANK - CON | 144 | 2.0% | 10.4% [6.4%, 16.5%] | 0.171 [0.120, 0.222] | -0.010 | Sparse |
| A CON - BUL; A SMY - ANK; F ANK - BLA | 94 | 1.3% | 8.5% [4.4%, 15.9%] | 0.170 [0.109, 0.230] | -0.012 | Sparse |
| A CON - BUL; A SMY H; F ANK - BLA | 66 | 0.9% | 7.6% [3.3%, 16.5%] | 0.145 [0.078, 0.211] | -0.037 | Sparse |
| A CON - BUL; A SMY - CON; F ANK - ARM | 65 | 0.9% | 15.4% [8.6%, 26.1%] | 0.193 [0.104, 0.281] | +0.011 | Sparse |

### Public press — Tiers 1–3

918 games. Country baseline: 0.216 score; 13.2% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A CON - BUL; A SMY - CON; F ANK - BLA | 493 | 53.7% | 16.2% [13.2%, 19.7%] | 0.252 [0.219, 0.284] | +0.036 | n ≥ 200 |
| A CON - BUL; A SMY - ARM; F ANK - BLA | 190 | 20.7% | 12.1% [8.2%, 17.5%] | 0.228 [0.180, 0.276] | +0.012 | Sparse |
| A CON H; A SMY H; F ANK H | 61 | 6.6% | 4.9% [1.7%, 13.5%] | 0.083 [0.024, 0.142] | -0.134 | Sparse |
| A CON - BUL; A SMY - ANK; F ANK - CON | 54 | 5.9% | 11.1% [5.2%, 22.2%] | 0.171 [0.085, 0.257] | -0.045 | Sparse |
| A CON - BUL; A SMY H; F ANK - CON | 39 | 4.2% | 5.1% [1.4%, 16.9%] | 0.099 [0.021, 0.176] | -0.118 | Sparse |
| A CON - BUL; A SMY - ARM; F ANK - CON | 33 | 3.6% | 6.1% [1.7%, 19.6%] | 0.147 [0.057, 0.238] | -0.069 | Sparse |
| A CON - BUL; A SMY - CON; F ANK H | 16 | 1.7% | 25.0% [10.2%, 49.5%] | 0.340 [0.133, 0.547] | +0.124 | Sparse |
| A CON - BUL; A SMY - ANK; F ANK - BLA | 5 | 0.5% | 0.0% [0.0%, 43.4%] | 0.000 [unavailable] | -0.216 | Sparse |
| A CON - BUL; A SMY H; F ANK - BLA | 4 | 0.4% | 0.0% [0.0%, 49.0%] | 0.050 [0.000, 0.147] | -0.166 | Sparse |
| A CON - BUL; A SMY - CON; F ANK - ARM | 4 | 0.4% | 25.0% [4.6%, 69.9%] | 0.250 [0.000, 0.740] | +0.034 | Sparse |

### Public press — Tier 1

314 games. Country baseline: 0.207 score; 10.5% solo.

| Orders | Games | Share | Solo % [95% interval] | Mean score [95% interval] | Score lift | Evidence |
|---|---:|---:|---:|---:|---:|---|
| A CON - BUL; A SMY - CON; F ANK - BLA | 173 | 55.1% | 11.6% [7.6%, 17.2%] | 0.219 [0.170, 0.268] | +0.012 | Sparse |
| A CON - BUL; A SMY - ARM; F ANK - BLA | 66 | 21.0% | 15.2% [8.4%, 25.7%] | 0.278 [0.192, 0.365] | +0.071 | Sparse |
| A CON - BUL; A SMY - ANK; F ANK - CON | 19 | 6.1% | 5.3% [0.9%, 24.6%] | 0.151 [0.036, 0.267] | -0.056 | Sparse |
| A CON H; A SMY H; F ANK H | 16 | 5.1% | 0.0% [0.0%, 19.4%] | 0.029 [0.000, 0.061] | -0.178 | Sparse |
| A CON - BUL; A SMY - ARM; F ANK - CON | 12 | 3.8% | 0.0% [0.0%, 24.2%] | 0.162 [0.054, 0.270] | -0.046 | Sparse |
| A CON - BUL; A SMY H; F ANK - CON | 11 | 3.5% | 9.1% [1.6%, 37.7%] | 0.205 [0.013, 0.397] | -0.003 | Sparse |
| A CON - BUL; A SMY - CON; F ANK H | 5 | 1.6% | 20.0% [3.6%, 62.4%] | 0.224 [0.000, 0.607] | +0.017 | Sparse |
| A CON - BUL; A SMY - CON; F ANK S A SMY - CON | 2 | 0.6% | 0.0% [0.0%, 65.8%] | 0.000 [unavailable] | -0.207 | Sparse |
| A CON - BUL; A SMY - CON; F ANK S F SEV - BLA | 1 | 0.3% | 0.0% [0.0%, 79.3%] | 0.000 [unavailable] | -0.207 | Sparse |
| A CON - BUL; A SMY - ANK; F ANK - BLA | 1 | 0.3% | 0.0% [0.0%, 79.3%] | 0.000 [unavailable] | -0.207 | Sparse |
