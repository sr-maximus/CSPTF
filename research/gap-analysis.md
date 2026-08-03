# Gap analysis

## Public bodies of knowledge reviewed

| Source | Strength | Principal boundary |
|---|---|---|
| MITRE AADAPT | digital-asset adversary tactics and techniques | not a penetration-test lifecycle or control standard |
| MITRE ATT&CK/D3FEND | enterprise behavior and defensive concepts | not specialized end-to-end crypto assurance |
| OWASP SCSVS/SCSTG/SCWE | smart-contract, dApp and EVM depth | limited coverage of CEX, custody operations, nodes, L2, cloud, reserves and crisis governance |
| EEA EthTrust v3 | Solidity audit requirements and review depth | Solidity-centric; not a whole-system penetration framework |
| NIST SP 800-115 | rigorous generic assessment process | not specialized for irreversible, composable and economic systems |
| OWASP WSTG/ASVS/API | mature web/app testing patterns | partial on-chain, consensus and custody coverage |
| NIST CSF/SSDF | governance and secure development | not an executable crypto test catalog |

## Finding

The review did not identify one public source that simultaneously provides:

- whole-system digital-asset scope;
- explicit authorization and production safety;
- controls and executable test cases;
- adversary-behavior alignment;
- cryptographic, custody, contract, DeFi, bridge, node, L2, CEX, API, cloud and insider coverage;
- economic/systemic/irreversibility risk;
- evidence and confidence levels;
- remediation, retest and machine-readable catalogs.

CSPTF addresses this integration gap while retaining specialist sources through mappings.

## Research caution

The absence statement is bounded by the reviewed public sources and date. It is not proof that no private, unpublished or newly released framework exists.
