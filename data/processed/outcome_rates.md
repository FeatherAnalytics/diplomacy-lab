# Country outcome rates

Report cohort: 37203 games from no_press, press_with_msgs, and public_press, filtered to in_scope (standard map, quality tiers 1-3, ended by solo or draw vote, standard build rules, ended by 1930). The press_without_msgs source is excluded from these comparisons because its draws are almost never detected, making its eligible sample almost entirely solos. Unknown endings remain excluded in the other sources too; these are descriptive rates among games with detectable endings, not population or causal estimates. game_outcomes.parquet retains all 62719 in-scope games across all four sources.

Solo = 18+ centers at the end. 'In draw vote' = survived a game classified as ending == draw_vote; solo games are excluded even when their terminal orders are empty. Draw votes are inferred from empty orders, not confirmed site outcomes. Finished with centers (excluding solos) includes draw participants, so these report columns overlap. The explorer's Survived category excludes both solos and draws. In a solo game, SoS score is 1 for the winner and 0 for everyone else, including survivors. In a draw, score is centers^2 / sum(centers^2) across the seven powers.

## All included press levels

| power | games | solo % | in draw vote % | finished with centers (excluding solos) % | eliminated % | mean final SC | mean SoS score |
|---|---|---|---|---|---|---|---|
| austria | 37203 | 7.1 | 14.4 | 31.7 | 61.2 | 3.57 | 0.11 |
| england | 37203 | 8.0 | 20.7 | 50.8 | 41.3 | 5.11 | 0.13 |
| france | 37203 | 11.5 | 22.9 | 54.9 | 33.7 | 5.81 | 0.171 |
| germany | 37203 | 9.5 | 18.7 | 42.4 | 48.1 | 4.6 | 0.143 |
| italy | 37203 | 6.5 | 18.2 | 47.2 | 46.3 | 3.93 | 0.103 |
| russia | 37203 | 11.2 | 16.1 | 38.0 | 50.8 | 4.34 | 0.15 |
| turkey | 37203 | 13.0 | 21.7 | 52.1 | 34.9 | 6.64 | 0.193 |

## Solo % by press level

| press_level | austria | england | france | germany | italy | russia | turkey |
|---|---|---|---|---|---|---|---|
| no_press | 6.6 | 7.1 | 12.1 | 10.3 | 7.3 | 8.2 | 13.8 |
| press_with_msgs | 7.6 | 8.6 | 11.1 | 9.1 | 5.9 | 13.5 | 12.5 |
| public_press | 4.9 | 6.6 | 8.9 | 7.2 | 5.6 | 10.1 | 13.2 |

## Eliminated % by press level

| press_level | austria | england | france | germany | italy | russia | turkey |
|---|---|---|---|---|---|---|---|
| no_press | 61.1 | 43.7 | 30.4 | 44.0 | 42.4 | 49.8 | 31.9 |
| press_with_msgs | 61.2 | 39.6 | 36.0 | 51.0 | 49.2 | 51.6 | 37.3 |
| public_press | 60.0 | 38.2 | 34.5 | 46.7 | 45.9 | 49.1 | 30.8 |

## Mean SoS score x 100 by press level

| press_level | austria | england | france | germany | italy | russia | turkey |
|---|---|---|---|---|---|---|---|
| no_press | 10.7 | 11.9 | 17.8 | 15.5 | 11.6 | 11.9 | 20.6 |
| press_with_msgs | 11.3 | 13.8 | 16.6 | 13.4 | 9.3 | 17.3 | 18.3 |
| public_press | 10.0 | 13.9 | 16.1 | 13.3 | 10.0 | 15.1 | 21.6 |

## Sensitivity: Tier 1 only (14537 games)

Same three sources, restricted to games with no detected dropout. The main tables retain tiers 1-3, including major dropouts. Tier 1 uses the all-hold-streak heuristic and does not guarantee uninterrupted play.

| power | games | solo % | in draw vote % | finished with centers (excluding solos) % | eliminated % | mean final SC | mean SoS score |
|---|---|---|---|---|---|---|---|
| austria | 14537 | 6.4 | 18.4 | 34.7 | 58.9 | 3.65 | 0.113 |
| england | 14537 | 7.3 | 25.6 | 52.6 | 40.1 | 5.08 | 0.134 |
| france | 14537 | 10.7 | 29.1 | 59.6 | 29.7 | 5.96 | 0.175 |
| germany | 14537 | 8.3 | 23.7 | 45.9 | 45.8 | 4.6 | 0.141 |
| italy | 14537 | 5.7 | 22.8 | 50.9 | 43.4 | 3.94 | 0.101 |
| russia | 14537 | 10.2 | 20.4 | 41.3 | 48.5 | 4.31 | 0.148 |
| turkey | 14537 | 11.5 | 26.5 | 54.7 | 33.8 | 6.46 | 0.189 |

## Reference: playdiplomacy finished standard games (outcomes only, different platform)

| power | games | solo % | draw % | lost % |
|---|---|---|---|---|
| austria | 76798 | 11.0 | 15.8 | 73.2 |
| england | 76798 | 12.3 | 20.4 | 67.3 |
| france | 76798 | 7.2 | 20.6 | 72.2 |
| germany | 76798 | 6.3 | 17.3 | 76.4 |
| italy | 76798 | 4.0 | 14.1 | 81.9 |
| russia | 76798 | 8.7 | 16.2 | 75.1 |
| turkey | 76798 | 8.5 | 20.8 | 70.8 |
