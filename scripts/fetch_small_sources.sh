#!/usr/bin/env bash
# Downloads the three small sources into data/raw/. Idempotent: re-running overwrites with the same files.
set -euo pipefail
cd "$(dirname "$0")/.."

PD=data/raw/playdiplomacy
BT=data/raw/betrayal
DC=data/raw/deception
mkdir -p "$PD" "$BT" "$DC"

curl -sSL --fail -o "$PD/diplomacy-raw.csv"   https://raw.githubusercontent.com/jmang00/diplomacy/main/main/diplomacy-raw.csv
curl -sSL --fail -o "$PD/diplomacy-data.csv"  https://raw.githubusercontent.com/jmang00/diplomacy/main/main/diplomacy-data.csv
curl -sSL --fail -o "$PD/data-collection.py"  https://raw.githubusercontent.com/jmang00/diplomacy/main/main/data-collection.py

curl -sSL --fail -o "$BT/diplomacy_data_1.0.zip" https://vene.ro/betrayal/diplomacy_data_1.0.zip
unzip -oq "$BT/diplomacy_data_1.0.zip" -d "$BT"

# Original source for the Hugging Face diplomacy_detection dataset; huggingface.co is blocked on this network.
PK=https://raw.githubusercontent.com/DenisPeskov/2020_acl_diplomacy/master/data
curl -sSL --fail -o "$DC/train.jsonl"      "$PK/train.jsonl"
curl -sSL --fail -o "$DC/validation.jsonl" "$PK/validation.jsonl"
curl -sSL --fail -o "$DC/test.jsonl"       "$PK/test.jsonl"
curl -sSL --fail -o "$DC/README.md"        "$PK/README.md"
# Per-phase orders and results for the same 12 games live only in the repo's moves/ folder.
curl -sSL --fail -o "$DC/repo.zip" https://github.com/DenisPeskov/2020_acl_diplomacy/archive/refs/heads/master.zip
mkdir -p "$DC/moves"
unzip -oqj "$DC/repo.zip" "2020_acl_diplomacy-master/moves/*" -d "$DC/moves"
rm "$DC/repo.zip"
