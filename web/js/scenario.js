// Shareable explorer URLs. Version 3 defaults and ID formats are part of the sharing
// contract: bump VERSION if either changes so saved links never silently change meaning.
const VERSION = "3";
const RESET = "Reset the explorer to start again.";
const defaults = Object.freeze({ press_level: "all", quality_group: "tier_1",
  browse_power: "france", browse_phase: "S1901M", search: "", sort_by: "frequency", rank_sparse: false, show_estimates: false, offset: 0, limit: 12 });
const powers = ["austria", "england", "france", "germany", "italy", "russia", "turkey"];
const phases = ["S1901M", "S1901R", "F1901M", "F1901R", "W1901A"];
const fields = Object.keys(defaults).filter((field) => field !== "limit");
const options = {
  press_level: ["all", "no_press", "press_with_msgs", "public_press"],
  quality_group: ["tier_1", "tiers_1_3"], browse_power: powers, sort_by: ["frequency", "mean_score"], browse_phase: phases,
};
const booleans = ["rank_sparse", "show_estimates"];
const TURN_ID = /^p1_[0-9a-f]{12}$/;

function fail(message) {
  throw new Error(`${message} ${RESET}`);
}

function turnKey(key) {
  const [power, phase, extra] = key.split(".");
  return extra === undefined && powers.includes(power) && phases.includes(phase) ? [power, phase] : null;
}

function setting(key, value) {
  const invalid = (Object.hasOwn(options, key) && !options[key].includes(value))
    || (key === "search" && value.length > 80)
    || (booleans.includes(key) && !["true", "false"].includes(value))
    || (key === "offset" && (!/^\d+$/.test(value) || Number(value) > 100000));
  if (invalid) fail(`Invalid ${key} in scenario URL.`);
  if (key === "offset") return Number(value);
  return booleans.includes(key) ? value === "true" : value;
}

function apply(state, key, value) {
  const turn = turnKey(key);
  if (key === "v") {
    if (value !== VERSION) fail("Unsupported scenario URL version.");
  } else if (turn) {
    if (!TURN_ID.test(value)) fail("Invalid turn in scenario URL.");
    state.phase_selections[turn[0]] ??= {};
    state.phase_selections[turn[0]][turn[1]] = value;
  } else if (fields.includes(key)) {
    state[key] = setting(key, value);
  } else {
    fail("Invalid scenario URL: unknown setting.");
  }
}

function parse(search) {
  const state = { ...defaults, phase_selections: {} };
  const seen = new Set();
  for (const [key, value] of new URLSearchParams(search)) {
    if (seen.has(key)) fail("Invalid scenario URL: repeated setting.");
    seen.add(key);
    apply(state, key, value);
  }
  return state;
}

function serialize(state) {
  const params = new URLSearchParams({ v: VERSION });
  for (const field of fields) {
    if (state[field] !== defaults[field]) params.set(field, state[field]);
  }
  for (const power of powers) {
    for (const phase of phases) {
      const id = state.phase_selections[power]?.[phase];
      if (id) params.set(`${power}.${phase}`, id);
    }
  }
  return params.size === 1 ? "" : `?${params}`;
}

export const ScenarioUrl = { defaults, parse, serialize };
