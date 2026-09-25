# Analysis ideas

Backlog of analyses and the data each one needs. Ordered roughly easiest first within each section. Everything filters on `in_scope` in `games.parquet` (standard map, tier 1-3, solo or draw-vote ending, standard build rules, ended by 1930). Nothing is deleted from the tables. For expected-ending questions, also restrict to the three files where draws are detectable; see the opening book section.

Effort: S = games.parquet only, a query. M = needs a phase-level pass over the JSONL. L = needs modeling or a new data source.

## Descriptive, from games.parquet

- **Country win and survival rates** by press level and tier. Solo share per power, final center distribution, elimination rate. Cross-check against `data/raw/playdiplomacy/diplomacy-data.csv` for a second platform. Effort S. Done: `data/processed/outcome_rates.md`, built by `pipeline/outcome_rates.py`, which also writes per-game per-power sum-of-squares scores to `game_outcomes.parquet`. The report uses the three draw-detectable sources and includes a tier-1 sensitivity table; the score parquet retains all in-scope games.
- **Game length** distribution by press level, tier, and outcome. Where solos happen (year), how long non-solo games run before stopping. Effort S.
- **Dropout profile**: which powers drop out most, in which year, at what center count. Effort S.
- **Does press change outcomes**: solo rate, game length, and center concentration in no_press vs press vs press_with_msgs, controlling for tier. Effort S.

## Descriptive, needs a phase table

- **Phase-level table**: one row per game, phase, power with centers, unit count, orders, and result flags. Done: `pipeline/build_phases.py` and `data/processed/phases.parquet`.
- **Opening book**: own-country, all-country and selected-country exact matches for Spring and full 1901 are implemented in `pipeline/exact_openings.py`. Reports: `data/processed/opening_exact.md` and `opening_exact_pairs.md`. The original Spring report remains available.
- **Center trajectories**: median and spread of center count by year per power, split by eventual outcome. Effort M.
- **Order mix over time**: share of holds, moves, supports, convoys by year and by power. Effort M.

## Opening book, expanded

Question: for each power's first-turn order set, how common is it and what ending does it lead to? Ending = sum-of-squares score from `game_outcomes.parquet` (0 to 1, sums to 1 per game, 18+ centers = 1). All of this is one join of `phases.parquet` at `phase_idx == 0` and `phase_name == "S1901M"` to `game_outcomes.parquet`, then group-bys. Check the phase name explicitly: one in-scope game starts at S1902M. Effort S once the phase table exists (it does).

Data rule: use only the three files where draws are detectable (no_press, press_with_msgs, public_press; about 37,000 in-scope games). The press_without_msgs in-scope set is 99.8 percent solos, so expected endings from it are conditional on a solo having happened.

Opening key: the power's S1901M order list, sorted, with coasts kept. Treat as an unordered set.

Three levels, in order:

1. **Own opening only.** Per power and opening: n games, share of that power's games, solo rate, mean SoS, standard error or bootstrap interval, lift vs the power's baseline mean SoS. A few hundred legal sets per power, a handful used heavily; the top openings have thousands of games. Flag rather than rank anything under about 200 games.
2. **Own opening given selected countries' openings.** Implemented: any subset of countries can be required to match exactly, with outcomes for any target country. All 21 pairs have coverage summaries and bounded common-pattern examples for both Spring and full 1901, separately by communication setting and quality cohort. See `data/processed/opening_exact_pairs.md`. Larger subsets remain on-demand queries. Pair matrices could be a future presentation; equilibrium or best-response analysis remains separate speculative work because descriptive conditional outcomes are not causal payoffs.
3. **Own opening given everyone else.** Exact matching is implemented for Spring and full 1901, returning each country's observed outcomes and the matching game count. Spring has 35,742 joint profiles across 37,202 games (34,885 profiles occur once; the largest has 18 matches). Every full-1901 joint history is unique. Singletons are presented as individual historical outcomes, and unseen patterns return no exact matches. The explorer has no similarity search, smoothing or fallback model. A separate offline shrinkage experiment is documented below.

Every view should explain its sample and the limits of interpretation. Results are descriptive, unknown endings are excluded, and sparse samples are labeled. Reports already include uncertainty intervals; suitable intervals for the explorer remain a follow-up.

Implemented level 1: `data/processed/openings_own.parquet` and `.md` (all seven powers), reusable `openings_observations.parquet`, and `openings_manifest.json`. CLI: `pipeline/openings.py`; selection, statistics and rendering live in separate modules under `pipeline/analysis/`. See `docs/OPENING_BOOK.md` for the versioned data contract. Pair coverage and common examples are in `opening_exact_pair_coverage.parquet` and `opening_exact_pair_examples.parquet`; all exact combinations remain queryable from the observation table.

Implemented extension: own-country full 1901 plus both all-country contexts, with normalized catalogs, compact observations, precomputed own-country aggregates and an exact JSON lookup. Build/report CLI: `pipeline/exact_openings.py`; contract: `docs/EXACT_OPENINGS.md`. A full-year history records adaptive decisions through Winter, not a precommitted Spring strategy. The website can reuse these artifacts and query functions without scanning raw game histories.

## Explorer and dashboard

Implemented in the explorer: exact country selections, Spring/full-1901
windows, quality-tier explanations, opening frequency and mean final SoS on each
choice, sorting by frequency or mean score, shareable scenario URLs, and persistent
selected/filtered sample counts and percentages. Defaults are All press settings
and Tier 1 only. Scores and frequencies share the
eligible population under the other selected countries. Sparse samples remain
visible and labeled; score order is descriptive, not a recommendation. Mean-score
sorting now puts non-sparse choices first, with an off-by-default toggle to allow
sparse choices to rank at the top. Singleton outcomes show recorded Yes/No values.
Full 1901 now supports exact, independently removable selections for each turn,
including empty-order turns, with immediate filtering and URL persistence.
Automatic Spring-to-full-year carry-forward remains off; an explicit optional
carry-forward action could be considered later.
Choice cards now include mutually exclusive Solo, In draw, Survived and Eliminated outcomes, plus observed score
differences versus the browsing country's game-weighted eligible baseline. The
comparison keeps all other selected countries/turns, includes the candidate in
the baseline, and is explicitly descriptive rather than causal.

- **Opening-playbook follow-ups:** the core exact-match analysis is implemented.
  Prioritize clearer sample coverage and uncertainty before building a map.
  Conditional baseline score comparisons are now in the explorer. The offline
  own-opening reports already have uncertainty intervals; exposing intervals in
  the explorer still needs treatment of the overlapping conditional samples.
  A popularity-versus-outcome dashboard is a useful next presentation. Modeled
  estimates are now an optional explorer feature for the evaluated own-country contexts.
- **Expected-score benchmark (completed offline):** country baseline versus raw
  exact means versus validation-tuned shrinkage, with whole-game train/validation/
  test splits. Covers own, all 21 pair and all-country contexts for Spring and
  Full 1901. Primary Tier 1 results: about 1.0% lower test MSE than baseline for
  own Spring and 2.4% for own full-year histories. Raw exact averages become
  unstable in sparse groups; all-country full-year test coverage is zero.
  [Report](data/processed/score_benchmark/report.md) and
  [methodology](docs/SCORE_BENCHMARK.md). An off-by-default estimated-score toggle
  now serves own-country models with All press settings and either quality filter.
  Full 1901 requires all five turns; partial-year and other-country constraints
  receive no estimate. Held-out test games remain excluded from fitting. Any
  follow-up tuning should preserve the held-out test set and avoid treating it
  as fresh validation data.
- **External game import (deferred):** WebDiplomacy import needs API access; no
  API key is available. Loading a game already in the local dataset would be a
  separate feature and would not require external access.
- **Opening move map (deferred, optional):** a reusable standard-map SVG with a separate
  order overlay. Start with Spring 1901 and fixed starting positions; show issued
  moves, supports, holds and convoys from existing `steps` in the explorer engine.
  Preserve coast distinctions and label attempted orders, not successful moves.
  No raw-game reads or new statistical pipeline are needed for this view. Map
  geometry/coordinates and its license still need to be chosen; none is bundled.
  Later add phase selection for full 1901. Actual board replay is a separate
  feature requiring a specific game's positions and adjudication, since matching
  one country's orders does not determine the board state.
- **Opening dashboard:** reuse the same exact-match filters and definitions.
  Start with a frequency-versus-mean-score scatter plot to show popularity and
  historical outcome together; a table supplies exact values and order details.
  Sparse observations must be visibly distinguished, with an optional minimum
  sample filter and a clear indication of the population it removes. Use a
  scatter plot here because a sorted bar chart would hide the relationship
  between the two quantities.
- **Country and quality comparisons:** aligned dot plots for each country's
  solo rate, draw participation, survival and mean score; compare Tier 1 with
  Tiers 1–3 under otherwise identical filters. Use the explorer's four exclusive
  outcomes: Solo, In draw, Survived and Eliminated. These can form a part-to-whole
  chart; mean score is a separate measure. Use consistent scales within each
  metric and show each comparison's denominator.
- **Coverage dashboard:** show the share of games represented by repeated
  openings versus unique histories as more countries or all of 1901 are required.
  Reuse pair-coverage artifacts and on-demand exact queries; cache by snapshot
  and filters. A shared aggregation layer should supply tables and charts, with
  bounded payloads rather than browser-side raw-game scans. No generalized
  estimates or predictive models are part of these views.

## Alliances and betrayal, from orders only

- **Alliance labeler**: replicate the Niculae et al. definition on orders. Reciprocated supports across three or more seasons with no more than five seasons between acts. Output one row per ally pair per season. Effort M.
- **Betrayal labeler**: an alliance followed by two or more attacks. Attack = move into or support against the ally's unit or center. Effort M, depends on alliance labeler.
- **Betrayal base rates**: how often alliances end in a stab, by press level, by year, by relative strength of the pair. Effort S once labels exist.
- **Stab timing**: hazard of a stab by alliance age and by board state. Effort L.
- **Stab predictor**: P(stab next season | board features). Effort L.

## Utility

- **Which scoring rule do humans act like they maximize**: compare draw-size scoring vs sum-of-squares as explanations for late-game behavior, split gunboat vs press, leader vs trailer. Effort L. Blocked by draw detection.
- **Value function**: V(board, power) = expected score, fit on tier 1 and 2 games. Effort L. Blocked by draw detection for anything beyond solo probability.
- **Solo probability only**: P(solo | board, power) is fittable now since solos are marked. Effort L but unblocked.

## Game theory

- **Opening matchups (implemented):** the site's Matchups page (`web/matchup.html`) treats two countries' top 2–5 Spring 1901 openings as a bimatrix game with observed mean SoS payoffs, marks best replies (flagging ones within an approximate 95% noise band), pure equilibria, and each side's gain from best-replying to the other's historical mix. Payoffs are descriptive, not causal. Follow-ups: mixed equilibria via support enumeration, shrinkage payoffs for sparse 5×5 cells, and a three-country view.
- **Local situation games**: pick a recurring board pattern, pull all historical instances, build the payoff matrix from empirical outcomes, compare equilibrium to what humans played. Effort L, needs value function.
- **Regret matching over sampled order sets**, Meta SearchBot style, at hobby scale. Effort L.

## Paths

- **Center-set Markov chain**: P(solo | power holds set of centers by year Y). Mine transitions from the phase table. Effort M.
- **Live re-evaluation**: evaluate a board mid-game against the chain or value function. Effort L.

## Messages, press_with_msgs (30,423 games)

- **Message volume vs outcome**: messages per phase per pair, relation to alliance and stab labels. Effort M.
- **Deception validation**: any text-based signal gets checked against the 12 Deception games, which have lie labels and full orders in `data/raw/deception/moves/`. Effort L.

## Data gaps to close

- **Unknown endings**: excluded by decision via `in_scope` (only solo and draw-vote endings are analyzed). That drops about 54,000 games, mostly from press_without_msgs, where almost no game shows a draw vote. Recovering them means the webDiplomacy API, which needs admin access and a fresh scrape since dataset IDs do not map to webDip IDs.
- **Outlier games (handled)**: the raw standard-map data reaches year 2000; the scope filter excludes games ending after 1930.
- **NMR below the threshold**: a player missing one or two turns is invisible. Accept or lower the dropout streak.
