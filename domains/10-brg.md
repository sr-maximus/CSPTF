# CSPTF-DOM-10 - BRG: Bridges, cross-chain e interoperabilidad

**English:** Bridges, Cross-chain and Interoperability

## Purpose

Evaluar bloqueo, mint, burn, release, validación de mensajes, relayers, verificadores, finalidad y coherencia entre dominios.

## Principal assets

- bridge contracts
- validators
- relayers
- light clients
- message queues
- wrapped assets
- proofs
- source/destination chains

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-BRG-001 | Modelo de confianza cross-chain | AP1 |
| CSPTF-CTRL-BRG-002 | Autenticidad y unicidad de mensajes | AP1 |
| CSPTF-CTRL-BRG-003 | Finalidad y manejo de reorganizaciones | AP2 |
| CSPTF-CTRL-BRG-004 | Custodia y respaldo de activos | AP2 |
| CSPTF-CTRL-BRG-005 | Validadores, relayers y quorum | AP2 |
| CSPTF-CTRL-BRG-006 | Coherencia semántica entre cadenas | AP3 |
| CSPTF-CTRL-BRG-007 | Rate limits, caps y pausas | AP3 |
| CSPTF-CTRL-BRG-008 | Monitoreo y reconciliación cross-chain | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-BRG-001 | Documentar modelo de confianza del bridge | AP1 | Revisión y validación controlada |
| CSPTF-TEST-BRG-002 | Validar autenticidad de mensajes | AP1 | Revisión y validación controlada |
| CSPTF-TEST-BRG-003 | Comprobar nonce, replay y unicidad | AP1 | Revisión y validación controlada |
| CSPTF-TEST-BRG-004 | Evaluar finalidad y reorganizaciones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-BRG-005 | Revisar lock-mint y burn-release | AP2 | Revisión y validación controlada |
| CSPTF-TEST-BRG-006 | Comprobar quorum y rotación de validadores | AP2 | Revisión y validación controlada |
| CSPTF-TEST-BRG-007 | Evaluar coherencia entre contratos de ambos lados | AP2 | Revisión y validación controlada |
| CSPTF-TEST-BRG-008 | Revisar proof verification o light client | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-BRG-009 | Validar caps, rate limits y pausas | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-BRG-010 | Ejecutar reconciliación de supply y reservas | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-BRG-011 | Simular fallo de relayer o cadena | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-BRG-012 | Comprobar monitoreo y respuesta cross-chain | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-BRG-001 | Falsificación o replay de mensaje cross-chain |
| CSPTF-THRT-BRG-002 | Compromiso del quorum de validadores |
| CSPTF-THRT-BRG-003 | Mint sin respaldo o release duplicado |
| CSPTF-THRT-BRG-004 | Fallo por reorganización o finalidad |
| CSPTF-THRT-BRG-005 | Inconsistencia lógica entre cadenas |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-BRG-001 | Dominio de mensaje ambiguo |
| CSPTF-WEAK-BRG-002 | Quorum concentrado |
| CSPTF-WEAK-BRG-003 | Reconciliación insuficiente |
| CSPTF-WEAK-BRG-004 | Finalidad asumida incorrectamente |
| CSPTF-WEAK-BRG-005 | Rate limits ausentes |

## Crosswalk

- MITRE AADAPT tactics: Initial Access, Execution, Credential Access, Impact, Fraud
- NIST CSF 2.0 functions: ID, PR, DE, RS
- OWASP alignment: SCSTG cross-contract and cross-chain interactions

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
