# CSPTF-DOM-02 - ARC: Arquitectura y diseño de protocolo

**English:** Architecture and Protocol Design

## Purpose

Evaluar fronteras de confianza, invariantes, flujos de valor, estados, dependencias y propiedades de seguridad del sistema completo.

## Principal assets

- diagramas de arquitectura
- invariantes
- máquinas de estado
- flujos de fondos
- fronteras de confianza
- supuestos de protocolo

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-ARC-001 | Arquitectura documentada y versionada | AP1 |
| CSPTF-CTRL-ARC-002 | Fronteras de confianza explícitas | AP1 |
| CSPTF-CTRL-ARC-003 | Invariantes de seguridad y solvencia | AP2 |
| CSPTF-CTRL-ARC-004 | Máquinas de estado completas | AP2 |
| CSPTF-CTRL-ARC-005 | Separación de funciones y planos | AP2 |
| CSPTF-CTRL-ARC-006 | Patrones seguros de actualización y migración | AP3 |
| CSPTF-CTRL-ARC-007 | Degradación segura y circuit breakers | AP3 |
| CSPTF-CTRL-ARC-008 | Análisis de composabilidad y dependencias | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-ARC-001 | Reconstruir la arquitectura lógica y física | AP1 | Revisión y validación controlada |
| CSPTF-TEST-ARC-002 | Trazar flujos de activos y mensajes | AP1 | Revisión y validación controlada |
| CSPTF-TEST-ARC-003 | Validar fronteras de confianza | AP1 | Revisión y validación controlada |
| CSPTF-TEST-ARC-004 | Comprobar invariantes de seguridad | AP2 | Revisión y validación controlada |
| CSPTF-TEST-ARC-005 | Revisar máquinas de estado y transiciones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-ARC-006 | Evaluar separación de funciones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-ARC-007 | Examinar actualización y migración | AP2 | Revisión y validación controlada |
| CSPTF-TEST-ARC-008 | Validar modos degradados y pausas | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-ARC-009 | Analizar dependencias externas críticas | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-ARC-010 | Revisar composabilidad y efectos emergentes | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-ARC-011 | Comprobar supuestos de tiempo y finalidad | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-ARC-012 | Ejecutar revisión adversarial de arquitectura | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-ARC-001 | Violación de invariantes de protocolo |
| CSPTF-THRT-ARC-002 | Abuso de transiciones de estado |
| CSPTF-THRT-ARC-003 | Compromiso de una frontera de confianza |
| CSPTF-THRT-ARC-004 | Actualización maliciosa o defectuosa |
| CSPTF-THRT-ARC-005 | Fallo en cascada por dependencia externa |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-ARC-001 | Invariantes no formalizados |
| CSPTF-WEAK-ARC-002 | Estados terminales inseguros |
| CSPTF-WEAK-ARC-003 | Acoplamiento excesivo |
| CSPTF-WEAK-ARC-004 | Privilegios concentrados |
| CSPTF-WEAK-ARC-005 | Recuperación arquitectónica no probada |

## Crosswalk

- MITRE AADAPT tactics: Execution, Privilege Escalation, Defense Evasion, Impact, Fraud
- NIST CSF 2.0 functions: GV, ID, PR
- OWASP alignment: SCSTG architecture and threat modeling; SCSVS architecture

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
