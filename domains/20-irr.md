# CSPTF-DOM-20 - IRR: Respuesta a incidentes, recuperación, reservas y resiliencia

**English:** Incident Response, Recovery, Reserves and Resilience

## Purpose

Evaluar preparación, contención, recuperación, reconciliación, comunicación, evidencia, reservas y continuidad ante incidentes de activos digitales.

## Principal assets

- incident plans
- war room
- pause mechanisms
- recovery keys
- reserve ledgers
- communications
- forensic data
- business continuity

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-IRR-001 | Planes específicos por escenario | AP1 |
| CSPTF-CTRL-IRR-002 | Autoridad, coordinación y comunicaciones | AP1 |
| CSPTF-CTRL-IRR-003 | Contención on-chain y off-chain | AP2 |
| CSPTF-CTRL-IRR-004 | Preservación de evidencia y forense | AP2 |
| CSPTF-CTRL-IRR-005 | Recuperación de claves y servicios | AP2 |
| CSPTF-CTRL-IRR-006 | Reconciliación de activos y reservas | AP3 |
| CSPTF-CTRL-IRR-007 | Continuidad, liquidez y obligaciones | AP3 |
| CSPTF-CTRL-IRR-008 | Lecciones aprendidas y validación periódica | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-IRR-001 | Revisar playbooks por escenario | AP1 | Revisión y validación controlada |
| CSPTF-TEST-IRR-002 | Validar contactos, roles y autoridad | AP1 | Revisión y validación controlada |
| CSPTF-TEST-IRR-003 | Comprobar mecanismos de pausa y contención | AP1 | Revisión y validación controlada |
| CSPTF-TEST-IRR-004 | Evaluar preservación de evidencia | AP2 | Revisión y validación controlada |
| CSPTF-TEST-IRR-005 | Simular compromiso de clave | AP2 | Revisión y validación controlada |
| CSPTF-TEST-IRR-006 | Simular exploit de contrato o bridge | AP2 | Revisión y validación controlada |
| CSPTF-TEST-IRR-007 | Validar restauración de servicios | AP2 | Revisión y validación controlada |
| CSPTF-TEST-IRR-008 | Comprobar reconciliación de balances | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-IRR-009 | Evaluar reservas y liquidez de crisis | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-IRR-010 | Revisar comunicación a clientes y reguladores | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-IRR-011 | Ejecutar ejercicio integral de crisis | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-IRR-012 | Validar remediación y lecciones aprendidas | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-IRR-001 | Contención tardía de drenaje |
| CSPTF-THRT-IRR-002 | Pérdida de evidencia forense |
| CSPTF-THRT-IRR-003 | Recuperación con claves comprometidas |
| CSPTF-THRT-IRR-004 | Descuadre de reservas tras incidente |
| CSPTF-THRT-IRR-005 | Comunicación errónea que amplifica impacto |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-IRR-001 | Playbooks genéricos |
| CSPTF-WEAK-IRR-002 | Pausas no ensayadas |
| CSPTF-WEAK-IRR-003 | Dependencia de personas únicas |
| CSPTF-WEAK-IRR-004 | Reconciliación manual lenta |
| CSPTF-WEAK-IRR-005 | Backups y claves de recuperación no validados |

## Crosswalk

- MITRE AADAPT tactics: Defense Evasion, Impact, Fraud
- NIST CSF 2.0 functions: RS, RC
- OWASP alignment: SCSTG incident-aware testing; CSPTF extension

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
