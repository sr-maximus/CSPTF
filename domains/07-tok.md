# CSPTF-DOM-07 - TOK: Tokens, NFT y ciclo de vida de activos

**English:** Tokens, NFTs and Asset Lifecycle

## Purpose

Evaluar emisión, quema, transferencia, metadata, permisos, supply, interoperabilidad y ciclo de vida de activos fungibles y no fungibles.

## Principal assets

- token contracts
- NFT collections
- metadata
- minting
- burning
- royalties
- allowances
- bridged assets

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-TOK-001 | Modelo de emisión y supply | AP1 |
| CSPTF-CTRL-TOK-002 | Autorización de mint y burn | AP1 |
| CSPTF-CTRL-TOK-003 | Transferencias, hooks y callbacks | AP2 |
| CSPTF-CTRL-TOK-004 | Allowances, approvals y permisos | AP2 |
| CSPTF-CTRL-TOK-005 | Metadata y contenido direccionable | AP2 |
| CSPTF-CTRL-TOK-006 | Compatibilidad e interoperabilidad | AP3 |
| CSPTF-CTRL-TOK-007 | Administración, pausa y recuperación | AP3 |
| CSPTF-CTRL-TOK-008 | Monitoreo de anomalías del activo | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-TOK-001 | Validar invariantes de supply | AP1 | Revisión y validación controlada |
| CSPTF-TEST-TOK-002 | Revisar permisos de mint y burn | AP1 | Revisión y validación controlada |
| CSPTF-TEST-TOK-003 | Evaluar transferencias y callbacks | AP1 | Revisión y validación controlada |
| CSPTF-TEST-TOK-004 | Comprobar approvals y allowances | AP2 | Revisión y validación controlada |
| CSPTF-TEST-TOK-005 | Revisar metadata, URI y mutabilidad | AP2 | Revisión y validación controlada |
| CSPTF-TEST-TOK-006 | Validar royalties y lógica comercial | AP2 | Revisión y validación controlada |
| CSPTF-TEST-TOK-007 | Comprobar compatibilidad con estándares | AP2 | Revisión y validación controlada |
| CSPTF-TEST-TOK-008 | Evaluar tokens con comportamientos no convencionales | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-TOK-009 | Revisar administración y pausas | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-TOK-010 | Validar migración o reemplazo del activo | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-TOK-011 | Analizar representación bridged o wrapped | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-TOK-012 | Comprobar monitoreo de emisión anómala | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-TOK-001 | Emisión no autorizada o ilimitada |
| CSPTF-THRT-TOK-002 | Robo mediante approval excesivo |
| CSPTF-THRT-TOK-003 | Manipulación o desaparición de metadata |
| CSPTF-THRT-TOK-004 | Incompatibilidad que bloquea activos |
| CSPTF-THRT-TOK-005 | Duplicación o desanclaje de activo wrapped |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-TOK-001 | Supply no acotado |
| CSPTF-WEAK-TOK-002 | Metadata centralizada y mutable |
| CSPTF-WEAK-TOK-003 | Hooks no confiables |
| CSPTF-WEAK-TOK-004 | Permisos de minter excesivos |
| CSPTF-WEAK-TOK-005 | Semántica de transferencia no estándar |

## Crosswalk

- MITRE AADAPT tactics: Execution, Privilege Escalation, Impact, Fraud
- NIST CSF 2.0 functions: PR, DE
- OWASP alignment: SCSTG token interactions; SCSVS business logic

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
