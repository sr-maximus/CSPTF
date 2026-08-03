# CSPTF-DOM-16 - IAM: Identidad, acceso privilegiado y riesgo interno

**English:** Identity, Privileged Access and Insider Risk

## Purpose

Evaluar identidades humanas y de máquina, acceso privilegiado, segregación, revisiones, monitoreo y controles frente a fraude o abuso interno.

## Principal assets

- workforce identities
- service accounts
- PAM
- break-glass accounts
- admin consoles
- signer roles
- vendors
- joiner-mover-leaver

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-IAM-001 | Gobierno del ciclo de identidad | AP1 |
| CSPTF-CTRL-IAM-002 | MFA resistente y autenticación fuerte | AP1 |
| CSPTF-CTRL-IAM-003 | Mínimo privilegio y acceso just-in-time | AP2 |
| CSPTF-CTRL-IAM-004 | Segregación de funciones críticas | AP2 |
| CSPTF-CTRL-IAM-005 | PAM, sesiones y cuentas break-glass | AP2 |
| CSPTF-CTRL-IAM-006 | Identidades de máquina y workloads | AP3 |
| CSPTF-CTRL-IAM-007 | Monitoreo de comportamiento privilegiado | AP3 |
| CSPTF-CTRL-IAM-008 | Gestión de terceros y salida segura | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-IAM-001 | Revisar altas, cambios y bajas | AP1 | Revisión y validación controlada |
| CSPTF-TEST-IAM-002 | Evaluar MFA y recuperación de acceso | AP1 | Revisión y validación controlada |
| CSPTF-TEST-IAM-003 | Comprobar privilegios efectivos | AP1 | Revisión y validación controlada |
| CSPTF-TEST-IAM-004 | Validar segregación de funciones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-IAM-005 | Revisar PAM y grabación de sesiones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-IAM-006 | Comprobar cuentas break-glass | AP2 | Revisión y validación controlada |
| CSPTF-TEST-IAM-007 | Evaluar identidades de máquina | AP2 | Revisión y validación controlada |
| CSPTF-TEST-IAM-008 | Revisar accesos de terceros | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-IAM-009 | Validar recertificación periódica | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-IAM-010 | Comprobar monitoreo de acciones críticas | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-IAM-011 | Ejecutar tabletop de abuso interno | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-IAM-012 | Validar revocación y preservación de evidencia | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-IAM-001 | Abuso de administrador o firmante |
| CSPTF-THRT-IAM-002 | Toma de cuenta privilegiada |
| CSPTF-THRT-IAM-003 | Persistencia de excolaborador o tercero |
| CSPTF-THRT-IAM-004 | Colusión entre funciones críticas |
| CSPTF-THRT-IAM-005 | Uso no autorizado de identidad de máquina |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-IAM-001 | Privilegios permanentes |
| CSPTF-WEAK-IAM-002 | MFA recuperable por canal débil |
| CSPTF-WEAK-IAM-003 | Segregación de funciones incompleta |
| CSPTF-WEAK-IAM-004 | Cuentas compartidas |
| CSPTF-WEAK-IAM-005 | Recertificación insuficiente |

## Crosswalk

- MITRE AADAPT tactics: Initial Access, Privilege Escalation, Credential Access, Lateral Movement, Collection, Fraud
- NIST CSF 2.0 functions: GV, PR, DE
- OWASP alignment: OWASP ASVS authentication and access control

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
