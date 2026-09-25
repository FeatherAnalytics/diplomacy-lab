import { loadDataset } from "./dataset.js";
import { matchup } from "./game-theory.js";

const $ = (id) => document.getElementById(id);
const number = new Intl.NumberFormat("en-US");
const title = (text) => text.charAt(0).toUpperCase() + text.slice(1);
const code = (power) => power.slice(0, 3).toUpperCase();
const defaults = { power_a: "england", power_b: "france", rank_by: "frequency", top_k: 3, press_level: "all", quality_group: "tier_1" };
const controls = { "power-a": "power_a", "power-b": "power_b", "rank-by": "rank_by", "top-k": "top_k", press: "press_level", quality: "quality_group" };
const state = { ...defaults };
let dataset;

function element(tag, text, className) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (className) node.className = className;
  return node;
}

function readUrl(powers) {
  const params = new URLSearchParams(location.search);
  for (const field of Object.keys(defaults)) {
    const value = params.get(field);
    if (value === null) continue;
    const options = [...$(Object.keys(controls).find((id) => controls[id] === field)).options].map((o) => o.value);
    if (options.includes(value)) state[field] = field === "top_k" ? Number(value) : value;
  }
  if (!powers.includes(state.power_a) || !powers.includes(state.power_b) || state.power_a === state.power_b) {
    state.power_a = defaults.power_a;
    state.power_b = defaults.power_b;
  }
}

function writeUrl() {
  const params = new URLSearchParams();
  for (const [field, value] of Object.entries(state)) if (value !== defaults[field]) params.set(field, value);
  const target = location.pathname + (params.size ? `?${params}` : "");
  if (target !== location.pathname + location.search) history.replaceState(null, "", target);
}

function percent(count, total) {
  return total ? `${(100 * count / total).toFixed(1)}%` : "—";
}

function orders(strategy) {
  return strategy.steps.flatMap((step) => step.orders);
}

function openingLabel(strategy, total) {
  const node = element("span", undefined, "matrix-opening");
  node.append(...orders(strategy).map((order) => element("span", order, "order")));
  const share = element("span", `${percent(strategy.n_games, total)} of games`, "eyebrow share");
  share.title = `${number.format(strategy.n_games)} of ${number.format(total)} games in this table`;
  node.append(share);
  return node;
}

function payoffLine(power, value, best, clear) {
  const line = element("span", undefined, "payoff");
  line.append(element("span", code(power), "eyebrow"), element("strong", value === null ? "—" : value.toFixed(3)));
  if (best) {
    const mark = element("span", clear ? "▲" : "△", "best-mark");
    mark.title = clear ? `${title(power)}'s best reply` : `${title(power)}'s best reply, but within noise of the runner-up`;
    line.append(mark);
  }
  return line;
}

function renderCell(cell, data) {
  const [a, b] = data.powers;
  const td = element("td");
  td.classList.toggle("nash", Boolean(cell.nash));
  td.append(payoffLine(a, cell.mean_a, cell.best_for_a, cell.clear_for_a), payoffLine(b, cell.mean_b, cell.best_for_b, cell.clear_for_b));
  const share = element("span", `${percent(cell.n_games, data.covered_games)} of games`, "eyebrow cell-games");
  share.title = `${number.format(cell.n_games)} of ${number.format(data.covered_games)} games in this table`;
  td.append(share);
  if (cell.nash) td.append(element("span", "Equilibrium", "eyebrow cell-tag"));
  else if (cell.n_games < data.min_games) td.append(element("span", cell.n_games ? "Sparse" : "No games", "eyebrow cell-tag"));
  return td;
}

function renderMatrix(data) {
  const [a, b] = data.powers;
  const head = element("tr");
  head.append(element("td", undefined, "matrix-corner"));
  $("column-country").textContent = `${title(b)} →`;
  $("row-country").textContent = `← ${title(a)}`;
  $("matrix-caption").textContent = `${title(a)} openings by row, ${title(b)} openings by column: mean final scores for each pair`;
  for (const column of data.columns) {
    const th = element("th");
    th.scope = "col";
    th.append(openingLabel(column, data.covered_games));
    head.append(th);
  }
  $("matrix").tHead.replaceChildren(head);
  $("matrix").tBodies[0].replaceChildren(...data.rows.map((row, i) => {
    const tr = element("tr");
    const th = element("th");
    th.scope = "row";
    th.append(openingLabel(row, data.covered_games));
    tr.append(th, ...data.cells[i].map((cell) => renderCell(cell, data)));
    return tr;
  }));
  $("matrix-size").textContent = `${data.rows.length} × ${data.columns.length}`;
}

function mixCard(power, opponent, mix, strategies) {
  const card = element("div", undefined, "mix-card");
  card.append(element("p", title(power), "eyebrow"));
  const score = element("p", undefined, "mix-score");
  score.append(element("strong", mix.expected_score.toFixed(3)), element("span", " expected score from the historical mix"));
  const reply = strategies[mix.best_response];
  const best = element("p", `Best reply to ${title(opponent)}’s mix: ${orders(reply).join(", ")}`, "mix-reply");
  const gain = element("p", undefined, "mix-gain");
  gain.append(element("strong", `+${mix.gain.toFixed(3)}`), element("span", ` (${mix.best_response_score.toFixed(3)} if always played)`));
  card.append(score, best, gain);
  return card;
}

function renderSummary(data) {
  const [a, b] = data.powers;
  $("coverage").textContent = `${number.format(data.covered_games)} of ${number.format(data.pair_games)} filtered games `
    + `(${(100 * data.covered_games / data.pair_games).toFixed(1)}%) had both countries play one of these openings.`;
  $("sparse-threshold").textContent = number.format(data.min_games);
  $("score-threshold").textContent = number.format(data.min_games);
  const short = [[a, data.rows.length], [b, data.columns.length]].filter(([, n]) => n < data.top_k);
  if (short.length) {
    $("coverage").textContent += ` Only ${short.map(([power, n]) => `${n} ${title(power)}`).join(" and ")} opening${short.length === 1 && short[0][1] === 1 ? "" : "s"} met the ${number.format(data.min_games)}-game minimum.`;
  }
  if (!data.complete) {
    $("mix-cards").replaceChildren(element("p", "At least one pair of openings was never played together under these filters, so best replies and equilibria are not computed. Choose fewer openings or broader filters.", "empty"));
    $("equilibria").replaceChildren();
    return;
  }
  $("mix-cards").replaceChildren(mixCard(a, b, data.mix.a, data.rows), mixCard(b, a, data.mix.b, data.columns));
  const items = data.equilibria.map(([i, j]) => element("li", `${title(a)}: ${orders(data.rows[i]).join(", ")} · ${title(b)}: ${orders(data.columns[j]).join(", ")}`));
  $("equilibria").replaceChildren(element("p", items.length ? `Pure equilibria in this table: ${items.length}` : "No pure equilibrium in this table: at least one country always has a better reply.", "eyebrow"));
  if (items.length) {
    const list = element("ul");
    list.append(...items);
    $("equilibria").append(list);
  }
}

function refresh() {
  writeUrl();
  $("error").hidden = true;
  try {
    const data = matchup(dataset, state);
    renderSummary(data);
    renderMatrix(data);
    $("activity").textContent = "Matchup updated.";
  } catch (error) {
    $("error-message").textContent = error.message;
    $("error").hidden = false;
  }
  $("matchup").setAttribute("aria-busy", "false");
}

function bindControls() {
  for (const [id, field] of Object.entries(controls)) {
    $(id).value = String(state[field]);
    $(id).addEventListener("change", () => {
      const value = field === "top_k" ? Number($(id).value) : $(id).value;
      const other = { power_a: "power_b", power_b: "power_a" }[field];
      if (other && value === state[other]) {
        state[other] = state[field];
        $(Object.keys(controls).find((key) => controls[key] === other)).value = state[other];
      }
      state[field] = value;
      refresh();
    });
  }
}

async function start() {
  try {
    $("activity").textContent = "Loading the data snapshot.";
    dataset = await loadDataset();
    for (const id of ["power-a", "power-b"]) {
      $(id).replaceChildren(...dataset.powers.map((power) => new Option(title(power), power)));
    }
    const { n_games: games, built_at: builtAt } = dataset.meta;
    $("data-note").textContent = `${number.format(games)} historical games · Snapshot ${builtAt.slice(0, 10)}`;
    readUrl(dataset.powers);
    bindControls();
    refresh();
  } catch (error) {
    $("error-message").textContent = error.message;
    $("error").hidden = false;
  }
}

$("matchup-filters").addEventListener("submit", (event) => event.preventDefault());
$("retry").addEventListener("click", () => (dataset ? refresh() : start()));
start();
