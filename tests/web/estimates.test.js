// Shrinkage estimates fitted on training + validation games only.
import assert from "node:assert/strict";
import test from "node:test";
import { estimatedScore } from "../../web/js/estimates.js";
import { explore } from "../../web/js/explore.js";
import { PHASES, buildDataset, exploreState, turnId } from "./fixture.js";

const TRAIN = 0;
const VALIDATION = 1;
const TEST = 2;

test("estimates shrink exact means toward a baseline that excludes test games", () => {
  const turns = { france: Object.fromEntries(PHASES.map((phase, i) => [phase, [[turnId(90 + i), []]]])) };
  turns.france.S1901M = [[turnId(1), ["A PAR - BUR"]], [turnId(2), ["A PAR - PIC"]], [turnId(5), ["A PAR H"]]];
  // Three complete histories that differ only in their Spring movement turn.
  const year = { france: [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0]] };
  const games = [
    { year: { france: 0 }, centers: { france: 18 }, split: TRAIN },
    { year: { france: 0 }, centers: { germany: 18 }, split: TRAIN },
    { year: { france: 1 }, centers: { germany: 18 }, split: VALIDATION },
    { year: { france: 0 }, centers: { france: 18 }, split: TEST },
  ];
  const estimates = { model_id: "fixture", models: { year1901: { tier_1: { strength: 2, fit_games: 3 } } } };
  const dataset = buildDataset({ games, turns, year, estimates });
  const otherTurns = Object.fromEntries(PHASES.slice(1).map((phase, i) => [phase, turnId(91 + i)]));
  const result = explore(dataset, exploreState({ show_estimates: true, phase_selections: { france: otherTurns } }));
  assert.equal(result.score_estimates.status, "available");
  assert.ok(Math.abs(result.score_estimates.baseline_mean_sos - 1 / 3) < 1e-12);
  const [common, rare] = result.choices.items;
  assert.equal(common.n_games, 3);
  assert.equal(common.estimated_score.support, 2);
  assert.ok(Math.abs(common.estimated_score.mean_sos - (1 + 2 / 3) / 4) < 1e-12);
  assert.ok(Math.abs(rare.estimated_score.mean_sos - (2 / 3) / 3) < 1e-12);
  const unseen = estimatedScore(dataset, { horizon: "year1901", qualityGroup: "tier_1", p: 2, sequence: 2 });
  assert.deepEqual(unseen, { mean_sos: 1 / 3, support: 0, source: "baseline_only" });
});
