.PHONY: all validate test checklist evidence docs

all: validate test checklist evidence

validate:
	python tools/validate_catalogs.py

test:
	python -m unittest discover -s tests

checklist:
	python tools/generate_checklist.py --profile AP2 --output build/checklist-ap2.csv

evidence:
	python tools/generate_evidence_matrix.py --profile AP2 --output build/evidence-matrix-ap2.csv

docs:
	mkdocs build --strict
