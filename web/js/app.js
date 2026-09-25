import { loadDataset } from "./dataset.js";
import { explore } from "./explore.js";
import { ScenarioUrl } from "./scenario.js";

const $ = (id) => document.getElementById(id);
const number = new Intl.NumberFormat("en-US");
function percentage(count, total) {
  if (!total) return "—";
  const value = 100 * count / total;
  return value > 0 && value < 0.1 ? "<0.1%" : `${value.toFixed(1)}%`;
}
function signedDifference(value, decimals) {
  const magnitude = Math.abs(value);
  const amount = magnitude > 0 && magnitude < .5 * 10 ** -decimals
    ? `<${(10 ** -decimals).toFixed(decimals)}` : magnitude.toFixed(decimals);
  return `${value > 0 ? "+" : value < 0 ? "−" : ""}${amount}`;
}
function outcomeCount(row, field) {
  // The stored survival count includes solo winners and draw participants.
  if (field === "n_survived_only") return row.n_survived - row.n_solos - row.n_draws;
  if (field === "n_eliminated") return row.n_games - row.n_survived;
  return row[field];
}
const title = (text) => text.charAt(0).toUpperCase() + text.slice(1);
const state = { ...ScenarioUrl.defaults, phase_selections: {} };
const controls = { press: "press_level", quality: "quality_group", sort: "sort_by", "order-search": "search" };
const phaseNames = { S1901M: "Spring 1901", S1901R: "Spring retreats", F1901M: "Fall 1901",
  F1901R: "Fall retreats", W1901A: "Winter adjustments" };
let dataset;
let searchTimer;
let invalidScenario = false;

function syncUrl(mode) {
  if (mode === "none") return;
  const target = location.pathname + ScenarioUrl.serialize(state) + location.hash;
  if (target !== location.pathname + location.search + location.hash) {
    history[mode === "replace" ? "replaceState" : "pushState"](null, "", target);
  }
}

function loadScenario() {
  clearTimeout(searchTimer);
  try {
    const restored = ScenarioUrl.parse(location.search);
    Object.assign(state, restored);
    invalidScenario = false;
    for (const [id, field] of Object.entries(controls)) $(id).value = state[field];
    $("rank-sparse").checked = state.rank_sparse;
    $("show-estimates").checked = state.show_estimates;
    renderSelections([]);
    refresh("none");
  } catch (error) {
    invalidScenario = true;
    renderSelections([]);
    showError(error);
    busy(false);
  }
}

window.addEventListener("popstate", () => dataset ? loadScenario() : start());

function element(tag, text, className) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (className) node.className = className;
  return node;
}

function button(text, action, className) {
  const node = element("button", text, className);
  node.type = "button";
  node.addEventListener("click", action);
  return node;
}

function busy(value) {
  $("workspace").setAttribute("aria-busy", String(value));
  $("activity").textContent = value ? "Updating exact matches." : $("error").hidden ? "Results updated." : "Unable to load results.";
  if (value) {
    $("previous").disabled = true;
    $("next").disabled = true;
  }
}

function renderCountries() {
  $("countries").replaceChildren(...dataset.powers.map((country) => {
    const node = button(title(country), () => browse(country));
    node.dataset.country = country;
    node.dataset.constrained = String(Boolean(state.phase_selections[country]));
    node.setAttribute("aria-pressed", String(state.browse_power === country));
    return node;
  }));
}

function browse(country, phase = state.browse_phase) {
  state.browse_power = country;
  state.browse_phase = phase;
  state.search = "";
  state.offset = 0;
  $("order-search").value = "";
  refresh();
}

function removeSelection(item) {
  const turns = state.phase_selections[item.power];
  if (turns) {
    delete turns[item.phase];
    if (!Object.keys(turns).length) delete state.phase_selections[item.power];
  }
  state.offset = 0;
  refresh();
}

function renderSelections(selected) {
  const chips = selected.flatMap((item) => item.steps.map((step) => ({ power: item.power, phase: step.phase, steps: [step] })));
  $("constraints").replaceChildren(...chips.map((item) => {
    const wrapper = element("div", undefined, "constraint");
    const label = `${title(item.power)} · ${phaseNames[item.phase]}`;
    const edit = button(label, () => browse(item.power, item.phase));
    edit.title = item.steps.map((step) => `${phaseNames[step.phase]}: ${step.orders.join(", ") || "No recorded orders"}`).join("; ");
    const remove = button("×", () => removeSelection(item), "remove-constraint");
    remove.setAttribute("aria-label", `Remove ${label} selection`);
    wrapper.append(edit, remove);
    return wrapper;
  }));
  $("selection-hint").hidden = selected.length > 0;
}

function renderTurns() {
  $("turns").replaceChildren(...Object.entries(phaseNames).map(([phase, label]) => {
    const node = button(label, () => browse(state.browse_power, phase));
    node.dataset.phase = phase;
    node.setAttribute("aria-pressed", String(phase === state.browse_phase));
    node.dataset.constrained = String(Boolean(state.phase_selections[state.browse_power]?.[phase]));
    return node;
  }));
}

function renderEstimateContext(info = { status: "off" }) {
  const node = $("estimate-context");
  node.hidden = info.status === "off";
  const messages = {
    off: "",
    unsupported_press: "Estimates require All press settings; individual press settings have not been tested.",
    other_countries: "Estimates use one country’s orders. Remove selections for other countries to see them.",
    incomplete_year: "To estimate a complete 1901 history, select this country’s orders for the other four turns, including turns with no recorded orders.",
    model_unavailable: "Estimated scores are unavailable for this data snapshot. Historical results are still available.",
  };
  node.textContent = info.status === "available"
    ? `Experimental complete-1901 estimates. Fitted ${title(state.browse_power)} baseline: ${info.baseline_mean_sos.toFixed(3)} (0–1), from ${number.format(info.fit_games)} fitting games. Estimates blend exact matches with this country average.`
    : messages[info.status] || "Estimated scores are unavailable.";
}

const OUTCOME_FIELDS = [["Solo", "n_solos"], ["In draw", "n_draws"], ["Survived", "n_survived_only"], ["Eliminated", "n_eliminated"]];
const OUTCOME_DEFINITIONS = {
  n_eliminated: "Zero supply centers at the end.",
  n_survived_only: "Still held supply centers when another country soloed; excludes Solo and In draw.",
};

function choiceHistory(item) {
  const history = element("span");
  for (const step of item.steps) {
    const phase = element("span", undefined, "phase");
    phase.append(element("span", phaseNames[step.phase] || step.phase, "phase-name"));
    const orders = element("span", undefined, "orders");
    orders.append(...step.orders.map((order) => element("span", order, "order")));
    if (!step.orders.length) orders.append(element("span", "No recorded orders", "order"));
    phase.append(orders);
    history.append(phase);
  }
  return history;
}

function scoreBlock(item, baseline) {
  const score = element("span", undefined, "opening-score");
  score.append(element("strong", item.mean_sos.toFixed(3)), element("span", "historical mean"));
  // Ignore arithmetic noise far below the displayed score precision.
  const delta = Math.abs(item.score_delta) < 1e-12 ? 0 : item.score_delta;
  const relative = baseline > 0 ? signedDifference(100 * delta / baseline, 1) : "N/A";
  const deltaNode = element("span", `${signedDifference(delta, 2)} (${relative}%) vs baseline`, "score-delta");
  deltaNode.classList.toggle("positive", delta > 0);
  deltaNode.classList.toggle("negative", delta < 0);
  deltaNode.title = `Mean ${item.mean_sos.toFixed(6)} − baseline ${baseline.toFixed(6)}. Percentage = difference ÷ baseline × 100 (N/A when baseline is zero). Historical comparison, not a predicted gain.`;
  score.append(deltaNode);
  return score;
}

function estimateBlock(estimate) {
  const block = element("span", undefined, "estimated-score");
  block.append(element("strong", estimate.mean_sos.toFixed(3)), element("span", "estimated score"));
  const prefix = estimate.source === "baseline_only" ? "Baseline only · " : "";
  block.append(element("span", `${prefix}${number.format(estimate.support)} fitting ${estimate.support === 1 ? "match" : "matches"}`, "estimate-support"));
  block.title = "Estimate on the 0–1 score scale. Fitting matches exclude held-out test games. This is not a causal gain from choosing these orders.";
  return block;
}

function countBlock(item, choices, minGames, selected) {
  const count = element("span", undefined, "opening-count");
  count.append(element("strong", percentage(item.n_games, choices.population_games)), element("span", "of eligible games"));
  count.title = `${number.format(item.n_games)} of ${number.format(choices.population_games)} eligible games`;
  count.append(scoreBlock(item, choices.baseline_mean_sos));
  if (item.estimated_score) count.append(estimateBlock(item.estimated_score));
  if (item.n_games < minGames) count.append(element("span", item.n_games === 1 ? "One historical game" : "Sparse sample", "sample-label"));
  if (selected) count.append(element("span", "Selected", "selected-label"));
  return count;
}

function outcomeBlock(item) {
  const outcomes = element("span", undefined, "choice-outcomes");
  outcomes.append(element("span", "Historical outcomes", "outcome-heading"));
  for (const [label, field] of OUTCOME_FIELDS) {
    const metric = element("span", undefined, "choice-outcome");
    const count = outcomeCount(item, field);
    metric.append(element("span", label), element("strong", outcomeValue(count, item.n_games)));
    const definition = OUTCOME_DEFINITIONS[field] ?? "Each game counts in exactly one outcome category.";
    metric.title = `${number.format(count)} of ${number.format(item.n_games)} games with these orders. ${definition}`;
    outcomes.append(metric);
  }
  return outcomes;
}

function choiceCard(item, choices, minGames) {
  const node = button(undefined, () => {
    if ($("workspace").getAttribute("aria-busy") === "true") return;
    state.phase_selections[state.browse_power] = { ...state.phase_selections[state.browse_power], [state.browse_phase]: item.phase_id };
    state.offset = 0;
    refresh();
  }, "opening");
  const selected = state.phase_selections[state.browse_power]?.[state.browse_phase] === item.phase_id;
  node.setAttribute("aria-pressed", String(selected));
  node.dataset.phaseId = item.phase_id;
  node.append(choiceHistory(item), countBlock(item, choices, minGames, selected), outcomeBlock(item));
  return node;
}

function renderChoices(choices, minGames) {
  $("browse-title").textContent = `${title(state.browse_power)} · ${phaseNames[state.browse_phase]}`;
  $("choice-count").textContent = `${number.format(choices.total)} variations`;
  $("choice-context").textContent = `Eligible games match your filters and all other selected countries and turns. Choosing orders replaces only ${title(state.browse_power)}’s ${phaseNames[state.browse_phase]} selection.`;
  $("sparse-sort").hidden = state.sort_by !== "mean_score";
  const order = state.sort_by !== "mean_score" ? "Most frequent first. " : state.rank_sparse
    ? "Highest mean score first, including sparse samples. " : "Highest mean score first within each group: larger samples, then sparse samples. ";
  $("score-context").textContent = `${order}Sparse = fewer than ${number.format(minGames)} games.`;
  $("baseline-context").textContent = choices.baseline_mean_sos === null
    ? "No eligible games for a score baseline."
    : `${title(state.browse_power)} baseline mean: ${choices.baseline_mean_sos.toFixed(3)} (0–1). Score differences describe past results, not predicted gains.`;
  $("baseline-context").title = `Game-weighted mean across all ${number.format(choices.population_games)} eligible games, including each choice and its alternatives. Search, sort and pagination do not change the baseline.`;
  $("choices").replaceChildren(...choices.items.map((item) => choiceCard(item, choices, minGames)));
  $("choices-empty").hidden = choices.items.length > 0;
  $("previous").disabled = choices.offset === 0;
  $("next").disabled = choices.offset + choices.limit >= choices.total;
  $("page-range").textContent = choices.total
    ? `${number.format(choices.offset + 1)}–${number.format(choices.offset + choices.items.length)} of ${number.format(choices.total)}` : "No variations";
}

function outcomeValue(count, total) {
  return total === 1 ? (count ? "Yes" : "No") : percentage(count, total);
}

function outcomeCell(count, total) {
  const cell = element("td", outcomeValue(count, total));
  cell.title = total === 1 ? "Recorded outcome in the one matching game; not an estimated probability"
    : `${number.format(count)} of ${number.format(total)} included games`;
  return cell;
}

function highlightColumn(cells, values) {
  const available = values.filter((value) => value !== null);
  const highest = Math.max(...available);
  const lowest = Math.min(...available);
  if (highest === lowest) return;
  cells.forEach((cell, index) => {
    const value = values[index];
    if (value === null) return;
    const kind = value === highest ? "highest" : value === lowest ? "lowest" : null;
    if (!kind) return;
    cell.classList.add(kind);
    const label = `${kind} in this column (including ties)`;
    cell.title = cell.title ? `${cell.title}; ${label}` : label;
    cell.setAttribute("aria-label", `${cell.textContent}, ${label}`);
  });
}

function renderResults(data) {
  const result = data.result;
  const constrained = data.selected.length > 0;
  $("match-count").textContent = number.format(result.n_matches);
  $("match-count").dataset.count = result.n_matches;
  $("match-label").textContent = constrained ? "exact matching games" : "games under these filters";
  $("cohort-count").textContent = `out of ${number.format(data.cohort_games)} filtered games (${percentage(result.n_matches, data.cohort_games)})`;
  let evidence = "Repeated matches";
  let note = "Outcomes in games matching every selection. Historical results do not predict your next game.";
  if (result.n_matches === 0) {
    evidence = "No exact matches";
    note = "No games match every selection. Remove a country or turn, or change the filters. No matches means no evidence for this combination.";
  } else if (!constrained) {
    evidence = "All filtered games";
    note = "Select orders to narrow these results to matching games.";
  } else if (result.n_matches === 1) {
    evidence = "One historical game";
    note = "Yes/No shows what happened in this game. Mean score is its final score, not a prediction.";
  } else if (result.n_matches < data.min_games) {
    evidence = "Sparse sample";
    note = `Fewer than ${number.format(data.min_games)} matching games. A few games can strongly affect these percentages and scores.`;
  }
  $("evidence").textContent = evidence;
  $("evidence").classList.toggle("sparse", constrained && result.n_matches < data.min_games);
  $("result-note").textContent = note;
  const rows = result.outcomes.map((row) => {
    const tr = element("tr");
    tr.classList.toggle("constrained", Boolean(state.phase_selections[row.power]));
    tr.append(element("td", title(row.power)), outcomeCell(row.n_solos, row.n_games),
      outcomeCell(row.n_draws, row.n_games), outcomeCell(outcomeCount(row, "n_survived_only"), row.n_games),
      outcomeCell(outcomeCount(row, "n_eliminated"), row.n_games),
      element("td", row.mean_sos.toFixed(3)));
    tr.cells[4].classList.add("lower-is-better");
    return tr;
  });
  ["n_solos", "n_draws", "n_survived_only", "n_eliminated", "mean_sos"].forEach((field, index) => {
    const values = result.outcomes.map((row) => field === "mean_sos" ? row[field]
      : row.n_games > 1 ? outcomeCount(row, field) / row.n_games : null);
    highlightColumn(rows.map((row) => row.cells[index + 1]), values);
  });
  $("outcomes").querySelector("tbody").replaceChildren(...rows);
}

function showError(error) {
  $("error-message").textContent = error.message || "Could not load results. Reload the page to try again.";
  $("error").hidden = false;
  $("choices").replaceChildren();
  $("outcomes").querySelector("tbody").replaceChildren();
  $("match-count").textContent = "—";
  $("match-count").dataset.count = "";
  $("cohort-count").textContent = "";
  $("choice-count").textContent = "";
  $("baseline-context").textContent = "";
  $("baseline-context").title = "";
  renderEstimateContext();
  $("page-range").textContent = "";
  $("evidence").textContent = "Unavailable";
  $("result-note").textContent = "Results could not be loaded. Check the error above and try again.";
  $("previous").disabled = true;
  $("next").disabled = true;
}

function refresh(historyMode = "push") {
  clearTimeout(searchTimer);
  if (invalidScenario) {
    busy(false);
    return;
  }
  $("error").hidden = true;
  renderCountries();
  renderTurns();
  try {
    syncUrl(historyMode);
    const data = explore(dataset, state);
    renderSelections(data.selected);
    renderEstimateContext(data.score_estimates);
    renderChoices(data.choices, data.min_games);
    renderResults(data);
  } catch (error) {
    showError(error);
  } finally {
    busy(false);
  }
}

$("filters").addEventListener("submit", (event) => event.preventDefault());
for (const [id, field] of Object.entries(controls).filter(([id]) => id !== "order-search")) {
  $(id).addEventListener("change", () => {
    state[field] = $(id).value;
    state.offset = 0;
    refresh();
  });
}
$("order-search").addEventListener("input", () => {
  state.search = $("order-search").value;
  state.offset = 0;
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => refresh("replace"), 150);
});
$("rank-sparse").addEventListener("change", () => {
  state.rank_sparse = $("rank-sparse").checked;
  state.offset = 0;
  refresh();
});
$("show-estimates").addEventListener("change", () => {
  state.show_estimates = $("show-estimates").checked;
  refresh();
});
function paginate(direction) {
  if ($("workspace").getAttribute("aria-busy") === "true") return;
  state.offset = Math.max(0, state.offset + direction * state.limit);
  refresh();
}
$("previous").addEventListener("click", () => paginate(-1));
$("next").addEventListener("click", () => paginate(1));
$("reset").addEventListener("click", () => {
  state.phase_selections = {};
  state.search = "";
  state.offset = 0;
  $("order-search").value = "";
  refresh();
});

async function start() {
  try {
    $("activity").textContent = "Loading the data snapshot.";
    dataset = await loadDataset();
    const { n_games: games, built_at: builtAt } = dataset.meta;
    $("data-note").textContent = `${number.format(games)} historical games · Snapshot ${builtAt.slice(0, 10)}`;
    loadScenario();
  } catch (error) {
    showError(error);
    busy(false);
  }
}
$("retry").addEventListener("click", () => dataset ? loadScenario() : start());
start();
