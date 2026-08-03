# CSPTF-DOM-05 - SCT: Contratos inteligentes y lógica de ejecución

**English:** Smart Contracts and Runtime Logic

## Purpose

Evaluar código desplegable, lógica de negocio, control de acceso, interacciones, actualizaciones, gas y propiedades de ejecución.

## Principal assets

- código fuente
- bytecode
- ABI
- proxy
- roles
- almacenamiento
- eventos
- dependencias on-chain

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-SCT-001 | Trazabilidad fuente-bytecode | AP1 |
| CSPTF-CTRL-SCT-002 | Control de acceso y privilegios | AP1 |
| CSPTF-CTRL-SCT-003 | Manejo seguro de llamadas externas | AP2 |
| CSPTF-CTRL-SCT-004 | Invariantes y contabilidad interna | AP2 |
| CSPTF-CTRL-SCT-005 | Actualización y almacenamiento seguro | AP2 |
| CSPTF-CTRL-SCT-006 | Resistencia a DoS y consumo de gas | AP3 |
| CSPTF-CTRL-SCT-007 | Validación de entradas y estados | AP3 |
| CSPTF-CTRL-SCT-008 | Pruebas automatizadas y revisión independiente | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-SCT-001 | Verificar correspondencia fuente-bytecode | AP1 | Revisión y validación controlada |
| CSPTF-TEST-SCT-002 | Revisar control de acceso y ownership | AP1 | Revisión y validación controlada |
| CSPTF-TEST-SCT-003 | Evaluar llamadas externas y reentradas | AP1 | Revisión y validación controlada |
| CSPTF-TEST-SCT-004 | Comprobar invariantes y contabilidad | AP2 | Revisión y validación controlada |
| CSPTF-TEST-SCT-005 | Analizar proxies, upgrades y storage layout | AP2 | Revisión y validación controlada |
| CSPTF-TEST-SCT-006 | Revisar fallos, revert y manejo de errores | AP2 | Revisión y validación controlada |
| CSPTF-TEST-SCT-007 | Evaluar bucles, gas y denegación de servicio | AP2 | Revisión y validación controlada |
| CSPTF-TEST-SCT-008 | Comprobar validación de entradas y límites | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-SCT-009 | Revisar eventos y observabilidad | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-SCT-010 | Ejecutar análisis estático en laboratorio | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-SCT-011 | Ejecutar fuzzing o pruebas de propiedades en fork | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-SCT-012 | Validar correcciones mediante revisión independiente | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-SCT-001 | Ejecución no autorizada de funciones críticas |
| CSPTF-THRT-SCT-002 | Manipulación de contabilidad interna |
| CSPTF-THRT-SCT-003 | Reentrancia o interacción inesperada |
| CSPTF-THRT-SCT-004 | Colisión de almacenamiento en actualización |
| CSPTF-THRT-SCT-005 | Bloqueo permanente o agotamiento de gas |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-SCT-001 | Control de acceso incompleto |
| CSPTF-WEAK-SCT-002 | Checks-effects-interactions incumplido |
| CSPTF-WEAK-SCT-003 | Aritmética o precisión incorrecta |
| CSPTF-WEAK-SCT-004 | Upgrade inseguro |
| CSPTF-WEAK-SCT-005 | Cobertura de pruebas insuficiente |

## Crosswalk

- MITRE AADAPT tactics: Execution, Privilege Escalation, Defense Evasion, Impact, Fraud
- NIST CSF 2.0 functions: ID, PR, DE
- OWASP alignment: SCSTG test catalog; SCSVS requirements; SCWE weaknesses

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
