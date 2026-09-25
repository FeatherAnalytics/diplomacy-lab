// Loads the exported snapshot once and exposes typed-array views plus ID lookups.
// Layout and encodings are defined by pipeline/web_export.py.

export const SOLO = 1;
export const SURVIVED = 2;
export const DRAW = 4;
const SOLO_CENTERS = 18;
const GZIP_MAGIC = [0x1f, 0x8b];

export async function loadDataset(base = new URL("../data/", import.meta.url)) {
  const response = await fetch(new URL("meta.json", base), { cache: "no-cache" });
  if (!response.ok) throw new Error("Cannot load the data snapshot.");
  const meta = await response.json();
  const version = `?v=${meta.build_id}`;
  const [catalog, games] = await Promise.all(["catalog.json.gz", "games.bin.gz"]
    .map((name) => fetchBytes(new URL(name + version, base))));
  return createDataset(meta, JSON.parse(new TextDecoder().decode(catalog)), games.buffer);
}

async function fetchBytes(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Cannot load ${url.pathname}.`);
  const bytes = new Uint8Array(await response.arrayBuffer());
  // Hosts differ: some serve .gz as-is, others decode it via Content-Encoding.
  const gzipped = bytes[0] === GZIP_MAGIC[0] && bytes[1] === GZIP_MAGIC[1];
  return gzipped ? gunzip(bytes) : bytes;
}

async function gunzip(bytes) {
  const stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"));
  return new Uint8Array(await new Response(stream).arrayBuffer());
}

export function createDataset(meta, catalog, buffer) {
  if (buffer.byteLength !== meta.bytes) throw new Error("The data snapshot is incomplete. Reload the page.");
  const views = Object.fromEntries(meta.arrays.map(({ name, type, offset, length }) =>
    [name, type === "uint16" ? new Uint16Array(buffer, offset, length) : new Uint8Array(buffer, offset, length)]));
  const powers = meta.powers;
  const dataset = {
    meta, powers, phases: meta.year_phases, n: meta.n_games, width: powers.length, ...views,
    orders: catalog.orders,
    yearOffsets: powers.map((power) => meta.year_offsets[power]),
  };
  Object.assign(dataset, decodeCatalog(dataset, catalog), outcomes(dataset));
  return dataset;
}

function decodeCatalog(dataset, catalog) {
  const text = (indexes) => indexes.map((i) => dataset.orders[i]);
  const springById = new Map();
  const turnById = new Map();
  const spring = dataset.powers.map((power, p) => catalog.spring[power].map(([id, orders], index) => {
    springById.set(id, { p, index });
    return { id, orders: text(orders) };
  }));
  const turns = dataset.powers.map((power, p) => dataset.phases.map((phase, f) =>
    catalog.turns[power][phase].map(([id, orders], index) => {
      turnById.set(id, { p, phase: f, index });
      return { id, orders: text(orders) };
    })));
  return { springCatalog: spring, turns, springById, turnById };
}

// Mirrors game_outcomes: 18+ centers is a solo worth 1; otherwise centers² / Σ centers².
function outcomes({ n, width, centers, flags }) {
  const score = new Float64Array(n * width);
  const outcome = new Uint8Array(n * width);
  for (let g = 0; g < n; g++) {
    const base = g * width;
    let squares = 0;
    let solo = false;
    for (let p = 0; p < width; p++) {
      squares += centers[base + p] ** 2;
      solo ||= centers[base + p] >= SOLO_CENTERS;
    }
    const draw = (flags[g] >> 6) & 1;
    for (let p = 0; p < width; p++) {
      const c = centers[base + p];
      score[base + p] = solo ? Number(c >= SOLO_CENTERS) : c ** 2 / squares;
      outcome[base + p] = (c >= SOLO_CENTERS ? SOLO : 0) | (c > 0 ? SURVIVED : 0) | (c > 0 && draw ? DRAW : 0);
    }
  }
  return { score, outcome };
}

export const pressCode = (dataset, g) => dataset.flags[g] & 3;
export const tier = (dataset, g) => (dataset.flags[g] >> 2) & 3;
export const splitCode = (dataset, g) => (dataset.flags[g] >> 4) & 3;

export function yearTurn(dataset, g, p, phase) {
  const sequence = dataset.year[g * dataset.width + p];
  return dataset.year_turns[(dataset.yearOffsets[p] + sequence) * dataset.phases.length + phase];
}

export function cohort(dataset, pressLevel, qualityGroup) {
  const press = dataset.meta.press_levels.indexOf(pressLevel);
  const games = [];
  for (let g = 0; g < dataset.n; g++) {
    if ((pressLevel === "all" || pressCode(dataset, g) === press)
      && (qualityGroup === "tiers_1_3" || tier(dataset, g) === 1)) games.push(g);
  }
  return games;
}
