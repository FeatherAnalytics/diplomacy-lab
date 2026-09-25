// Shareable URL contract: defaults stay out of the URL, and bad links fail loudly.
import assert from "node:assert/strict";
import test from "node:test";
import { ScenarioUrl } from "../../web/js/scenario.js";

const turn = "p1_0123456789ab";

test("defaults serialize to an empty query and round-trip selections", () => {
  const defaults = ScenarioUrl.parse("");
  assert.equal(ScenarioUrl.serialize(defaults), "");
  const state = { ...defaults, browse_phase: "F1901M", show_estimates: true, offset: 12, phase_selections: { france: { S1901M: turn } } };
  assert.deepEqual(ScenarioUrl.parse(ScenarioUrl.serialize(state)), state);
});

test("invalid, repeated, unknown or old-version settings are rejected", () => {
  for (const search of ["?v=2", "?v=3&v=3", "?v=3&horizon=spring1901", "?v=3&france.S1901M=p1_short", "?v=3&offset=-1",
    "?v=3&unknown=1", "?v=3&france=o1_0123456789ab", "?v=3&browse_phase=S1902M"]) {
    assert.throws(() => ScenarioUrl.parse(search), /Reset the explorer/, search);
  }
});
