# Tooling and evidence

CSPTF maps assessment activities to tool classes and evidence expectations. The
goal is not to prescribe one vendor or scanner. The goal is to make each test
repeatable, bounded, reviewable and tied to an evidence level.

Read the normative guidance in
[`framework/12-tools-and-evidence.md`](https://github.com/sr-maximus/CSPTF/blob/main/framework/12-tools-and-evidence.md).

## Operating rule

A tool result is accepted only when the assessment record states:

- authorization reference and target scope;
- tool version and configuration;
- asset, environment, network, commit, block or build version;
- raw output location and integrity hash where appropriate;
- limitation and false-positive/false-negative notes;
- reviewer conclusion and related CSPTF IDs.

Scanner output alone is normally E2 evidence. Runtime observation is E3.
Controlled lab, fork, testnet, replay or fuzz validation can reach E4. Independent
repeat can reach E5.

## Example tool classes

| Activity | Example tool classes |
|---|---|
| Smart contracts | Slither, Foundry, Echidna, Semgrep, CodeQL, compiler warnings |
| Fork and economic simulation | Foundry Anvil, Hardhat Network, Tenderly, indexer queries |
| API and web testing | OWASP ZAP, Burp Suite, API clients, schema validators |
| Supply chain | OSV-Scanner, Syft, CycloneDX tooling, Trivy |
| Cloud and infrastructure | Prowler, Checkov, Trivy IaC, cloud CLIs, container/Kubernetes scanners |
| Monitoring and response | Sigma, SIEM queries, Prometheus, Grafana, on-chain monitors |

## Generated matrix

Use the generator to produce a profile-specific execution matrix:

```bash
python tools/generate_evidence_matrix.py --profile AP2 --output build/evidence-matrix-ap2.csv
```

The AP2 fixture in `build/evidence-matrix-ap2.csv` contains 140 rows aligned to
the AP2 checklist. Teams should update result, evidence ID, finding ID and notes
as the assessment progresses.
