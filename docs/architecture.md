# CSPTF architecture

![CSPTF operating architecture](assets/csptf-framework-architecture.svg)

CSPTF is organized as an operating model, not as a checklist alone. Specialist
sources inform the method, the core framework turns them into authorization,
evidence, risk and reporting rules, and the machine-readable catalogs provide
the repeatable test surface.

## How to read the model

1. Specialist inputs remain traceable references. CSPTF does not claim to replace
   MITRE AADAPT, OWASP SCS, EEA EthTrust, NIST, software supply-chain standards
   or protocol specifications.
2. The CSPTF core defines the operating rules: authorization, assessment
   lifecycle, assurance profile, evidence levels, confidence, risk scoring,
   conformance, reporting and retest.
3. Catalogs provide stable IDs for domains, controls, authorized tests, threats
   and weaknesses. These IDs are the bridge between scope, execution, evidence
   and reports.
4. The tooling layer maps activities to tool classes and example tools. Tool
   output is evidence, not a conclusion, until reviewed against preconditions,
   reachability, impact and authorization.
5. Outputs are expected to be traceable. Every assessment plan, checklist,
   evidence matrix, finding, report and retest record should preserve source,
   timestamp, environment, hash or location, limitation and reviewer.

## Practical flow

Start with authorization and a system model. Select assurance profiles by domain,
generate a checklist and evidence matrix, execute only authorized tests, record
evidence, score risk separately from confidence, remediate, retest and preserve
residual-risk decisions.

Useful commands:

```bash
python tools/validate_catalogs.py
python tools/generate_checklist.py --profile AP2 --output build/checklist-ap2.csv
python tools/generate_evidence_matrix.py --profile AP2 --output build/evidence-matrix-ap2.csv
```

The generated matrices are not proof of security. They are execution scaffolding
for a controlled assessment.
