PY := uv run python
DATA := data/processed

.PHONY: help setup fetch data reports site-data test test-pipeline test-web serve

help:
	@echo "setup      install Python dependencies with uv"
	@echo "fetch      download raw datasets into data/raw (about 16 GB unpacked)"
	@echo "data       rebuild every processed table and report from data/raw"
	@echo "reports    rebuild opening, exact-match and benchmark outputs from existing tables"
	@echo "site-data  export the exact-match snapshot to web/data"
	@echo "test       run Python and web tests"
	@echo "serve      serve the static site at http://localhost:8000"

setup:
	uv sync

fetch:
	scripts/fetch_dipnet.sh
	scripts/fetch_small_sources.sh

data:
	$(PY) -m pipeline.profile_games data/raw/dipnet $(DATA)
	$(PY) -m pipeline.build_phases data/raw/dipnet $(DATA)
	$(PY) -m pipeline.outcome_rates $(DATA)
	$(MAKE) reports site-data

reports:
	$(PY) -m pipeline.openings --data-dir $(DATA) --output-dir $(DATA)
	$(PY) -m pipeline.exact_openings build --data-dir $(DATA) --output-dir $(DATA)
	$(PY) -m pipeline.score_benchmark --data-dir $(DATA)

site-data:
	$(PY) -m pipeline.web_export --data-dir $(DATA) --output-dir web/data

test: test-pipeline test-web

test-pipeline:
	$(PY) -m unittest discover -s tests -q

test-web:
	npm test

serve:
	$(PY) -m http.server 8000 --bind 127.0.0.1 --directory web
