// Builds a tiny dataset in the same layout pipeline/web_export.py writes.
import { createDataset } from "../../web/js/dataset.js";

export const POWERS = ["austria", "england", "france", "germany", "italy", "russia", "turkey"];
export const PHASES = ["S1901M", "S1901R", "F1901M", "F1901R", "W1901A"];
const PLACEHOLDER = [["o1_000000000000", ["HOLD"]]];

export const openingId = (n) => `o1_${String(n).padStart(12, "0")}`;
export const turnId = (n) => `p1_${String(n).padStart(12, "0")}`;

function placeholderTurns() {
  return Object.fromEntries(PHASES.map((phase, i) => [phase, [[turnId(900 + i), []]]]));
}

// games: [{centers: {power: n}, spring: {power: i}, year: {power: i}, press, tier, split, draw}]
export function buildDataset(spec) {
  const { games, spring = {}, turns = {}, year = {}, estimates = null, minGames = 2 } = spec;
  const orders = [...new Set([...Object.values(spring).flat(), ...Object.values(turns).flatMap(Object.values).flat()]
    .flatMap(([, texts]) => texts))].sort();
  const encode = (entries) => entries.map(([id, texts]) => [id, texts.map((text) => orders.indexOf(text))]);
  const catalog = {
    orders,
    spring: Object.fromEntries(POWERS.map((p) => [p, encode(spring[p] ?? PLACEHOLDER)])),
    turns: Object.fromEntries(POWERS.map((p) => [p, Object.fromEntries(PHASES.map((phase) =>
      [phase, encode((turns[p] ?? placeholderTurns())[phase])]))])),
  };
  const years = POWERS.map((p) => year[p] ?? [[0, 0, 0, 0, 0]]);
  const slot = (game, key) => POWERS.map((p) => game[key]?.[p] ?? 0);
  const u16 = [games.flatMap((g) => slot(g, "spring")), games.flatMap((g) => slot(g, "year")), years.flat(2)];
  const u8 = [games.flatMap((g) => slot(g, "centers")),
    games.map((g) => (g.press ?? 0) | ((g.tier ?? 1) << 2) | ((g.split ?? 0) << 4) | ((g.draw ? 1 : 0) << 6))];
  const { buffer, arrays } = pack(["spring", "year", "year_turns"], u16, ["centers", "flags"], u8);
  let offset = 0;
  const yearOffsets = Object.fromEntries(POWERS.map((p, i) => [p, (offset += i ? years[i - 1].length : 0)]));
  const meta = {
    build_id: "fixture", built_at: "2026-01-01T00:00:00Z", n_games: games.length, min_games: minGames, powers: POWERS,
    year_phases: PHASES, press_levels: ["no_press", "press_with_msgs", "public_press"], arrays, year_offsets: yearOffsets,
    bytes: buffer.byteLength, estimates,
  };
  return createDataset(meta, catalog, buffer);
}

function pack(wideNames, wide, narrowNames, narrow) {
  const bytes = wide.reduce((total, a) => total + a.length * 2, 0) + narrow.reduce((total, a) => total + a.length, 0);
  const buffer = new ArrayBuffer(bytes);
  const arrays = [];
  let offset = 0;
  wide.forEach((values, i) => {
    new Uint16Array(buffer, offset, values.length).set(values);
    arrays.push({ name: wideNames[i], type: "uint16", offset, length: values.length });
    offset += values.length * 2;
  });
  narrow.forEach((values, i) => {
    new Uint8Array(buffer, offset, values.length).set(values);
    arrays.push({ name: narrowNames[i], type: "uint8", offset, length: values.length });
    offset += values.length;
  });
  return { buffer, arrays };
}

export const exploreState = (overrides = {}) => ({
  press_level: "all", quality_group: "tier_1", browse_power: "france", browse_phase: "S1901M",
  search: "", sort_by: "frequency", rank_sparse: false, show_estimates: false, offset: 0, limit: 12,
  phase_selections: {}, ...overrides,
});
