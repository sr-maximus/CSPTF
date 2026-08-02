# CSPTF-DOM-01 - GOV: Gobernanza, alcance y modelado de amenazas

**English:** Governance, Scope and Threat Modeling

## Purpose

Establecer autorización, objetivos, límites, responsables, supuestos, apetito de riesgo y modelos de amenaza antes de ejecutar cualquier prueba.

## Principal assets

- mandato de evaluación
- inventario de activos
- matriz RACI
- modelo de amenazas
- presupuestos de pérdida
- criterios de detención

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-GOV-001 | Gobierno y responsabilidad del programa | AP1 |
| CSPTF-CTRL-GOV-002 | Inventario y clasificación de activos digitales | AP1 |
| CSPTF-CTRL-GOV-003 | Reglas de compromiso y autorización | AP2 |
| CSPTF-CTRL-GOV-004 | Modelado de amenazas orientado al negocio | AP2 |
| CSPTF-CTRL-GOV-005 | Gestión de terceros y dependencias críticas | AP2 |
| CSPTF-CTRL-GOV-006 | Presupuestos de riesgo, pérdida y transacción | AP3 |
| CSPTF-CTRL-GOV-007 | Gestión de cambios durante la evaluación | AP3 |
| CSPTF-CTRL-GOV-008 | Aceptación, excepción y cierre de hallazgos | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-GOV-001 | Verificar la autorización y el alcance formal | AP1 | Revisión y validación controlada |
| CSPTF-TEST-GOV-002 | Validar el inventario de activos y flujos de valor | AP1 | Revisión y validación controlada |
| CSPTF-TEST-GOV-003 | Revisar roles, escalamiento y autoridad de detención | AP1 | Revisión y validación controlada |
| CSPTF-TEST-GOV-004 | Evaluar el modelo de amenazas y supuestos | AP2 | Revisión y validación controlada |
| CSPTF-TEST-GOV-005 | Comprobar exclusiones y dependencias de terceros | AP2 | Revisión y validación controlada |
| CSPTF-TEST-GOV-006 | Validar presupuestos de pérdida, gas y transacciones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-GOV-007 | Revisar ventanas, monitoreo y comunicaciones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-GOV-008 | Comprobar criterios de evidencia y custodia | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-GOV-009 | Evaluar la gestión de cambios de alcance | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-GOV-010 | Validar el tratamiento de datos sensibles | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-GOV-011 | Revisar aceptación de riesgo y excepciones | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-GOV-012 | Ejecutar una mesa de crisis previa a pruebas críticas | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-GOV-001 | Pruebas sin autorización efectiva |
| CSPTF-THRT-GOV-002 | Activos críticos omitidos del alcance |
| CSPTF-THRT-GOV-003 | Conflictos de interés o independencia insuficiente |
| CSPTF-THRT-GOV-004 | Cambios no controlados durante el ejercicio |
| CSPTF-THRT-GOV-005 | Aceptación de riesgo sin autoridad competente |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-GOV-001 | Alcance ambiguo |
| CSPTF-WEAK-GOV-002 | Inventario incompleto |
| CSPTF-WEAK-GOV-003 | Reglas de detención inexistentes |
| CSPTF-WEAK-GOV-004 | RACI no definido |
| CSPTF-WEAK-GOV-005 | Evidencia sin cadena de custodia |

## Crosswalk

- MITRE AADAPT tactics: Reconnaissance, Resource Development, Initial Access, Impact, Fraud
- NIST CSF 2.0 functions: GV, ID
- OWASP alignment: SCSTG engagement planning; SCSVS governance context

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
