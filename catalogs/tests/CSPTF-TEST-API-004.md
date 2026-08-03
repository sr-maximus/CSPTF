# CSPTF-TEST-API-004 - Revisar métodos RPC sensibles

- **Domain:** API
- **Minimum assurance:** AP2
- **Test type:** Revisión y validación controlada
- **Related control:** CSPTF-CTRL-API-002
- **Status:** draft

## Objective

Determinar, mediante evidencia verificable y validación no destructiva, si revisar métodos rpc sensibles reduce el riesgo esperado.

## Authorized environment

Producción solo para lectura y observación; cualquier acción activa requiere autorización explícita. Preferir laboratorio, testnet, staging o fork.

## Prerequisites

Alcance firmado; owner técnico disponible; respaldo o rollback; monitoreo activo; criterios de detención; datos de prueba; presupuesto de transacción o pérdida igual a cero salvo autorización expresa.

## Procedure

1. Confirmar que el test ID, objetivo, activo, entorno, ventana y operador están expresamente autorizados.
2. Obtener la línea base de diseño, configuración y evidencia relacionada con **revisar métodos rpc sensibles** sin modificar el sistema.
3. Definir el invariante o resultado esperado, datos sintéticos, límites, criterios de detención y método de rollback/reconciliación.
4. Ejecutar una validación no destructiva de **revisar métodos rpc sensibles** mediante consultas de solo lectura, revisión, test account, simulación, testnet o fork determinístico.
5. Correlacionar el resultado con logs, estados on-chain/off-chain, versiones, hashes y controles relacionados; descartar falsos positivos.
6. Restaurar o eliminar artefactos de prueba, reconciliar balances/estado, preservar evidencia y registrar pass, fail, not-tested o inconclusive.

## Evidence

Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.

## Pass criteria

Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar métodos rpc sensibles.

## Fail criteria

Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

## Safety constraints

- Do not use real customer funds or identities.
- Do not exceed approved transaction, rate, gas, volume or time budgets.
- Do not perform destructive, availability-impacting, consensus-disrupting or market-manipulating variants unless separately authorized.
- Stop on unexpected state, balance, availability, privacy or third-party impact.
- A test description never grants authorization.

## Threat alignment

AADAPT tactics: Reconnaissance; Initial Access; Execution; Credential Access; Collection; Impact
