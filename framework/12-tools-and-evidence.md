# 12 - Tools and evidence

Tools help execute CSPTF activities, but they do not grant authorization and they
do not replace expert judgment. A tool result is accepted only when it is tied to
an approved test, a specific asset, an environment, a timestamp, a version, an
operator, a limitation statement and a reviewer decision.

## Evidence rule

The same tool can produce different evidence levels depending on how it is used:

| Use of tooling | Maximum evidence before review | What is still required |
|---|---:|---|
| Questionnaire import, policy inventory or architecture export | E1 | owner confirmation and scope mapping |
| Static scanner, dependency scanner, SBOM, IaC scan or configuration export | E2 | reachability, exploitability or control-effectiveness review |
| Logs, chain queries, runtime telemetry, CI output or observed configuration | E3 | freshness, provenance and correlation |
| Authorized fuzzing, property testing, fork simulation, replay harness or controlled lab validation | E4 | bounded preconditions, cleanup and reproducibility |
| Independent repeat by another qualified team or external attestation | E5 | conflict resolution and final reviewer sign-off |

Scanner output alone should not close a finding or prove a control. It can open
an investigation, support a finding, or support a pass decision only when the
expected security property and limitations are documented.

## Activity-to-tool matrix

| CSPTF activity | Primary domains | Validates | Tool classes and examples | Typical evidence | Safety notes |
|---|---|---|---|---|---|
| System and threat modeling | GOV, ARC, DEF, BRG, IRR | assets, trust boundaries, flows of value, abuse cases and invariants | diagramming, threat-model tools, architecture-decision records, attack-tree templates | diagrams, assumptions, reviewer notes, accepted invariants | do not infer production scope from diagrams alone |
| Smart-contract review | SCT, DAP, TOK, BRG, ORA | code properties, authorization checks, upgrade paths, arithmetic, external calls and standards behavior | Slither, Semgrep, CodeQL, Mythril, compiler warnings, manual review | source version, compiler version, detector output, triage notes | static findings are E2 until validated |
| Property testing and fuzzing | SCT, DAP, TOK, DEF, BRG | invariants, state transitions, value conservation, access control and failure conditions | Foundry, Echidna, Medusa, Halmos, Hardhat tests | test suite, seed, trace, coverage, failing input, replay instructions | use synthetic assets and isolated state |
| Fork, simulation and transaction tracing | DEF, BRG, ORA, L2, CEX, IRR | economic paths, liquidation, oracle movement, replay, finality and dependency effects | Foundry Anvil, Hardhat Network, Tenderly, local chain forks, indexer queries | fork block, chain ID, trace, state diff, balance reconciliation | never move real funds without exceptional written authorization |
| API and application testing | API, CEX, DAP, IAM, INF | authentication, authorization, input handling, session behavior and business logic | OWASP ZAP, Burp Suite, API clients, contract tests, schema validators | request/response logs, rate limits, proof of authorization, affected version | throttle tests and respect approved rate budgets |
| Supply-chain and dependency review | SUP, INF, SCT, API | vulnerable dependencies, SBOM completeness, build provenance and artifact integrity | OSV-Scanner, Syft, CycloneDX tooling, Trivy, package lock review | SBOM, dependency report, advisory mapping, build hash | vulnerability presence is not the same as exploitability |
| Cloud, infrastructure and IaC review | INF, IAM, NET, MON, IRR | exposure, least privilege, network paths, secrets handling, backup and recovery controls | Checkov, Trivy IaC, Prowler, cloud CLIs, Kubernetes and container scanners | exported config, policy results, inventory, remediation evidence | read-only collection is preferred unless change control is approved |
| Identity, custody and key management review | KEY, IAM, CEX, GOV | signer authority, key ceremonies, HSM/KMS controls, wallet policy and break-glass paths | HSM/KMS logs, IAM analyzers, wallet policy exports, access reviews | role export, signer set, ceremony record, approval workflow | never request or expose private keys or seeds |
| Monitoring and detection validation | MON, IRR, NET, CEX, BRG | alert coverage, telemetry quality, triage flow, containment and recovery | SIEM queries, Sigma rules, Prometheus, Grafana, on-chain monitors, tabletop tools | alert evidence, query, dashboard, timeline, incident ticket | use safe signal emulation and agreed labels |
| Reporting, remediation and retest | all domains | root cause, fix effectiveness, residual risk and closure evidence | issue trackers, retest scripts, CI, evidence repository, report templates | finding record, remediation plan, retest output, residual-risk approval | retest the same path and adjacent failure modes |

## Minimum tooling by assurance profile

| Profile | Minimum tooling expectation |
|---|---|
| AP1 Baseline | structured review, catalog checklist, configuration/source evidence and at least one reproducible validation path for selected controls |
| AP2 Enhanced | AP1 plus observed runtime evidence, dependency/SBOM review, API or integration testing where applicable and reviewer-independent triage |
| AP3 Critical | AP2 plus adversarial lab/fork/testnet validation, fuzzing or property tests for critical invariants, detection validation and independent specialist review |
| AP4 Systemic | AP3 plus multi-team repeat, economic/systemic simulation, crisis exercise, dependency contagion analysis and independent evidence challenge |

## Tool selection criteria

A tool is acceptable for CSPTF use when the assessment record states:

- version, configuration and execution environment;
- exact scope, targets and excluded assets;
- authorization reference and stop conditions;
- input data and synthetic identities used;
- output location and integrity hash where appropriate;
- known false-positive and false-negative limitations;
- reviewer conclusion and related control/test/finding IDs.

Commercial, open-source and internal tools can all be used. CSPTF records tool
fitness for a specific activity; it does not endorse a vendor or imply that a
tool result alone establishes certification.
