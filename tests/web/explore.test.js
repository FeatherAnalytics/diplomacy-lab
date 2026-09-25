// Hand-counted explorer queries.
import assert from "node:assert/strict";
import test from "node:test";
import { explore } from "../../web/js/explore.js";
import { PHASES, buildDataset, exploreState, turnId } from "./fixture.js";

const turn = (id, orders) => [turnId(id), orders];
const emptyTurns = (id) => Object.fromEntries(PHASES.map((phase) => [phase, [turn(id, [])]]));
const turns = { france: emptyTurns(90), germany: emptyTurns(91) };
turns.france.S1901M = [turn(1, ["A PAR - BUR"]), turn(2, ["A PAR - PIC"])];
turns.germany.S1901M = [turn(3, ["A MUN - BUR"]), turn(4, ["A MUN - RUH"])];
// Each country's full-year histories: index 0 opens with the first Spring turn, index 1 with the second.
const year = { france: [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0]], germany: [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0]] };
const games = [
  { year: { france: 0, germany: 0 }, centers: { france: 18, germany: 4 } },
  { year: { france: 0, germany: 1 }, centers: { france: 5, germany: 5 }, draw: true },
  { year: { france: 1, germany: 0 }, centers: { france: 2, germany: 18 } },
  { year: { france: 0, germany: 0 }, centers: { france: 3, germany: 3, austria: 6 }, draw: true },
];

test("selections intersect within games and alternatives keep other countries fixed", () => {
  const state = exploreState({ phase_selections: { france: { S1901M: turnId(1) } }, browse_power: "germany" });
  const result = explore(buildDataset({ games, turns, year }), state);
  assert.equal(result.cohort_games, 4);
  assert.equal(result.result.n_matches, 3);
  const france = result.result.outcomes.find((row) => row.power === "france");
  assert.deepEqual([france.n_solos, france.n_draws, france.n_survived], [1, 2, 3]);
  assert.ok(Math.abs(france.mean_sos - (1 + 0.5 + 9 / 54) / 3) < 1e-12);
  const [first, second] = result.choices.items;
  assert.deepEqual([first.phase_id, first.n_games, second.phase_id, second.n_games], [turnId(3), 2, turnId(4), 1]);
  assert.ok(Math.abs(result.choices.baseline_mean_sos - (0 + 0.5 + 9 / 54) / 3) < 1e-12);
  assert.ok(Math.abs(first.score_delta - ((0 + 9 / 54) / 2 - result.choices.baseline_mean_sos)) < 1e-12);
  assert.deepEqual(result.selected, [{ power: "france", phase_ids: { S1901M: turnId(1) }, steps: [{ phase: "S1901M", orders: ["A PAR - BUR"] }] }]);
});

test("unknown or mismatched turns are rejected", () => {
  const dataset = buildDataset({ games, turns, year });
  assert.throws(() => explore(dataset, exploreState({ phase_selections: { france: { S1901M: turnId(3) } } })), /does not belong/);
});

test("full-1901 turns constrain only the selected turn", () => {
  const fallTurns = { france: emptyTurns(90) };
  fallTurns.france.S1901M = [turn(1, ["A PAR - BUR"]), turn(2, ["A PAR - PIC"])];
  fallTurns.france.F1901M = [turn(3, ["A BUR - BEL"]), turn(4, ["A BUR H"])];
  const fallYear = { france: [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0]] };
  const dataset = buildDataset({ games: [0, 1, 2].map((i) => ({ year: { france: i }, centers: { france: 3 } })), turns: fallTurns, year: fallYear });
  const state = exploreState({ browse_phase: "F1901M", phase_selections: { france: { S1901M: turnId(1) } }, show_estimates: true });
  const fall = explore(dataset, state);
  assert.equal(fall.result.n_matches, 2);
  assert.deepEqual(fall.choices.items.map((item) => [item.phase_id, item.n_games]), [[turnId(3), 1], [turnId(4), 1]]);
  assert.equal(fall.score_estimates.status, "incomplete_year");
  const springTurn = explore(dataset, { ...state, browse_phase: "S1901M" });
  assert.deepEqual(springTurn.choices.items.map((item) => [item.phase_id, item.n_games]), [[turnId(1), 2], [turnId(2), 1]]);
});
