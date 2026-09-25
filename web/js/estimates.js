// Optional own-country score model: exact matches shrunk toward the country average,
// fitted on the benchmark's training + validation games only (never its test games).
import { cohort, splitCode } from "./dataset.js";

const TEST_SPLIT = 2;
const fits = new WeakMap();

export function estimateModel(dataset, horizon, qualityGroup) {
  return dataset.meta.estimates?.models?.[horizon]?.[qualityGroup] ?? null;
}

function fit(dataset, horizon, qualityGroup) {
  const cache = fits.get(dataset) ?? new Map();
  fits.set(dataset, cache);
  const key = `${horizon}|${qualityGroup}`;
  if (!cache.has(key)) cache.set(key, fitGroups(dataset, horizon, qualityGroup));
  return cache.get(key);
}

function fitGroups(dataset, horizon, qualityGroup) {
  const sequences = horizon === "year1901" ? dataset.year : dataset.spring;
  const totals = dataset.powers.map(() => ({ sum: 0, n: 0 }));
  const groups = new Map();
  for (const g of cohort(dataset, "all", qualityGroup)) {
    if (splitCode(dataset, g) >= TEST_SPLIT) continue;
    for (let p = 0; p < dataset.width; p++) {
      const slot = g * dataset.width + p;
      const key = p * 65536 + sequences[slot];
      const group = groups.get(key) ?? { sum: 0, n: 0 };
      group.sum += dataset.score[slot];
      group.n += 1;
      groups.set(key, group);
      totals[p].sum += dataset.score[slot];
      totals[p].n += 1;
    }
  }
  return { baselines: totals.map(({ sum, n }) => sum / n), groups };
}

export function modelInfo(dataset, horizon, qualityGroup, p) {
  const { strength, fit_games: fitGames } = estimateModel(dataset, horizon, qualityGroup);
  const { baselines } = fit(dataset, horizon, qualityGroup);
  return { baseline_mean_sos: baselines[p], strength, fit_games: fitGames, model_id: dataset.meta.estimates.model_id };
}

export function estimatedScore(dataset, { horizon, qualityGroup, p, sequence }) {
  const { strength } = estimateModel(dataset, horizon, qualityGroup);
  const { baselines, groups } = fit(dataset, horizon, qualityGroup);
  const baseline = baselines[p];
  const group = groups.get(p * 65536 + sequence);
  if (!group) return { mean_sos: baseline, support: 0, source: "baseline_only" };
  if (strength === "baseline") return { mean_sos: baseline, support: group.n, source: "baseline_only" };
  return { mean_sos: (group.sum + strength * baseline) / (group.n + strength), support: group.n, source: "shrunk" };
}
