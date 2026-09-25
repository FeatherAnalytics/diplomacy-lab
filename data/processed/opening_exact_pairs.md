# Exact matches for country pairs

Each match requires both countries' recorded orders in the same game. The other five countries may vary. All 21 pairs are included for Spring and full 1901. Selected-country lookup also supports any larger combination and can return outcomes for any country, including an unselected one.

Coverage measures how often exact patterns repeat, not whether a pair is strategically good. The threshold is a configurable sample-size flag, not proof of reliability. Games in repeated patterns means games whose pattern appears at least twice within that same cohort. Each pair partitions its cohort; rows for different pairs overlap and must not be added together.

The existing scope, detectable-ending sources and quality filters apply. Tier 1 means no detected terminal dropout. Outcomes are descriptive; skill and negotiation are not controlled for. Full-year histories include adaptive Fall, retreat and Winter decisions. Exact orders need not imply identical board states.

Each pair's most frequent pattern is shown below its coverage table, with counts and observed rates. A single match is one historical outcome, with rate fields unavailable. Unseen patterns return no exact matches. The examples Parquet contains the configured top N patterns per pair/cohort; lookup retains access to every pattern. Pooled-source summaries are available in Parquet; this report separates communication settings.

Mean score averages final sum-of-squares scores: a solo gives the winner 1 and everyone else 0. In a draw, each country scores its final centers squared divided by the sum of those squares. Finished with centers includes solo winners and draw participants; it is broader than the explorer's Survived category. Dataset game IDs are not WebDiplomacy game IDs.

## Spring 1901

### no_press — Tiers 1–3

15,333 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Turkey | 451 | 245 | 15,088 | 12 | 11,886 | 2,728 |
| Germany / Turkey | 754 | 422 | 14,911 | 11 | 10,453 | 3,360 |
| England / Germany | 825 | 459 | 14,874 | 15 | 10,177 | 1,807 |
| Russia / Turkey | 1,111 | 639 | 14,694 | 13 | 9,671 | 4,295 |
| France / Turkey | 678 | 342 | 14,991 | 15 | 9,519 | 2,314 |
| Italy / Turkey | 774 | 397 | 14,936 | 13 | 8,883 | 2,196 |
| England / France | 762 | 380 | 14,953 | 20 | 8,828 | 1,275 |
| Austria / Turkey | 858 | 446 | 14,887 | 11 | 8,632 | 2,875 |
| England / Russia | 1,258 | 719 | 14,614 | 12 | 8,232 | 2,265 |
| Austria / England | 964 | 490 | 14,843 | 13 | 7,823 | 1,492 |
| Germany / Italy | 1,431 | 812 | 14,521 | 19 | 7,792 | 1,421 |
| England / Italy | 879 | 462 | 14,871 | 15 | 7,618 | 1,203 |
| Germany / Russia | 1,800 | 1,113 | 14,220 | 10 | 7,363 | 2,838 |
| Austria / Germany | 1,530 | 894 | 14,439 | 12 | 6,936 | 2,008 |
| France / Germany | 1,274 | 677 | 14,656 | 13 | 6,840 | 1,561 |
| France / Russia | 1,893 | 1,115 | 14,218 | 12 | 6,546 | 1,956 |
| Italy / Russia | 2,053 | 1,222 | 14,111 | 11 | 6,128 | 1,847 |
| Austria / Russia | 2,141 | 1,314 | 14,019 | 9 | 5,877 | 2,586 |
| Austria / Italy | 1,715 | 882 | 14,451 | 13 | 5,498 | 1,057 |
| Austria / France | 1,520 | 756 | 14,577 | 10 | 4,956 | 1,439 |
| France / Italy | 1,430 | 725 | 14,608 | 12 | 4,713 | 991 |

#### England / Turkey — 2,728 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 188 | 6.9% | 625 | 22.9% | 1546 | 0.123 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 380 | 13.9% | 691 | 25.3% | 1920 | 0.216 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Germany / Turkey — 3,360 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 396 | 11.8% | 836 | 24.9% | 2074 | 0.183 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 500 | 14.9% | 909 | 27.1% | 2375 | 0.231 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Germany — 1,807 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 120 | 6.6% | 399 | 22.1% | 1021 | 0.116 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 191 | 10.6% | 400 | 22.1% | 1060 | 0.161 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Russia / Turkey — 4,295 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 376 | 8.8% | 904 | 21.0% | 2366 | 0.133 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 533 | 12.4% | 1133 | 26.4% | 2993 | 0.200 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### France / Turkey — 2,314 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 385 | 16.6% | 749 | 32.4% | 1791 | 0.244 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 293 | 12.7% | 638 | 27.6% | 1617 | 0.207 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Italy / Turkey — 2,196 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 234 | 10.7% | 411 | 18.7% | 1321 | 0.153 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 388 | 17.7% | 566 | 25.8% | 1669 | 0.256 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / France — 1,275 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 81 | 6.4% | 283 | 22.2% | 689 | 0.114 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 236 | 18.5% | 379 | 29.7% | 999 | 0.261 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36
```

#### Austria / Turkey — 2,875 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 255 | 8.9% | 628 | 21.8% | 1417 | 0.152 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 263 | 9.1% | 729 | 25.4% | 1830 | 0.161 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Russia — 2,265 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 175 | 7.7% | 485 | 21.4% | 1283 | 0.124 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 201 | 8.9% | 428 | 18.9% | 1236 | 0.130 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / England — 1,492 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 173 | 11.6% | 325 | 21.8% | 772 | 0.182 |
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 92 | 6.2% | 345 | 23.1% | 824 | 0.115 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177
```

#### Germany / Italy — 1,421 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 144 | 10.1% | 316 | 22.2% | 894 | 0.153 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 179 | 12.6% | 253 | 17.8% | 828 | 0.169 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### England / Italy — 1,203 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 90 | 7.5% | 237 | 19.7% | 694 | 0.122 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 132 | 11.0% | 227 | 18.9% | 710 | 0.156 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### Germany / Russia — 2,838 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 347 | 12.2% | 691 | 24.3% | 1783 | 0.185 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 213 | 7.5% | 494 | 17.4% | 1442 | 0.113 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Germany — 2,008 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 192 | 9.6% | 454 | 22.6% | 1027 | 0.165 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 228 | 11.4% | 558 | 27.8% | 1261 | 0.188 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### France / Germany — 1,561 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 240 | 15.4% | 483 | 30.9% | 1191 | 0.220 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 149 | 9.5% | 407 | 26.1% | 932 | 0.160 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### France / Russia — 1,956 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 320 | 16.4% | 606 | 31.0% | 1509 | 0.239 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 154 | 7.9% | 428 | 21.9% | 1078 | 0.127 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Italy / Russia — 1,847 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 238 | 12.9% | 361 | 19.5% | 1175 | 0.176 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 190 | 10.3% | 329 | 17.8% | 1075 | 0.140 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Russia — 2,586 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 233 | 9.0% | 562 | 21.7% | 1277 | 0.153 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 190 | 7.3% | 505 | 19.5% | 1323 | 0.113 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Italy — 1,057 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 50 | 4.7% | 124 | 11.7% | 331 | 0.073 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 89 | 8.4% | 194 | 18.4% | 612 | 0.124 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### Austria / France — 1,439 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 119 | 8.3% | 333 | 23.1% | 716 | 0.154 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 220 | 15.3% | 514 | 35.7% | 1114 | 0.236 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36
```

#### France / Italy — 991 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 175 | 17.7% | 295 | 29.8% | 813 | 0.247 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 99 | 10.0% | 206 | 20.8% | 604 | 0.150 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tiers_1_3 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

### no_press — Tier 1

7,106 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Turkey | 276 | 145 | 6,961 | 7 | 5,013 | 1,354 |
| England / Germany | 484 | 256 | 6,850 | 10 | 4,475 | 964 |
| Germany / Turkey | 470 | 268 | 6,838 | 7 | 4,434 | 1,714 |
| Russia / Turkey | 708 | 410 | 6,696 | 6 | 3,827 | 2,097 |
| France / Turkey | 429 | 206 | 6,900 | 9 | 3,802 | 1,154 |
| Austria / Turkey | 542 | 283 | 6,823 | 6 | 3,569 | 1,558 |
| Austria / England | 591 | 317 | 6,789 | 7 | 3,224 | 834 |
| England / Russia | 765 | 441 | 6,665 | 4 | 3,200 | 1,146 |
| Italy / Turkey | 495 | 238 | 6,868 | 6 | 2,922 | 941 |
| Austria / Germany | 901 | 546 | 6,560 | 5 | 2,644 | 1,169 |
| Germany / Russia | 1,080 | 710 | 6,396 | 3 | 2,637 | 1,475 |
| England / France | 465 | 217 | 6,889 | 6 | 2,603 | 659 |
| England / Italy | 527 | 257 | 6,849 | 7 | 2,472 | 545 |
| France / Germany | 810 | 470 | 6,636 | 6 | 2,316 | 820 |
| France / Russia | 1,157 | 692 | 6,414 | 5 | 2,298 | 1,009 |
| Austria / Russia | 1,260 | 785 | 6,321 | 3 | 2,253 | 1,494 |
| Germany / Italy | 867 | 499 | 6,607 | 6 | 2,173 | 641 |
| Italy / Russia | 1,271 | 803 | 6,303 | 4 | 2,039 | 830 |
| Austria / Italy | 1,057 | 580 | 6,526 | 5 | 1,726 | 544 |
| Austria / France | 953 | 489 | 6,617 | 3 | 1,490 | 822 |
| France / Italy | 933 | 475 | 6,631 | 4 | 1,262 | 461 |

#### England / Turkey — 1,354 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 86 | 6.4% | 322 | 23.8% | 736 | 0.118 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 153 | 11.3% | 353 | 26.1% | 932 | 0.190 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Germany — 964 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 62 | 6.4% | 238 | 24.7% | 528 | 0.119 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 109 | 11.3% | 233 | 24.2% | 561 | 0.174 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Germany / Turkey — 1,714 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 206 | 12.0% | 463 | 27.0% | 1052 | 0.191 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 184 | 10.7% | 507 | 29.6% | 1184 | 0.195 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Russia / Turkey — 2,097 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 176 | 8.4% | 479 | 22.8% | 1166 | 0.134 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 204 | 9.7% | 586 | 27.9% | 1427 | 0.179 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### France / Turkey — 1,154 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 188 | 16.3% | 439 | 38.0% | 905 | 0.253 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 104 | 9.0% | 353 | 30.6% | 798 | 0.178 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Austria / Turkey — 1,558 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 139 | 8.9% | 366 | 23.5% | 779 | 0.155 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 126 | 8.1% | 429 | 27.5% | 983 | 0.156 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Austria / England — 834 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 91 | 10.9% | 203 | 24.3% | 430 | 0.182 |
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 46 | 5.5% | 208 | 24.9% | 451 | 0.111 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177
```

#### England / Russia — 1,146 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 80 | 7.0% | 268 | 23.4% | 648 | 0.119 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 102 | 8.9% | 236 | 20.6% | 626 | 0.134 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Italy / Turkey — 941 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 107 | 11.4% | 167 | 17.7% | 567 | 0.157 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 138 | 14.7% | 253 | 26.9% | 717 | 0.235 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Austria / Germany — 1,169 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 115 | 9.8% | 283 | 24.2% | 602 | 0.167 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 112 | 9.6% | 356 | 30.5% | 733 | 0.178 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Germany / Russia — 1,475 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 173 | 11.7% | 390 | 26.4% | 914 | 0.184 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 114 | 7.7% | 284 | 19.3% | 759 | 0.120 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### England / France — 659 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 39 | 5.9% | 165 | 25.0% | 347 | 0.114 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 112 | 17.0% | 228 | 34.6% | 518 | 0.260 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36
```

#### England / Italy — 545 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 37 | 6.8% | 101 | 18.5% | 296 | 0.110 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 58 | 10.6% | 96 | 17.6% | 315 | 0.148 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### France / Germany — 820 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 128 | 15.6% | 296 | 36.1% | 634 | 0.233 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 73 | 8.9% | 238 | 29.0% | 481 | 0.164 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### France / Russia — 1,009 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 151 | 15.0% | 360 | 35.7% | 782 | 0.235 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 74 | 7.3% | 243 | 24.1% | 548 | 0.126 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Russia — 1,494 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 127 | 8.5% | 354 | 23.7% | 740 | 0.152 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 105 | 7.0% | 316 | 21.2% | 767 | 0.113 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Germany / Italy — 641 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 54 | 8.4% | 151 | 23.6% | 386 | 0.134 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 71 | 11.1% | 111 | 17.3% | 363 | 0.149 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### Italy / Russia — 830 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 98 | 11.8% | 159 | 19.2% | 529 | 0.163 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 88 | 10.6% | 156 | 18.8% | 487 | 0.144 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Italy — 544 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 23 | 4.2% | 62 | 11.4% | 159 | 0.066 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 47 | 8.6% | 96 | 17.6% | 308 | 0.125 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### Austria / France — 822 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 65 | 7.9% | 209 | 25.4% | 408 | 0.153 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 110 | 13.4% | 338 | 41.1% | 638 | 0.230 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36
```

#### France / Italy — 461 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 80 | 17.4% | 155 | 33.6% | 378 | 0.249 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 43 | 9.3% | 95 | 20.6% | 276 | 0.142 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level no_press --quality-group tier_1 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

### press_with_msgs — Tiers 1–3

20,951 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Turkey | 786 | 451 | 20,500 | 21 | 16,114 | 3,676 |
| England / Germany | 1,382 | 779 | 20,172 | 23 | 13,479 | 2,386 |
| Germany / Turkey | 1,225 | 679 | 20,272 | 19 | 13,162 | 3,280 |
| France / Turkey | 1,040 | 539 | 20,412 | 23 | 12,382 | 1,916 |
| Italy / Turkey | 1,197 | 645 | 20,306 | 22 | 11,929 | 2,038 |
| England / France | 1,193 | 636 | 20,315 | 24 | 11,618 | 1,502 |
| England / Italy | 1,358 | 745 | 20,206 | 21 | 10,889 | 1,450 |
| Austria / Turkey | 1,244 | 637 | 20,314 | 18 | 10,753 | 1,979 |
| Austria / England | 1,434 | 764 | 20,187 | 20 | 10,506 | 1,387 |
| Russia / Turkey | 1,782 | 996 | 19,955 | 19 | 9,906 | 2,835 |
| England / Russia | 2,003 | 1,133 | 19,818 | 20 | 9,107 | 1,676 |
| France / Germany | 1,975 | 1,063 | 19,888 | 20 | 8,776 | 1,175 |
| Germany / Italy | 2,194 | 1,235 | 19,716 | 19 | 8,711 | 1,322 |
| Austria / Germany | 2,363 | 1,354 | 19,597 | 18 | 8,398 | 1,296 |
| Germany / Russia | 3,090 | 1,876 | 19,075 | 15 | 6,749 | 1,483 |
| France / Italy | 1,970 | 1,020 | 19,931 | 17 | 6,508 | 773 |
| Austria / Italy | 2,321 | 1,233 | 19,718 | 15 | 6,209 | 800 |
| Austria / France | 2,113 | 1,047 | 19,904 | 15 | 6,039 | 741 |
| Italy / Russia | 3,272 | 1,897 | 19,054 | 13 | 5,134 | 1,032 |
| France / Russia | 2,957 | 1,627 | 19,324 | 13 | 4,912 | 827 |
| Austria / Russia | 3,370 | 1,952 | 18,999 | 12 | 4,716 | 1,017 |

#### England / Turkey — 3,676 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 342 | 9.3% | 840 | 22.9% | 2340 | 0.152 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 576 | 15.7% | 841 | 22.9% | 2423 | 0.226 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Germany — 2,386 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 197 | 8.3% | 536 | 22.5% | 1426 | 0.139 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 234 | 9.8% | 500 | 21.0% | 1280 | 0.155 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Germany / Turkey — 3,280 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 369 | 11.2% | 706 | 21.5% | 1838 | 0.172 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 452 | 13.8% | 758 | 23.1% | 2194 | 0.208 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### France / Turkey — 1,916 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 234 | 12.2% | 405 | 21.1% | 1277 | 0.178 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 318 | 16.6% | 398 | 20.8% | 1266 | 0.228 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Italy / Turkey — 2,038 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 182 | 8.9% | 370 | 18.2% | 1142 | 0.132 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 335 | 16.4% | 511 | 25.1% | 1473 | 0.241 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / France — 1,502 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 157 | 10.5% | 337 | 22.4% | 1061 | 0.168 |
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 182 | 12.1% | 307 | 20.4% | 1009 | 0.174 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b
```

#### England / Italy — 1,450 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 120 | 8.3% | 338 | 23.3% | 912 | 0.140 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 130 | 9.0% | 273 | 18.8% | 786 | 0.135 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### Austria / Turkey — 1,979 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB | 175 | 8.8% | 320 | 16.2% | 883 | 0.134 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 222 | 11.2% | 375 | 18.9% | 1183 | 0.163 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=o1_ca91817eceef1a29be02c8de18075863718dd4e98bbcd16c3a0e3e3971731a0b --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Austria / England — 1,387 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB | 132 | 9.5% | 228 | 16.4% | 668 | 0.142 |
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 139 | 10.0% | 281 | 20.3% | 841 | 0.155 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=o1_ca91817eceef1a29be02c8de18075863718dd4e98bbcd16c3a0e3e3971731a0b --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177
```

#### Russia / Turkey — 2,835 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 462 | 16.3% | 606 | 21.4% | 1651 | 0.220 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 323 | 11.4% | 707 | 24.9% | 1850 | 0.186 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Russia — 1,676 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 138 | 8.2% | 395 | 23.6% | 1038 | 0.142 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 255 | 15.2% | 337 | 20.1% | 917 | 0.207 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### France / Germany — 1,175 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - PIC, F BRE - MAO | 119 | 10.1% | 292 | 24.9% | 776 | 0.162 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 149 | 12.7% | 267 | 22.7% | 694 | 0.194 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select france=o1_2bdca8a4b28b75d74773fbc90a20e272ab55a6401c9ad1de964f28bd6a8fae87 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Germany / Italy — 1,322 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 149 | 11.3% | 302 | 22.8% | 732 | 0.175 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 93 | 7.0% | 295 | 22.3% | 759 | 0.117 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9
```

#### Austria / Germany — 1,296 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB | 123 | 9.5% | 232 | 17.9% | 641 | 0.150 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 158 | 12.2% | 256 | 19.8% | 716 | 0.176 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=o1_ca91817eceef1a29be02c8de18075863718dd4e98bbcd16c3a0e3e3971731a0b --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Germany / Russia — 1,483 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 150 | 10.1% | 335 | 22.6% | 839 | 0.165 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 223 | 15.0% | 274 | 18.5% | 755 | 0.196 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### France / Italy — 773 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 107 | 13.8% | 158 | 20.4% | 536 | 0.190 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 73 | 9.4% | 114 | 14.7% | 414 | 0.126 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### Austria / Italy — 800 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 94 | 11.8% | 205 | 25.6% | 447 | 0.200 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 44 | 5.5% | 211 | 26.4% | 496 | 0.109 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9
```

#### Austria / France — 741 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB | 71 | 9.6% | 112 | 15.1% | 358 | 0.137 |
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 91 | 12.3% | 140 | 18.9% | 503 | 0.172 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=o1_ca91817eceef1a29be02c8de18075863718dd4e98bbcd16c3a0e3e3971731a0b --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b
```

#### Italy / Russia — 1,032 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 100 | 9.7% | 216 | 20.9% | 636 | 0.148 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 200 | 19.4% | 196 | 19.0% | 635 | 0.246 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### France / Russia — 827 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 88 | 10.6% | 174 | 21.0% | 551 | 0.160 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 151 | 18.3% | 140 | 16.9% | 443 | 0.231 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Russia — 1,017 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 101 | 9.9% | 240 | 23.6% | 510 | 0.168 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 116 | 11.4% | 217 | 21.3% | 512 | 0.166 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

### press_with_msgs — Tier 1

7,116 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Turkey | 399 | 230 | 6,886 | 6 | 3,766 | 1,338 |
| England / Germany | 722 | 413 | 6,703 | 8 | 3,178 | 912 |
| Germany / Turkey | 616 | 326 | 6,790 | 6 | 3,041 | 1,191 |
| Italy / Turkey | 637 | 325 | 6,791 | 6 | 2,440 | 770 |
| France / Turkey | 582 | 288 | 6,828 | 6 | 2,379 | 652 |
| England / Italy | 723 | 398 | 6,718 | 7 | 2,348 | 577 |
| Austria / Turkey | 688 | 364 | 6,752 | 5 | 2,215 | 701 |
| Austria / England | 784 | 453 | 6,663 | 6 | 2,122 | 492 |
| England / France | 646 | 348 | 6,768 | 6 | 2,067 | 540 |
| England / Russia | 1,051 | 615 | 6,501 | 6 | 1,976 | 677 |
| Russia / Turkey | 970 | 558 | 6,558 | 4 | 1,934 | 1,117 |
| France / Germany | 1,052 | 603 | 6,513 | 6 | 1,740 | 437 |
| Austria / Germany | 1,227 | 749 | 6,367 | 4 | 1,474 | 467 |
| Germany / Italy | 1,136 | 663 | 6,453 | 4 | 1,464 | 555 |
| Germany / Russia | 1,533 | 972 | 6,144 | 3 | 1,131 | 585 |
| France / Italy | 1,111 | 577 | 6,539 | 4 | 985 | 266 |
| Austria / France | 1,210 | 639 | 6,477 | 4 | 921 | 245 |
| Austria / Italy | 1,284 | 721 | 6,395 | 3 | 887 | 354 |
| France / Russia | 1,591 | 943 | 6,173 | 3 | 841 | 303 |
| Italy / Russia | 1,699 | 1,055 | 6,061 | 2 | 789 | 398 |
| Austria / Russia | 1,739 | 1,085 | 6,031 | 2 | 728 | 484 |

#### England / Turkey — 1,338 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 117 | 8.7% | 403 | 30.1% | 894 | 0.158 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 178 | 13.3% | 382 | 28.6% | 874 | 0.217 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Germany — 912 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 77 | 8.4% | 261 | 28.6% | 573 | 0.154 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 72 | 7.9% | 248 | 27.2% | 489 | 0.149 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Germany / Turkey — 1,191 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 99 | 8.3% | 335 | 28.1% | 659 | 0.157 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 145 | 12.2% | 349 | 29.3% | 788 | 0.205 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Italy / Turkey — 770 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 36 | 4.7% | 224 | 29.1% | 460 | 0.100 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 75 | 9.7% | 205 | 26.6% | 448 | 0.167 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### France / Turkey — 652 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 76 | 11.7% | 182 | 27.9% | 451 | 0.183 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 77 | 11.8% | 175 | 26.8% | 427 | 0.194 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Italy — 577 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 44 | 7.6% | 174 | 30.2% | 364 | 0.152 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 24 | 4.2% | 169 | 29.3% | 327 | 0.093 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9
```

#### Austria / Turkey — 701 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 48 | 6.8% | 183 | 26.1% | 336 | 0.149 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 63 | 9.0% | 182 | 26.0% | 410 | 0.160 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Austria / England — 492 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB | 45 | 9.1% | 122 | 24.8% | 263 | 0.163 |
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 40 | 8.1% | 133 | 27.0% | 302 | 0.156 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=o1_ca91817eceef1a29be02c8de18075863718dd4e98bbcd16c3a0e3e3971731a0b --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177
```

#### England / France — 540 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 56 | 10.4% | 160 | 29.6% | 394 | 0.184 |
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 59 | 10.9% | 151 | 28.0% | 380 | 0.178 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b
```

#### England / Russia — 677 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 48 | 7.1% | 199 | 29.4% | 434 | 0.139 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 82 | 12.1% | 169 | 25.0% | 366 | 0.185 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Russia / Turkey — 1,117 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 156 | 14.0% | 308 | 27.6% | 658 | 0.208 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 108 | 9.7% | 361 | 32.3% | 730 | 0.185 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### France / Germany — 437 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - PIC, F BRE - MAO | 35 | 8.0% | 145 | 33.2% | 305 | 0.157 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 41 | 9.4% | 132 | 30.2% | 265 | 0.178 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select france=o1_2bdca8a4b28b75d74773fbc90a20e272ab55a6401c9ad1de964f28bd6a8fae87 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Austria / Germany — 467 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 40 | 8.6% | 129 | 27.6% | 233 | 0.169 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 48 | 10.3% | 135 | 28.9% | 272 | 0.183 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Germany / Italy — 555 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 50 | 9.0% | 167 | 30.1% | 309 | 0.168 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 29 | 5.2% | 161 | 29.0% | 322 | 0.113 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9
```

#### Germany / Russia — 585 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 44 | 7.5% | 171 | 29.2% | 341 | 0.158 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 81 | 13.8% | 141 | 24.1% | 310 | 0.192 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### France / Italy — 266 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - PIC, F BRE - MAO | 23 | 8.6% | 90 | 33.8% | 186 | 0.173 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 10 | 3.8% | 76 | 28.6% | 152 | 0.094 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select france=o1_2bdca8a4b28b75d74773fbc90a20e272ab55a6401c9ad1de964f28bd6a8fae87 --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9
```

#### Austria / France — 245 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB | 30 | 12.2% | 42 | 17.1% | 122 | 0.171 |
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 25 | 10.2% | 59 | 24.1% | 167 | 0.157 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=o1_ca91817eceef1a29be02c8de18075863718dd4e98bbcd16c3a0e3e3971731a0b --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b
```

#### Austria / Italy — 354 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 28 | 7.9% | 114 | 32.2% | 199 | 0.184 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 9 | 2.5% | 106 | 29.9% | 206 | 0.084 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9
```

#### France / Russia — 303 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - PIC, F BRE - MAO | 18 | 5.9% | 97 | 32.0% | 204 | 0.138 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 48 | 15.8% | 72 | 23.8% | 172 | 0.215 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select france=o1_2bdca8a4b28b75d74773fbc90a20e272ab55a6401c9ad1de964f28bd6a8fae87 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Italy / Russia — 398 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 37 | 9.3% | 124 | 31.2% | 262 | 0.164 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 66 | 16.6% | 102 | 25.6% | 247 | 0.233 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Russia — 484 matches

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 34 | 7.0% | 142 | 29.3% | 241 | 0.155 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 52 | 10.7% | 137 | 28.3% | 251 | 0.170 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

### public_press — Tiers 1–3

918 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Turkey | 113 | 52 | 866 | 0 | 0 | 162 |
| France / Turkey | 169 | 85 | 833 | 0 | 0 | 106 |
| Germany / Turkey | 161 | 94 | 824 | 0 | 0 | 165 |
| England / France | 199 | 102 | 816 | 0 | 0 | 71 |
| Italy / Turkey | 198 | 111 | 807 | 0 | 0 | 135 |
| England / Germany | 195 | 116 | 802 | 0 | 0 | 118 |
| Austria / Turkey | 219 | 126 | 792 | 0 | 0 | 106 |
| England / Italy | 232 | 134 | 784 | 0 | 0 | 76 |
| Russia / Turkey | 241 | 140 | 778 | 0 | 0 | 170 |
| France / Germany | 260 | 147 | 771 | 0 | 0 | 70 |
| Austria / England | 255 | 152 | 766 | 0 | 0 | 70 |
| England / Russia | 268 | 168 | 750 | 0 | 0 | 114 |
| Germany / Italy | 288 | 186 | 732 | 0 | 0 | 76 |
| France / Italy | 333 | 201 | 717 | 0 | 0 | 49 |
| Austria / France | 348 | 225 | 693 | 0 | 0 | 39 |
| Austria / Germany | 326 | 227 | 691 | 0 | 0 | 80 |
| Germany / Russia | 337 | 235 | 683 | 0 | 0 | 104 |
| Austria / Italy | 373 | 244 | 674 | 0 | 0 | 40 |
| France / Russia | 372 | 250 | 668 | 0 | 0 | 55 |
| Italy / Russia | 395 | 280 | 638 | 0 | 0 | 81 |
| Austria / Russia | 413 | 296 | 622 | 0 | 0 | 69 |

#### England / Turkey — 162 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 9 | 5.6% | 59 | 36.4% | 105 | 0.143 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 23 | 14.2% | 69 | 42.6% | 128 | 0.256 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### France / Turkey — 106 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 13 | 12.3% | 37 | 34.9% | 74 | 0.204 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 14 | 13.2% | 37 | 34.9% | 78 | 0.213 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Germany / Turkey — 165 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 13 | 7.9% | 49 | 29.7% | 99 | 0.154 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 26 | 15.8% | 59 | 35.8% | 122 | 0.258 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / France — 71 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 4 | 5.6% | 33 | 46.5% | 51 | 0.189 |
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 7 | 9.9% | 31 | 43.7% | 49 | 0.206 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b
```

#### Italy / Turkey — 135 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 8 | 5.9% | 28 | 20.7% | 74 | 0.108 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 28 | 20.7% | 39 | 28.9% | 105 | 0.301 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Germany — 118 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 5 | 4.2% | 45 | 38.1% | 74 | 0.118 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 8 | 6.8% | 38 | 32.2% | 73 | 0.149 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Austria / Turkey — 106 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 3 | 2.8% | 28 | 26.4% | 58 | 0.088 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 8 | 7.5% | 37 | 34.9% | 75 | 0.153 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Italy — 76 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 7 | 9.2% | 16 | 21.1% | 45 | 0.152 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 6 | 7.9% | 11 | 14.5% | 38 | 0.109 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### Russia / Turkey — 170 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 24 | 14.1% | 50 | 29.4% | 104 | 0.204 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 24 | 14.1% | 59 | 34.7% | 128 | 0.235 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### France / Germany — 70 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 5 | 7.1% | 28 | 40.0% | 52 | 0.179 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 6 | 8.6% | 23 | 32.9% | 42 | 0.170 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Austria / England — 70 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 3 | 4.3% | 26 | 37.1% | 43 | 0.144 |
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 6 | 8.6% | 34 | 48.6% | 50 | 0.197 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177
```

#### England / Russia — 114 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 6 | 5.3% | 42 | 36.8% | 71 | 0.150 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 15 | 13.2% | 39 | 34.2% | 68 | 0.210 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Germany / Italy — 76 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 5 | 6.6% | 18 | 23.7% | 40 | 0.126 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 3 | 3.9% | 20 | 26.3% | 43 | 0.097 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### France / Italy — 49 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 10 | 20.4% | 15 | 30.6% | 39 | 0.266 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 4 | 8.2% | 8 | 16.3% | 26 | 0.121 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### Austria / France — 39 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 1 | 2.6% | 13 | 33.3% | 25 | 0.103 |
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 3 | 7.7% | 16 | 41.0% | 28 | 0.157 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b
```

#### Austria / Germany — 80 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 4 | 5.0% | 24 | 30.0% | 45 | 0.134 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 5 | 6.2% | 29 | 36.2% | 49 | 0.150 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Germany / Russia — 104 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 8 | 7.7% | 33 | 31.7% | 62 | 0.154 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 13 | 12.5% | 30 | 28.8% | 58 | 0.189 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Italy — 40 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 2 | 5.0% | 5 | 12.5% | 14 | 0.072 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 1 | 2.5% | 7 | 17.5% | 22 | 0.062 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### France / Russia — 55 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 3 | 5.5% | 14 | 25.5% | 36 | 0.113 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 8 | 14.5% | 12 | 21.8% | 32 | 0.193 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Italy / Russia — 81 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 10 | 12.3% | 12 | 14.8% | 48 | 0.171 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 13 | 16.0% | 13 | 16.0% | 50 | 0.197 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Russia — 69 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 3 | 4.3% | 16 | 23.2% | 38 | 0.100 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 10 | 14.5% | 22 | 31.9% | 42 | 0.203 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

### public_press — Tier 1

314 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Turkey | 64 | 34 | 280 | 0 | 0 | 67 |
| England / France | 103 | 53 | 261 | 0 | 0 | 32 |
| Germany / Turkey | 84 | 53 | 261 | 0 | 0 | 60 |
| France / Turkey | 94 | 58 | 256 | 0 | 0 | 43 |
| Italy / Turkey | 107 | 65 | 249 | 0 | 0 | 44 |
| England / Germany | 98 | 66 | 248 | 0 | 0 | 51 |
| France / Germany | 124 | 67 | 247 | 0 | 0 | 30 |
| Austria / Turkey | 109 | 69 | 245 | 0 | 0 | 41 |
| Russia / Turkey | 115 | 71 | 243 | 0 | 0 | 60 |
| Austria / England | 119 | 75 | 239 | 0 | 0 | 29 |
| England / Italy | 123 | 79 | 235 | 0 | 0 | 30 |
| England / Russia | 126 | 81 | 233 | 0 | 0 | 42 |
| Austria / Germany | 139 | 99 | 215 | 0 | 0 | 33 |
| Austria / France | 155 | 101 | 213 | 0 | 0 | 15 |
| Germany / Italy | 144 | 106 | 208 | 0 | 0 | 31 |
| France / Italy | 163 | 108 | 206 | 0 | 0 | 16 |
| France / Russia | 161 | 110 | 204 | 0 | 0 | 22 |
| Germany / Russia | 151 | 119 | 195 | 0 | 0 | 41 |
| Austria / Italy | 182 | 132 | 182 | 0 | 0 | 19 |
| Italy / Russia | 178 | 133 | 181 | 0 | 0 | 27 |
| Austria / Russia | 178 | 134 | 180 | 0 | 0 | 28 |

#### England / Turkey — 67 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 2 | 3.0% | 31 | 46.3% | 46 | 0.137 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 6 | 9.0% | 33 | 49.3% | 52 | 0.211 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / France — 32 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 0 | 0.0% | 21 | 65.6% | 26 | 0.182 |
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 3 | 9.4% | 17 | 53.1% | 23 | 0.196 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b
```

#### Germany / Turkey — 60 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 6 | 10.0% | 22 | 36.7% | 36 | 0.208 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 4 | 6.7% | 28 | 46.7% | 44 | 0.179 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### France / Turkey — 43 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 4 | 9.3% | 22 | 51.2% | 33 | 0.191 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 4 | 9.3% | 21 | 48.8% | 30 | 0.203 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Italy / Turkey — 44 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 0 | 0.0% | 15 | 34.1% | 26 | 0.058 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 7 | 15.9% | 19 | 43.2% | 36 | 0.291 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### England / Germany — 51 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 2 | 3.9% | 24 | 47.1% | 35 | 0.125 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 4 | 7.8% | 21 | 41.2% | 35 | 0.181 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### France / Germany — 30 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 1 | 3.3% | 17 | 56.7% | 26 | 0.162 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 2 | 6.7% | 14 | 46.7% | 19 | 0.200 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Austria / Turkey — 41 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 2 | 4.9% | 12 | 29.3% | 21 | 0.132 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 2 | 4.9% | 19 | 46.3% | 28 | 0.151 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Russia / Turkey — 60 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 8 | 13.3% | 21 | 35.0% | 34 | 0.209 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA | 8 | 13.3% | 26 | 43.3% | 47 | 0.231 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd --select turkey=o1_aec5fb4fd393a3bffbfb2dc688d3ca95295ac482518ce91d78cb851f166e290b
```

#### Austria / England — 29 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 2 | 6.9% | 11 | 37.9% | 16 | 0.181 |
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 1 | 3.4% | 16 | 55.2% | 23 | 0.187 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177
```

#### England / Italy — 30 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 1 | 3.3% | 9 | 30.0% | 22 | 0.106 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 1 | 3.3% | 6 | 20.0% | 13 | 0.054 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### England / Russia — 42 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH | 1 | 2.4% | 21 | 50.0% | 30 | 0.157 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 3 | 7.1% | 17 | 40.5% | 25 | 0.145 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select england=o1_8872d4419fcd4656dbcbd9874309d001d928376ccbcdd2211366160d0c7b9177 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Germany — 33 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 1 | 3.0% | 9 | 27.3% | 17 | 0.131 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 4 | 12.1% | 15 | 45.5% | 24 | 0.255 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956
```

#### Austria / France — 15 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 0 | 0.0% | 9 | 60.0% | 11 | 0.151 |
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 0 | 0.0% | 10 | 66.7% | 13 | 0.116 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b
```

#### Germany / Italy — 31 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 3 | 9.7% | 14 | 45.2% | 21 | 0.228 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 2 | 6.5% | 11 | 35.5% | 18 | 0.116 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9
```

#### France / Italy — 16 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO | 2 | 12.5% | 7 | 43.8% | 13 | 0.210 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 0 | 0.0% | 5 | 31.2% | 9 | 0.033 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select france=o1_60b99a649f0dfeaed75f7f10337f721d3bbdac09b14a8474eb5d5798f7873f4b --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace
```

#### France / Russia — 22 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO | 1 | 4.5% | 8 | 36.4% | 15 | 0.130 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 3 | 13.6% | 7 | 31.8% | 14 | 0.190 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select france=o1_ea1ad71eb727352c65c452188b0d7c17dbd81f0b569657825532bcb20c48ac36 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Germany / Russia — 41 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN | 4 | 9.8% | 17 | 41.5% | 26 | 0.195 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 5 | 12.2% | 15 | 36.6% | 25 | 0.184 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select germany=o1_5fd5e9ac6a77cc789fd65de5c63399673fe7142b793be9be3f35bb270f337956 --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Italy — 19 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 0 | 0.0% | 4 | 21.1% | 9 | 0.056 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION | 0 | 0.0% | 6 | 31.6% | 12 | 0.093 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select italy=o1_5ffda7ce07fc2d9c4db7e32146c8c5109b31e9c44ff29222e06995ea60309cc9
```

#### Italy / Russia — 27 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION | 2 | 7.4% | 6 | 22.2% | 19 | 0.128 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 6 | 22.2% | 8 | 29.6% | 19 | 0.276 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select italy=o1_39252782daf09726d1e559290beea8e1dce346e9ca1183bae6b2118a099d6ace --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

#### Austria / Russia — 28 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB | 1 | 3.6% | 7 | 25.0% | 16 | 0.108 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT | 5 | 17.9% | 9 | 32.1% | 16 | 0.205 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon spring1901 --context selected --press-level public_press --quality-group tier_1 --select austria=o1_e04b9c626d4d2091f3c77a38cd2f800809b657bbe60955d7445e9ac53cf8cc6a --select russia=o1_4c47d7f7c17d0555bd7566be7fe4bfaf787fb935e06e2225aff93db98865b5dd
```

## Full 1901

### no_press — Tiers 1–3

15,333 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Turkey | 11,294 | 9,862 | 5,471 | 0 | 0 | 68 |
| England / Germany | 11,919 | 10,400 | 4,933 | 0 | 0 | 50 |
| England / France | 11,892 | 10,455 | 4,878 | 0 | 0 | 104 |
| Russia / Turkey | 11,572 | 10,475 | 4,858 | 0 | 0 | 92 |
| Austria / Italy | 11,677 | 10,515 | 4,818 | 0 | 0 | 124 |
| Germany / Turkey | 11,992 | 10,737 | 4,596 | 0 | 0 | 61 |
| Italy / Turkey | 12,034 | 10,857 | 4,476 | 0 | 0 | 92 |
| Austria / Turkey | 11,954 | 10,903 | 4,430 | 0 | 0 | 161 |
| France / Germany | 12,520 | 11,305 | 4,028 | 0 | 0 | 52 |
| France / Turkey | 12,620 | 11,581 | 3,752 | 0 | 0 | 107 |
| England / Italy | 12,916 | 11,748 | 3,585 | 0 | 0 | 39 |
| Germany / Italy | 13,280 | 12,265 | 3,068 | 0 | 0 | 30 |
| Austria / England | 13,291 | 12,381 | 2,952 | 0 | 0 | 46 |
| France / Italy | 13,334 | 12,406 | 2,927 | 0 | 0 | 43 |
| Austria / Russia | 13,347 | 12,650 | 2,683 | 0 | 0 | 77 |
| England / Russia | 13,565 | 12,681 | 2,652 | 0 | 0 | 31 |
| Germany / Russia | 13,715 | 12,909 | 2,424 | 0 | 0 | 28 |
| Austria / Germany | 13,655 | 12,911 | 2,422 | 0 | 0 | 32 |
| Austria / France | 13,928 | 13,269 | 2,064 | 0 | 0 | 40 |
| Italy / Russia | 14,049 | 13,401 | 1,932 | 0 | 0 | 30 |
| France / Russia | 14,343 | 13,824 | 1,509 | 0 | 0 | 20 |

#### England / Turkey — 68 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - BEL VIA, F NTH C A YOR - BEL, F NWG - NWY; W1901A: F LON B | 4 | 5.9% | 17 | 25.0% | 32 | 0.113 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 8 | 11.8% | 21 | 30.9% | 51 | 0.213 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=y1_bfdaffcaf300956288c9ffaef64a4b9f7be8d521e8f8402549b726a7f5755192 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### England / Germany — 50 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - EDI, F EDI - NWG, F LON - NTH; F1901M: A EDI - NWY VIA, F NTH - DEN, F NWG C A EDI - NWY; W1901A: F LON B | 6 | 12.0% | 7 | 14.0% | 27 | 0.157 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - HOL; F1901M: A KIE - DEN, A RUH - BEL, F HOL S A RUH - BEL; W1901A: A MUN B, F BER B | 9 | 18.0% | 9 | 18.0% | 34 | 0.230 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=y1_4b2b0ded4f2f4cb7f11ed86cff65833bdd686e193aa38d1a98960e7618dc2830 --select germany=y1_b6b6a4c85def8cbbb86a12048e6390ec9c170afed2c435f166fcc61da9e3bf3f
```

#### England / France — 104 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - BEL VIA, F NTH C A YOR - BEL, F NWG - NWY; W1901A: F LON B | 5 | 4.8% | 13 | 12.5% | 37 | 0.062 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 23 | 22.1% | 27 | 26.0% | 84 | 0.287 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=y1_bfdaffcaf300956288c9ffaef64a4b9f7be8d521e8f8402549b726a7f5755192 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9
```

#### Russia / Turkey — 92 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, A STP B | 12 | 13.0% | 27 | 29.3% | 67 | 0.202 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 8 | 8.7% | 28 | 30.4% | 69 | 0.166 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select russia=y1_8ea7154322eda3d2763e106805a20c4e8f50fc54c8de46db081ac1d7de3d6479 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### Austria / Italy — 124 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - TRI, F ALB - GRE; W1901A: A BUD B, A VIE B | 20 | 16.1% | 38 | 30.6% | 82 | 0.259 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 9 | 7.3% | 30 | 24.2% | 74 | 0.118 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=y1_e7b3d34ab4c0b3b1110552dcd1ce29a8cce5615f091c03c2e20909f9471e7dc3 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Germany / Turkey — 61 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A MUN B, F KIE B | 10 | 16.4% | 15 | 24.6% | 39 | 0.247 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 10 | 16.4% | 17 | 27.9% | 46 | 0.222 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select germany=y1_0cb3534ff5f7df6185fa004342394949f65af564a98623a128fd92e11f869ef6 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### Italy / Turkey — 92 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 6 | 6.5% | 29 | 31.5% | 63 | 0.129 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 3 | 3.3% | 18 | 19.6% | 43 | 0.086 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### Austria / Turkey — 161 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 15 | 9.3% | 48 | 29.8% | 95 | 0.186 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 5 | 3.1% | 48 | 29.8% | 98 | 0.103 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### France / Germany — 52 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 7 | 13.5% | 20 | 38.5% | 41 | 0.214 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A MUN B, F KIE B | 7 | 13.5% | 19 | 36.5% | 35 | 0.226 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select germany=y1_0cb3534ff5f7df6185fa004342394949f65af564a98623a128fd92e11f869ef6
```

#### France / Turkey — 107 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 22 | 20.6% | 36 | 33.6% | 90 | 0.313 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 11 | 10.3% | 31 | 29.0% | 76 | 0.197 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### England / Italy — 39 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - NWY VIA, F NTH C A YOR - NWY, F NWG - BAR; W1901A: F LON B | 6 | 15.4% | 10 | 25.6% | 31 | 0.194 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 2.6% | 7 | 17.9% | 19 | 0.072 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=y1_9fda7efbed54953193fa0661547778293f46c287196a68b316c4af3377884b86 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Germany / Italy — 30 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 3 | 10.0% | 5 | 0.001 |
| Italy | S1901M: A ROM H, A VEN H, F NAP H; F1901M: A ROM H, A VEN H, F NAP H | 0 | 0.0% | 4 | 13.3% | 12 | 0.011 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84 --select italy=y1_40ff40b0e4dad05aedea2e73c143b33fc80b8fea9045a788ce39f11127e4cc16
```

#### Austria / England — 46 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 5 | 10.9% | 15 | 32.6% | 25 | 0.244 |
| England | S1901M: A LVP - EDI, F EDI - NWG, F LON - NTH; F1901M: A EDI - NWY VIA, F NTH - SKA, F NWG C A EDI - NWY; W1901A: F LON B | 3 | 6.5% | 16 | 34.8% | 27 | 0.146 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select england=y1_adb2dc9b5532a57fea1f3a1ce330aadf7f5f7a9b453cba1d4b96f47c3dae5613
```

#### France / Italy — 43 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 4 | 9.3% | 14 | 32.6% | 33 | 0.164 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 6 | 14.0% | 9 | 20.9% | 27 | 0.185 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Austria / Russia — 77 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 7 | 9.1% | 16 | 20.8% | 35 | 0.145 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, A STP B | 7 | 9.1% | 25 | 32.5% | 48 | 0.163 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select russia=y1_8ea7154322eda3d2763e106805a20c4e8f50fc54c8de46db081ac1d7de3d6479
```

#### England / Russia — 31 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 0 | 0.0% | 4 | 12.9% | 12 | 0.006 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 1 | 3.2% | 7 | 0.006 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Germany / Russia — 28 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 3 | 10.7% | 6 | 0.019 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 2 | 7.1% | 10 | 0.018 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Austria / Germany — 32 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - TRI, F ALB - GRE; W1901A: A BUD B, A VIE B | 3 | 9.4% | 10 | 31.2% | 22 | 0.226 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - MUN, F DEN - SWE; W1901A: A KIE B, F BER B | 8 | 25.0% | 11 | 34.4% | 23 | 0.359 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=y1_e7b3d34ab4c0b3b1110552dcd1ce29a8cce5615f091c03c2e20909f9471e7dc3 --select germany=y1_cdf77a8cab51979f0a32c290a07e41786e6e0b708e13c5a6356527c91186cb30
```

#### Austria / France — 40 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 1 | 2.5% | 15 | 37.5% | 22 | 0.174 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - MAR, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 5 | 12.5% | 19 | 47.5% | 30 | 0.228 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select france=y1_43ef5e2463cc47d99aa7db27a73cd1766531b0e4684ccacb74a6b3c684b3e82b
```

#### Italy / Russia — 30 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM H, A VEN H, F NAP H; F1901M: A ROM H, A VEN H, F NAP H | 0 | 0.0% | 4 | 13.3% | 10 | 0.010 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 3 | 10.0% | 6 | 0.009 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select italy=y1_40ff40b0e4dad05aedea2e73c143b33fc80b8fea9045a788ce39f11127e4cc16 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### France / Russia — 20 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 3 | 15.0% | 6 | 30.0% | 14 | 0.245 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, A STP B | 1 | 5.0% | 8 | 40.0% | 13 | 0.171 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tiers_1_3 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select russia=y1_8ea7154322eda3d2763e106805a20c4e8f50fc54c8de46db081ac1d7de3d6479
```

### no_press — Tier 1

7,106 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Turkey | 5,554 | 4,961 | 2,145 | 0 | 0 | 44 |
| Austria / Italy | 5,656 | 5,142 | 1,964 | 0 | 0 | 72 |
| Russia / Turkey | 5,625 | 5,151 | 1,955 | 0 | 0 | 57 |
| Austria / Turkey | 5,697 | 5,251 | 1,855 | 0 | 0 | 110 |
| England / Germany | 5,927 | 5,291 | 1,815 | 0 | 0 | 27 |
| England / France | 5,927 | 5,358 | 1,748 | 0 | 0 | 55 |
| Italy / Turkey | 5,877 | 5,397 | 1,709 | 0 | 0 | 62 |
| Germany / Turkey | 5,922 | 5,427 | 1,679 | 0 | 0 | 36 |
| France / Turkey | 6,109 | 5,690 | 1,416 | 0 | 0 | 66 |
| France / Germany | 6,177 | 5,694 | 1,412 | 0 | 0 | 30 |
| England / Italy | 6,283 | 5,808 | 1,298 | 0 | 0 | 26 |
| Austria / England | 6,272 | 5,899 | 1,207 | 0 | 0 | 29 |
| Austria / Russia | 6,274 | 5,982 | 1,124 | 0 | 0 | 54 |
| France / Italy | 6,395 | 6,029 | 1,077 | 0 | 0 | 28 |
| Germany / Italy | 6,453 | 6,059 | 1,047 | 0 | 0 | 14 |
| England / Russia | 6,473 | 6,130 | 976 | 0 | 0 | 14 |
| Austria / Germany | 6,454 | 6,132 | 974 | 0 | 0 | 19 |
| Germany / Russia | 6,566 | 6,259 | 847 | 0 | 0 | 16 |
| Austria / France | 6,543 | 6,284 | 822 | 0 | 0 | 29 |
| Italy / Russia | 6,668 | 6,430 | 676 | 0 | 0 | 16 |
| France / Russia | 6,793 | 6,624 | 482 | 0 | 0 | 14 |

#### England / Turkey — 44 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - BEL VIA, F NTH C A YOR - BEL, F NWG - NWY; W1901A: F LON B | 2 | 4.5% | 12 | 27.3% | 18 | 0.110 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 4 | 9.1% | 14 | 31.8% | 33 | 0.217 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select england=y1_bfdaffcaf300956288c9ffaef64a4b9f7be8d521e8f8402549b726a7f5755192 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### Austria / Italy — 72 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - TRI, F ALB - GRE; W1901A: A BUD B, A VIE B | 13 | 18.1% | 21 | 29.2% | 44 | 0.251 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 4 | 5.6% | 19 | 26.4% | 41 | 0.098 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select austria=y1_e7b3d34ab4c0b3b1110552dcd1ce29a8cce5615f091c03c2e20909f9471e7dc3 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Russia / Turkey — 57 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, A STP B | 9 | 15.8% | 19 | 33.3% | 44 | 0.236 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 4 | 7.0% | 16 | 28.1% | 42 | 0.133 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select russia=y1_8ea7154322eda3d2763e106805a20c4e8f50fc54c8de46db081ac1d7de3d6479 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### Austria / Turkey — 110 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 11 | 10.0% | 31 | 28.2% | 64 | 0.177 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 3 | 2.7% | 32 | 29.1% | 67 | 0.100 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### England / Germany — 27 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - EDI, F EDI - NWG, F LON - NTH; F1901M: A EDI - NWY VIA, F NTH - DEN, F NWG C A EDI - NWY; W1901A: F LON B | 4 | 14.8% | 4 | 14.8% | 15 | 0.196 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - HOL; F1901M: A KIE - DEN, A RUH - BEL, F HOL S A RUH - BEL; W1901A: A MUN B, F BER B | 3 | 11.1% | 5 | 18.5% | 17 | 0.134 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select england=y1_4b2b0ded4f2f4cb7f11ed86cff65833bdd686e193aa38d1a98960e7618dc2830 --select germany=y1_b6b6a4c85def8cbbb86a12048e6390ec9c170afed2c435f166fcc61da9e3bf3f
```

#### England / France — 55 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - BEL VIA, F NTH C A YOR - BEL, F NWG - NWY; W1901A: F LON B | 3 | 5.5% | 7 | 12.7% | 17 | 0.070 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 10 | 18.2% | 17 | 30.9% | 46 | 0.258 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select england=y1_bfdaffcaf300956288c9ffaef64a4b9f7be8d521e8f8402549b726a7f5755192 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9
```

#### Italy / Turkey — 62 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 5 | 8.1% | 19 | 30.6% | 41 | 0.130 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 2 | 3.2% | 14 | 22.6% | 31 | 0.085 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### Germany / Turkey — 36 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - MUN, F DEN - SWE; W1901A: A KIE B, F BER B | 5 | 13.9% | 11 | 30.6% | 22 | 0.202 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 2 | 5.6% | 13 | 36.1% | 23 | 0.187 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select germany=y1_cdf77a8cab51979f0a32c290a07e41786e6e0b708e13c5a6356527c91186cb30 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### France / Turkey — 66 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 12 | 18.2% | 26 | 39.4% | 56 | 0.289 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 3 | 4.5% | 19 | 28.8% | 44 | 0.149 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### France / Germany — 30 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 6 | 20.0% | 16 | 53.3% | 28 | 0.317 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A MUN B, F KIE B | 3 | 10.0% | 12 | 40.0% | 20 | 0.194 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select germany=y1_0cb3534ff5f7df6185fa004342394949f65af564a98623a128fd92e11f869ef6
```

#### England / Italy — 26 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - NWY VIA, F NTH C A YOR - NWY, F NWG - BAR; W1901A: F LON B | 5 | 19.2% | 6 | 23.1% | 20 | 0.233 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 3.8% | 3 | 11.5% | 13 | 0.067 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select england=y1_9fda7efbed54953193fa0661547778293f46c287196a68b316c4af3377884b86 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Austria / England — 29 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 2 | 6.9% | 9 | 31.0% | 13 | 0.186 |
| England | S1901M: A LVP - EDI, F EDI - NWG, F LON - NTH; F1901M: A EDI - NWY VIA, F NTH - SKA, F NWG C A EDI - NWY; W1901A: F LON B | 2 | 6.9% | 12 | 41.4% | 17 | 0.177 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select england=y1_adb2dc9b5532a57fea1f3a1ce330aadf7f5f7a9b453cba1d4b96f47c3dae5613
```

#### Austria / Russia — 54 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 4 | 7.4% | 14 | 25.9% | 30 | 0.147 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B | 3 | 5.6% | 8 | 14.8% | 21 | 0.093 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select russia=y1_627154b2546acca6b61175d84fd4ce23c56b7da6515a83868810c5a3d6e55d8e
```

#### France / Italy — 28 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 3 | 10.7% | 10 | 35.7% | 20 | 0.185 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 2 | 7.1% | 6 | 21.4% | 19 | 0.114 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Germany / Italy — 14 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A MUN B, F KIE B | 1 | 7.1% | 7 | 50.0% | 9 | 0.218 |
| Italy | S1901M: A ROM - APU, A VEN S F TRI, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 7.1% | 6 | 42.9% | 9 | 0.163 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select germany=y1_0cb3534ff5f7df6185fa004342394949f65af564a98623a128fd92e11f869ef6 --select italy=y1_d6407e14828b29f4164c4b79f2102d5e53106bd6d209a5dc0fa63cb1f4f05eff
```

#### England / Russia — 14 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - EDI, F EDI - NWG, F LON - NTH; F1901M: A EDI - NWY VIA, F NTH - SKA, F NWG C A EDI - NWY; W1901A: F LON B | 2 | 14.3% | 6 | 42.9% | 9 | 0.197 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, A STP B | 0 | 0.0% | 5 | 35.7% | 7 | 0.055 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select england=y1_adb2dc9b5532a57fea1f3a1ce330aadf7f5f7a9b453cba1d4b96f47c3dae5613 --select russia=y1_8ea7154322eda3d2763e106805a20c4e8f50fc54c8de46db081ac1d7de3d6479
```

#### Austria / Germany — 19 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 1 | 5.3% | 6 | 31.6% | 12 | 0.156 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A MUN B, F KIE B | 2 | 10.5% | 6 | 31.6% | 12 | 0.166 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select germany=y1_0cb3534ff5f7df6185fa004342394949f65af564a98623a128fd92e11f869ef6
```

#### Germany / Russia — 16 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - MUN, F DEN - SWE; W1901A: A KIE B, F BER B | 0 | 0.0% | 6 | 37.5% | 8 | 0.088 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B | 1 | 6.2% | 3 | 18.8% | 6 | 0.069 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select germany=y1_cdf77a8cab51979f0a32c290a07e41786e6e0b708e13c5a6356527c91186cb30 --select russia=y1_627154b2546acca6b61175d84fd4ce23c56b7da6515a83868810c5a3d6e55d8e
```

#### Austria / France — 29 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 1 | 3.4% | 9 | 31.0% | 13 | 0.159 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - MAR, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 4 | 13.8% | 16 | 55.2% | 24 | 0.276 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select france=y1_43ef5e2463cc47d99aa7db27a73cd1766531b0e4684ccacb74a6b3c684b3e82b
```

#### Italy / Russia — 16 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 2 | 12.5% | 6 | 37.5% | 9 | 0.195 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B | 1 | 6.2% | 2 | 12.5% | 7 | 0.122 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e --select russia=y1_627154b2546acca6b61175d84fd4ce23c56b7da6515a83868810c5a3d6e55d8e
```

#### France / Russia — 14 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 2 | 14.3% | 6 | 42.9% | 9 | 0.204 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, F STP/NC B | 1 | 7.1% | 3 | 21.4% | 8 | 0.114 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level no_press --quality-group tier_1 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select russia=y1_64b9609fe614a49c8323db71e19e0faede49772f8fe71946056231e32ffd2be7
```

### press_with_msgs — Tiers 1–3

20,951 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| England / Germany | 17,660 | 16,152 | 4,799 | 0 | 0 | 51 |
| England / Turkey | 17,970 | 16,468 | 4,483 | 0 | 0 | 72 |
| England / France | 18,000 | 16,494 | 4,457 | 0 | 0 | 53 |
| Austria / Italy | 17,818 | 16,657 | 4,294 | 0 | 0 | 131 |
| Italy / Turkey | 18,163 | 16,936 | 4,015 | 0 | 0 | 61 |
| England / Italy | 18,265 | 17,015 | 3,936 | 0 | 0 | 63 |
| France / Germany | 18,590 | 17,405 | 3,546 | 0 | 0 | 56 |
| Germany / Turkey | 18,620 | 17,474 | 3,477 | 0 | 0 | 78 |
| Austria / Turkey | 18,693 | 17,617 | 3,334 | 0 | 0 | 37 |
| Germany / Italy | 18,731 | 17,730 | 3,221 | 0 | 0 | 69 |
| France / Italy | 18,931 | 17,923 | 3,028 | 0 | 0 | 54 |
| Russia / Turkey | 19,007 | 18,106 | 2,845 | 0 | 0 | 72 |
| France / Turkey | 19,210 | 18,265 | 2,686 | 0 | 0 | 63 |
| Austria / England | 19,378 | 18,517 | 2,434 | 0 | 0 | 30 |
| Austria / Germany | 19,670 | 18,975 | 1,976 | 0 | 0 | 45 |
| Austria / France | 20,025 | 19,510 | 1,441 | 0 | 0 | 46 |
| England / Russia | 20,015 | 19,520 | 1,431 | 0 | 0 | 38 |
| Austria / Russia | 20,104 | 19,664 | 1,287 | 0 | 0 | 45 |
| Italy / Russia | 20,160 | 19,721 | 1,230 | 0 | 0 | 51 |
| Germany / Russia | 20,180 | 19,770 | 1,181 | 0 | 0 | 75 |
| France / Russia | 20,451 | 20,196 | 755 | 0 | 0 | 56 |

#### England / Germany — 51 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 2 | 3.9% | 3 | 5.9% | 21 | 0.042 |
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 4 | 7.8% | 10 | 0.004 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84
```

#### England / Turkey — 72 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 2 | 2.8% | 6 | 8.3% | 24 | 0.037 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 2 | 2.8% | 4 | 5.6% | 22 | 0.036 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### England / France — 53 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 3 | 5.7% | 9 | 17.0% | 25 | 0.071 |
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 5 | 9.4% | 6 | 11.3% | 27 | 0.109 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c
```

#### Austria / Italy — 131 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 22 | 16.8% | 33 | 25.2% | 92 | 0.246 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 3 | 2.3% | 27 | 20.6% | 64 | 0.057 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Italy / Turkey — 61 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 2 | 3.3% | 16 | 26.2% | 31 | 0.080 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 2 | 3.3% | 19 | 31.1% | 37 | 0.094 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### England / Italy — 63 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 0 | 0.0% | 6 | 9.5% | 17 | 0.004 |
| Italy | S1901M: A ROM H, A VEN H, F NAP H; F1901M: A ROM H, A VEN H, F NAP H | 0 | 0.0% | 5 | 7.9% | 23 | 0.009 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select italy=y1_40ff40b0e4dad05aedea2e73c143b33fc80b8fea9045a788ce39f11127e4cc16
```

#### France / Germany — 56 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 3 | 5.4% | 9 | 16.1% | 28 | 0.075 |
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 4 | 7.1% | 10 | 0.004 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84
```

#### Germany / Turkey — 78 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 2 | 2.6% | 7 | 9.0% | 18 | 0.035 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 0 | 0.0% | 8 | 10.3% | 22 | 0.020 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84 --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### Austria / Turkey — 37 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD H, A VIE H, F TRI H; F1901M: A BUD H, A VIE H, F TRI H | 1 | 2.7% | 2 | 5.4% | 7 | 0.051 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 2 | 5.4% | 4 | 10.8% | 12 | 0.094 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=y1_b6605c54b15973327a20bbafdcfd315e648a64684ed3aab2f174b0dc3fa25277 --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### Germany / Italy — 69 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 1 | 1.4% | 3 | 4.3% | 7 | 0.015 |
| Italy | S1901M: A ROM H, A VEN H, F NAP H; F1901M: A ROM H, A VEN H, F NAP H | 0 | 0.0% | 4 | 5.8% | 14 | 0.003 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84 --select italy=y1_40ff40b0e4dad05aedea2e73c143b33fc80b8fea9045a788ce39f11127e4cc16
```

#### France / Italy — 54 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 1 | 1.9% | 9 | 16.7% | 18 | 0.030 |
| Italy | S1901M: A ROM H, A VEN H, F NAP H; F1901M: A ROM H, A VEN H, F NAP H | 2 | 3.7% | 10 | 18.5% | 24 | 0.057 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c --select italy=y1_40ff40b0e4dad05aedea2e73c143b33fc80b8fea9045a788ce39f11127e4cc16
```

#### Russia / Turkey — 72 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 1 | 1.4% | 11 | 15.3% | 17 | 0.028 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 4 | 5.6% | 17 | 23.6% | 36 | 0.098 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### France / Turkey — 63 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 1 | 1.6% | 10 | 15.9% | 22 | 0.031 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 1 | 1.6% | 7 | 11.1% | 22 | 0.027 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### Austria / England — 30 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD H, A VIE H, F TRI H; F1901M: A BUD H, A VIE H, F TRI H; F1901R: F TRI D | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 0 | 0.0% | 4 | 13.3% | 10 | 0.017 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=y1_4e863ba254737425f819cd4a93fb36359015b5743f742c66b0c1504db669f921 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a
```

#### Austria / Germany — 45 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD H, A VIE H, F TRI H; F1901M: A BUD H, A VIE H, F TRI H | 0 | 0.0% | 2 | 4.4% | 6 | 0.016 |
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 2 | 4.4% | 5 | 0.005 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=y1_b6605c54b15973327a20bbafdcfd315e648a64684ed3aab2f174b0dc3fa25277 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84
```

#### Austria / France — 46 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 4 | 8.7% | 9 | 19.6% | 27 | 0.157 |
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 2 | 4.3% | 4 | 8.7% | 16 | 0.056 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c
```

#### England / Russia — 38 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 0 | 0.0% | 5 | 13.2% | 12 | 0.021 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 2 | 5.3% | 7 | 0.001 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Austria / Russia — 45 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD H, A VIE H, F TRI H; F1901M: A BUD H, A VIE H, F TRI H | 3 | 6.7% | 0 | 0.0% | 7 | 0.067 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 1 | 2.2% | 4 | 8.9% | 7 | 0.037 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select austria=y1_b6605c54b15973327a20bbafdcfd315e648a64684ed3aab2f174b0dc3fa25277 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Italy / Russia — 51 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM H, A VEN H, F NAP H; F1901M: A ROM H, A VEN H, F NAP H | 1 | 2.0% | 3 | 5.9% | 10 | 0.020 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 4 | 7.8% | 7 | 0.006 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select italy=y1_40ff40b0e4dad05aedea2e73c143b33fc80b8fea9045a788ce39f11127e4cc16 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Germany / Russia — 75 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - DEN, A RUH - HOL, F DEN - SWE; W1901A: A BER B, A MUN B, F KIE B | 19 | 25.3% | 21 | 28.0% | 55 | 0.349 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 1 | 1.3% | 6 | 0.006 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select germany=y1_f22f0f2b26c1db0566f1e9a8622b0314f90a6b08b7dcad0687c02502cb21aabe --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### France / Russia — 56 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 1 | 1.8% | 6 | 10.7% | 20 | 0.038 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 1 | 1.8% | 5 | 8.9% | 12 | 0.025 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tiers_1_3 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

### press_with_msgs — Tier 1

7,116 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| Austria / Italy | 6,419 | 6,134 | 982 | 0 | 0 | 55 |
| England / Germany | 6,534 | 6,168 | 948 | 0 | 0 | 20 |
| England / Turkey | 6,576 | 6,234 | 882 | 0 | 0 | 14 |
| Italy / Turkey | 6,537 | 6,242 | 874 | 0 | 0 | 33 |
| England / Italy | 6,570 | 6,271 | 845 | 0 | 0 | 18 |
| England / France | 6,633 | 6,303 | 813 | 0 | 0 | 21 |
| Germany / Italy | 6,709 | 6,485 | 631 | 0 | 0 | 19 |
| France / Germany | 6,734 | 6,492 | 624 | 0 | 0 | 14 |
| Austria / Turkey | 6,723 | 6,493 | 623 | 0 | 0 | 11 |
| Germany / Turkey | 6,757 | 6,516 | 600 | 0 | 0 | 14 |
| France / Italy | 6,760 | 6,537 | 579 | 0 | 0 | 13 |
| Russia / Turkey | 6,765 | 6,549 | 567 | 0 | 0 | 13 |
| France / Turkey | 6,841 | 6,643 | 473 | 0 | 0 | 13 |
| Austria / England | 6,861 | 6,681 | 435 | 0 | 0 | 9 |
| Austria / Germany | 6,913 | 6,763 | 353 | 0 | 0 | 7 |
| Austria / France | 6,974 | 6,873 | 243 | 0 | 0 | 12 |
| Austria / Russia | 6,972 | 6,874 | 242 | 0 | 0 | 10 |
| England / Russia | 6,990 | 6,900 | 216 | 0 | 0 | 8 |
| Italy / Russia | 7,022 | 6,951 | 165 | 0 | 0 | 10 |
| Germany / Russia | 7,019 | 6,958 | 158 | 0 | 0 | 13 |
| France / Russia | 7,062 | 7,026 | 90 | 0 | 0 | 7 |

#### Austria / Italy — 55 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 9 | 16.4% | 17 | 30.9% | 34 | 0.240 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 1.8% | 19 | 34.5% | 34 | 0.079 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### England / Germany — 20 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - DEN VIA, F NTH C A YOR - DEN, F NWG - NWY; W1901A: F LON B | 1 | 5.0% | 5 | 25.0% | 12 | 0.091 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - HOL; F1901M: A KIE - DEN, A RUH - BEL, F HOL S A RUH - BEL; W1901A: A MUN B, F BER B | 0 | 0.0% | 4 | 20.0% | 7 | 0.036 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=y1_63a9f0b3857a63f15801a2d84a3fd00e699d6e2447d227a94e94eb47c2ff90ab --select germany=y1_b6b6a4c85def8cbbb86a12048e6390ec9c170afed2c435f166fcc61da9e3bf3f
```

#### England / Turkey — 14 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 0 | 0.0% | 2 | 14.3% | 8 | 0.037 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 2 | 14.3% | 3 | 21.4% | 8 | 0.183 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### Italy / Turkey — 33 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 3.0% | 9 | 27.3% | 14 | 0.067 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 2 | 6.1% | 13 | 39.4% | 24 | 0.161 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### England / Italy — 18 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - NWY VIA, F NTH C A YOR - NWY, F NWG S A YOR - NWY; W1901A: F LON B | 0 | 0.0% | 11 | 61.1% | 14 | 0.125 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 5.6% | 5 | 27.8% | 8 | 0.148 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=y1_14c42aca3b58b67850924a54376f07237374e74350af5e302a52f3b4134cf5c7 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### England / France — 21 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - BEL VIA, F NTH C A YOR - BEL, F NWG - NWY; W1901A: F LON B | 0 | 0.0% | 5 | 23.8% | 10 | 0.043 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 1 | 4.8% | 9 | 42.9% | 17 | 0.182 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=y1_bfdaffcaf300956288c9ffaef64a4b9f7be8d521e8f8402549b726a7f5755192 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9
```

#### Germany / Italy — 19 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 1 | 5.3% | 6 | 0.021 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 5.3% | 2 | 10.5% | 10 | 0.064 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### France / Germany — 14 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 1 | 7.1% | 3 | 21.4% | 7 | 0.123 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - HOL; F1901M: A KIE - DEN, A RUH - BEL, F HOL S A RUH - BEL; W1901A: A BER B, A MUN B, F KIE B | 0 | 0.0% | 3 | 21.4% | 6 | 0.081 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c --select germany=y1_38b4f37c3b860a10c0d8da0700ea07479a2496af2e4ebbf2cecd9922e2bfd003
```

#### Austria / Turkey — 11 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 3 | 27.3% | 2 | 18.2% | 6 | 0.339 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - RUM, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 0 | 0.0% | 3 | 27.3% | 6 | 0.038 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select turkey=y1_c57efb33fc45d24467e8dab57edabcbe1c9b89f858f2855a214e28e6b3d7bdab
```

#### Germany / Turkey — 14 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 2 | 14.3% | 6 | 0.012 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 0 | 0.0% | 6 | 42.9% | 8 | 0.075 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84 --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### France / Italy — 13 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B, F MAR B | 4 | 30.8% | 4 | 30.8% | 13 | 0.438 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 0 | 0.0% | 3 | 23.1% | 8 | 0.021 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select france=y1_44e18181b3a869ede574a8ac76e6b6d2cc6cfdfd363da732325506316098cb1f --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Russia / Turkey — 13 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 7 | 53.8% | 8 | 0.015 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 1 | 7.7% | 5 | 38.5% | 9 | 0.087 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### France / Turkey — 13 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 0 | 0.0% | 7 | 53.8% | 8 | 0.043 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 0 | 0.0% | 5 | 38.5% | 7 | 0.026 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### Austria / England — 9 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 0 | 0.0% | 6 | 66.7% | 6 | 0.208 |
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - BEL VIA, F NTH C A YOR - BEL, F NWG - NWY; W1901A: F LON B | 1 | 11.1% | 3 | 33.3% | 5 | 0.188 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select england=y1_bfdaffcaf300956288c9ffaef64a4b9f7be8d521e8f8402549b726a7f5755192
```

#### Austria / Germany — 7 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 1 | 14.3% | 2 | 28.6% | 5 | 0.236 |
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84
```

#### Austria / France — 12 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD H, A VIE H, F TRI H; F1901M: A BUD H, A VIE H, F TRI H | 1 | 8.3% | 2 | 16.7% | 3 | 0.086 |
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 0 | 0.0% | 4 | 33.3% | 7 | 0.016 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=y1_b6605c54b15973327a20bbafdcfd315e648a64684ed3aab2f174b0dc3fa25277 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c
```

#### Austria / Russia — 10 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD H, A VIE H, F TRI H; F1901M: A BUD H, A VIE H, F TRI H | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 2 | 20.0% | 2 | 0.023 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select austria=y1_b6605c54b15973327a20bbafdcfd315e648a64684ed3aab2f174b0dc3fa25277 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### England / Russia — 8 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 0 | 0.0% | 2 | 25.0% | 4 | 0.037 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Italy / Russia — 10 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 0 | 0.0% | 2 | 20.0% | 5 | 0.063 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 1 | 10.0% | 2 | 0.012 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Germany / Russia — 13 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - DEN, A RUH - HOL, F DEN - SWE; W1901A: A BER B, A MUN B, F KIE B | 5 | 38.5% | 7 | 53.8% | 12 | 0.592 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select germany=y1_f22f0f2b26c1db0566f1e9a8622b0314f90a6b08b7dcad0687c02502cb21aabe --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### France / Russia — 7 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 0 | 0.0% | 2 | 28.6% | 3 | 0.001 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 2 | 28.6% | 2 | 0.018 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level press_with_msgs --quality-group tier_1 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

### public_press — Tiers 1–3

918 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| Austria / Italy | 881 | 859 | 59 | 0 | 0 | 8 |
| Italy / Turkey | 887 | 866 | 52 | 0 | 0 | 4 |
| England / Turkey | 893 | 871 | 47 | 0 | 0 | 3 |
| England / Italy | 893 | 875 | 43 | 0 | 0 | 4 |
| England / France | 897 | 876 | 42 | 0 | 0 | 2 |
| Russia / Turkey | 898 | 881 | 37 | 0 | 0 | 4 |
| France / Germany | 901 | 885 | 33 | 0 | 0 | 3 |
| Germany / Turkey | 899 | 886 | 32 | 0 | 0 | 4 |
| France / Italy | 903 | 891 | 27 | 0 | 0 | 3 |
| France / Turkey | 904 | 893 | 25 | 0 | 0 | 4 |
| Germany / Italy | 905 | 893 | 25 | 0 | 0 | 3 |
| Austria / Turkey | 905 | 894 | 24 | 0 | 0 | 4 |
| England / Germany | 907 | 899 | 19 | 0 | 0 | 3 |
| Austria / England | 910 | 902 | 16 | 0 | 0 | 2 |
| Austria / Germany | 910 | 902 | 16 | 0 | 0 | 2 |
| Austria / Russia | 912 | 906 | 12 | 0 | 0 | 2 |
| Italy / Russia | 912 | 907 | 11 | 0 | 0 | 3 |
| Germany / Russia | 912 | 908 | 10 | 0 | 0 | 4 |
| Austria / France | 914 | 910 | 8 | 0 | 0 | 2 |
| England / Russia | 917 | 916 | 2 | 0 | 0 | 2 |
| France / Russia | 917 | 916 | 2 | 0 | 0 | 2 |

#### Austria / Italy — 8 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 0 | 0.0% | 2 | 25.0% | 5 | 0.083 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 0 | 0.0% | 2 | 25.0% | 4 | 0.031 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Italy / Turkey — 4 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 0 | 0.0% | 1 | 25.0% | 1 | 0.019 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 0 | 0.0% | 3 | 75.0% | 3 | 0.266 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### England / Turkey — 3 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - LON, F NTH - BEL, F NWG - NWY; W1901A: F LVP B | 0 | 0.0% | 2 | 66.7% | 2 | 0.146 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=y1_68f5ebc67abf7b6f36a967bc7e3b75dac9160bb7752ed6bf0666c0b6455c6c67 --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### England / Italy — 4 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP H, F EDI H, F LON H; F1901M: A LVP H, F EDI H, F LON H | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 25.0% | 1 | 25.0% | 4 | 0.298 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=y1_7e764822c3c41c70e395fbf54daa1d2df94b69d92e5ea4ad954558e472b7e33a --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### England / France — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - NWY VIA, F NTH C A YOR - NWY, F NWG S A YOR - NWY; W1901A: F LON B | 0 | 0.0% | 1 | 50.0% | 2 | 0.031 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A BRE B, A PAR B, F MAR B | 0 | 0.0% | 1 | 50.0% | 1 | 0.048 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=y1_14c42aca3b58b67850924a54376f07237374e74350af5e302a52f3b4134cf5c7 --select france=y1_6d48880fc8bbbd501cfd99b2919f1be6fdf3729d31e373f09db33671ce45b4a3
```

#### Russia / Turkey — 4 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 1 | 25.0% | 2 | 0.001 |
| Turkey | S1901M: A CON - BUL, A SMY - ARM, F ANK - BLA; F1901M: A ARM - SEV, A BUL - RUM, F BLA S A ARM - SEV; W1901A: A CON B, F SMY B | 1 | 25.0% | 2 | 50.0% | 4 | 0.406 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d --select turkey=y1_8d672411926d8ad12316d2845e3a55be6dedbcf84d62a7f30fd8423066b1676b
```

#### France / Germany — 3 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A SPA H, F MAO - POR; W1901A: A PAR B, F BRE B | 1 | 33.3% | 0 | 0.0% | 2 | 0.333 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A MUN B, F BER B | 1 | 33.3% | 0 | 0.0% | 2 | 0.333 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select france=y1_b0e0fa63ce6f8af358c09d89a97a85cc4bc1f031f17e01e823111982449cfe92 --select germany=y1_a2294bee2c1cc82984de91541b1ba0ded8522b6b1558ef3530ba39efd471180b
```

#### Germany / Turkey — 4 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A BER B, A MUN B, F KIE B | 0 | 0.0% | 2 | 50.0% | 2 | 0.174 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 0 | 0.0% | 1 | 25.0% | 1 | 0.057 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select germany=y1_7142af45a6493a51db4261521cd4fae9c0db0b91e93c6dc258e26ba16f349449 --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### France / Italy — 3 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 2 | 66.7% | 0 | 0.0% | 3 | 0.667 |
| Italy | S1901M: A ROM - NAP, A VEN H, F NAP - ION; F1901M: A NAP - TUN VIA, A VEN H, F ION C A NAP - TUN; W1901A: F NAP B | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select italy=y1_87e8c93620e29f642ce7520e68c680ceac15a4cdb128e3ff70b47493a0c90466
```

#### France / Turkey — 4 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR H, A PAR H, F BRE H; F1901M: A MAR H, A PAR H, F BRE H | 0 | 0.0% | 1 | 25.0% | 2 | 0.079 |
| Turkey | S1901M: A CON H, A SMY H, F ANK H; F1901M: A CON H, A SMY H, F ANK H | 0 | 0.0% | 1 | 25.0% | 1 | 0.057 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select france=y1_ec7c6ff5c3b86a4bbb84f65bbdbf5101cdfca7975e3e1faec6987194b6b85f7c --select turkey=y1_84e2291580be0b72f544d03e03917c43f0c8a0f7634c2934f7512f203c312b03
```

#### Germany / Italy — 3 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - HOL; F1901M: A KIE - DEN, A RUH - BEL, F HOL S A RUH - BEL; W1901A: A BER B, A KIE B | 0 | 0.0% | 1 | 33.3% | 2 | 0.056 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 1 | 33.3% | 1 | 33.3% | 2 | 0.358 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select germany=y1_7fba5ddab28ee4551d25590ce8c5c52826b3634f0a29bb965e656252c7a3e038 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Austria / Turkey — 4 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - RUM, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 0 | 0.0% | 2 | 50.0% | 4 | 0.102 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select turkey=y1_c57efb33fc45d24467e8dab57edabcbe1c9b89f858f2855a214e28e6b3d7bdab
```

#### England / Germany — 3 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - NWY VIA, F NTH C A YOR - NWY, F NWG - BAR; W1901A: F LON B | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - HOL; F1901M: A KIE - DEN, A RUH - BEL, F HOL S A RUH - BEL; W1901A: A BER B, A MUN B, F KIE B | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=y1_9fda7efbed54953193fa0661547778293f46c287196a68b316c4af3377884b86 --select germany=y1_38b4f37c3b860a10c0d8da0700ea07479a2496af2e4ebbf2cecd9922e2bfd003
```

#### Austria / England — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI - BUD, F ALB - GRE; W1901A: A BUD B, A VIE B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |
| England | S1901M: A LVP - YOR, F EDI - NTH, F LON - ENG; F1901M: A YOR - NWY VIA, F LON - ENG, F NTH C A YOR - NWY | 0 | 0.0% | 1 | 50.0% | 1 | 0.012 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=y1_33ad2849c625a455c2ce91f3a46b3ea7070e2ad6bfa4139349526cf2383035fd --select england=y1_0e0b536fd46b0a9b1de421f1add4bda4f93387fd5d260712ad9af1899be5ca31
```

#### Austria / Germany — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - VEN; F1901M: A SER - GRE, A VIE - GAL, F TRI H; W1901A: A BUD B | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A BER B, A MUN B, F KIE B | 0 | 0.0% | 1 | 50.0% | 1 | 0.142 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=y1_4470946898e01cedff4e37966dadb0c9a72ed9d6aa59c15fff6bff67215c9ef9 --select germany=y1_7142af45a6493a51db4261521cd4fae9c0db0b91e93c6dc258e26ba16f349449
```

#### Austria / Russia — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A STP B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=y1_15393ed9b58f669c85a035f5121df5a9202021287978f964c216d82b11a9f7ba --select russia=y1_5e3f486cbd5a88f545d6dba2a06ae7476a092487c0434d75ad37698fa71fa100
```

#### Italy / Russia — 3 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM H, A VEN H, F NAP H; F1901M: A ROM H, A VEN H, F NAP H | 0 | 0.0% | 2 | 66.7% | 2 | 0.015 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 2 | 66.7% | 3 | 0.039 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select italy=y1_40ff40b0e4dad05aedea2e73c143b33fc80b8fea9045a788ce39f11127e4cc16 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Germany / Russia — 4 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER H, A MUN H, F KIE H; F1901M: A BER H, A MUN H, F KIE H | 0 | 0.0% | 1 | 25.0% | 1 | 0.004 |
| Russia | S1901M: A MOS H, A WAR H, F SEV H, F STP/SC H; F1901M: A MOS H, A WAR H, F SEV H, F STP/SC H | 0 | 0.0% | 1 | 25.0% | 1 | 0.071 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select germany=y1_b4f53f35ce075b68705dd33962b6951002588d5b4f8d26e10a4e326c47fa8d84 --select russia=y1_cdfe2f8036753130995dc9897809cb4530b4d4b98406e2fc239eba46be3aae2d
```

#### Austria / France — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD H, A VIE H, F TRI H; F1901M: A BUD H, A VIE H, F TRI H; F1901R: F TRI D | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B, F MAR B | 1 | 50.0% | 1 | 50.0% | 2 | 0.525 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select austria=y1_4e863ba254737425f819cd4a93fb36359015b5743f742c66b0c1504db669f921 --select france=y1_44e18181b3a869ede574a8ac76e6b6d2cc6cfdfd363da732325506316098cb1f
```

#### England / Russia — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - DEN VIA, F NTH C A YOR - DEN, F NWG - NWY; W1901A: F EDI B, F LON B | 0 | 0.0% | 2 | 100.0% | 2 | 0.521 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, A STP B | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select england=y1_105d7d3c7a0a56cea0c2c9350af49147682b15b3597d5d770dfafdd033901693 --select russia=y1_8ea7154322eda3d2763e106805a20c4e8f50fc54c8de46db081ac1d7de3d6479
```

#### France / Russia — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A SPA H, F MAO - POR; W1901A: A PAR B, F BRE B | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A GAL S A UKR - RUM, A UKR - RUM, F BOT - SWE, F SEV - BLA; W1901A: A WAR B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tiers_1_3 --select france=y1_b0e0fa63ce6f8af358c09d89a97a85cc4bc1f031f17e01e823111982449cfe92 --select russia=y1_0add22305b8307e0aec080ccb95a8c4ec360c1b9843e335960cb6f64bdbe31b1
```

### public_press — Tier 1

314 games in this cohort. Threshold: 200 matches.

| Pair | Patterns | Singletons | Games in repeated patterns | Patterns ≥ 200 | Games ≥ 200 | Largest match count |
|---|---:|---:|---:|---:|---:|---:|
| Italy / Turkey | 307 | 302 | 12 | 0 | 0 | 3 |
| Austria / Italy | 307 | 303 | 11 | 0 | 0 | 5 |
| England / Italy | 310 | 307 | 7 | 0 | 0 | 3 |
| England / France | 311 | 308 | 6 | 0 | 0 | 2 |
| Germany / Turkey | 311 | 308 | 6 | 0 | 0 | 2 |
| Austria / Turkey | 312 | 310 | 4 | 0 | 0 | 2 |
| France / Germany | 312 | 310 | 4 | 0 | 0 | 2 |
| France / Italy | 312 | 310 | 4 | 0 | 0 | 2 |
| Austria / England | 313 | 312 | 2 | 0 | 0 | 2 |
| Austria / France | 313 | 312 | 2 | 0 | 0 | 2 |
| Austria / Russia | 313 | 312 | 2 | 0 | 0 | 2 |
| England / Germany | 313 | 312 | 2 | 0 | 0 | 2 |
| England / Russia | 313 | 312 | 2 | 0 | 0 | 2 |
| England / Turkey | 313 | 312 | 2 | 0 | 0 | 2 |
| Germany / Italy | 313 | 312 | 2 | 0 | 0 | 2 |
| Austria / Germany | 314 | 314 | 0 | 0 | 0 | 1 |
| France / Russia | 314 | 314 | 0 | 0 | 0 | 1 |
| France / Turkey | 314 | 314 | 0 | 0 | 0 | 1 |
| Germany / Russia | 314 | 314 | 0 | 0 | 0 | 1 |
| Italy / Russia | 314 | 314 | 0 | 0 | 0 | 1 |
| Russia / Turkey | 314 | 314 | 0 | 0 | 0 | 1 |

#### Italy / Turkey — 3 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |
| Turkey | S1901M: A CON - BUL, A SMY - ARM, F ANK - BLA; F1901M: A ARM - SEV, A BUL - RUM, F ANK - BLA; W1901A: F CON B | 1 | 33.3% | 1 | 33.3% | 2 | 0.374 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e --select turkey=y1_d387935f96009205c4ebfb4f45e936cbe283d6606e9df29c153f109ab966b0cd
```

#### Austria / Italy — 5 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - TRI, F ALB - GRE; W1901A: A BUD B, A VIE B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 0 | 0.0% | 1 | 20.0% | 1 | 0.066 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select austria=y1_e7b3d34ab4c0b3b1110552dcd1ce29a8cce5615f091c03c2e20909f9471e7dc3 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### England / Italy — 3 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - BEL VIA, F NTH C A YOR - BEL, F NWG - NWY; W1901A: F LON B | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION; F1901M: A TYR S A VEN - TRI, A VEN - TRI, F ION - TUN; W1901A: A VEN B, F NAP B | 1 | 33.3% | 0 | 0.0% | 1 | 0.333 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select england=y1_bfdaffcaf300956288c9ffaef64a4b9f7be8d521e8f8402549b726a7f5755192 --select italy=y1_fa42b38c4588784284145484dc8194fe88ad4d882310ed1f6508269835653c73
```

#### England / France — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - NWY VIA, F NTH C A YOR - NWY, F NWG - BAR; W1901A: A LON B | 0 | 0.0% | 1 | 50.0% | 1 | 0.102 |
| France | S1901M: A MAR - SPA, A PAR - GAS, F BRE - MAO; F1901M: A GAS - SPA, A SPA - POR, F MAO - WES; W1901A: A PAR B, F MAR B | 0 | 0.0% | 2 | 100.0% | 2 | 0.251 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select england=y1_aebe4b7c0ef0fdf4481f96091e2b9441cdaa8a513e9a1ad4ed2c6abd469dd4de --select france=y1_d6c32c1a105eeea3b7b1cd3b68ce161a274187d330a90dace81dec9b2c514f60
```

#### Germany / Turkey — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A MUN B, F KIE B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 0 | 0.0% | 1 | 50.0% | 2 | 0.132 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select germany=y1_0cb3534ff5f7df6185fa004342394949f65af564a98623a128fd92e11f869ef6 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### Austria / Turkey — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - RUM, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 0 | 0.0% | 1 | 50.0% | 2 | 0.082 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select turkey=y1_c57efb33fc45d24467e8dab57edabcbe1c9b89f858f2855a214e28e6b3d7bdab
```

#### France / Germany — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR - SPA, A PAR - PIC, F BRE - MAO; F1901M: A PIC - BEL, A SPA S F MAO - POR, F MAO - POR; W1901A: A MAR B, A PAR B, F BRE B | 0 | 0.0% | 1 | 50.0% | 1 | 0.203 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH S A KIE - HOL, F DEN - SWE; W1901A: A BER B, A MUN B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select france=y1_0b81c850bdbd0d1132c4e9a7c040c755e5cbf23a10467ca11ca6575fb40f04a0 --select germany=y1_13ebafd4a63295e51072fed99d66d5c806d14e05493ca7600fa4d0613b9dbab3
```

#### France / Italy — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - BEL, A MAR - SPA, F MAO - POR; W1901A: A PAR B, F BRE B | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |
| Italy | S1901M: A ROM - VEN, A VEN - TYR, F NAP - ION; F1901M: A TYR S A VEN - TRI, A VEN - TRI, F ION - TUN; W1901A: A VEN B, F NAP B | 0 | 0.0% | 0 | 0.0% | 1 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select france=y1_56c185c92a7fa3ac8c105361448361208653b15f131a7da657200c7ab08afed9 --select italy=y1_fa42b38c4588784284145484dc8194fe88ad4d882310ed1f6508269835653c73
```

#### Austria / England — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - TRI, F ALB - GRE; W1901A: A BUD B, A VIE B | 0 | 0.0% | 2 | 100.0% | 2 | 0.524 |
| England | S1901M: A LVP - EDI, F EDI - NWG, F LON - NTH; F1901M: A EDI - NWY VIA, F NTH C A EDI - NWY, F NWG - BAR; W1901A: A LON B | 0 | 0.0% | 1 | 50.0% | 1 | 0.164 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select austria=y1_e7b3d34ab4c0b3b1110552dcd1ce29a8cce5615f091c03c2e20909f9471e7dc3 --select england=y1_ca89e9ab2d1a0d92b18cca7a0d2bbdfb328c72a67b17bf9111af51175f86f9b6
```

#### Austria / France — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TRI, F TRI - ALB; F1901M: A SER S F ALB - GRE, A TRI H, F ALB - GRE; W1901A: A BUD B, A VIE B | 0 | 0.0% | 2 | 100.0% | 2 | 0.399 |
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - MUN, A MAR - SPA, F MAO - POR; W1901A: A MAR B, A PAR B, F BRE B | 0 | 0.0% | 2 | 100.0% | 2 | 0.200 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select austria=y1_807bb8abe6f43b3ee430b9c3de090ee2b1741d8e58f4824cc5a28d892f922816 --select france=y1_007419c52b85039c42ba253620887e3d9e3e991c20125cbabe8995b889b08630
```

#### Austria / Russia — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - GAL, F TRI - ALB; F1901M: A SER S F ALB - GRE, A VIE - GAL, F ALB - GRE; W1901A: A BUD B, A TRI B | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, F STP/NC B | 1 | 50.0% | 0 | 0.0% | 1 | 0.500 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select austria=y1_cecb151c298fa175a6e604de5b329c30812b3c83ae8438fb847fba221ab3759a --select russia=y1_64b9609fe614a49c8323db71e19e0faede49772f8fe71946056231e32ffd2be7
```

#### England / Germany — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - EDI, F EDI - NWG, F LON - NTH; F1901M: A EDI - BEL VIA, F NTH C A EDI - BEL, F NWG - NWY; W1901A: F LON B | 0 | 0.0% | 1 | 50.0% | 2 | 0.054 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH - BEL, F DEN - SWE; W1901A: A BER B | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select england=y1_a5ef3aa584ec039a8e0d575f50332c6e7f48f8ff121c636a5ca9223565a5e2fd --select germany=y1_b02630ed6e68de0270d46f6e28dabaec79a2c90da6ae182c13493fe6976c3100
```

#### England / Russia — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - DEN VIA, F NTH C A YOR - DEN, F NWG - NWY; W1901A: F EDI B, F LON B | 0 | 0.0% | 2 | 100.0% | 2 | 0.521 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A MOS B, A STP B | 0 | 0.0% | 0 | 0.0% | 0 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select england=y1_105d7d3c7a0a56cea0c2c9350af49147682b15b3597d5d770dfafdd033901693 --select russia=y1_8ea7154322eda3d2763e106805a20c4e8f50fc54c8de46db081ac1d7de3d6479
```

#### England / Turkey — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| England | S1901M: A LVP - YOR, F EDI - NWG, F LON - NTH; F1901M: A YOR - BEL VIA, F NTH C A YOR - BEL, F NWG - NWY; W1901A: F LON B | 1 | 50.0% | 0 | 0.0% | 2 | 0.500 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: F SMY B | 0 | 0.0% | 0 | 0.0% | 2 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select england=y1_bfdaffcaf300956288c9ffaef64a4b9f7be8d521e8f8402549b726a7f5755192 --select turkey=y1_9a8c11faf99a2009563a1e2bf706b4c1685d508e47492b2bcdc1cb2f6b75f1c9
```

#### Germany / Italy — 2 matches

Below the sample-size threshold; these are observed fractions from a sparse sample.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH S A KIE - HOL, F DEN H; W1901A: A MUN B, F BER B | 0 | 0.0% | 1 | 50.0% | 1 | 0.168 |
| Italy | S1901M: A ROM - APU, A VEN H, F NAP - ION; F1901M: A APU - TUN VIA, A VEN H, F ION C A APU - TUN; W1901A: F NAP B | 0 | 0.0% | 1 | 50.0% | 1 | 0.089 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select germany=y1_1a6467e49755cf3ffcca6fc8b84aeecf534e35a9ded48c0d4c4c8e94532a2179 --select italy=y1_21510e957361d2af27e8833e8f6e1ad614a1de7b3b55377fd169865fbf5ac13e
```

#### Austria / Germany — 1 matches

One historical game; outcome rates are unavailable.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Austria | S1901M: A BUD - SER, A VIE - TYR, F TRI - ADR; F1901M: A SER S A APU - GRE, A TYR - TRI, F ADR - TRI; W1901A: F TRI B | 0 | — | 0 | — | 0 | 0.000 |
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - DEN; F1901M: A KIE - HOL, A RUH S A KIE - HOL, F DEN - SWE; W1901A: A BER B | 0 | — | 1 | — | 1 | 0.196 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select austria=y1_004f75001513f3b323b2c17ca3359d750cc0a81f717bf29c9fcf97c5ea153b29 --select germany=y1_1da5803657610d65803a791d787cad4cdee330a631ee3bcbccd3bf0a0a14df0f
```

#### France / Russia — 1 matches

One historical game; outcome rates are unavailable.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - MUN, A MAR - SPA, F MAO - POR; W1901A: A MAR B, A PAR B, F BRE B | 0 | — | 1 | — | 1 | 0.104 |
| Russia | S1901M: A MOS - WAR, A WAR - UKR, F SEV - BLA, F STP/SC - BOT; F1901M: A UKR - RUM, A WAR - GAL, F BOT - SWE, F SEV S A UKR - RUM; W1901A: A STP B | 0 | — | 0 | — | 0 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select france=y1_007419c52b85039c42ba253620887e3d9e3e991c20125cbabe8995b889b08630 --select russia=y1_13acb06cd2f15668a2afa17455b4929fa3b28fb53dc316e945f5d271a1416360
```

#### France / Turkey — 1 matches

One historical game; outcome rates are unavailable.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| France | S1901M: A MAR S A PAR - BUR, A PAR - BUR, F BRE - MAO; F1901M: A BUR - MUN, A MAR - SPA, F MAO - POR; W1901A: A MAR B, A PAR B, F BRE B | 0 | — | 1 | — | 1 | 0.193 |
| Turkey | S1901M: A CON - BUL, A SMY - ARM, F ANK - BLA; F1901M: A ARM - SMY, A BUL - RUM, F ANK - CON; W1901A: F ANK B | 0 | — | 0 | — | 0 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select france=y1_007419c52b85039c42ba253620887e3d9e3e991c20125cbabe8995b889b08630 --select turkey=y1_746344f98a5723f85e7915cbce11b2d7bd5c59e69bbf3b060c587cafd52dc89d
```

#### Germany / Russia — 1 matches

One historical game; outcome rates are unavailable.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Germany | S1901M: A BER - KIE, A MUN - RUH, F KIE - HOL; F1901M: A KIE - DEN, A RUH - BUR, F HOL S A WAL - BEL; W1901A: A MUN B, F KIE B | 0 | — | 0 | — | 1 | 0.000 |
| Russia | S1901M: A MOS - UKR, A WAR - GAL, F SEV - RUM, F STP/SC - BOT; F1901M: A UKR - SEV, A WAR - GAL, F BOT - SWE, F RUM - SEV; W1901A: A STP B, F SEV B | 0 | — | 0 | — | 1 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select germany=y1_0014ab938b7b83a14a960aa7f80339650484eeac9289a9bca80f6cd72590cefa --select russia=y1_8403945a9cfa5766af71ba086b81da34e7dce39840d78e287dd2a0d025e0c6f3
```

#### Italy / Russia — 1 matches

One historical game; outcome rates are unavailable.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Italy | S1901M: A ROM - APU, A VEN S F TRI, F NAP - ION; F1901M: A APU - TUN VIA, A VEN S F TRI, F ION C A APU - TUN; W1901A: F NAP B | 0 | — | 0 | — | 0 | 0.000 |
| Russia | S1901M: A MOS - STP, A WAR - GAL, F SEV - RUM, F STP/SC - BOT; F1901M: A STP H, A WAR - SIL, F BOT - BAL, F RUM S F CON - BUL; W1901A: A WAR B | 0 | — | 0 | — | 0 | 0.000 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select italy=y1_012eb7a63b979ad82b12524fa5d6c57c6a24b56c9353e7f3caa1b91b5af36d9c --select russia=y1_4cbce4783f05808579c24beae6a6d6aa11ad70bc50c022af8e993a9c74cda0f4
```

#### Russia / Turkey — 1 matches

One historical game; outcome rates are unavailable.

| Country | Recorded orders | Solos | Solo rate | Draws | Draw rate | Finished with centers | Mean score |
|---|---|---:|---:|---:|---:|---:|---:|
| Russia | S1901M: A MOS - STP, A WAR - UKR, F SEV - BLA, F STP/SC - BOT; F1901M: A STP - NWY, A UKR - RUM, F BOT - SWE, F SEV - BLA; W1901A: A MOS B | 0 | — | 0 | — | 0 | 0.000 |
| Turkey | S1901M: A CON - BUL, A SMY - CON, F ANK - BLA; F1901M: A BUL - GRE, A CON - BUL, F ANK - BLA; W1901A: A SMY B, F CON B | 0 | — | 1 | — | 1 | 0.313 |

```sh
uv run python -m pipeline.exact_openings lookup --horizon year1901 --context selected --press-level public_press --quality-group tier_1 --select russia=y1_000a380462876eddb94da008a476da31b8117fc4aacdebcd5929fb8bbc369e85 --select turkey=y1_42d2ce6202b70a1982400fddde89c2140d85394599b5d06335291e0521f78204
```
