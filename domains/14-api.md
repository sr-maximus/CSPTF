# CSPTF-DOM-14 - API: APIs, RPC, WebSocket y plataformas para desarrolladores

**English:** APIs, RPC, WebSocket and Developer Platforms

## Purpose

Evaluar autenticación, autorización, exposición, rate limiting, seguridad de métodos, datos y disponibilidad en interfaces programáticas.

## Principal assets

- REST APIs
- GraphQL
- JSON-RPC
- WebSocket
- API keys
- developer portals
- webhooks
- indexers

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-API-001 | Inventario y clasificación de interfaces | AP1 |
| CSPTF-CTRL-API-002 | Autenticación y gestión de credenciales | AP1 |
| CSPTF-CTRL-API-003 | Autorización por objeto y función | AP2 |
| CSPTF-CTRL-API-004 | Métodos RPC y superficies administrativas | AP2 |
| CSPTF-CTRL-API-005 | Rate limiting, cuotas y antiabuso | AP2 |
| CSPTF-CTRL-API-006 | Validación de entradas y salidas | AP3 |
| CSPTF-CTRL-API-007 | Webhooks, WebSocket y eventos | AP3 |
| CSPTF-CTRL-API-008 | Observabilidad, versionado y retiro seguro | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-API-001 | Inventariar endpoints, métodos y versiones | AP1 | Revisión y validación controlada |
| CSPTF-TEST-API-002 | Evaluar autenticación y ciclo de API keys | AP1 | Revisión y validación controlada |
| CSPTF-TEST-API-003 | Comprobar autorización por objeto | AP1 | Revisión y validación controlada |
| CSPTF-TEST-API-004 | Revisar métodos RPC sensibles | AP2 | Revisión y validación controlada |
| CSPTF-TEST-API-005 | Validar rate limiting y cuotas | AP2 | Revisión y validación controlada |
| CSPTF-TEST-API-006 | Evaluar validación de parámetros | AP2 | Revisión y validación controlada |
| CSPTF-TEST-API-007 | Comprobar filtrado de datos sensibles | AP2 | Revisión y validación controlada |
| CSPTF-TEST-API-008 | Revisar WebSocket, suscripciones y sesiones | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-API-009 | Validar autenticidad de webhooks | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-API-010 | Evaluar errores, logs y exposición de stack | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-API-011 | Comprobar versionado y compatibilidad | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-API-012 | Ejecutar pruebas de resiliencia no destructivas | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-API-001 | Abuso de método RPC administrativo |
| CSPTF-THRT-API-002 | Acceso no autorizado a objetos |
| CSPTF-THRT-API-003 | Exfiltración de datos por API |
| CSPTF-THRT-API-004 | Agotamiento de cuota o recursos |
| CSPTF-THRT-API-005 | Falsificación de webhook o evento |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-API-001 | API keys de larga duración |
| CSPTF-WEAK-API-002 | Autorización a nivel objeto ausente |
| CSPTF-WEAK-API-003 | RPC administrativo expuesto |
| CSPTF-WEAK-API-004 | Rate limits inconsistentes |
| CSPTF-WEAK-API-005 | Errores excesivamente informativos |

## Crosswalk

- MITRE AADAPT tactics: Reconnaissance, Initial Access, Execution, Credential Access, Collection, Impact
- NIST CSF 2.0 functions: PR, DE
- OWASP alignment: OWASP API Security Top 10; SCSTG RPC interactions

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
