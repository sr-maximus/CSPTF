# 02 - Reglas de compromiso (Rules of Engagement)

## Autorización obligatoria

Ningún test comienza sin autorización firmada que identifique owner, tester, sistemas, ambientes, fechas, contactos, técnicas y límites. La autorización DEBE permitir a un tercero decidir si una acción estaba permitida.

## Prioridad de ambientes

Debe utilizarse el ambiente más seguro que responda la pregunta:

1. revisión estática y documental;
2. unit/integration local;
3. simulación aislada;
4. fork determinístico o shadow environment;
5. testnet;
6. staging/preproducción;
7. observación read-only de producción;
8. prueba activa de producción expresamente autorizada.

Descender exige razón documentada y controles adicionales.

## Salvaguardas de producción

Las pruebas activas requieren:

- tests IDs individualizados;
- approver y stop authority;
- monitoring y canal de comunicación;
- backup, rollback o recuperación compensatoria;
- cero activos de clientes por defecto;
- límites de transacciones, gas, volumen y tiempo;
- rate/concurrency limits;
- reconciliación antes/después;
- criterios de terminación;
- conversión a incidente;
- custodia de evidencia y divulgación.

## Acciones prohibidas por defecto

Sin autorización individual, NO DEBE:

- mover, bloquear, quemar o exponer activos reales de clientes;
- degradar consenso, disponibilidad o integridad de mercado;
- manipular precios o crear actividad engañosa;
- usar credenciales, seeds o keys robadas;
- crear persistencia no controlada;
- evadir controles legales de identidad, sanciones o crimen financiero;
- acceder a datos ajenos al objetivo;
- divulgar una falla no corregida que aumente materialmente el riesgo.

## Stop conditions

Detener ante movimiento inesperado, posible afectación de integridad/disponibilidad/solvencia, scope incierto, pérdida de monitoring, exposición de terceros, actividad adversaria real, imposibilidad de rollback/reconciliación o instrucción del stop authority.

## Evidencia y limpieza

Cada acción activa debe registrar operador, tiempo, target, propósito, efecto esperado, efecto observado y cleanup. Identidades, allowances, roles, contratos, datos e infraestructura de prueba deben revocarse o eliminarse.
