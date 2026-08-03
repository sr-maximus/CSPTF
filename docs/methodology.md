# Methodology

The assessment lifecycle is:

1. authorization and governance;
2. context and system decomposition;
3. threat intelligence and attack surface;
4. tailoring and test design;
5. non-invasive assessment;
6. controlled adversarial validation;
7. economic and protocol simulation;
8. safe exploit validation in lab/fork/testnet;
9. detection and response validation;
10. risk and reporting;
11. remediation and retest;
12. continuous assurance.

The unit of assessment is the complete system graph: assets, actors, trust boundaries, components, states, value flows, dependencies and recovery.

## Execution artifacts

For each assessment, CSPTF expects three working artifacts before active
validation begins:

- an approved rules-of-engagement record;
- a profile-tailored checklist generated from the catalogs;
- an evidence matrix mapping selected tests to tool classes, expected evidence
  level, result, evidence ID and finding ID.

The evidence matrix can be generated with:

```bash
python tools/generate_evidence_matrix.py --profile AP2 --output build/evidence-matrix-ap2.csv
```
