# CSPTF-DOM-04 - KEY: Gestión de claves, custodia, wallets y firma

**English:** Key Management, Custody, Wallets and Signing

## Purpose

Evaluar generación, almacenamiento, uso, recuperación, rotación y destrucción de claves, junto con políticas de firma y custodia.

## Principal assets

- hot wallets
- cold wallets
- HSM
- MPC
- seed phrases
- firmantes
- políticas de retiro
- recuperación

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-KEY-001 | Ceremonias de generación y respaldo | AP1 |
| CSPTF-CTRL-KEY-002 | Custodia segregada por propósito | AP1 |
| CSPTF-CTRL-KEY-003 | Políticas de firma y límites | AP2 |
| CSPTF-CTRL-KEY-004 | MPC, multisig y quorum | AP2 |
| CSPTF-CTRL-KEY-005 | Protección de hot wallets | AP2 |
| CSPTF-CTRL-KEY-006 | Cold storage y movimiento controlado | AP3 |
| CSPTF-CTRL-KEY-007 | Rotación, recuperación y destrucción | AP3 |
| CSPTF-CTRL-KEY-008 | Monitoreo y respuesta ante compromiso | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-KEY-001 | Revisar ceremonia de generación de claves | AP1 | Revisión y validación controlada |
| CSPTF-TEST-KEY-002 | Validar segregación hot, warm y cold | AP1 | Revisión y validación controlada |
| CSPTF-TEST-KEY-003 | Comprobar políticas de firma y límites | AP1 | Revisión y validación controlada |
| CSPTF-TEST-KEY-004 | Evaluar quorum, multisig o MPC | AP2 | Revisión y validación controlada |
| CSPTF-TEST-KEY-005 | Revisar almacenamiento y acceso a seeds | AP2 | Revisión y validación controlada |
| CSPTF-TEST-KEY-006 | Validar procesos de retiro y allowlists | AP2 | Revisión y validación controlada |
| CSPTF-TEST-KEY-007 | Comprobar rotación y revocación | AP2 | Revisión y validación controlada |
| CSPTF-TEST-KEY-008 | Evaluar recuperación y continuidad | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-KEY-009 | Revisar firmware y cadena de suministro de dispositivos | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-KEY-010 | Comprobar telemetría de operaciones de firma | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-KEY-011 | Ejecutar simulación de compromiso de firmante | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-KEY-012 | Validar destrucción y retiro de material | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-KEY-001 | Robo o exposición de clave privada |
| CSPTF-THRT-KEY-002 | Colusión o compromiso de firmantes |
| CSPTF-THRT-KEY-003 | Drenaje de hot wallet |
| CSPTF-THRT-KEY-004 | Abuso del proceso de recuperación |
| CSPTF-THRT-KEY-005 | Sustitución de dirección o transacción |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-KEY-001 | Seeds sin protección suficiente |
| CSPTF-WEAK-KEY-002 | Quorum mal configurado |
| CSPTF-WEAK-KEY-003 | Límites de firma ausentes |
| CSPTF-WEAK-KEY-004 | Recuperación no ensayada |
| CSPTF-WEAK-KEY-005 | Segregación de wallets insuficiente |

## Crosswalk

- MITRE AADAPT tactics: Credential Access, Collection, Defense Evasion, Impact, Fraud
- NIST CSF 2.0 functions: PR, DE, RS
- OWASP alignment: SCSTG authentication and authorization; SCSVS access control

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
