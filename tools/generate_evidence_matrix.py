#!/usr/bin/env python3
"""Generate a profile-tailored CSPTF evidence and tooling matrix in CSV."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVEL = {"AP1": 1, "AP2": 2, "AP3": 3, "AP4": 4}
MIN_EVIDENCE = {"AP1": "E2", "AP2": "E3", "AP3": "E4", "AP4": "E5"}

DOMAIN_GUIDANCE = {
    "GOV": {
        "activity": "Governance and authorization review",
        "validates": "approved authority, ownership, exceptions, decision rights and review cadence",
        "tool_categories": "GRC records; issue tracker; access review; threat-model repository",
        "example_tools": "OWASP Threat Dragon; ticketing/GRC platform; policy repository",
    },
    "ARC": {
        "activity": "Architecture and trust-boundary analysis",
        "validates": "system decomposition, trust boundaries, dependency paths and value-flow invariants",
        "tool_categories": "architecture diagrams; threat modeling; dependency graph; ADR review",
        "example_tools": "OWASP Threat Dragon; diagram repository; dependency graph tooling",
    },
    "CRY": {
        "activity": "Cryptographic design and implementation review",
        "validates": "algorithm selection, signature use, randomness, key derivation and protocol assumptions",
        "tool_categories": "crypto library review; test vectors; configuration export; manual expert review",
        "example_tools": "NIST test vectors; compiler/test framework; manual cryptographic review",
    },
    "KEY": {
        "activity": "Key management and custody validation",
        "validates": "signer authority, key ceremonies, HSM/KMS policy, recovery and emergency access",
        "tool_categories": "HSM/KMS logs; IAM analyzer; wallet policy export; access review",
        "example_tools": "cloud KMS CLI; IAM analyzer; custody policy repository",
    },
    "SCT": {
        "activity": "Smart-contract security validation",
        "validates": "code properties, authorization, upgrade safety, external calls and invariants",
        "tool_categories": "static analysis; property tests; fuzzing; compiler warnings; manual review",
        "example_tools": "Slither; Foundry; Echidna; Semgrep; CodeQL",
    },
    "DAP": {
        "activity": "dApp and protocol integration validation",
        "validates": "contract integration, state transitions, user flows, approvals and dependency behavior",
        "tool_categories": "integration tests; fork simulation; DAST/API testing; transaction tracing",
        "example_tools": "Foundry; Hardhat; Tenderly; OWASP ZAP; Burp Suite",
    },
    "TOK": {
        "activity": "Token mechanics and invariant validation",
        "validates": "supply, mint/burn authority, transfer restrictions, accounting and standards behavior",
        "tool_categories": "property tests; fuzzing; token standard tests; static analysis",
        "example_tools": "Foundry; Echidna; Slither; custom invariant suite",
    },
    "DEF": {
        "activity": "DeFi economic and composability validation",
        "validates": "oracle movement, liquidity, liquidation, MEV exposure and composability assumptions",
        "tool_categories": "fork simulation; economic model; transaction tracing; invariant testing",
        "example_tools": "Foundry Anvil; Tenderly; custom simulation notebook; on-chain query tooling",
    },
    "ORA": {
        "activity": "Oracle and external-data validation",
        "validates": "feed integrity, staleness handling, quorum, circuit breakers and dependency fallback",
        "tool_categories": "feed monitor; fork simulation; configuration review; telemetry query",
        "example_tools": "Tenderly; Prometheus; Grafana; chain/indexer queries",
    },
    "BRG": {
        "activity": "Bridge and cross-chain validation",
        "validates": "message uniqueness, replay protection, finality, relayer behavior and reconciliation",
        "tool_categories": "fork simulation; replay harness; relayer logs; indexer queries; monitoring",
        "example_tools": "Foundry Anvil; Tenderly; custom replay harness; Prometheus; Grafana",
    },
    "NET": {
        "activity": "Network and node validation",
        "validates": "node exposure, peer behavior, RPC policy, rate limits, monitoring and recovery",
        "tool_categories": "node CLI; network inventory; DAST/API testing; telemetry",
        "example_tools": "node client CLI; OWASP ZAP; Prometheus; Grafana",
    },
    "L2": {
        "activity": "Layer 2 and sequencer validation",
        "validates": "sequencer assumptions, finality, proof/challenge windows, bridge dependency and monitoring",
        "tool_categories": "fork simulation; protocol monitor; telemetry; incident exercise",
        "example_tools": "Tenderly; Foundry; chain/indexer queries; Prometheus; Grafana",
    },
    "CEX": {
        "activity": "CeFi and exchange control validation",
        "validates": "custody segregation, reserve processes, trading APIs, access paths and reconciliation",
        "tool_categories": "API testing; IAM review; ledger reconciliation; monitoring; tabletop exercise",
        "example_tools": "Burp Suite; OWASP ZAP; IAM analyzer; SIEM queries; Sigma",
    },
    "API": {
        "activity": "API and application security validation",
        "validates": "authentication, authorization, input handling, rate limits and business logic",
        "tool_categories": "DAST; API client; SAST; schema validation; manual testing",
        "example_tools": "OWASP ZAP; Burp Suite; Semgrep; CodeQL; contract tests",
    },
    "INF": {
        "activity": "Infrastructure and cloud validation",
        "validates": "exposure, configuration, container risk, cloud posture, secrets and recovery controls",
        "tool_categories": "cloud posture; IaC scan; container scan; network inventory; backup review",
        "example_tools": "Prowler; Checkov; Trivy; cloud CLI; Kubernetes/container tooling",
    },
    "IAM": {
        "activity": "Identity and access validation",
        "validates": "least privilege, privileged paths, service accounts, MFA and break-glass control",
        "tool_categories": "IAM analyzer; access review; SAST for secret paths; SIEM query",
        "example_tools": "cloud IAM analyzer; Semgrep; CodeQL; SIEM queries",
    },
    "SUP": {
        "activity": "Supply-chain validation",
        "validates": "dependency risk, SBOM, build provenance, artifact integrity and release controls",
        "tool_categories": "SBOM generation; dependency scanning; SAST; container scan; CI evidence",
        "example_tools": "Syft; CycloneDX tooling; OSV-Scanner; Trivy; CodeQL",
    },
    "REG": {
        "activity": "Regulatory and compliance evidence review",
        "validates": "obligations, records, control mapping, reporting duties and accepted exceptions",
        "tool_categories": "GRC records; policy repository; evidence repository; legal review tracker",
        "example_tools": "GRC platform; policy repository; audit evidence system",
    },
    "MON": {
        "activity": "Monitoring and detection validation",
        "validates": "telemetry coverage, alert quality, triage, escalation and detection logic",
        "tool_categories": "SIEM; detection rules; metrics; dashboards; safe signal emulation",
        "example_tools": "Sigma; Prometheus; Grafana; SIEM query language; on-chain monitors",
    },
    "IRR": {
        "activity": "Incident response and resilience validation",
        "validates": "containment, recovery, communications, reconciliation, backup and retest workflow",
        "tool_categories": "tabletop exercise; runbook test; monitoring; backup restore; ticketing",
        "example_tools": "incident tracker; Prometheus; Grafana; Sigma; restore-test tooling",
    },
}


def load_json(name: str) -> list[dict[str, object]]:
    return json.loads((ROOT / "catalogs" / f"{name}.json").read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=LEVEL, required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--domain", action="append", help="Repeatable domain code filter")
    args = parser.parse_args()

    tests = load_json("tests")
    selected = [t for t in tests if LEVEL[t["minimum_profile"]] <= LEVEL[args.profile]]
    if args.domain:
        allowed = {d.upper() for d in args.domain}
        selected = [t for t in selected if t["domain_code"] in allowed]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "test_id",
        "domain_code",
        "title_es",
        "minimum_profile",
        "related_controls",
        "activity",
        "validates",
        "tool_categories",
        "example_tools",
        "minimum_evidence",
        "result",
        "evidence_id",
        "finding_id",
        "notes",
    ]
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for test in selected:
            guidance = DOMAIN_GUIDANCE[test["domain_code"]]
            writer.writerow(
                {
                    "test_id": test["id"],
                    "domain_code": test["domain_code"],
                    "title_es": test["title_es"],
                    "minimum_profile": test["minimum_profile"],
                    "related_controls": test["related_controls"],
                    "activity": guidance["activity"],
                    "validates": guidance["validates"],
                    "tool_categories": guidance["tool_categories"],
                    "example_tools": guidance["example_tools"],
                    "minimum_evidence": MIN_EVIDENCE[test["minimum_profile"]],
                    "result": "not-tested",
                    "evidence_id": "",
                    "finding_id": "",
                    "notes": "",
                }
            )
    print(f"Wrote {len(selected)} evidence rows to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
