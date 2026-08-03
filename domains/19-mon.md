# CSPTF-DOM-19 - MON: Monitoreo, detección, analítica on-chain y fraude

**English:** Monitoring, Detection, On-chain Analytics and Fraud

## Purpose

Evaluar cobertura, calidad, correlación y respuesta de telemetría off-chain/on-chain frente a fraude, compromiso y anomalías económicas.

## Principal assets

- SIEM
- on-chain analytics
- fraud rules
- wallet monitoring
- node logs
- contract events
- alerting
- case management

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-MON-001 | Estrategia y cobertura de telemetría | AP1 |
| CSPTF-CTRL-MON-002 | Calidad, tiempo y sincronización de logs | AP1 |
| CSPTF-CTRL-MON-003 | Detecciones on-chain y off-chain | AP2 |
| CSPTF-CTRL-MON-004 | Monitoreo de wallets y contratos críticos | AP2 |
| CSPTF-CTRL-MON-005 | Detección de fraude y abuso | AP2 |
| CSPTF-CTRL-MON-006 | Correlación, enriquecimiento y atribución | AP3 |
| CSPTF-CTRL-MON-007 | Gestión de alertas y casos | AP3 |
| CSPTF-CTRL-MON-008 | Validación continua de detecciones | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-MON-001 | Mapear telemetría a activos y amenazas | AP1 | Revisión y validación controlada |
| CSPTF-TEST-MON-002 | Validar fuentes, integridad y retención de logs | AP1 | Revisión y validación controlada |
| CSPTF-TEST-MON-003 | Comprobar sincronización temporal | AP1 | Revisión y validación controlada |
| CSPTF-TEST-MON-004 | Evaluar eventos de contratos y nodos | AP2 | Revisión y validación controlada |
| CSPTF-TEST-MON-005 | Revisar monitoreo de wallets críticas | AP2 | Revisión y validación controlada |
| CSPTF-TEST-MON-006 | Probar detecciones de cambios administrativos | AP2 | Revisión y validación controlada |
| CSPTF-TEST-MON-007 | Evaluar reglas de fraude y anomalías | AP2 | Revisión y validación controlada |
| CSPTF-TEST-MON-008 | Comprobar correlación on-chain/off-chain | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-MON-009 | Validar enriquecimiento y contexto | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-MON-010 | Revisar SLAs y escalamiento | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-MON-011 | Ejecutar emulación segura de señales | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-MON-012 | Medir cobertura, precisión y mejora continua | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-MON-001 | Actividad maliciosa no detectada |
| CSPTF-THRT-MON-002 | Supresión o manipulación de telemetría |
| CSPTF-THRT-MON-003 | Falsos positivos que ocultan señales reales |
| CSPTF-THRT-MON-004 | Fraude coordinado multicanal |
| CSPTF-THRT-MON-005 | Respuesta tardía a drenaje o compromiso |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-MON-001 | Logs críticos ausentes |
| CSPTF-WEAK-MON-002 | Eventos sin contexto de negocio |
| CSPTF-WEAK-MON-003 | Alertas sin owner |
| CSPTF-WEAK-MON-004 | Cobertura no medida |
| CSPTF-WEAK-MON-005 | Retención insuficiente para investigación |

## Crosswalk

- MITRE AADAPT tactics: Defense Evasion, Collection, Impact, Fraud
- NIST CSF 2.0 functions: DE, RS
- OWASP alignment: SCSTG logging and event verification

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
