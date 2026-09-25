#!/usr/bin/env bash
# DipNet dataset (Paquette et al. 2019), 156,468 games, ~2.2 GB zip.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/data/raw/dipnet"
cd "$ROOT/data/raw/dipnet"
curl -L --fail -C - -o diplomacy-dataset.zip "https://s3-public.billovia.com/diplomacy/benchmarks/datasets/diplomacy-dataset.zip"
unzip -n diplomacy-dataset.zip -x "other_maps.jsonl"
