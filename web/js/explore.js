// Exact-match queries over full 1901, one turn at a time. No smoothing or similarity: a game
// matches only if every selected country's recorded orders are identical for each selected turn.
import { DRAW, SOLO, SURVIVED, cohort, yearTurn } from "./dataset.js";
import { estimateModel, estimatedScore, modelInfo } from "./estimates.js";

const HORIZON = "year1901";

// Selections become index constraints: {p, turns: [[phase, turn]]}.
function constraints(dataset, state) {
  return Object.entries(state.phase_selections).map(([power, turns]) => ({
    p: dataset.powers.indexOf(power),
    turns: Object.entries(turns).map(([phase, id]) => turnIndex(dataset, power, phase, id)),
  }));
}

function turnIndex(dataset, power, phase, id) {
  const entry = dataset.turnById.get(id);
  if (!entry || dataset.powers[entry.p] !== power || dataset.phases[entry.phase] !== phase) {
    throw new Error("A turn does not belong to its selected country and phase.");
  }
  return [entry.phase, entry.index];
}

function matches(dataset, g, rules) {
  return rules.every((rule) => rule.turns.every(([phase, turn]) => yearTurn(dataset, g, rule.p, phase) === turn));
}

// Alternatives replace only the active choice; all other constraints stay.
function otherConstraints(rules, p, phase) {
  return rules.flatMap((rule) => {
    if (rule.p !== p) return [rule];
    const turns = rule.turns.filter(([f]) => f !== phase);
    return turns.length ? [{ p, turns }] : [];
  });
}

function summarize(dataset, games) {
  const outcomes = dataset.powers.map((power, p) => {
    const row = { power, n_games: games.length, n_solos: 0, n_draws: 0, n_survived: 0, mean_sos: 0 };
    for (const g of games) {
      const slot = g * dataset.width + p;
      const outcome = dataset.outcome[slot];
      row.n_solos += (outcome & SOLO) > 0;
      row.n_draws += (outcome & DRAW) > 0;
      row.n_survived += (outcome & SURVIVED) > 0;
      row.mean_sos += dataset.score[slot];
    }
    row.mean_sos /= games.length;
    return row;
  });
  const status = ["no_exact_matches", "single_historical_game"][games.length] ?? "exact_matches";
  return { status, n_matches: games.length, outcomes: games.length ? outcomes : [] };
}

function estimateStatus(dataset, state, others, p) {
  if (!state.show_estimates) return "off";
  if (state.press_level !== "all") return "unsupported_press";
  if (others.some((rule) => rule.p !== p)) return "other_countries";
  const ownTurns = others.find((rule) => rule.p === p)?.turns.length ?? 0;
  if (ownTurns !== dataset.phases.length - 1) return "incomplete_year";
  return estimateModel(dataset, HORIZON, state.quality_group) ? "available" : "model_unavailable";
}

function groupChoices(dataset, state, games, p) {
  const phase = dataset.phases.indexOf(state.browse_phase);
  const groups = new Map();
  for (const g of games) {
    const slot = g * dataset.width + p;
    const key = yearTurn(dataset, g, p, phase);
    const group = groups.get(key) ?? { key, n: 0, sum: 0, solos: 0, draws: 0, survived: 0, sequence: dataset.year[slot], mixed: false };
    const outcome = dataset.outcome[slot];
    group.n += 1;
    group.sum += dataset.score[slot];
    group.solos += (outcome & SOLO) > 0;
    group.draws += (outcome & DRAW) > 0;
    group.survived += (outcome & SURVIVED) > 0;
    group.mixed ||= group.sequence !== dataset.year[slot];
    groups.set(key, group);
  }
  return [...groups.values()];
}

function describe(dataset, state, p, group) {
  const turn = dataset.turns[p][dataset.phases.indexOf(state.browse_phase)][group.key];
  return { id: turn.id, steps: [{ phase: state.browse_phase, orders: turn.orders }] };
}

function compareBy(fields) {
  return (a, b) => {
    for (const [field, descending] of fields) {
      if (a[field] !== b[field]) return (a[field] < b[field]) === descending ? 1 : -1;
    }
    return 0;
  };
}

function sortChoices(state, choices, minGames) {
  const fields = state.sort_by === "mean_score" ? [["mean", true], ["n", true], ["id", false]] : [["n", true], ["id", false]];
  if (state.sort_by === "mean_score" && !state.rank_sparse) {
    for (const choice of choices) choice.supported = choice.n >= minGames;
    fields.unshift(["supported", true]);
  }
  return choices.sort(compareBy(fields));
}

function searchChoices(state, choices) {
  const needle = state.search.trim().toUpperCase();
  if (!needle) return choices;
  return choices.filter((choice) => choice.steps.some((step) => step.orders.join("\n").toUpperCase().includes(needle)));
}

function choiceItem(dataset, state, choice, context) {
  const item = {
    phase_id: choice.id, n_games: choice.n, mean_sos: choice.mean, n_solos: choice.solos,
    n_draws: choice.draws, n_survived: choice.survived, score_delta: choice.mean - context.baseline, steps: choice.steps,
  };
  if (context.estimates && !choice.mixed) {
    item.estimated_score = estimatedScore(dataset, { horizon: HORIZON, qualityGroup: state.quality_group, p: context.p, sequence: choice.sequence });
  }
  return item;
}

function choiceList(dataset, state, eligible, estimates) {
  const p = dataset.powers.indexOf(state.browse_power);
  const groups = groupChoices(dataset, state, eligible, p);
  const population = groups.reduce((total, group) => total + group.n, 0);
  // Game-weighted over every eligible game, before search or paging; includes the candidate itself.
  const baseline = population ? groups.reduce((total, group) => total + group.sum, 0) / population : null;
  const described = groups.map((group) => ({ ...group, mean: group.sum / group.n, ...describe(dataset, state, p, group) }));
  const sorted = sortChoices(state, searchChoices(state, described), dataset.meta.min_games);
  const context = { baseline, estimates, p };
  return {
    items: sorted.slice(state.offset, state.offset + state.limit).map((choice) => choiceItem(dataset, state, choice, context)),
    total: sorted.length, offset: state.offset, limit: state.limit, population_games: population, baseline_mean_sos: baseline,
  };
}

function selectedItems(dataset, state) {
  return Object.entries(state.phase_selections).map(([power, turns]) => {
    const phases = dataset.phases.filter((phase) => phase in turns);
    const steps = phases.map((phase) => {
      const { p, phase: f, index } = dataset.turnById.get(turns[phase]);
      return { phase, orders: dataset.turns[p][f][index].orders };
    });
    return { power, phase_ids: Object.fromEntries(phases.map((phase) => [phase, turns[phase]])), steps };
  }).sort((a, b) => (a.power < b.power ? -1 : 1));
}

export function explore(dataset, state) {
  const rules = constraints(dataset, state);
  const p = dataset.powers.indexOf(state.browse_power);
  const others = otherConstraints(rules, p, dataset.phases.indexOf(state.browse_phase));
  const games = cohort(dataset, state.press_level, state.quality_group);
  const status = estimateStatus(dataset, state, others, p);
  const eligible = games.filter((g) => matches(dataset, g, others));
  return {
    build_id: dataset.meta.build_id, cohort_games: games.length, min_games: dataset.meta.min_games,
    result: summarize(dataset, games.filter((g) => matches(dataset, g, rules))),
    choices: choiceList(dataset, state, eligible, status === "available"),
    score_estimates: status === "available" ? { status, ...modelInfo(dataset, HORIZON, state.quality_group, p) } : { status },
    selected: selectedItems(dataset, state),
  };
}
