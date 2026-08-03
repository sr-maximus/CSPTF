# CSPTF-DOM-08 - DEF: DeFi y seguridad económica

**English:** DeFi and Economic Security

## Purpose

Evaluar solvencia, precios, incentivos, liquidaciones, AMM, préstamos, vaults, MEV y ataques de composición económica.

## Principal assets

- pools
- AMM
- lending markets
- vaults
- liquidation bots
- governance tokens
- collateral
- fee models

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-DEF-001 | Invariantes económicas y solvencia | AP1 |
| CSPTF-CTRL-DEF-002 | Modelos de precio y deslizamiento | AP1 |
| CSPTF-CTRL-DEF-003 | Colateralización y liquidación | AP2 |
| CSPTF-CTRL-DEF-004 | Resistencia a manipulación temporal | AP2 |
| CSPTF-CTRL-DEF-005 | Límites, caps y circuit breakers | AP2 |
| CSPTF-CTRL-DEF-006 | Contabilidad de fees, shares y rewards | AP3 |
| CSPTF-CTRL-DEF-007 | Riesgo de composabilidad y dependencia | AP3 |
| CSPTF-CTRL-DEF-008 | Simulación económica y monitoreo | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-DEF-001 | Modelar invariantes económicas | AP1 | Revisión y validación controlada |
| CSPTF-TEST-DEF-002 | Validar valoración de activos y shares | AP1 | Revisión y validación controlada |
| CSPTF-TEST-DEF-003 | Evaluar colateral y factores de liquidación | AP1 | Revisión y validación controlada |
| CSPTF-TEST-DEF-004 | Comprobar exposición a flash liquidity | AP2 | Revisión y validación controlada |
| CSPTF-TEST-DEF-005 | Analizar slippage, profundidad y concentración | AP2 | Revisión y validación controlada |
| CSPTF-TEST-DEF-006 | Revisar caps, pausas y límites dinámicos | AP2 | Revisión y validación controlada |
| CSPTF-TEST-DEF-007 | Evaluar redondeo, precisión y acumulación de fees | AP2 | Revisión y validación controlada |
| CSPTF-TEST-DEF-008 | Comprobar incentivos y ataques de gobernanza económica | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-DEF-009 | Analizar MEV, ordenamiento y sandwich risk | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-DEF-010 | Ejecutar simulaciones históricas y de estrés | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-DEF-011 | Validar insolvencia y socialización de pérdidas | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-DEF-012 | Comprobar alertas de manipulación económica | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-DEF-001 | Manipulación de precio y extracción de valor |
| CSPTF-THRT-DEF-002 | Insolvencia por liquidaciones fallidas |
| CSPTF-THRT-DEF-003 | Ataque de liquidez temporal |
| CSPTF-THRT-DEF-004 | Drenaje por error de contabilidad de shares |
| CSPTF-THRT-DEF-005 | Captura de gobernanza económica |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-DEF-001 | Oráculo poco robusto |
| CSPTF-WEAK-DEF-002 | Caps inexistentes |
| CSPTF-WEAK-DEF-003 | Supuestos de liquidez irreales |
| CSPTF-WEAK-DEF-004 | Redondeo acumulativo |
| CSPTF-WEAK-DEF-005 | Dependencia de una sola ruta de liquidación |

## Crosswalk

- MITRE AADAPT tactics: Execution, Impact, Fraud
- NIST CSF 2.0 functions: ID, PR, DE
- OWASP alignment: SCSTG DeFi and economic testing; SCSVS business logic

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
