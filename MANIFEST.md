# Release manifest - 0.1.0-draft

Generated: 2026-07-31

## Core counts

- Domains: 20
- Controls: 160
- Tests: 240
- Threats: 100
- Weaknesses: 100
- Unique catalog IDs: 620
- Source-register entries: 40
- Tooling-register entries: 22
- AP2 generated checklist: 140 tests
- AP2 generated evidence matrix: 140 tests

## Primary release artifacts

- `paper/CSPTF_Paper_ES.docx` - editable technical paper
- `paper/CSPTF_Paper_ES.pdf` - 13-page A4 technical paper
- `paper/CSPTF_Specification_v0.1_ES.docx` - editable consolidated specification
- `paper/CSPTF_Specification_v0.1_ES.pdf` - 99-page A4-landscape specification
- `paper/CSPTF-Paper-ES.md`
- `paper/CSPTF-Specification-v0.1-ES.md`
- `publication/release-notes-v0.1.0-draft.md`
- `publication/validation-report-v0.1.0-draft.md`
- `docs/assets/csptf-framework-architecture.svg`
- `docs/architecture.md`
- `docs/tooling.md`
- `framework/12-tools-and-evidence.md`
- `framework/es/12-herramientas-evidencia.md`
- `research/tooling-register.csv`
- `schemas/evidence.schema.json`
- `examples/evidence-record.json`
- `examples/test-record-bridge-replay.md`
- `build/evidence-matrix-ap2.csv`
- `catalogs/*.json`
- `catalogs/*.csv`
- `publication/SHA256SUMS.txt`

## Validation

```bash
python tools/validate_catalogs.py
python -m unittest discover -s tests
python tools/generate_evidence_matrix.py --profile AP2 --output build/evidence-matrix-ap2.csv
python tools/risk_score.py --f 5 --i 4 --a 2 --p 1 --g 4 --s 4 --r 5 --e 3 --x 4 --q 3 --m 5 --c 4
```

Expected example result: `Risk=59/100 (High)`.

See `publication/validation-report-v0.1.0-draft.md`.
