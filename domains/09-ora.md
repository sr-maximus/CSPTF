# CSPTF-DOM-09 - ORA: Oráculos, datos externos y automatización

**English:** Oracles, External Data and Automation

## Purpose

Evaluar autenticidad, frescura, disponibilidad, agregación y uso seguro de precios, datos, keepers y automatizaciones off-chain.

## Principal assets

- price feeds
- data providers
- keepers
- relayers
- webhooks
- time sources
- fallbacks
- aggregation logic

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-ORA-001 | Diversidad y gobernanza de fuentes | AP1 |
| CSPTF-CTRL-ORA-002 | Frescura, heartbeat y staleness | AP1 |
| CSPTF-CTRL-ORA-003 | Agregación y tolerancia a outliers | AP2 |
| CSPTF-CTRL-ORA-004 | Autenticidad e integridad de datos | AP2 |
| CSPTF-CTRL-ORA-005 | Fallbacks y degradación segura | AP2 |
| CSPTF-CTRL-ORA-006 | Seguridad de keepers y automatización | AP3 |
| CSPTF-CTRL-ORA-007 | Límites de uso y sanity checks | AP3 |
| CSPTF-CTRL-ORA-008 | Monitoreo y respuesta de oráculos | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-ORA-001 | Inventariar fuentes y dependencias | AP1 | Revisión y validación controlada |
| CSPTF-TEST-ORA-002 | Validar frescura y heartbeat | AP1 | Revisión y validación controlada |
| CSPTF-TEST-ORA-003 | Evaluar agregación y outliers | AP1 | Revisión y validación controlada |
| CSPTF-TEST-ORA-004 | Comprobar autenticidad de actualizaciones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-ORA-005 | Revisar límites y sanity checks | AP2 | Revisión y validación controlada |
| CSPTF-TEST-ORA-006 | Evaluar fallbacks y modo degradado | AP2 | Revisión y validación controlada |
| CSPTF-TEST-ORA-007 | Comprobar permisos de actualización | AP2 | Revisión y validación controlada |
| CSPTF-TEST-ORA-008 | Revisar keepers, jobs y secretos | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-ORA-009 | Simular indisponibilidad de fuente | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-ORA-010 | Evaluar manipulación de mercado subyacente | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-ORA-011 | Comprobar observabilidad y alertas | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-ORA-012 | Validar recuperación tras datos incorrectos | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-ORA-001 | Manipulación de feed |
| CSPTF-THRT-ORA-002 | Uso de datos obsoletos |
| CSPTF-THRT-ORA-003 | Compromiso de updater o keeper |
| CSPTF-THRT-ORA-004 | Indisponibilidad coordinada de fuentes |
| CSPTF-THRT-ORA-005 | Desviación de mercado de referencia |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-ORA-001 | Fuente única |
| CSPTF-WEAK-ORA-002 | Staleness no controlado |
| CSPTF-WEAK-ORA-003 | Agregación débil |
| CSPTF-WEAK-ORA-004 | Fallback inseguro |
| CSPTF-WEAK-ORA-005 | Límites de precio ausentes |

## Crosswalk

- MITRE AADAPT tactics: Execution, Defense Evasion, Impact, Fraud
- NIST CSF 2.0 functions: PR, DE, RS
- OWASP alignment: SCSTG oracle security; SCSVS oracle controls

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
