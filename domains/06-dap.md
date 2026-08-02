# CSPTF-DOM-06 - DAP: dApps, frontend, sesiones e integración de wallets

**English:** dApps, Frontend, Sessions and Wallet Integration

## Purpose

Evaluar aplicaciones cliente, sesiones, proveedores Web3, solicitudes de firma, resolución de red y controles que conectan usuarios con funciones on-chain.

## Principal assets

- frontend
- backend BFF
- wallet connectors
- sesiones
- deep links
- firmas EIP-712
- DNS/CDN
- proveedores RPC

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-DAP-001 | Integridad de frontend y distribución | AP1 |
| CSPTF-CTRL-DAP-002 | Vinculación segura de sesión y wallet | AP1 |
| CSPTF-CTRL-DAP-003 | Presentación clara de solicitudes de firma | AP2 |
| CSPTF-CTRL-DAP-004 | Validación de red, cadena y contrato | AP2 |
| CSPTF-CTRL-DAP-005 | Autenticación y autorización off-chain | AP2 |
| CSPTF-CTRL-DAP-006 | Protección de APIs y secretos de cliente | AP3 |
| CSPTF-CTRL-DAP-007 | Seguridad de contenido, DNS y dependencias | AP3 |
| CSPTF-CTRL-DAP-008 | Detección de manipulación y respuesta | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-DAP-001 | Revisar integridad del artefacto frontend | AP1 | Revisión y validación controlada |
| CSPTF-TEST-DAP-002 | Validar vinculación de cuenta, sesión y wallet | AP1 | Revisión y validación controlada |
| CSPTF-TEST-DAP-003 | Evaluar mensajes y transacciones solicitadas | AP1 | Revisión y validación controlada |
| CSPTF-TEST-DAP-004 | Comprobar chain ID, contrato y red objetivo | AP2 | Revisión y validación controlada |
| CSPTF-TEST-DAP-005 | Revisar autenticación y autorización off-chain | AP2 | Revisión y validación controlada |
| CSPTF-TEST-DAP-006 | Evaluar exposición de secretos y configuración | AP2 | Revisión y validación controlada |
| CSPTF-TEST-DAP-007 | Comprobar protección contra inyección y XSS | AP2 | Revisión y validación controlada |
| CSPTF-TEST-DAP-008 | Revisar dependencias, CDN y carga remota | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-DAP-009 | Validar deep links y redirecciones | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-DAP-010 | Evaluar disponibilidad y confianza del RPC | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-DAP-011 | Simular manipulación de interfaz en laboratorio | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-DAP-012 | Comprobar detección y revocación de sesiones | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-DAP-001 | Manipulación de interfaz para desviar fondos |
| CSPTF-THRT-DAP-002 | Firma engañosa o autorización excesiva |
| CSPTF-THRT-DAP-003 | Secuestro de sesión vinculada a wallet |
| CSPTF-THRT-DAP-004 | Sustitución de RPC, red o contrato |
| CSPTF-THRT-DAP-005 | Compromiso de dominio o cadena de distribución |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-DAP-001 | Firmas ciegas |
| CSPTF-WEAK-DAP-002 | Chain ID no validado |
| CSPTF-WEAK-DAP-003 | Sesiones no ligadas al firmante |
| CSPTF-WEAK-DAP-004 | Dependencias remotas sin integridad |
| CSPTF-WEAK-DAP-005 | Mensajes de riesgo poco comprensibles |

## Crosswalk

- MITRE AADAPT tactics: Initial Access, Execution, Credential Access, Collection, Fraud
- NIST CSF 2.0 functions: PR, DE
- OWASP alignment: SCSTG dApp and client interaction; SCSVS communications

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
