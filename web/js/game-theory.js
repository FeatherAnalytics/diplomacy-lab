// Two-country opening games whose payoffs are observed mean scores for each exact pair.
// Payoffs are descriptive: the other five countries and player skill vary across cells.
import { cohort } from "./dataset.js";

const Z_95 = 1.959963984540054;
const TIE = 1e-12;

function pairGames(dataset, pa, pb, games) {
  return games.map((g) => {
    const base = g * dataset.width;
    return { a: dataset.spring[base + pa], b: dataset.spring[base + pb], scoreA: dataset.score[base + pa], scoreB: dataset.score[base + pb] };
  });
}

function topOpenings(dataset, pair, side, options) {
  const p = side === "a" ? options.pa : options.pb;
  const stats = new Map();
  for (const game of pair) {
    const entry = stats.get(game[side]) ?? { index: game[side], n: 0, sum: 0 };
    entry.n += 1;
    entry.sum += side === "a" ? game.scoreA : game.scoreB;
    stats.set(game[side], entry);
  }
  let ranked = [...stats.values()].map((entry) => ({ ...entry, mean: entry.sum / entry.n, id: dataset.springCatalog[p][entry.index].id }));
  if (options.rankBy === "mean_score") ranked = ranked.filter((entry) => entry.n >= options.minGames);
  const byId = (x, y) => (x.id < y.id ? -1 : 1);
  const order = options.rankBy === "mean_score"
    ? (x, y) => y.mean - x.mean || y.n - x.n || byId(x, y)
    : (x, y) => y.n - x.n || byId(x, y);
  return ranked.sort(order).slice(0, options.topK).map((entry) => entry.index);
}

function stats(values) {
  const n = values.length;
  if (!n) return { mean: null, se: null };
  const mean = values.reduce((total, v) => total + v, 0) / n;
  if (n < 2) return { mean, se: null };
  const variance = values.reduce((total, v) => total + (v - mean) ** 2, 0) / (n - 1);
  return { mean, se: Math.sqrt(variance) / Math.sqrt(n) };
}

function payoffCells(subgame, rows, columns) {
  return rows.map((a) => columns.map((b) => {
    const games = subgame.filter((game) => game.a === a && game.b === b);
    const sa = stats(games.map((game) => game.scoreA));
    const sb = stats(games.map((game) => game.scoreB));
    return { n_games: games.length, mean_a: sa.mean, mean_b: sb.mean, se_a: sa.se, se_b: sb.se };
  }));
}

// A unique best whose lead over the runner-up exceeds an approximate 95% noise band.
function clearlyBest(values, errors, best) {
  if (best.length !== 1 || values.length < 2) return false;
  const leader = best[0];
  const runner = values.reduce((top, value, i) => (i !== leader && (top < 0 || value > values[top]) ? i : top), -1);
  if (errors[leader] === null || errors[runner] === null) return false;
  return values[leader] - values[runner] > Z_95 * Math.hypot(errors[leader], errors[runner]);
}

function markLine(line, side) {
  const values = line.map((cell) => cell[`mean_${side}`]);
  const top = Math.max(...values);
  const best = values.flatMap((value, i) => (value >= top - TIE ? [i] : []));
  const clear = clearlyBest(values, line.map((cell) => cell[`se_${side}`]), best);
  line.forEach((cell, i) => {
    cell[`best_for_${side}`] = best.includes(i);
    cell[`clear_for_${side}`] = clear && best.includes(i);
  });
}

// Country A picks the row, so its best replies are per column; B's are per row.
function markBestResponses(cells) {
  cells[0].forEach((_, j) => markLine(cells.map((row) => row[j]), "a"));
  cells.forEach((row) => markLine(row, "b"));
  const equilibria = [];
  cells.forEach((row, i) => row.forEach((cell, j) => {
    cell.nash = cell.best_for_a && cell.best_for_b;
    if (cell.nash) equilibria.push([i, j]);
  }));
  return equilibria;
}

function regret(values, mix) {
  const current = values.reduce((total, value, i) => total + mix[i] * value, 0);
  const best = values.reduce((top, value, i) => (value > values[top] ? i : top), 0);
  return { expected_score: current, expected_by_choice: values, best_response: best, best_response_score: values[best], gain: values[best] - current };
}

// Each country's gain from always playing one opening while the other keeps its historical mix.
function historicalMix(cells, p, q) {
  const rows = cells.map((row) => row.reduce((total, cell, j) => total + q[j] * cell.mean_a, 0));
  const columns = q.map((_, j) => cells.reduce((total, row, i) => total + p[i] * row[j].mean_b, 0));
  return { a: regret(rows, p), b: regret(columns, q) };
}

function strategies(dataset, subgame, side, indexes, p) {
  return indexes.map((index) => {
    const n = subgame.filter((game) => game[side] === index).length;
    const opening = dataset.springCatalog[p][index];
    return { sequence_id: opening.id, n_games: n, share: subgame.length ? n / subgame.length : 0, steps: [{ phase: "S1901M", orders: opening.orders }] };
  });
}

export function matchup(dataset, state) {
  const [pa, pb] = [state.power_a, state.power_b].map((power) => dataset.powers.indexOf(power));
  if (pa < 0 || pb < 0 || pa === pb) throw new Error("Choose two different countries.");
  const options = { pa, pb, topK: state.top_k, rankBy: state.rank_by, minGames: dataset.meta.min_games };
  const pair = pairGames(dataset, pa, pb, cohort(dataset, state.press_level, state.quality_group));
  const rowIds = topOpenings(dataset, pair, "a", options);
  const columnIds = topOpenings(dataset, pair, "b", options);
  const subgame = pair.filter((game) => rowIds.includes(game.a) && columnIds.includes(game.b));
  const cells = payoffCells(subgame, rowIds, columnIds);
  const rows = strategies(dataset, subgame, "a", rowIds, pa);
  const columns = strategies(dataset, subgame, "b", columnIds, pb);
  const complete = cells.length > 0 && cells[0].length > 0 && cells.every((row) => row.every((cell) => cell.n_games > 0));
  return {
    build_id: dataset.meta.build_id, min_games: dataset.meta.min_games, powers: [state.power_a, state.power_b],
    top_k: state.top_k, rank_by: state.rank_by, pair_games: pair.length, covered_games: subgame.length,
    rows, columns, cells, complete,
    equilibria: complete ? markBestResponses(cells) : [],
    mix: complete ? historicalMix(cells, rows.map((r) => r.share), columns.map((c) => c.share)) : null,
  };
}
