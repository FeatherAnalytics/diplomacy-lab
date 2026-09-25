# Data Dictionary

One section per source: where it came from, what one record is, what fields it has, and what we use it for.

## DipNet (diplomacy/research)

- Source: https://github.com/diplomacy/research (Paquette et al. 2019, No Press Diplomacy). Download: https://s3-public.billovia.com/diplomacy/benchmarks/datasets/diplomacy-dataset.zip (2.2 GB zip, files dated 2019-07-30). Games scraped from webDiplomacy and playdiplomacy; no player identity. License: none stated in the README.
- Fetched: 2026-09-10 via `fetch_dipnet.sh`. Local: `data/raw/dipnet/` = the zip plus four extracted JSONL files (14.3 GB): `standard_no_press.jsonl` (2.7 GB), `standard_press_without_msgs.jsonl` (6.3 GB), `standard_press_with_msgs.jsonl` (5.1 GB), `standard_public_press.jsonl` (163 MB). `other_maps.jsonl` (16,633 non-standard-map games, 3.0 GB) is in the zip and not extracted.
- Grain: one line per game, full replay. Every phase carries the board state before adjudication, every power's orders, per-unit results, and messages.
- Verified counts: no_press 33,279; press_without_msgs 74,843; press_with_msgs 30,423; public_press 1,290; total 139,835. The README says 106,456 press games without messages and 50 with; the file split differs but the total (106,556 press) matches. "standard" here means standard-map rules family: `map` is `standard` for 93% of games but the no_press file also holds two-player variants (`standard_france_austria`, `standard_germany_italy`, about 36% of that file) and a few others (`standard_age_of_empires`, `standard_fleet_rome`). Filter on `map == "standard"` for seven-power analysis.

| Field | Type | Meaning |
|---|---|---|
| id | str | 16-char game ID, unique across files. Not joinable to any other source. |
| map | str | Map variant name (see above). |
| rules | list[str] | Engine rules. Seen: `POWER_CHOICE` (always), `NO_PRESS`, `PUBLIC_PRESS`, `NO_CHECK` (orders not validated on entry), `BUILD_ANY`. |
| phases[] | list | Phases in order. Normally starts at `S1901M` (`S0001M` on age_of_empires); one in-scope standard game starts at `S1902M`. Opening analyses must check the phase name. |
| phases[].name | str | `S1901M`, `F1901R`, `W1901A`: season (S/F/W) + year + type (M movement, R retreat, A adjustment). Last phase is `COMPLETED` only when a solo happened. |
| phases[].state.units | dict power -> list[str] | Units on the board before adjudication, e.g. `A PAR`, `F STP/NC`. Dislodged units are prefixed `*`. |
| phases[].state.centers | dict power -> list[str] | Supply centers owned. |
| phases[].state.homes | dict power -> list[str] | Home centers. |
| phases[].state.influence | dict power -> list[str] | Provinces last occupied by that power. |
| phases[].state.retreats | dict power -> dict unit -> list[str] | Dislodged units and legal retreat destinations (retreat phases only). |
| phases[].state.builds | dict power -> {count, homes} | Builds owed (positive) or disbands owed (negative) and open home centers (adjustment phases). |
| phases[].state.civil_disorder | dict power -> int | Always 0 in this dataset. Not usable. |
| phases[].state.note | str | Empty except on the `COMPLETED` phase, where it reads `Victory by: XXX` with a 3-letter power code. |
| phases[].state.name, game_id, map, rules, zobrist_hash, timestamp | | Duplicates of the phase and game headers, a position hash, and the conversion timestamp (2018-11, not game time). |
| phases[].orders | dict power -> list[str] or null | Order strings in engine notation: `A PAR - BUR`, `A PAR H`, `F MAO S A PAR - BUR`, `F ENG C A LON - BRE`, `A PAR B`, `A PAR D`, `A PAR R BUR`, `WAIVE`. `null` = phase never adjudicated (the trailing phase of a no_solo game). `[]` for every surviving power in one movement phase = game ended by draw or cancel vote. Missing orders were filled in as `H` when the data was built, so NMR is invisible except as all-hold streaks. |
| phases[].results | dict unit -> list[str] | Adjudication result per unit: `[]` success, `bounce`, `cut`, `dislodged`, `void`, `disband`, `no convoy`, `""` (builds). Empty dict on unadjudicated phases. |
| phases[].messages[] | list | Only populated in `press_with_msgs`, `public_press`, and a handful of no_press games. Fields `sender` (power or `SYSTEM`), `recipient` (power or `GLOBAL`), `time_sent` (unix seconds), `phase`, `message` (text). |

Outcome inference: `solo` when the last phase is `COMPLETED` (the note always names the winner; 18+ centers on standard map). Everything else is `no_solo`: draws, cancellations, abandoned games, and games still running at scrape time are not distinguished by any field. `ended_by_vote` (last adjudicated movement phase has `[]` orders for every surviving power) marks roughly half of no_solo games in the no_press, press_with_msgs, and public_press files and almost none in press_without_msgs, so it is a partial draw marker at best. It also fires on 2,522 in-scope solo games with empty terminal orders; always use `ending == "draw_vote"` for draw participation, since `ending` gives solos precedence.

Dropout inference: a power whose every unit holds in every movement phase from some point until it is eliminated or the record ends, for at least 3 movement phases. A power that all-holds and then moves again is not counted (a replacement player may have taken over).

Quality tiers (from `pipeline/profile_games.py`):

- 1 clean: last_year >= 1904 and no dropout (no power all-held its last 3+ movement phases)
- 2 minor dropout: last_year >= 1904 and every dropout began with the power holding <= 2 centers
- 3 major dropout: last_year >= 1904 and some dropout began with the power holding >= 3 centers
- 4 short: last_year < 1904

Tier 4 stays in `games.parquet` but is excluded from all analysis.

Ending: `solo` when the last phase is `COMPLETED`, `draw_vote` when `ended_by_vote`, else `unknown` (draws recorded another way, abandoned, or still running at scrape time; not distinguishable).

Scope (`in_scope` column, from `pipeline/profile_games.py`): `map == "standard"` and `quality_tier <= 3` and `ending != "unknown"` and `"BUILD_ANY"` not in `rules` and `last_year <= 1930` and not (`ending == "solo"` and the winner's final centers < 18). Every analysis filters on `in_scope`; nothing is deleted from `games.parquet`.

Processed output: `data/processed/games.parquet`, one row per game, built by `uv run python -m pipeline.profile_games`. Columns: `game_id`, `source_file`, `press_level` (no_press / press / press_with_msgs / public_press, from the file), `map`, `rules` (comma-joined), `n_phases`, `n_movement_phases` (adjudicated), `first_phase`, `last_phase`, `last_year` (last adjudicated phase), `outcome_type` (solo / no_solo), `ending` (solo / draw_vote / unknown), `winner` (full power name or null), `ended_by_vote`, `n_alive_at_end`, `n_messages`, `n_phases_with_cd` (always 0, kept as a check), `n_powers_dropout`, `first_dropout_year`, `max_centers_of_dropout_power`, `quality_tier`, `centers_<power>` (7 columns, final count), `in_scope` (bool, see Scope above). Summary tables in `data/processed/quality_summary.md`.

Outcome scores: `data/processed/game_outcomes.parquet`, one row per game and power, built by `uv run python -m pipeline.outcome_rates` from `games.parquet` filtered on `in_scope`. Columns: `game_id`, `press_level`, `quality_tier`, `power`, `final_centers`, `survived` (centers > 0), `solo` (centers >= 18), `draw_vote` (survived and `ending == "draw_vote"`), `sos_score`. Sum-of-squares score: 1 for a power with 18+ centers and 0 for the others in that game; otherwise `centers^2 / sum(centers^2)` over the seven powers, so scores in a game sum to 1. The parquet retains all 62,719 in-scope games (439,033 rows), including press_without_msgs for analyses conditioned on solos.

Per-power rate tables in `data/processed/outcome_rates.md` use only the 37,203 in-scope games from no_press, press_with_msgs, and public_press. press_without_msgs is excluded because its draws are almost never detectable (25,457 solos versus 59 draw votes in scope). The report includes a tier-1 sensitivity table (14,537 games from the same three sources). These are descriptive rates conditional on detectable endings, not population or causal estimates. Regression checks: `uv run python -m unittest discover -s tests -v`.

- Limitations: no confirmed draw results or draw sizes; draws are only partially inferable. No player identity or wall-clock game dates. Dropouts are inferred from hold patterns. The snapshot dates to 2019.
- Use in this project: the primary orders and board-state corpus. Everything modeled downstream starts from `games.parquet` filtered by `map`, `press_level`, and `quality_tier`.

## DipNet phase table

- Path: `data/processed/phases.parquet` (530 MB, 33,371,282 rows), built by `uv run python -m pipeline.build_phases` in about 5 minutes (four worker processes, one per source file). `--sample N` writes `phases_sample.parquet` instead.
- Grain: one row per game, phase, and power, for every game with `map == "standard"` in the four standard JSONL files (127,621 games). Every power gets a row in every phase, including eliminated powers (empty lists, zero counts). Messages are not included.
- Every phase of a game is present, including the trailing one. `adjudicated == True` marks phases that were played; `adjudicated == False` is the single trailing phase per game: the pending never-adjudicated phase, or the `COMPLETED` marker after a solo. That row carries the final board state (its `n_centers` equals `centers_<power>` in `games.parquet`), and its orders-derived columns are null because about 9% of games have orders sitting there that were never adjudicated. So `phases_from_end == 0` is the end position and `phases_from_end == 1` is the last phase actually played.

| Column | Type | Meaning |
|---|---|---|
| game_id | str | Joins to `games.parquet`. |
| phase_idx | int32 | 0-based position in the game's phase list. |
| phases_from_end | int32 | 0 = trailing phase (end state), counting backwards. |
| phase_name | str | `S1901M` etc., or `COMPLETED`. |
| year | int16 | Game year from the phase name; null for `COMPLETED`. |
| season | str | `S`, `F`, `W`; null for `COMPLETED`. |
| phase_type | str | `M` movement, `R` retreat, `A` adjustment; null for `COMPLETED`. |
| adjudicated | bool | False on the trailing phase only. |
| power | str | `AUSTRIA` ... `TURKEY`. |
| n_centers | int8 | Supply centers owned at the start of the phase. |
| n_units | int8 | Entries in `units`, dislodged units included. |
| centers | list[str] | Province codes owned. |
| units | list[str] | `A PAR`, `F STP/NC`; dislodged units keep the `*` prefix. |
| orders | list[str] | Orders as submitted, engine notation; null when not adjudicated. |
| n_orders | int8 | Length of `orders`; null when not adjudicated. |
| n_failed | int8 | Orders whose unit's result has a non-empty entry (`bounce`, `cut`, `void`, `dislodged`, `no convoy`, `disband` on a non-disband order). Builds (`[""]`) and `WAIVE` never count. Malformed orders under `NO_CHECK` are keyed by their own text and marked `void`; an order with no result entry at all counts as failed. Null when not adjudicated. |
| all_hold | bool | Every order ends in ` H`; null when not adjudicated. |

- Verified: 127,621 distinct games; row count equals 7 x `n_phases` and adjudicated rows equal 7 x (`n_phases` - 1) for every game; final `n_centers` equals `centers_<power>` in `games.parquet` for all 127,621 games; three phases of one game hand-checked field by field against the raw JSON, including `n_failed`.
- Limitations: no `in_scope` filter applied; no messages; `n_failed` is order-level, so a support that was cut and a move that bounced count the same.
- Use in this project: the base table for openings, trajectories, alliance and betrayal labeling, and any end-backwards analysis; always join to `games.parquet` and filter `in_scope`.

## Opening book

- Built by `uv run python -m pipeline.openings` from the three processed DipNet tables. Uses `in_scope`, the three draw-detectable sources, and an adjudicated first phase named `S1901M`.
- `data/processed/openings_observations.parquet`: 260,414 rows, one per game and power across 37,202 games. Contains stable opening IDs, sorted exact orders, source/quality metadata and outcome labels. Reusable for neighbor-opening analysis.
- `data/processed/openings_own.parquet`: 8,417 rows, one per quality cohort, press setting, power and opening ID. Includes counts, frequencies, solo/survival/draw rates, mean SoS, matched baselines, score lift, standard errors, 95% intervals and sparse-sample flags. All 1,873 observed order sets are retained across their applicable cohorts.
- `data/processed/openings_own.md`: common openings for all seven powers, separately by press setting, with tier-1 comparisons. The default report shows ten openings per table ordered by frequency; the Parquet retains all openings.
- `data/processed/openings_manifest.json`: versioned schemas, configuration, input/code/output hashes, cohort/exclusion counts and timings. Artifact consumers should verify output hashes before using a build.
- One otherwise eligible S1902M-start game is excluded, leaving 14,536 tier-1 games within the opening cohort. Structural order validation and join integrity checks fail the build on malformed or unmatched data rather than silently dropping rows.
- Full field definitions, interval assumptions, publication behavior and extension points: [Opening-book data contract](../docs/OPENING_BOOK.md).

### Exact Spring and full-1901 histories

- Built by `uv run python -m pipeline.exact_openings build`, using the same 37,202 games and source/quality rules. Full 1901 includes movements, retreats and Winter adjustments; reaching Spring 1902 validates the end of the window without using 1902 orders as features.
- `opening_exact_observations.parquet`: 520,828 rows, one per `(horizon, game_id, power)`. Country sequence ID, seven-country joint ID, source/quality metadata and outcomes.
- `opening_exact_sequences.parquet`: 63,202 unique country histories with canonical phase/order JSON: 1,873 Spring and 61,329 full-year histories.
- `opening_exact_profiles.parquet`: 72,944 joint profiles mapping each joint ID to seven country sequence IDs in fixed country order. Spring has 35,742 profiles; full 1901 has 37,202, each observed once.
- `opening_exact_own_rates.parquet`: 215,167 own-country aggregate rows across horizons, communication settings and quality cohorts. Includes counts, frequencies, scores, baselines, intervals and sparse flags. Singleton rates and rate intervals are null; counts and observed scores remain available.
- `opening_exact.md` presents all four views. Joint outcomes are aggregated on demand by `lookup_exact`, with no generalized estimate or fallback for unseen patterns.
- `opening_exact_manifest.json` records schemas, hashes, counts, versions and timings. Full field and identity definitions: [Exact-history contract](../docs/EXACT_OPENINGS.md).
- The same build now writes `opening_exact_pair_coverage.parquet` (336 rows across all 21 pairs, two horizons and source/quality cohorts), `opening_exact_pair_examples.parquet` (up to five patterns per pair/cohort by default; currently 1,680 rows), and `opening_exact_pairs.md`. Coverage counts include all patterns before example truncation. Pair examples contain both countries' sequence IDs, event counts, observed rates and mean SoS; singleton rates are null.
- `lookup --context selected --select COUNTRY=SEQUENCE_ID ...` supports any one to seven countries. Every selected sequence must occur in the same game. Other countries may vary; the requested outcome country can be outside the selection. Larger subsets are queried on demand without additional persisted combination tables.

## webDiplomacy finished games (classic)

- Source: the public finished-games listing at `https://webdiplomacy.net/gamelistings.php?gamelistType=Finished&sortCol=processTime&sortType=asc&pagenum=N`, 20 games per page, server-rendered, no login. The site's robots.txt allows general crawling (Content-Signal `ai-train=no`, so this data is for analysis, not model training). The Finished tab excludes bot-only games (`playerTypes <> 'MemberVsBots'`) but includes games where bots filled vacated seats (`fill_with_bots`). Board pages and the API were not used (Cloudflare challenge; API key required).
- Fetched: started 2026-09-11 via `uv run python -m pipeline.scrape_webdip_finished fetch`, one request per 1.5 s plus server latency (about 4 s per page in practice, roughly 7 hours for the full listing). Local: `data/raw/webdip_finished/pages/page_NNNNN.html` (about 200 KB each), `fetch_log.txt` records progress and where a run stopped. The fetch resumes from cached pages but is not incremental; a refresh needs an empty pages directory. When `fetch_log.txt` ends with `last page is N`, run `uv run python -m pipeline.scrape_webdip_finished parse`.
- Status 2026-09-11: PAUSED by decision at 984 of 5,864 pages (the run died once on a server read timeout at page 866 and was restarted; then stopped deliberately). `webdip_finished.parquet` currently holds 18,051 Classic games from those pages, the oldest finished games on the site (sorted by finish time ascending). Parse report on the partial set: 71 duplicate classic IDs (games shifting across page boundaries between the two runs; the parquet is deduped), 7 drawn games with fewer than 2 Drawn members (site data), everything else clean. To resume: `uv run python -m pipeline.scrape_webdip_finished fetch` continues from page 985, then `parse`. Because the listing is sorted ascending by finish time, games that finished after 2026-09-11 append at the end and do not shift the earlier pages.
- Site total at fetch time: 117,277 finished games across all variants on 5,864 pages. Classic is the large majority (pages 1 to 158 were 100 percent Classic; the last page was 8 of 17). Non-Classic panels (two-player `ClassicFvA` and `ClassicGvI`, `AncMed`, `Modern2`, others) are counted for the completeness check and dropped.
- Grain: one row per Classic game in `data/processed/webdip_finished.parquet`, all variants counted but only Classic parsed. Verified on the first 158 pages (3,160 games): 0 duplicate IDs, every game has 7 members, every won game has exactly one Won member, 0 placeholder finish times. Four 2006-era games are recorded by the site as drawn with a single Drawn member (everyone else resigned or was eliminated); that is site data, not a parse error.

| Field | Type | Meaning |
|---|---|---|
| game_id | int | webDiplomacy game ID. Not joinable to DipNet `id`. |
| game_name | str | Player-chosen game name. |
| variant | str | Always `Classic` in the parquet. |
| settings | str | The site's comma-joined options line, e.g. `Classic, No messaging, Anonymous players, Draw-Size Scoring, Hidden draw votes`. The fields below are parsed from it. |
| press_type | str | `Regular`, `No messaging`, `Public messaging only`, or `Rulebook press`. |
| scoring | str or null | `Draw-Size`, `Sum-of-Squares`, `Survivors-Win`, `Points-per-supply-center`, `Unranked`, or null when the line names none. Early games are mostly Survivors-Win. |
| anon | bool | Anonymous players. Names are revealed once a game finishes, so `user_id_*` is still populated. |
| hidden_draw_votes | bool | Draw votes hidden during play. |
| fill_with_bots | bool | Vacated seats were filled by site bots. |
| phase_length | str | Deadline text, e.g. `1 day /phase` or `1 day /phase (M) \| 12 hours /phase (R, B)`. |
| pot | int | Points pot. |
| last_season, last_year | str, int | Game date at finish, e.g. `Autumn`, 1912. |
| finished_unixtime | int or null | Site processTime at finish. Null where the site stores the placeholder 2000000000 (some 2006 to 2010 games). |
| excused_missed_turns | int | Game setting for excused missed turns. |
| status | str | `won` or `drawn`, from the game notice bar. |
| winner_country | str or null | Country with member status Won. |
| n_members | int | Members listed; 7 for Classic. |
| n_won, n_drawn, n_survived, n_defeated, n_resigned, n_left | int | Count of members by final status. |
| n_civil_disorder | int | Rows in the panel's Civil Disorders table: players who left and were replaced. 0 when the table is absent. |
| result_<country> | str | Final member status for each of the seven countries: `Won`, `Drawn`, `Survived`, `Defeated`, `Resigned`, `Left`. |
| sc_<country> | int | Supply centers at finish. 0 for Defeated members, whose count the site does not display. |
| user_id_<country> | int or null | webDiplomacy user ID of the final holder of the seat. |

- Limitations: outcomes only, no orders or board history; not joinable to DipNet by ID; `sc_*` is 0 rather than unknown for Defeated; `finished_unixtime` is null for placeholder games; the listing sorts on processTime without a tiebreaker, so games sharing a timestamp can shift between page requests during the run, which `parse` reports as duplicates (dropped) and as a gap between unique IDs and the site total (not recoverable without a second pass).
- Use in this project: external reference for draw size, solo rate, and civil disorder rate by press type. Importing WebDiplomacy orders is deferred because no API key is available. The local dataset can be inspected without that access.

## playdiplomacy outcomes (jmang00)

- Source: https://github.com/jmang00/diplomacy (scrape of https://www.playdiplomacy.com/games.php?subpage=all_finished, standard map, regular type, finished games, as of 2021-02-28). License: none stated.
- Fetched: 2026-09-10 via `fetch_small_sources.sh`. Local: `data/raw/playdiplomacy/` (2.1 MB): `diplomacy-raw.csv`, `diplomacy-data.csv`, `data-collection.py` (the scraper, kept for provenance).
- Grain: `diplomacy-raw.csv` = one row per finished game. `diplomacy-data.csv` = one row per country, aggregated.
- Verified: 76,798 rows, 76,776 distinct game IDs (22 exact duplicate rows from scraper restarts). Result distribution: solo 44,449; 2-way 12,603; 3-way 12,849; 4-way 4,125; 5-way 1,027; 6-way 1,212; 7-way 533.

`diplomacy-raw.csv` fields:

| Field | Type | Meaning |
|---|---|---|
| Page | int | Search-results page the game was scraped from (1 to 5747). Not meaningful. |
| ID | int | playdiplomacy game ID. Not joinable to any other source. |
| Result | int | 1 = solo win, N >= 2 = N-way draw (max of the country columns). |
| England, France, Italy, Germany, Austria, Turkey, Russia | int | 0 = lost or eliminated; 1 = solo winner; N = shared in an N-way draw. |

`diplomacy-data.csv` fields: `Country`, then counts `Lost`, `Won`, `2-way Draw` ... `7-way Draw`.

- Limitations: outcomes only, no orders, board states, dates, or player identity. 195 rows (0.25%) flag fewer countries than `Result` implies (e.g. Result 3 with two countries marked); treat the country columns as the participation truth and drop or flag those rows. 22 duplicate rows to dedupe on `ID`.
- Verified against the live site 2026-09-11: six games compared row by row match exactly; the player list is always in the fixed order England, France, Italy, Germany, Austria, Turkey, Russia, so country assignment is correct. The high solo rates (58% of games, Austria 11%) are the site population, not a parsing bug: on a current listing page about half of all seats read `surrendered`, and one account can hold several powers in the same game (seen in game 190505). The CSV has no surrender or civil-disorder flags, so this cannot be filtered out.
- Use in this project: cross-platform reference only. Not comparable to DipNet tier 1-3 rates because dropout cannot be removed.

## Betrayal (Niculae et al. 2015)

- Source: https://vene.ro/betrayal/ (`diplomacy_data_1.0.zip`, v1.0, 2016-02-23). Paper: Linguistic Harbingers of Betrayal, ACL 2015. License: ODC-By 1.0 (`LICENSE.txt` kept). Games come from DPjudge and USAK, not webDiplomacy.
- Fetched: 2026-09-10 via `fetch_small_sources.sh`. Local: `data/raw/betrayal/diplomacy_data/diplomacy_data.json` (50.6 MB), plus `README.txt`, `LICENSE.txt`, `imbalance_plot.py`.
- Grain: one record per ally dyad (a friendship sequence). 500 records from 215 distinct games; 250 end in betrayal, 250 matched controls. 3 to 10 seasons per record. 9,660 message feature vectors total.
- Alliance definition used by the authors: at least two consecutive reciprocated supports spanning at least three seasons, no more than five seasons between acts. Betrayal: the friendship is followed by at least two attacks.

| Field | Type | Meaning |
|---|---|---|
| idx | int | Unique record ID (0 to 499). |
| game | int | Game ID within this dataset. Not joinable to any other source. |
| betrayal | bool | True if the friendship ended in betrayal. |
| people | str | Two single-letter country codes (A E F G I R T), e.g. `AT`. Order not documented; do not assume betrayer first. |
| seasons[] | list | One entry per game season in the sequence. |
| seasons[].season | float | Game year with .0 = spring, .5 = fall (1906.5 = fall 1906). |
| seasons[].interaction.victim, .betrayer | str or null | What each side did to the other at end of season: `support`, `attack`, or null. |
| seasons[].messages.victim[], .betrayer[] | list | Feature vectors for messages sent by that side to the other, in random order. |
| ...messages.*[].n_words, n_sentences, n_requests | int | Message length and request count. |
| ...messages.*[].politeness | float | Stanford politeness score of the requests, 0 to 1. |
| ...messages.*[].sentiment.positive, neutral, negative | int | Sentence counts by Stanford sentiment class. |
| ...messages.*[].lexicon_words | dict | Matched words per lexicon: `claim`, `premise`, `allsubj`, `disc_comparison`, `disc_contingency`, `disc_expansion`, `disc_temporal_future`, `disc_temporal_rest`. |
| ...messages.*[].frequent_words | list | Words appearing in at least 50 messages and 5 friendships, random order. |

- Limitations: no message text, no board state, no orders beyond the coarse support/attack flag. Message order within a season is randomized. `people` uses a different code set than every other source.
- Use in this project: source of the behavioral alliance and betrayal definition to replicate on DipNet orders, and a reference for message-level features.

## Deception (Peskov et al. 2020)

- Source: https://github.com/DenisPeskov/2020_acl_diplomacy (original for Hugging Face `community-datasets/diplomacy_detection`, which is blocked on this network). Paper: It Takes Two to Lie, ACL 2020. License: repo `LICENSE` (not fetched).
- Fetched: 2026-09-10 via `fetch_small_sources.sh`. Local: `data/raw/deception/` (5.9 MB): `train.jsonl`, `validation.jsonl`, `test.jsonl`, `README.md`, and `moves/` (342 per-phase JSON files).
- Grain (jsonl): one line per conversation = one pair of players in one game, with parallel per-message lists. 252 conversations (train 189 / validation 21 / test 42), 17,289 messages, 12 games (train games 1-3, 5-10; validation 11; test 4, 12).

Conversation fields (all per-message lists are the same length within a record):

| Field | Type | Meaning |
|---|---|---|
| game_id | int | 1 to 12. Joins to `moves/DiplomacyGame{game_id}_*.json`. Not joinable to other sources. |
| players | list[str] | The two countries in the conversation, lowercase names. |
| speakers[], receivers[] | str | Sender and receiver country per message, lowercase names. |
| messages[] | str | Raw message text. |
| sender_labels[] | bool | True = sender marked the message truthful, False = sender marked it a lie (887 lies). |
| receiver_labels[] | bool or "NOANNOTATION" | Receiver's perception; 1,506 unannotated. |
| game_score[] | str | Sender's supply center count at send time (0 to 18). |
| game_score_delta[] | str | Sender's centers minus receiver's (-18 to 18). |
| absolute_message_index[] | int | Message position within the whole game. |
| relative_message_index[] | int | Position within this conversation. |
| seasons[] | str | `Spring`, `Fall`, `Winter`. |
| years[] | str | 1901 to 1910 in practice. |

Grain (moves): one file per game phase, `DiplomacyGame{game}_{year}_{spring|fall|winter}.json`. 30 phases per game (1901 to 1910) except games 4 and 9 (21 phases, end in 1907). 7,895 orders.

| Field | Type | Meaning |
|---|---|---|
| sc | str | Raw HTML text; parse with `([A-Z][a-z]+) (\d+)` for supply center count per power. |
| territories | dict | Supply center abbreviation (`Par`, `BLA`) to owning power name. |
| orders.{Power}.{Loc} | dict | One order per unit location, keyed by 3-letter abbreviation (title case land, upper case sea). |
| orders.*.*.type | str | `MOVE`, `HOLD`, `SUPPORT`, `CONVOY`, `BUILD`, `DISBAND`. |
| orders.*.*.to, from | str | Destination and supported/convoyed origin. |
| orders.*.*.to_coast, coast | str | Coast qualifier where relevant. |
| orders.*.*.unit_type | str | `A` or `F`, builds only. |
| orders.*.*.retreat | str | Retreat destination after a dislodge. |
| orders.*.*.result | str | `SUCCEEDS` or `FAILS`. |
| orders.*.*.result_reason | str | Adjudicator explanation text. |

- Limitations: 12 games, 83 speakers, one platform, so nothing here supports probability estimates. Unit type is absent from movement orders. Countries are lowercase names in jsonl but title case in moves.
- Use in this project: validation set for any text-based deception signal, not for training. The `moves/` files also make it the only source where messages, lie labels, and full orders exist for the same games.
