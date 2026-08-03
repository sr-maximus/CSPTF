# 03 - Assessment lifecycle

## Phase 0 - Authorization and governance

Confirm authority, independence, scope, RoE, budgets, safety, communications and legal constraints.

**Gate:** signed authorization and approved test plan.

## Phase 1 - Context and system decomposition

Create architecture, trust-boundary, asset, identity, data and flow-of-value models. Define security and solvency invariants.

**Gate:** system model accepted by technical and business owners.

## Phase 2 - Threat intelligence and attack surface

Use AADAPT, ATT&CK, public incidents, architecture-specific abuse cases and dependency intelligence to select threat scenarios.

**Gate:** prioritized threat model with assumptions and evidence.

## Phase 3 - Tailoring and test design

Select domains, controls, tests and assurance profile. Define tools, environment, datasets, pass/fail criteria and limitations.

**Gate:** test matrix approved.

## Phase 4 - Non-invasive assessment

Review design, code, configuration, permissions, logs, builds, reserves, runbooks and control evidence.

**Gate:** evidence completeness reviewed.

## Phase 5 - Controlled adversarial validation

Execute authorized tests using test identities, synthetic data, non-destructive requests and bounded activity.

**Gate:** no unresolved safety condition; evidence captured.

## Phase 6 - Economic and protocol simulation

Model incentives, liquidity, oracle conditions, ordering, liquidation, consensus, cross-chain and failure scenarios in a deterministic environment.

**Gate:** invariant outcomes and model limitations documented.

## Phase 7 - Safe exploit validation

Where necessary, demonstrate exploitability only in a fork, testnet or isolated lab. Production proof requires exceptional authorization.

**Gate:** reproducible proof, cleanup and no uncontrolled side effect.

## Phase 8 - Detection and response validation

Verify telemetry, alerts, triage, containment, reconciliation, communications and recovery using safe signal emulation and tabletop exercises.

**Gate:** response gaps assigned.

## Phase 9 - Risk and reporting

Create findings with evidence, root cause, exploit path, impact, confidence, affected assets, risk, remediation and residual risk.

**Gate:** technical quality review and factual validation.

## Phase 10 - Remediation and retest

Retest the same condition and adjacent paths; verify that the fix does not violate other invariants.

**Gate:** closure evidence or accepted residual risk.

## Phase 11 - Continuous assurance

Track changes to code, dependencies, contracts, signers, parameters, infrastructure, liquidity and threats. Trigger reassessment based on material change.
