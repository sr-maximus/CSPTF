# CSPTF-DOM-18 - REG: Privacidad, cumplimiento, AML/KYT y protección de datos

**English:** Privacy, Compliance, AML/KYT and Data Protection

## Purpose

Evaluar obligaciones aplicables, minimización, trazabilidad, privacidad, controles AML/KYT y tratamiento seguro de datos personales y financieros.

## Principal assets

- PII
- KYC records
- transaction monitoring
- sanctions screening
- travel rule data
- audit records
- privacy notices
- retention systems

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-REG-001 | Inventario de obligaciones y jurisdicciones | AP1 |
| CSPTF-CTRL-REG-002 | Minimización y propósito de datos | AP1 |
| CSPTF-CTRL-REG-003 | Seguridad de KYC y datos sensibles | AP2 |
| CSPTF-CTRL-REG-004 | AML, KYT y screening basado en riesgo | AP2 |
| CSPTF-CTRL-REG-005 | Travel Rule y transferencia segura | AP2 |
| CSPTF-CTRL-REG-006 | Retención, borrado y derechos | AP3 |
| CSPTF-CTRL-REG-007 | Trazabilidad y evidencia regulatoria | AP3 |
| CSPTF-CTRL-REG-008 | Privacidad por diseño en datos on-chain | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-REG-001 | Identificar obligaciones y alcance regulatorio | AP1 | Revisión y validación controlada |
| CSPTF-TEST-REG-002 | Revisar inventario y clasificación de datos | AP1 | Revisión y validación controlada |
| CSPTF-TEST-REG-003 | Validar minimización y propósito | AP1 | Revisión y validación controlada |
| CSPTF-TEST-REG-004 | Evaluar protección de datos KYC | AP2 | Revisión y validación controlada |
| CSPTF-TEST-REG-005 | Comprobar controles AML y KYT | AP2 | Revisión y validación controlada |
| CSPTF-TEST-REG-006 | Revisar screening y manejo de falsos positivos | AP2 | Revisión y validación controlada |
| CSPTF-TEST-REG-007 | Validar Travel Rule y transferencias | AP2 | Revisión y validación controlada |
| CSPTF-TEST-REG-008 | Comprobar retención y eliminación | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-REG-009 | Evaluar privacidad y linkability on-chain | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-REG-010 | Revisar accesos y trazabilidad regulatoria | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-REG-011 | Validar respuesta a solicitudes de titulares | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-REG-012 | Ejecutar tabletop de incidente de datos | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-REG-001 | Exposición de datos KYC |
| CSPTF-THRT-REG-002 | Evasión de monitoreo transaccional |
| CSPTF-THRT-REG-003 | Transferencia regulada sin datos requeridos |
| CSPTF-THRT-REG-004 | Reidentificación o linkability indebida |
| CSPTF-THRT-REG-005 | Retención o uso incompatible de datos |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-REG-001 | Datos KYC sobreexpuestos |
| CSPTF-WEAK-REG-002 | Reglas AML estáticas |
| CSPTF-WEAK-REG-003 | Minimización insuficiente |
| CSPTF-WEAK-REG-004 | Cifrado o tokenización inadecuados |
| CSPTF-WEAK-REG-005 | Obligaciones no mapeadas por jurisdicción |

## Crosswalk

- MITRE AADAPT tactics: Collection, Defense Evasion, Impact, Fraud
- NIST CSF 2.0 functions: GV, ID, PR
- OWASP alignment: OWASP privacy and data protection themes

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
