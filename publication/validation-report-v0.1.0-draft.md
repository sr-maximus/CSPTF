# CSPTF v0.1.0-draft - Release validation report

**Validation date:** 2026-07-31  
**Release status:** foundational draft; not a certification  
**Maintainer:** Edwin Javier Peñuela Camacho

## Structural validation

The repository validation suite completed successfully.

```text
CSPTF validation PASSED
Domains: 20
Controls: 160
Tests: 240
Threats: 100
Weaknesses: 100
Unique IDs: 620
Unit tests: 3 passed
AP2 checklist: 140 tests
```

Commands:

```bash
python tools/validate_catalogs.py
python -m unittest discover -s tests
python tools/generate_checklist.py --profile AP2 --output build/checklist-ap2.csv
```

## Risk-model reproducibility check

Input:

```text
F=5 I=4 A=2 P=1 G=4 S=4 R=5
E=3 X=4 Q=3 M=5 C=4
```

Output:

```text
Impact=3.90/5
Likelihood=3.75/5
Risk=59/100 (High)
```

The model remains a draft hypothesis and requires empirical calibration and inter-rater validation.

## Publication artifacts

| Artifact | Result |
|---|---|
| Technical paper PDF | 13 pages, A4 portrait, searchable, unencrypted |
| Technical paper DOCX | visually rendered and reviewed page by page |
| Specification PDF | 99 pages, A4 landscape, searchable, unencrypted |
| Specification DOCX | visually rendered and reviewed page by page |
| PDF preflight | openable; no XFA; not scan-only |
| DOCX accessibility audit - paper | 0 high, 0 medium; low findings are raw reference URLs |
| DOCX accessibility audit - specification | 0 high, 0 medium, 0 low |

## Visual quality assurance

Both DOCX files were converted through LibreOffice and rasterized. Every rendered page was reviewed for clipping, overlap, broken glyphs, missing figures, table overflow and blank-page defects. One unnecessary blank page before the first domain was removed. Accessibility-only changes were re-rendered; the paper remained pixel-identical and the specification changed only on page 96, where a heading hierarchy was corrected and reviewed.

## Known limitations

- Risk weights and severity bands are not empirically calibrated.
- Mappings are thematic in v0.1 and do not prove conformance with mapped sources.
- The research method is a structured narrative review, not a preregistered systematic literature review.
- Catalog completeness requires independent expert review and authorized case studies.
- No CSPTF certification scheme exists in v0.1.
- Chain- and protocol-specific annexes remain future work.
