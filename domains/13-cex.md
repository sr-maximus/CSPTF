# CSPTF-DOM-13 - CEX: Exchanges centralizados, brokers e infraestructura de mercado

**English:** Centralized Exchanges, Brokers and Market Infrastructure

## Purpose

Evaluar onboarding, cuentas, trading, depósitos, retiros, matching, custodia, reservas, fraude y procesos operacionales de plataformas centralizadas.

## Principal assets

- accounts
- matching engine
- OMS
- deposit services
- withdrawal services
- custody
- market data
- treasury

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-CEX-001 | Seguridad de cuentas y autenticación | AP1 |
| CSPTF-CTRL-CEX-002 | Integridad de órdenes y matching | AP1 |
| CSPTF-CTRL-CEX-003 | Depósitos, confirmaciones y atribución | AP2 |
| CSPTF-CTRL-CEX-004 | Retiros, límites y aprobaciones | AP2 |
| CSPTF-CTRL-CEX-005 | Custodia y tesorería segregadas | AP2 |
| CSPTF-CTRL-CEX-006 | Market data y prevención de abuso | AP3 |
| CSPTF-CTRL-CEX-007 | Reservas, pasivos y reconciliación | AP3 |
| CSPTF-CTRL-CEX-008 | Fraude, monitoreo y continuidad operacional | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-CEX-001 | Evaluar registro, recuperación y MFA | AP1 | Revisión y validación controlada |
| CSPTF-TEST-CEX-002 | Revisar autorización de cuentas y roles | AP1 | Revisión y validación controlada |
| CSPTF-TEST-CEX-003 | Validar integridad del ciclo de órdenes | AP1 | Revisión y validación controlada |
| CSPTF-TEST-CEX-004 | Comprobar idempotencia y concurrencia | AP2 | Revisión y validación controlada |
| CSPTF-TEST-CEX-005 | Evaluar depósitos y políticas de confirmación | AP2 | Revisión y validación controlada |
| CSPTF-TEST-CEX-006 | Revisar retiros, allowlists y cooling-off | AP2 | Revisión y validación controlada |
| CSPTF-TEST-CEX-007 | Validar segregación de custodia y tesorería | AP2 | Revisión y validación controlada |
| CSPTF-TEST-CEX-008 | Comprobar reconciliación de libros y cadena | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-CEX-009 | Evaluar manipulación de market data | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-CEX-010 | Revisar controles antifraude y abuso interno | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-CEX-011 | Simular interrupción del matching en laboratorio | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-CEX-012 | Validar continuidad, reservas y comunicación | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-CEX-001 | Toma de cuenta y retiro fraudulento |
| CSPTF-THRT-CEX-002 | Manipulación o pérdida de órdenes |
| CSPTF-THRT-CEX-003 | Atribución incorrecta de depósitos |
| CSPTF-THRT-CEX-004 | Abuso interno de tesorería |
| CSPTF-THRT-CEX-005 | Descuadre entre reservas y pasivos |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-CEX-001 | Recuperación de cuenta débil |
| CSPTF-WEAK-CEX-002 | Idempotencia insuficiente |
| CSPTF-WEAK-CEX-003 | Límites de retiro inadecuados |
| CSPTF-WEAK-CEX-004 | Reconciliación tardía |
| CSPTF-WEAK-CEX-005 | Segregación de funciones deficiente |

## Crosswalk

- MITRE AADAPT tactics: Initial Access, Credential Access, Lateral Movement, Collection, Impact, Fraud
- NIST CSF 2.0 functions: GV, PR, DE, RS, RC
- OWASP alignment: OWASP scope is partial; CSPTF extension

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
