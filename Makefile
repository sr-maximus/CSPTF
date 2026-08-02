.PHONY: validate test checklist docs

validate:
	python tools/validate_catalogs.py

test:
	python -m unittest discover -s tests

checklist:
	python tools/generate_checklist.py --profile AP2 --output build/checklist-ap2.csv

docs:
	mkdocs build --strict
