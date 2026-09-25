// Hand-counted two-country opening game.
import assert from "node:assert/strict";
import test from "node:test";
import { matchup } from "../../web/js/game-theory.js";
import { buildDataset, openingId } from "./fixture.js";

const close = (actual, expected) => assert.ok(Math.abs(actual - expected) < 1e-12, `${actual} ≠ ${expected}`);

test("best replies, the pure equilibrium and gains against the historical mix", () => {
  const spring = {
    england: [[openingId(1), ["F LON - ENG"]], [openingId(2), ["F LON - NTH"]]],
    france: [[openingId(3), ["F BRE - MAO"]], [openingId(4), ["F BRE - ENG"]]],
  };
  // [England opening, France opening, England solos, France solos]
  const cells = [[0, 0, 3, 1], [0, 1, 0, 2], [1, 0, 1, 1], [1, 1, 1, 2]];
  const games = cells.flatMap(([e, f, englandSolos, franceSolos]) => [
    ...Array.from({ length: englandSolos }, () => ({ spring: { england: e, france: f }, centers: { england: 18, france: 3 } })),
    ...Array.from({ length: franceSolos }, () => ({ spring: { england: e, france: f }, centers: { england: 3, france: 18 } })),
  ]);
  const result = matchup(buildDataset({ games, spring }),
    { power_a: "england", power_b: "france", top_k: 2, press_level: "all", quality_group: "tier_1", rank_by: "frequency" });
  assert.deepEqual(result.rows.map((row) => row.sequence_id), [openingId(1), openingId(2)]);
  assert.deepEqual(result.cells.map((row) => row.map((cell) => cell.best_for_a)), [[true, false], [false, true]]);
  assert.deepEqual(result.cells.map((row) => row.map((cell) => cell.best_for_b)), [[false, true], [false, true]]);
  assert.deepEqual(result.equilibria, [[1, 1]]);
  const [p, q] = [[6 / 11, 5 / 11], [6 / 11, 5 / 11]];
  const englandRows = [q[0] * 0.75 + q[1] * 0, q[0] * 0.5 + q[1] / 3];
  close(result.mix.a.expected_score, p[0] * englandRows[0] + p[1] * englandRows[1]);
  assert.equal(result.mix.a.best_response, 1);
  const franceColumns = [p[0] * 0.25 + p[1] * 0.5, p[0] * 1 + p[1] * (2 / 3)];
  close(result.mix.b.gain, franceColumns[1] - (q[0] * franceColumns[0] + q[1] * franceColumns[1]));
});
