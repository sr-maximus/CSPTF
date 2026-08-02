# 03 - Ciclo de evaluación

## Fase 0 - Autorización y gobernanza

Confirmar autoridad, independencia, alcance, RoE, presupuestos, seguridad, comunicación y restricciones legales.

**Gate:** autorización y test plan aprobados.

## Fase 1 - Contexto y descomposición

Modelar arquitectura, fronteras, activos, identidades, datos y flujos de valor. Definir invariantes de seguridad y solvencia.

**Gate:** system model aceptado por owners técnicos y de negocio.

## Fase 2 - Threat intelligence y attack surface

Usar AADAPT, ATT&CK, incidentes públicos, abuse cases y dependency intelligence.

**Gate:** threat model priorizado.

## Fase 3 - Tailoring y diseño

Seleccionar dominios, controles, tests y perfil. Definir ambientes, tools, datasets, criterios y limitaciones.

**Gate:** test matrix aprobada.

## Fase 4 - Evaluación no invasiva

Revisar diseño, código, configuración, permisos, logs, builds, reservas y runbooks.

**Gate:** evidencia completa.

## Fase 5 - Validación adversarial controlada

Usar identidades de prueba, datos sintéticos, requests no destructivos y actividad acotada.

**Gate:** sin condición de seguridad pendiente.

## Fase 6 - Simulación económica y de protocolo

Modelar incentivos, liquidez, oráculos, ordering, liquidaciones, consenso, cross-chain y fallas en ambiente determinístico.

**Gate:** invariantes y limitaciones documentados.

## Fase 7 - Validación segura de exploitability

Demostrar solo cuando sea necesario y preferiblemente en fork, testnet o laboratorio. Producción exige autorización excepcional.

**Gate:** prueba reproducible, cleanup y ausencia de efectos no controlados.

## Fase 8 - Detección y respuesta

Validar telemetría, alertas, triage, contención, reconciliación, comunicación y recovery.

**Gate:** gaps asignados.

## Fase 9 - Riesgo y reporte

Crear findings con evidencia, root cause, path, impacto, confidence, assets, riesgo y remediación.

**Gate:** quality review y factual validation.

## Fase 10 - Remediación y retest

Repetir la condición y rutas adyacentes; verificar invariantes.

**Gate:** closure evidence o residual risk aceptado.

## Fase 11 - Aseguramiento continuo

Rastrear cambios de código, dependencias, contratos, signers, parámetros, infraestructura, liquidez y amenazas.
