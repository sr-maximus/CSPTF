# CSPTF Specification 0.1.0-draft

**Crypto Security Penetration Testing Framework**  
**Especificación normativa en español**  
**Autor inicial:** Edwin Javier Peñuela Camacho  
**Fecha:** 2026-07-31  
**Licencia:** Apache-2.0

> **Estado:** borrador fundacional. No constituye certificación, garantía de seguridad ni autorización para ejecutar pruebas.

## Cómo utilizar esta especificación

CSPTF define un núcleo metodológico y catálogos trazables para evaluaciones de seguridad autorizadas de sistemas de activos digitales. Debe utilizarse junto con autorización legal, Rules of Engagement, límites técnicos, monitoreo, planes de recuperación y las fuentes especializadas aplicables.

Los términos **DEBE** y **NO DEBE** son normativos. **DEBERÍA** admite una excepción documentada y aceptada. **PUEDE** indica una opción. Un caso de prueba describe una forma de evaluación, pero nunca concede autorización.

## Contenido

1. Carta y objetivos
2. Alcance y taxonomía
3. Reglas de compromiso
4. Ciclo de evaluación
5. Perfiles de aseguramiento
6. Evidencia y confianza
7. Modelo de riesgo
8. Identificadores y hallazgos
9. Conformidad, reporte y glosario
10. Dominios, controles y pruebas
11. Amenazas y debilidades
12. Mapeos, investigación y validación

# 00 - Carta del framework

## Misión

CSPTF proporciona un método repetible, autorizado y basado en evidencia para evaluar la seguridad del sistema completo de activos digitales, no solamente el código de contratos inteligentes.

## Objetivos

- integrar testing técnico, económico, operacional y de gobernanza;
- establecer identificadores estables y catálogos machine-readable;
- exigir autorización explícita y ejecución segura;
- hacer visibles la calidad de evidencia y la incertidumbre;
- permitir tailoring para arquitecturas y cadenas diferentes;
- mapear sin duplicar estándares especializados;
- mejorar comparabilidad sin eliminar contexto;
- cerrar el ciclo mediante remediación y retest.

## Fuera de objetivo

CSPTF no es:

- autorización legal;
- garantía de seguridad, solvencia o cumplimiento;
- manual para explotar sistemas en producción;
- sustituto de prueba criptográfica, verificación formal o auditoría financiera;
- programa de certificación en v0.1;
- framework limitado a EVM o blockchains públicas.

## Unidad de evaluación

La unidad es el **sistema de activos digitales**, representado como un grafo de activos, actores, fronteras de confianza, componentes, estados, flujos de valor, dependencias externas y mecanismos de recuperación.

## Propiedades de calidad

Una evaluación conforme debe ser autorizada, delimitada, threat-informed, reproducible, respaldada por evidencia, contextualizada por riesgo, segura, explícita sobre limitaciones, revisable de manera independiente y cerrada mediante remediación y retest.

# 01 - Alcance y taxonomía

## Capas del sistema

CSPTF modela diez capas interdependientes:

1. negocio, gobernanza y regulación;
2. diseño económico y comportamiento de mercado;
3. identidad, custodia y firma;
4. aplicación y lógica de contratos;
5. protocolo, consenso y comunicación cross-chain;
6. APIs, clientes e interfaces;
7. infraestructura, cloud y supply chain;
8. telemetría, fraude y threat intelligence;
9. respuesta, recuperación y reservas;
10. terceros y dependencias del ecosistema.

## Registro de alcance

El scope DEBE identificar:

- propietario legal y autoridad que autoriza;
- objetivo de la evaluación;
- activos incluidos y exclusiones explícitas;
- cadenas, redes, ambientes y direcciones de contratos;
- versiones de source, bytecode, build y deployment;
- wallets, firmantes, custodia y límites;
- APIs, nodos, cloud accounts, dominios y repositories;
- terceros y límites de dependencia;
- clasificación de datos;
- ventanas y técnicas prohibidas;
- presupuestos de transacciones, gas y pérdida;
- rollback y reconciliación;
- reporte y divulgación.

## Arquetipos

Puede adaptarse a L1/L2, dApp, protocolo DeFi, bridge, CEX/broker, custodio, wallet provider, token/NFT platform, blockchain empresarial, operador de validadores/nodos o developer platform.

## Regla de tailoring

Un dominio solo puede marcarse no aplicable cuando se documentan ausencia de activos/supuestos, evidencia, transferencia del riesgo a terceros y aprobación de la exclusión.

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

# 04 - Perfiles de aseguramiento

Los perfiles determinan profundidad mínima, evidencia e independencia; no certifican seguridad.

| Perfil | Uso típico | Evidencia mínima | Profundidad | Independencia |
|---|---|---|---|---|
| AP1 Baseline | prototipos, pilotos de bajo valor | E2 configuración | review + validación funcional acotada | revisión interna calificada |
| AP2 Enhanced | producción con activos materiales | E3 observada | dynamic testing threat-informed | reviewer independiente del implementador |
| AP3 Critical | custodia, CEX, bridges, validadores, DeFi | E4 adversarial | simulation, property testing y failure exercises | equipo especialista independiente |
| AP4 Systemic | impacto material de mercado/institucional/cross-chain | E5 independiente | multi-team review, crisis y modelado sistémico | assurance organizacionalmente independiente |

## Selección

Valorar 0-5: activos, volumen, usuarios, irreversibilidad, composabilidad, custodia, consenso/mercado, regulación, novedad y dificultad de recovery. AP1 no es apropiado cuando un factor es 4-5 sin rationale compensatorio.

## Herencia y perfiles mixtos

Los perfiles superiores heredan requisitos inferiores. Un sistema puede asignar AP3 a custody/bridge y AP2 a API; debe mostrarlo por dominio y justificarlo.

# 06 - Evidencia y confianza

## Niveles

| Nivel | Nombre | Significado |
|---|---|---|
| E0 | Declarativa | afirmación o questionnaire sin verificar |
| E1 | Documental | policy, diagram, ticket o design record |
| E2 | Configuración | source, build, configuration o control artifact |
| E3 | Observada | logs, queries o runtime output directos |
| E4 | Adversarial | test controlado reproduce propiedad o falla |
| E5 | Independiente | repetición independiente o attestation |

## Registro

Cada evidencia DEBE incluir ID, source/owner, fecha/hora/timezone, ambiente/versión, collector, hash cuando aplique, sensibilidad, relación con control/test/finding, limitaciones y retención.

## Confianza

- **C1 Low:** supuestos materiales no verificados.
- **C2 Moderate:** múltiples indicadores con gaps.
- **C3 High:** evidencia directa y repetible.
- **C4 Very high:** reproducción independiente y traceability completa.

Tool output por sí solo es E2 como máximo salvo validación de reachability, preconditions e impact. La contradicción entre evidencias debe resolverse o reducir confidence.

# 05 - Modelo preliminar de riesgo

> Modelo v0.1 sujeto a calibración empírica y a validación de concordancia entre evaluadores.

## Impacto (0-5)

- **F:** financiero.
- **I:** integridad.
- **A:** disponibilidad.
- **P:** privacidad.
- **G:** gobernanza.
- **S:** sistémico.
- **R:** irreversibilidad.

```text
Impact = 0.25F + 0.15I + 0.10A + 0.10P + 0.10G + 0.15S + 0.15R
```

## Probabilidad (0-5)

- **E:** explotabilidad.
- **X:** exposición.
- **Q:** precondiciones; la puntuación aumenta cuando existen menos precondiciones.
- **M:** incentivo.
- **C:** composabilidad.

```text
Likelihood = 0.30E + 0.20X + 0.15Q + 0.20M + 0.15C
RawRisk = 100 * (Impact / 5) * (Likelihood / 5)
Risk = floor(RawRisk + 0.5)  # redondeo half-up
```

## Bandas preliminares

| Score | Banda |
|---:|---|
| 0-9 | Informativo |
| 10-29 | Bajo |
| 30-49 | Medio |
| 50-69 | Alto |
| 70-89 | Crítico |
| 90-100 | Sistémico |

## Overrides y agregación

Una ruta creíble hacia un firmante raíz, una capacidad de emisión irrestricta, una mayoría de validadores de bridge, el libro de reservas o un retiro irreversible de alto valor no puede clasificarse por debajo de Alto sin una justificación explícita. No deben promediarse hallazgos sin conservar el riesgo máximo, la concentración, las causas compartidas, las dependencias correlacionadas y la incertidumbre.

## Riesgo, evidencia y confianza

Se reportan por separado. Un escenario de alto impacto puede tener baja confianza.


## Ejemplo

Las dimensiones `F=5, I=4, A=2, P=1, G=4, S=4, R=5` producen un impacto de `3.90`.  
Las dimensiones `E=3, X=4, Q=3, M=5, C=4` producen una probabilidad de `3.75`.  
El riesgo preliminar es `floor(100 × 3.90/5 × 3.75/5 + 0.5) = 59`, banda **Alta**.

# 07 - Identificadores

| Objeto | Patrón | Ejemplo |
|---|---|---|
| Dominio | `CSPTF-DOM-NN` | `CSPTF-DOM-10` |
| Control | `CSPTF-CTRL-CODE-NNN` | `CSPTF-CTRL-BRG-004` |
| Test | `CSPTF-TEST-CODE-NNN` | `CSPTF-TEST-BRG-009` |
| Amenaza | `CSPTF-THRT-CODE-NNN` | `CSPTF-THRT-KEY-001` |
| Debilidad | `CSPTF-WEAK-CODE-NNN` | `CSPTF-WEAK-SCT-002` |
| Finding | `CSPTF-FIND-NNNN` | `CSPTF-FIND-0042` |
| Evidencia | `CSPTF-EVID-NNNN` | `CSPTF-EVID-0088` |

Los IDs no codifican severidad, no se reutilizan y permanecen estables tras release. Los mappings declaran estado proposed, reviewed, verified o deprecated.

# 08 - Modelo de findings

Un finding es una afirmación verificable respaldada por evidencia.

## Campos obligatorios

- ID, title y status;
- assets, versions, networks y addresses;
- tests, controls, threats y weaknesses;
- observation y expected property;
- reproducción segura;
- preconditions y exploit path;
- dimensiones de impacto y probabilidad;
- risk band y override;
- evidence level y confidence;
- root cause;
- remediation y compensating controls;
- owner/target;
- disclosure restrictions;
- retest y residual risk.

## Estados

`draft -> validated -> accepted -> remediation in progress -> ready for retest -> closed`

Estados alternos: risk accepted, duplicate, not applicable, false positive o superseded. Cada cambio registra actor, tiempo, rationale y evidencia.

## Causa raíz

No crear un finding por cada línea de scanner cuando comparten causa; tampoco mezclar riesgos no relacionados.

# 09 - Conformidad de evaluaciones

CSPTF v0.1 permite declarar **assessment conformant - draft**, no product certification.

La evaluación debe:

1. identificar versión;
2. tener autorización y RoE;
3. definir arquetipo y scope;
4. asignar perfil por dominio;
5. registrar applicable, excluded y not-tested;
6. usar IDs CSPTF;
7. preservar evidencia y confidence;
8. aplicar scoring o alternativa transparente;
9. reportar limitaciones y residual risk;
10. incluir remediation y retest;
11. pasar validación estructural.

No puede declarar certificación, garantía, endorsement ni compliance automático con fuentes mapeadas.

## Cobertura

Reportar por separado control, tests, evidence, threats, domains y retest. Un porcentaje único puede ocultar rutas críticas.

# 10 - Estándar de reporte

## Reporte ejecutivo

- decisión soportada;
- scope y assurance;
- sistema y flujos de valor;
- riesgo máximo y concentración;
- escenarios críticos y efecto de negocio;
- fortalezas y limitaciones;
- acciones, owners y horizontes;
- residual risk y retest.

## Reporte técnico

- autorización y RoE;
- arquitectura y threat model;
- inventory versionado;
- test matrix;
- métodos, tools y limitaciones;
- evidence register;
- findings;
- calculations;
- detección/respuesta;
- remediation;
- exclusions;
- hashes y anexos.

## Reglas de lenguaje

Distinguir hecho observado, comportamiento reproducido, inferencia, supuesto e hipótesis no probada. Evitar “seguro”, “inhackeable” o “fully compliant” sin sustento.

## Distribución

Aplicar acceso por roles, cifrado, clasificación, retención controlada y resumen sanitizado para divulgación coordinada.

# 11 - Glosario

- **Activo:** elemento de valor o necesario para proteger valor.
- **Perfil de aseguramiento:** profundidad e independencia mínimas.
- **Bridge:** mecanismo que comunica o representa activos/estado entre cadenas.
- **CeFi:** servicio financiero de activos digitales operado centralmente.
- **Composabilidad:** interacción entre componentes, a menudo atómica.
- **Custodia:** control y protección de autoridad de firma o activos.
- **DeFi:** protocolo financiero implementado en sistemas descentralizados.
- **Evidencia:** artefacto que soporta o refuta una conclusión.
- **Finding:** afirmación de riesgo respaldada por evidencia.
- **Fork:** copia aislada del estado de una cadena.
- **Invariante:** propiedad que permanece verdadera en estados válidos.
- **MPC:** multi-party computation para distribuir operaciones de clave.
- **Oráculo:** mecanismo que entrega datos externos a blockchain.
- **Relayer:** actor off-chain que envía mensajes o transacciones.
- **Rollup:** Layer 2 que publica datos o pruebas en una base layer.
- **Impacto sistémico:** propagación más allá del componente afectado.
- **Test case:** procedimiento autorizado para evaluar una propiedad.
- **Amenaza:** actor/acción/escenario capaz de causar daño.
- **Debilidad:** condición que habilita o amplifica una amenaza.

# 12. Dominios, controles y pruebas

## 12.1 CSPTF-DOM-01 - GOV: Gobernanza, alcance y modelado de amenazas

**English:** Governance, Scope and Threat Modeling

**Propósito:** Establecer autorización, objetivos, límites, responsables, supuestos, apetito de riesgo y modelos de amenaza antes de ejecutar cualquier prueba.

**Activos principales:** mandato de evaluación, inventario de activos, matriz RACI, modelo de amenazas, presupuestos de pérdida, criterios de detención.

### Controles

#### CSPTF-CTRL-GOV-001 - Gobierno y responsabilidad del programa

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que gobierno y responsabilidad del programa se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gobierno y responsabilidad del programa, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gobierno y responsabilidad del programa.

#### CSPTF-CTRL-GOV-002 - Inventario y clasificación de activos digitales

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que inventario y clasificación de activos digitales se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar inventario y clasificación de activos digitales, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con inventario y clasificación de activos digitales.

#### CSPTF-CTRL-GOV-003 - Reglas de compromiso y autorización

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que reglas de compromiso y autorización se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar reglas de compromiso y autorización, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con reglas de compromiso y autorización.

#### CSPTF-CTRL-GOV-004 - Modelado de amenazas orientado al negocio

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que modelado de amenazas orientado al negocio se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar modelado de amenazas orientado al negocio, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con modelado de amenazas orientado al negocio.

#### CSPTF-CTRL-GOV-005 - Gestión de terceros y dependencias críticas

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que gestión de terceros y dependencias críticas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gestión de terceros y dependencias críticas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gestión de terceros y dependencias críticas.

#### CSPTF-CTRL-GOV-006 - Presupuestos de riesgo, pérdida y transacción

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que presupuestos de riesgo, pérdida y transacción se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar presupuestos de riesgo, pérdida y transacción, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con presupuestos de riesgo, pérdida y transacción.

#### CSPTF-CTRL-GOV-007 - Gestión de cambios durante la evaluación

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que gestión de cambios durante la evaluación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gestión de cambios durante la evaluación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gestión de cambios durante la evaluación.

#### CSPTF-CTRL-GOV-008 - Aceptación, excepción y cierre de hallazgos

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que aceptación, excepción y cierre de hallazgos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar aceptación, excepción y cierre de hallazgos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con aceptación, excepción y cierre de hallazgos.

### Pruebas

#### CSPTF-TEST-GOV-001 - Verificar la autorización y el alcance formal

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si verificar la autorización y el alcance formal reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con verificar la autorización y el alcance formal, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden verificar la autorización y el alcance formal.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-002 - Validar el inventario de activos y flujos de valor

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar el inventario de activos y flujos de valor reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar el inventario de activos y flujos de valor, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar el inventario de activos y flujos de valor.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-003 - Revisar roles, escalamiento y autoridad de detención

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar roles, escalamiento y autoridad de detención reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar roles, escalamiento y autoridad de detención, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar roles, escalamiento y autoridad de detención.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-004 - Evaluar el modelo de amenazas y supuestos

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar el modelo de amenazas y supuestos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar el modelo de amenazas y supuestos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar el modelo de amenazas y supuestos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-005 - Comprobar exclusiones y dependencias de terceros

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar exclusiones y dependencias de terceros reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar exclusiones y dependencias de terceros, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar exclusiones y dependencias de terceros.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-006 - Validar presupuestos de pérdida, gas y transacciones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar presupuestos de pérdida, gas y transacciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar presupuestos de pérdida, gas y transacciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar presupuestos de pérdida, gas y transacciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-007 - Revisar ventanas, monitoreo y comunicaciones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar ventanas, monitoreo y comunicaciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar ventanas, monitoreo y comunicaciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar ventanas, monitoreo y comunicaciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-008 - Comprobar criterios de evidencia y custodia

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar criterios de evidencia y custodia reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar criterios de evidencia y custodia, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar criterios de evidencia y custodia.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-009 - Evaluar la gestión de cambios de alcance

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar la gestión de cambios de alcance reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar la gestión de cambios de alcance, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar la gestión de cambios de alcance.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-010 - Validar el tratamiento de datos sensibles

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar el tratamiento de datos sensibles reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar el tratamiento de datos sensibles, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar el tratamiento de datos sensibles.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-011 - Revisar aceptación de riesgo y excepciones

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar aceptación de riesgo y excepciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar aceptación de riesgo y excepciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar aceptación de riesgo y excepciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-GOV-012 - Ejecutar una mesa de crisis previa a pruebas críticas

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar una mesa de crisis previa a pruebas críticas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar una mesa de crisis previa a pruebas críticas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar una mesa de crisis previa a pruebas críticas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-GOV-001` Pruebas sin autorización efectiva: Actor externo, interno o automatizado intenta provocar pruebas sin autorización efectiva para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-GOV-002` Activos críticos omitidos del alcance: Actor externo, interno o automatizado intenta provocar activos críticos omitidos del alcance para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-GOV-003` Conflictos de interés o independencia insuficiente: Actor externo, interno o automatizado intenta provocar conflictos de interés o independencia insuficiente para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-GOV-004` Cambios no controlados durante el ejercicio: Actor externo, interno o automatizado intenta provocar cambios no controlados durante el ejercicio para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-GOV-005` Aceptación de riesgo sin autoridad competente: Actor externo, interno o automatizado intenta provocar aceptación de riesgo sin autoridad competente para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-GOV-001` Alcance ambiguo: Condición de diseño, implementación u operación caracterizada por alcance ambiguo, capaz de facilitar amenazas del dominio GOV.
- `CSPTF-WEAK-GOV-002` Inventario incompleto: Condición de diseño, implementación u operación caracterizada por inventario incompleto, capaz de facilitar amenazas del dominio GOV.
- `CSPTF-WEAK-GOV-003` Reglas de detención inexistentes: Condición de diseño, implementación u operación caracterizada por reglas de detención inexistentes, capaz de facilitar amenazas del dominio GOV.
- `CSPTF-WEAK-GOV-004` RACI no definido: Condición de diseño, implementación u operación caracterizada por raci no definido, capaz de facilitar amenazas del dominio GOV.
- `CSPTF-WEAK-GOV-005` Evidencia sin cadena de custodia: Condición de diseño, implementación u operación caracterizada por evidencia sin cadena de custodia, capaz de facilitar amenazas del dominio GOV.

## 12.2 CSPTF-DOM-02 - ARC: Arquitectura y diseño de protocolo

**English:** Architecture and Protocol Design

**Propósito:** Evaluar fronteras de confianza, invariantes, flujos de valor, estados, dependencias y propiedades de seguridad del sistema completo.

**Activos principales:** diagramas de arquitectura, invariantes, máquinas de estado, flujos de fondos, fronteras de confianza, supuestos de protocolo.

### Controles

#### CSPTF-CTRL-ARC-001 - Arquitectura documentada y versionada

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que arquitectura documentada y versionada se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar arquitectura documentada y versionada, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con arquitectura documentada y versionada.

#### CSPTF-CTRL-ARC-002 - Fronteras de confianza explícitas

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que fronteras de confianza explícitas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar fronteras de confianza explícitas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con fronteras de confianza explícitas.

#### CSPTF-CTRL-ARC-003 - Invariantes de seguridad y solvencia

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que invariantes de seguridad y solvencia se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar invariantes de seguridad y solvencia, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con invariantes de seguridad y solvencia.

#### CSPTF-CTRL-ARC-004 - Máquinas de estado completas

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que máquinas de estado completas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar máquinas de estado completas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con máquinas de estado completas.

#### CSPTF-CTRL-ARC-005 - Separación de funciones y planos

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que separación de funciones y planos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar separación de funciones y planos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con separación de funciones y planos.

#### CSPTF-CTRL-ARC-006 - Patrones seguros de actualización y migración

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que patrones seguros de actualización y migración se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar patrones seguros de actualización y migración, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con patrones seguros de actualización y migración.

#### CSPTF-CTRL-ARC-007 - Degradación segura y circuit breakers

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que degradación segura y circuit breakers se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar degradación segura y circuit breakers, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con degradación segura y circuit breakers.

#### CSPTF-CTRL-ARC-008 - Análisis de composabilidad y dependencias

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que análisis de composabilidad y dependencias se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar análisis de composabilidad y dependencias, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con análisis de composabilidad y dependencias.

### Pruebas

#### CSPTF-TEST-ARC-001 - Reconstruir la arquitectura lógica y física

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si reconstruir la arquitectura lógica y física reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con reconstruir la arquitectura lógica y física, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden reconstruir la arquitectura lógica y física.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-002 - Trazar flujos de activos y mensajes

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si trazar flujos de activos y mensajes reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con trazar flujos de activos y mensajes, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden trazar flujos de activos y mensajes.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-003 - Validar fronteras de confianza

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar fronteras de confianza reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar fronteras de confianza, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar fronteras de confianza.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-004 - Comprobar invariantes de seguridad

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar invariantes de seguridad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar invariantes de seguridad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar invariantes de seguridad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-005 - Revisar máquinas de estado y transiciones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar máquinas de estado y transiciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar máquinas de estado y transiciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar máquinas de estado y transiciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-006 - Evaluar separación de funciones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar separación de funciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar separación de funciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar separación de funciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-007 - Examinar actualización y migración

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si examinar actualización y migración reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con examinar actualización y migración, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden examinar actualización y migración.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-008 - Validar modos degradados y pausas

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar modos degradados y pausas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar modos degradados y pausas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar modos degradados y pausas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-009 - Analizar dependencias externas críticas

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si analizar dependencias externas críticas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con analizar dependencias externas críticas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden analizar dependencias externas críticas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-010 - Revisar composabilidad y efectos emergentes

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar composabilidad y efectos emergentes reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar composabilidad y efectos emergentes, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar composabilidad y efectos emergentes.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-011 - Comprobar supuestos de tiempo y finalidad

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar supuestos de tiempo y finalidad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar supuestos de tiempo y finalidad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar supuestos de tiempo y finalidad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ARC-012 - Ejecutar revisión adversarial de arquitectura

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar revisión adversarial de arquitectura reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar revisión adversarial de arquitectura, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar revisión adversarial de arquitectura.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-ARC-001` Violación de invariantes de protocolo: Actor externo, interno o automatizado intenta provocar violación de invariantes de protocolo para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-ARC-002` Abuso de transiciones de estado: Actor externo, interno o automatizado intenta provocar abuso de transiciones de estado para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-ARC-003` Compromiso de una frontera de confianza: Actor externo, interno o automatizado intenta provocar compromiso de una frontera de confianza para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-ARC-004` Actualización maliciosa o defectuosa: Actor externo, interno o automatizado intenta provocar actualización maliciosa o defectuosa para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-ARC-005` Fallo en cascada por dependencia externa: Actor externo, interno o automatizado intenta provocar fallo en cascada por dependencia externa para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-ARC-001` Invariantes no formalizados: Condición de diseño, implementación u operación caracterizada por invariantes no formalizados, capaz de facilitar amenazas del dominio ARC.
- `CSPTF-WEAK-ARC-002` Estados terminales inseguros: Condición de diseño, implementación u operación caracterizada por estados terminales inseguros, capaz de facilitar amenazas del dominio ARC.
- `CSPTF-WEAK-ARC-003` Acoplamiento excesivo: Condición de diseño, implementación u operación caracterizada por acoplamiento excesivo, capaz de facilitar amenazas del dominio ARC.
- `CSPTF-WEAK-ARC-004` Privilegios concentrados: Condición de diseño, implementación u operación caracterizada por privilegios concentrados, capaz de facilitar amenazas del dominio ARC.
- `CSPTF-WEAK-ARC-005` Recuperación arquitectónica no probada: Condición de diseño, implementación u operación caracterizada por recuperación arquitectónica no probada, capaz de facilitar amenazas del dominio ARC.

## 12.3 CSPTF-DOM-03 - CRY: Criptografía, aleatoriedad y material criptográfico

**English:** Cryptography, Randomness and Cryptographic Material

**Propósito:** Verificar selección, implementación, uso y ciclo de vida de primitivas criptográficas, fuentes de entropía, firmas y pruebas.

**Activos principales:** algoritmos, parámetros, entropía, nonce, firmas, hashes, cifrado, pruebas de conocimiento cero.

### Controles

#### CSPTF-CTRL-CRY-001 - Primitivas y parámetros aprobados

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que primitivas y parámetros aprobados se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar primitivas y parámetros aprobados, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con primitivas y parámetros aprobados.

#### CSPTF-CTRL-CRY-002 - Generación de entropía y aleatoriedad

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que generación de entropía y aleatoriedad se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar generación de entropía y aleatoriedad, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con generación de entropía y aleatoriedad.

#### CSPTF-CTRL-CRY-003 - Gestión segura de nonces

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que gestión segura de nonces se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gestión segura de nonces, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gestión segura de nonces.

#### CSPTF-CTRL-CRY-004 - Validación canónica de firmas

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que validación canónica de firmas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar validación canónica de firmas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con validación canónica de firmas.

#### CSPTF-CTRL-CRY-005 - Separación de dominios criptográficos

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que separación de dominios criptográficos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar separación de dominios criptográficos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con separación de dominios criptográficos.

#### CSPTF-CTRL-CRY-006 - Protección contra replay y malleability

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que protección contra replay y malleability se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar protección contra replay y malleability, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con protección contra replay y malleability.

#### CSPTF-CTRL-CRY-007 - Agilidad y migración criptográfica

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que agilidad y migración criptográfica se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar agilidad y migración criptográfica, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con agilidad y migración criptográfica.

#### CSPTF-CTRL-CRY-008 - Verificación de implementaciones y bibliotecas

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que verificación de implementaciones y bibliotecas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar verificación de implementaciones y bibliotecas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con verificación de implementaciones y bibliotecas.

### Pruebas

#### CSPTF-TEST-CRY-001 - Inventariar primitivas y parámetros

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si inventariar primitivas y parámetros reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con inventariar primitivas y parámetros, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden inventariar primitivas y parámetros.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-002 - Revisar fuentes de entropía

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar fuentes de entropía reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar fuentes de entropía, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar fuentes de entropía.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-003 - Validar generación y reutilización de nonces

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar generación y reutilización de nonces reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar generación y reutilización de nonces, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar generación y reutilización de nonces.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-004 - Comprobar validación de firmas

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar validación de firmas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar validación de firmas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar validación de firmas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-005 - Evaluar separación de dominios

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar separación de dominios reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar separación de dominios, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar separación de dominios.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-006 - Probar controles anti-replay en entorno autorizado

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si probar controles anti-replay en entorno autorizado reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con probar controles anti-replay en entorno autorizado, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden probar controles anti-replay en entorno autorizado.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-007 - Revisar serialización y codificación canónica

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar serialización y codificación canónica reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar serialización y codificación canónica, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar serialización y codificación canónica.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-008 - Comprobar manejo de claves públicas inválidas

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar manejo de claves públicas inválidas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar manejo de claves públicas inválidas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar manejo de claves públicas inválidas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-009 - Evaluar bibliotecas y compilación criptográfica

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar bibliotecas y compilación criptográfica reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar bibliotecas y compilación criptográfica, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar bibliotecas y compilación criptográfica.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-010 - Revisar custodia de secretos criptográficos

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar custodia de secretos criptográficos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar custodia de secretos criptográficos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar custodia de secretos criptográficos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-011 - Validar plan de migración y agilidad

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar plan de migración y agilidad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar plan de migración y agilidad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar plan de migración y agilidad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CRY-012 - Ejecutar pruebas de interoperabilidad criptográfica

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar pruebas de interoperabilidad criptográfica reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar pruebas de interoperabilidad criptográfica, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar pruebas de interoperabilidad criptográfica.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-CRY-001` Predicción o sesgo de aleatoriedad: Actor externo, interno o automatizado intenta provocar predicción o sesgo de aleatoriedad para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-CRY-002` Reutilización de nonce y exposición de clave: Actor externo, interno o automatizado intenta provocar reutilización de nonce y exposición de clave para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-CRY-003` Replay de mensajes firmados: Actor externo, interno o automatizado intenta provocar replay de mensajes firmados para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-CRY-004` Degradación de algoritmo o parámetro: Actor externo, interno o automatizado intenta provocar degradación de algoritmo o parámetro para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-CRY-005` Fallo de validación criptográfica: Actor externo, interno o automatizado intenta provocar fallo de validación criptográfica para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-CRY-001` Entropía insuficiente: Condición de diseño, implementación u operación caracterizada por entropía insuficiente, capaz de facilitar amenazas del dominio CRY.
- `CSPTF-WEAK-CRY-002` Dominio de firma ambiguo: Condición de diseño, implementación u operación caracterizada por dominio de firma ambiguo, capaz de facilitar amenazas del dominio CRY.
- `CSPTF-WEAK-CRY-003` Parámetros obsoletos: Condición de diseño, implementación u operación caracterizada por parámetros obsoletos, capaz de facilitar amenazas del dominio CRY.
- `CSPTF-WEAK-CRY-004` Comparaciones no constantes: Condición de diseño, implementación u operación caracterizada por comparaciones no constantes, capaz de facilitar amenazas del dominio CRY.
- `CSPTF-WEAK-CRY-005` Manejo incorrecto de serialización: Condición de diseño, implementación u operación caracterizada por manejo incorrecto de serialización, capaz de facilitar amenazas del dominio CRY.

## 12.4 CSPTF-DOM-04 - KEY: Gestión de claves, custodia, wallets y firma

**English:** Key Management, Custody, Wallets and Signing

**Propósito:** Evaluar generación, almacenamiento, uso, recuperación, rotación y destrucción de claves, junto con políticas de firma y custodia.

**Activos principales:** hot wallets, cold wallets, HSM, MPC, seed phrases, firmantes, políticas de retiro, recuperación.

### Controles

#### CSPTF-CTRL-KEY-001 - Ceremonias de generación y respaldo

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que ceremonias de generación y respaldo se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar ceremonias de generación y respaldo, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con ceremonias de generación y respaldo.

#### CSPTF-CTRL-KEY-002 - Custodia segregada por propósito

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que custodia segregada por propósito se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar custodia segregada por propósito, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con custodia segregada por propósito.

#### CSPTF-CTRL-KEY-003 - Políticas de firma y límites

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que políticas de firma y límites se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar políticas de firma y límites, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con políticas de firma y límites.

#### CSPTF-CTRL-KEY-004 - MPC, multisig y quorum

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que mpc, multisig y quorum se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar mpc, multisig y quorum, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con mpc, multisig y quorum.

#### CSPTF-CTRL-KEY-005 - Protección de hot wallets

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que protección de hot wallets se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar protección de hot wallets, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con protección de hot wallets.

#### CSPTF-CTRL-KEY-006 - Cold storage y movimiento controlado

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que cold storage y movimiento controlado se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar cold storage y movimiento controlado, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con cold storage y movimiento controlado.

#### CSPTF-CTRL-KEY-007 - Rotación, recuperación y destrucción

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que rotación, recuperación y destrucción se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar rotación, recuperación y destrucción, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con rotación, recuperación y destrucción.

#### CSPTF-CTRL-KEY-008 - Monitoreo y respuesta ante compromiso

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que monitoreo y respuesta ante compromiso se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar monitoreo y respuesta ante compromiso, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con monitoreo y respuesta ante compromiso.

### Pruebas

#### CSPTF-TEST-KEY-001 - Revisar ceremonia de generación de claves

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar ceremonia de generación de claves reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar ceremonia de generación de claves, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar ceremonia de generación de claves.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-002 - Validar segregación hot, warm y cold

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar segregación hot, warm y cold reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar segregación hot, warm y cold, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar segregación hot, warm y cold.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-003 - Comprobar políticas de firma y límites

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar políticas de firma y límites reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar políticas de firma y límites, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar políticas de firma y límites.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-004 - Evaluar quorum, multisig o MPC

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar quorum, multisig o mpc reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar quorum, multisig o mpc, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar quorum, multisig o mpc.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-005 - Revisar almacenamiento y acceso a seeds

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar almacenamiento y acceso a seeds reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar almacenamiento y acceso a seeds, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar almacenamiento y acceso a seeds.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-006 - Validar procesos de retiro y allowlists

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar procesos de retiro y allowlists reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar procesos de retiro y allowlists, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar procesos de retiro y allowlists.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-007 - Comprobar rotación y revocación

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar rotación y revocación reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar rotación y revocación, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar rotación y revocación.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-008 - Evaluar recuperación y continuidad

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar recuperación y continuidad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar recuperación y continuidad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar recuperación y continuidad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-009 - Revisar firmware y cadena de suministro de dispositivos

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar firmware y cadena de suministro de dispositivos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar firmware y cadena de suministro de dispositivos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar firmware y cadena de suministro de dispositivos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-010 - Comprobar telemetría de operaciones de firma

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar telemetría de operaciones de firma reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar telemetría de operaciones de firma, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar telemetría de operaciones de firma.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-011 - Ejecutar simulación de compromiso de firmante

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar simulación de compromiso de firmante reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar simulación de compromiso de firmante, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar simulación de compromiso de firmante.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-KEY-012 - Validar destrucción y retiro de material

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar destrucción y retiro de material reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar destrucción y retiro de material, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar destrucción y retiro de material.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-KEY-001` Robo o exposición de clave privada: Actor externo, interno o automatizado intenta provocar robo o exposición de clave privada para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-KEY-002` Colusión o compromiso de firmantes: Actor externo, interno o automatizado intenta provocar colusión o compromiso de firmantes para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-KEY-003` Drenaje de hot wallet: Actor externo, interno o automatizado intenta provocar drenaje de hot wallet para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-KEY-004` Abuso del proceso de recuperación: Actor externo, interno o automatizado intenta provocar abuso del proceso de recuperación para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-KEY-005` Sustitución de dirección o transacción: Actor externo, interno o automatizado intenta provocar sustitución de dirección o transacción para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-KEY-001` Seeds sin protección suficiente: Condición de diseño, implementación u operación caracterizada por seeds sin protección suficiente, capaz de facilitar amenazas del dominio KEY.
- `CSPTF-WEAK-KEY-002` Quorum mal configurado: Condición de diseño, implementación u operación caracterizada por quorum mal configurado, capaz de facilitar amenazas del dominio KEY.
- `CSPTF-WEAK-KEY-003` Límites de firma ausentes: Condición de diseño, implementación u operación caracterizada por límites de firma ausentes, capaz de facilitar amenazas del dominio KEY.
- `CSPTF-WEAK-KEY-004` Recuperación no ensayada: Condición de diseño, implementación u operación caracterizada por recuperación no ensayada, capaz de facilitar amenazas del dominio KEY.
- `CSPTF-WEAK-KEY-005` Segregación de wallets insuficiente: Condición de diseño, implementación u operación caracterizada por segregación de wallets insuficiente, capaz de facilitar amenazas del dominio KEY.

## 12.5 CSPTF-DOM-05 - SCT: Contratos inteligentes y lógica de ejecución

**English:** Smart Contracts and Runtime Logic

**Propósito:** Evaluar código desplegable, lógica de negocio, control de acceso, interacciones, actualizaciones, gas y propiedades de ejecución.

**Activos principales:** código fuente, bytecode, ABI, proxy, roles, almacenamiento, eventos, dependencias on-chain.

### Controles

#### CSPTF-CTRL-SCT-001 - Trazabilidad fuente-bytecode

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que trazabilidad fuente-bytecode se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar trazabilidad fuente-bytecode, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con trazabilidad fuente-bytecode.

#### CSPTF-CTRL-SCT-002 - Control de acceso y privilegios

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que control de acceso y privilegios se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar control de acceso y privilegios, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con control de acceso y privilegios.

#### CSPTF-CTRL-SCT-003 - Manejo seguro de llamadas externas

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que manejo seguro de llamadas externas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar manejo seguro de llamadas externas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con manejo seguro de llamadas externas.

#### CSPTF-CTRL-SCT-004 - Invariantes y contabilidad interna

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que invariantes y contabilidad interna se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar invariantes y contabilidad interna, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con invariantes y contabilidad interna.

#### CSPTF-CTRL-SCT-005 - Actualización y almacenamiento seguro

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que actualización y almacenamiento seguro se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar actualización y almacenamiento seguro, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con actualización y almacenamiento seguro.

#### CSPTF-CTRL-SCT-006 - Resistencia a DoS y consumo de gas

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que resistencia a dos y consumo de gas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar resistencia a dos y consumo de gas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con resistencia a dos y consumo de gas.

#### CSPTF-CTRL-SCT-007 - Validación de entradas y estados

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que validación de entradas y estados se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar validación de entradas y estados, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con validación de entradas y estados.

#### CSPTF-CTRL-SCT-008 - Pruebas automatizadas y revisión independiente

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que pruebas automatizadas y revisión independiente se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar pruebas automatizadas y revisión independiente, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con pruebas automatizadas y revisión independiente.

### Pruebas

#### CSPTF-TEST-SCT-001 - Verificar correspondencia fuente-bytecode

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si verificar correspondencia fuente-bytecode reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con verificar correspondencia fuente-bytecode, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden verificar correspondencia fuente-bytecode.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-002 - Revisar control de acceso y ownership

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar control de acceso y ownership reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar control de acceso y ownership, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar control de acceso y ownership.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-003 - Evaluar llamadas externas y reentradas

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar llamadas externas y reentradas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar llamadas externas y reentradas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar llamadas externas y reentradas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-004 - Comprobar invariantes y contabilidad

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar invariantes y contabilidad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar invariantes y contabilidad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar invariantes y contabilidad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-005 - Analizar proxies, upgrades y storage layout

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si analizar proxies, upgrades y storage layout reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con analizar proxies, upgrades y storage layout, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden analizar proxies, upgrades y storage layout.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-006 - Revisar fallos, revert y manejo de errores

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar fallos, revert y manejo de errores reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar fallos, revert y manejo de errores, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar fallos, revert y manejo de errores.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-007 - Evaluar bucles, gas y denegación de servicio

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar bucles, gas y denegación de servicio reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar bucles, gas y denegación de servicio, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar bucles, gas y denegación de servicio.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-008 - Comprobar validación de entradas y límites

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar validación de entradas y límites reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar validación de entradas y límites, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar validación de entradas y límites.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-009 - Revisar eventos y observabilidad

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar eventos y observabilidad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar eventos y observabilidad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar eventos y observabilidad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-010 - Ejecutar análisis estático en laboratorio

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar análisis estático en laboratorio reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar análisis estático en laboratorio, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar análisis estático en laboratorio.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-011 - Ejecutar fuzzing o pruebas de propiedades en fork

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar fuzzing o pruebas de propiedades en fork reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar fuzzing o pruebas de propiedades en fork, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar fuzzing o pruebas de propiedades en fork.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SCT-012 - Validar correcciones mediante revisión independiente

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar correcciones mediante revisión independiente reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar correcciones mediante revisión independiente, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar correcciones mediante revisión independiente.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-SCT-001` Ejecución no autorizada de funciones críticas: Actor externo, interno o automatizado intenta provocar ejecución no autorizada de funciones críticas para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-SCT-002` Manipulación de contabilidad interna: Actor externo, interno o automatizado intenta provocar manipulación de contabilidad interna para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-SCT-003` Reentrancia o interacción inesperada: Actor externo, interno o automatizado intenta provocar reentrancia o interacción inesperada para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-SCT-004` Colisión de almacenamiento en actualización: Actor externo, interno o automatizado intenta provocar colisión de almacenamiento en actualización para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-SCT-005` Bloqueo permanente o agotamiento de gas: Actor externo, interno o automatizado intenta provocar bloqueo permanente o agotamiento de gas para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-SCT-001` Control de acceso incompleto: Condición de diseño, implementación u operación caracterizada por control de acceso incompleto, capaz de facilitar amenazas del dominio SCT.
- `CSPTF-WEAK-SCT-002` Checks-effects-interactions incumplido: Condición de diseño, implementación u operación caracterizada por checks-effects-interactions incumplido, capaz de facilitar amenazas del dominio SCT.
- `CSPTF-WEAK-SCT-003` Aritmética o precisión incorrecta: Condición de diseño, implementación u operación caracterizada por aritmética o precisión incorrecta, capaz de facilitar amenazas del dominio SCT.
- `CSPTF-WEAK-SCT-004` Upgrade inseguro: Condición de diseño, implementación u operación caracterizada por upgrade inseguro, capaz de facilitar amenazas del dominio SCT.
- `CSPTF-WEAK-SCT-005` Cobertura de pruebas insuficiente: Condición de diseño, implementación u operación caracterizada por cobertura de pruebas insuficiente, capaz de facilitar amenazas del dominio SCT.

## 12.6 CSPTF-DOM-06 - DAP: dApps, frontend, sesiones e integración de wallets

**English:** dApps, Frontend, Sessions and Wallet Integration

**Propósito:** Evaluar aplicaciones cliente, sesiones, proveedores Web3, solicitudes de firma, resolución de red y controles que conectan usuarios con funciones on-chain.

**Activos principales:** frontend, backend BFF, wallet connectors, sesiones, deep links, firmas EIP-712, DNS/CDN, proveedores RPC.

### Controles

#### CSPTF-CTRL-DAP-001 - Integridad de frontend y distribución

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que integridad de frontend y distribución se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar integridad de frontend y distribución, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con integridad de frontend y distribución.

#### CSPTF-CTRL-DAP-002 - Vinculación segura de sesión y wallet

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que vinculación segura de sesión y wallet se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar vinculación segura de sesión y wallet, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con vinculación segura de sesión y wallet.

#### CSPTF-CTRL-DAP-003 - Presentación clara de solicitudes de firma

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que presentación clara de solicitudes de firma se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar presentación clara de solicitudes de firma, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con presentación clara de solicitudes de firma.

#### CSPTF-CTRL-DAP-004 - Validación de red, cadena y contrato

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que validación de red, cadena y contrato se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar validación de red, cadena y contrato, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con validación de red, cadena y contrato.

#### CSPTF-CTRL-DAP-005 - Autenticación y autorización off-chain

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que autenticación y autorización off-chain se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar autenticación y autorización off-chain, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con autenticación y autorización off-chain.

#### CSPTF-CTRL-DAP-006 - Protección de APIs y secretos de cliente

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que protección de apis y secretos de cliente se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar protección de apis y secretos de cliente, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con protección de apis y secretos de cliente.

#### CSPTF-CTRL-DAP-007 - Seguridad de contenido, DNS y dependencias

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que seguridad de contenido, dns y dependencias se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar seguridad de contenido, dns y dependencias, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con seguridad de contenido, dns y dependencias.

#### CSPTF-CTRL-DAP-008 - Detección de manipulación y respuesta

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que detección de manipulación y respuesta se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar detección de manipulación y respuesta, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con detección de manipulación y respuesta.

### Pruebas

#### CSPTF-TEST-DAP-001 - Revisar integridad del artefacto frontend

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar integridad del artefacto frontend reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar integridad del artefacto frontend, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar integridad del artefacto frontend.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-002 - Validar vinculación de cuenta, sesión y wallet

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar vinculación de cuenta, sesión y wallet reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar vinculación de cuenta, sesión y wallet, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar vinculación de cuenta, sesión y wallet.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-003 - Evaluar mensajes y transacciones solicitadas

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar mensajes y transacciones solicitadas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar mensajes y transacciones solicitadas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar mensajes y transacciones solicitadas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-004 - Comprobar chain ID, contrato y red objetivo

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar chain id, contrato y red objetivo reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar chain id, contrato y red objetivo, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar chain id, contrato y red objetivo.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-005 - Revisar autenticación y autorización off-chain

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar autenticación y autorización off-chain reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar autenticación y autorización off-chain, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar autenticación y autorización off-chain.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-006 - Evaluar exposición de secretos y configuración

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar exposición de secretos y configuración reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar exposición de secretos y configuración, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar exposición de secretos y configuración.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-007 - Comprobar protección contra inyección y XSS

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar protección contra inyección y xss reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar protección contra inyección y xss, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar protección contra inyección y xss.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-008 - Revisar dependencias, CDN y carga remota

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar dependencias, cdn y carga remota reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar dependencias, cdn y carga remota, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar dependencias, cdn y carga remota.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-009 - Validar deep links y redirecciones

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar deep links y redirecciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar deep links y redirecciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar deep links y redirecciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-010 - Evaluar disponibilidad y confianza del RPC

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar disponibilidad y confianza del rpc reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar disponibilidad y confianza del rpc, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar disponibilidad y confianza del rpc.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-011 - Simular manipulación de interfaz en laboratorio

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si simular manipulación de interfaz en laboratorio reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con simular manipulación de interfaz en laboratorio, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden simular manipulación de interfaz en laboratorio.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DAP-012 - Comprobar detección y revocación de sesiones

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar detección y revocación de sesiones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar detección y revocación de sesiones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar detección y revocación de sesiones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-DAP-001` Manipulación de interfaz para desviar fondos: Actor externo, interno o automatizado intenta provocar manipulación de interfaz para desviar fondos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-DAP-002` Firma engañosa o autorización excesiva: Actor externo, interno o automatizado intenta provocar firma engañosa o autorización excesiva para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-DAP-003` Secuestro de sesión vinculada a wallet: Actor externo, interno o automatizado intenta provocar secuestro de sesión vinculada a wallet para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-DAP-004` Sustitución de RPC, red o contrato: Actor externo, interno o automatizado intenta provocar sustitución de rpc, red o contrato para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-DAP-005` Compromiso de dominio o cadena de distribución: Actor externo, interno o automatizado intenta provocar compromiso de dominio o cadena de distribución para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-DAP-001` Firmas ciegas: Condición de diseño, implementación u operación caracterizada por firmas ciegas, capaz de facilitar amenazas del dominio DAP.
- `CSPTF-WEAK-DAP-002` Chain ID no validado: Condición de diseño, implementación u operación caracterizada por chain id no validado, capaz de facilitar amenazas del dominio DAP.
- `CSPTF-WEAK-DAP-003` Sesiones no ligadas al firmante: Condición de diseño, implementación u operación caracterizada por sesiones no ligadas al firmante, capaz de facilitar amenazas del dominio DAP.
- `CSPTF-WEAK-DAP-004` Dependencias remotas sin integridad: Condición de diseño, implementación u operación caracterizada por dependencias remotas sin integridad, capaz de facilitar amenazas del dominio DAP.
- `CSPTF-WEAK-DAP-005` Mensajes de riesgo poco comprensibles: Condición de diseño, implementación u operación caracterizada por mensajes de riesgo poco comprensibles, capaz de facilitar amenazas del dominio DAP.

## 12.7 CSPTF-DOM-07 - TOK: Tokens, NFT y ciclo de vida de activos

**English:** Tokens, NFTs and Asset Lifecycle

**Propósito:** Evaluar emisión, quema, transferencia, metadata, permisos, supply, interoperabilidad y ciclo de vida de activos fungibles y no fungibles.

**Activos principales:** token contracts, NFT collections, metadata, minting, burning, royalties, allowances, bridged assets.

### Controles

#### CSPTF-CTRL-TOK-001 - Modelo de emisión y supply

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que modelo de emisión y supply se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar modelo de emisión y supply, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con modelo de emisión y supply.

#### CSPTF-CTRL-TOK-002 - Autorización de mint y burn

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que autorización de mint y burn se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar autorización de mint y burn, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con autorización de mint y burn.

#### CSPTF-CTRL-TOK-003 - Transferencias, hooks y callbacks

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que transferencias, hooks y callbacks se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar transferencias, hooks y callbacks, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con transferencias, hooks y callbacks.

#### CSPTF-CTRL-TOK-004 - Allowances, approvals y permisos

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que allowances, approvals y permisos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar allowances, approvals y permisos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con allowances, approvals y permisos.

#### CSPTF-CTRL-TOK-005 - Metadata y contenido direccionable

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que metadata y contenido direccionable se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar metadata y contenido direccionable, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con metadata y contenido direccionable.

#### CSPTF-CTRL-TOK-006 - Compatibilidad e interoperabilidad

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que compatibilidad e interoperabilidad se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar compatibilidad e interoperabilidad, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con compatibilidad e interoperabilidad.

#### CSPTF-CTRL-TOK-007 - Administración, pausa y recuperación

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que administración, pausa y recuperación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar administración, pausa y recuperación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con administración, pausa y recuperación.

#### CSPTF-CTRL-TOK-008 - Monitoreo de anomalías del activo

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que monitoreo de anomalías del activo se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar monitoreo de anomalías del activo, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con monitoreo de anomalías del activo.

### Pruebas

#### CSPTF-TEST-TOK-001 - Validar invariantes de supply

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar invariantes de supply reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar invariantes de supply, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar invariantes de supply.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-002 - Revisar permisos de mint y burn

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar permisos de mint y burn reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar permisos de mint y burn, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar permisos de mint y burn.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-003 - Evaluar transferencias y callbacks

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar transferencias y callbacks reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar transferencias y callbacks, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar transferencias y callbacks.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-004 - Comprobar approvals y allowances

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar approvals y allowances reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar approvals y allowances, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar approvals y allowances.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-005 - Revisar metadata, URI y mutabilidad

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar metadata, uri y mutabilidad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar metadata, uri y mutabilidad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar metadata, uri y mutabilidad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-006 - Validar royalties y lógica comercial

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar royalties y lógica comercial reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar royalties y lógica comercial, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar royalties y lógica comercial.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-007 - Comprobar compatibilidad con estándares

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar compatibilidad con estándares reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar compatibilidad con estándares, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar compatibilidad con estándares.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-008 - Evaluar tokens con comportamientos no convencionales

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar tokens con comportamientos no convencionales reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar tokens con comportamientos no convencionales, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar tokens con comportamientos no convencionales.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-009 - Revisar administración y pausas

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar administración y pausas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar administración y pausas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar administración y pausas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-010 - Validar migración o reemplazo del activo

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar migración o reemplazo del activo reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar migración o reemplazo del activo, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar migración o reemplazo del activo.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-011 - Analizar representación bridged o wrapped

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si analizar representación bridged o wrapped reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con analizar representación bridged o wrapped, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden analizar representación bridged o wrapped.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-TOK-012 - Comprobar monitoreo de emisión anómala

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar monitoreo de emisión anómala reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar monitoreo de emisión anómala, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar monitoreo de emisión anómala.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-TOK-001` Emisión no autorizada o ilimitada: Actor externo, interno o automatizado intenta provocar emisión no autorizada o ilimitada para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-TOK-002` Robo mediante approval excesivo: Actor externo, interno o automatizado intenta provocar robo mediante approval excesivo para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-TOK-003` Manipulación o desaparición de metadata: Actor externo, interno o automatizado intenta provocar manipulación o desaparición de metadata para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-TOK-004` Incompatibilidad que bloquea activos: Actor externo, interno o automatizado intenta provocar incompatibilidad que bloquea activos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-TOK-005` Duplicación o desanclaje de activo wrapped: Actor externo, interno o automatizado intenta provocar duplicación o desanclaje de activo wrapped para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-TOK-001` Supply no acotado: Condición de diseño, implementación u operación caracterizada por supply no acotado, capaz de facilitar amenazas del dominio TOK.
- `CSPTF-WEAK-TOK-002` Metadata centralizada y mutable: Condición de diseño, implementación u operación caracterizada por metadata centralizada y mutable, capaz de facilitar amenazas del dominio TOK.
- `CSPTF-WEAK-TOK-003` Hooks no confiables: Condición de diseño, implementación u operación caracterizada por hooks no confiables, capaz de facilitar amenazas del dominio TOK.
- `CSPTF-WEAK-TOK-004` Permisos de minter excesivos: Condición de diseño, implementación u operación caracterizada por permisos de minter excesivos, capaz de facilitar amenazas del dominio TOK.
- `CSPTF-WEAK-TOK-005` Semántica de transferencia no estándar: Condición de diseño, implementación u operación caracterizada por semántica de transferencia no estándar, capaz de facilitar amenazas del dominio TOK.

## 12.8 CSPTF-DOM-08 - DEF: DeFi y seguridad económica

**English:** DeFi and Economic Security

**Propósito:** Evaluar solvencia, precios, incentivos, liquidaciones, AMM, préstamos, vaults, MEV y ataques de composición económica.

**Activos principales:** pools, AMM, lending markets, vaults, liquidation bots, governance tokens, collateral, fee models.

### Controles

#### CSPTF-CTRL-DEF-001 - Invariantes económicas y solvencia

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que invariantes económicas y solvencia se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar invariantes económicas y solvencia, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con invariantes económicas y solvencia.

#### CSPTF-CTRL-DEF-002 - Modelos de precio y deslizamiento

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que modelos de precio y deslizamiento se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar modelos de precio y deslizamiento, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con modelos de precio y deslizamiento.

#### CSPTF-CTRL-DEF-003 - Colateralización y liquidación

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que colateralización y liquidación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar colateralización y liquidación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con colateralización y liquidación.

#### CSPTF-CTRL-DEF-004 - Resistencia a manipulación temporal

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que resistencia a manipulación temporal se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar resistencia a manipulación temporal, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con resistencia a manipulación temporal.

#### CSPTF-CTRL-DEF-005 - Límites, caps y circuit breakers

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que límites, caps y circuit breakers se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar límites, caps y circuit breakers, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con límites, caps y circuit breakers.

#### CSPTF-CTRL-DEF-006 - Contabilidad de fees, shares y rewards

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que contabilidad de fees, shares y rewards se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar contabilidad de fees, shares y rewards, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con contabilidad de fees, shares y rewards.

#### CSPTF-CTRL-DEF-007 - Riesgo de composabilidad y dependencia

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que riesgo de composabilidad y dependencia se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar riesgo de composabilidad y dependencia, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con riesgo de composabilidad y dependencia.

#### CSPTF-CTRL-DEF-008 - Simulación económica y monitoreo

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que simulación económica y monitoreo se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar simulación económica y monitoreo, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con simulación económica y monitoreo.

### Pruebas

#### CSPTF-TEST-DEF-001 - Modelar invariantes económicas

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si modelar invariantes económicas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con modelar invariantes económicas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden modelar invariantes económicas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-002 - Validar valoración de activos y shares

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar valoración de activos y shares reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar valoración de activos y shares, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar valoración de activos y shares.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-003 - Evaluar colateral y factores de liquidación

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar colateral y factores de liquidación reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar colateral y factores de liquidación, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar colateral y factores de liquidación.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-004 - Comprobar exposición a flash liquidity

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar exposición a flash liquidity reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar exposición a flash liquidity, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar exposición a flash liquidity.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-005 - Analizar slippage, profundidad y concentración

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si analizar slippage, profundidad y concentración reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con analizar slippage, profundidad y concentración, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden analizar slippage, profundidad y concentración.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-006 - Revisar caps, pausas y límites dinámicos

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar caps, pausas y límites dinámicos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar caps, pausas y límites dinámicos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar caps, pausas y límites dinámicos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-007 - Evaluar redondeo, precisión y acumulación de fees

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar redondeo, precisión y acumulación de fees reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar redondeo, precisión y acumulación de fees, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar redondeo, precisión y acumulación de fees.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-008 - Comprobar incentivos y ataques de gobernanza económica

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar incentivos y ataques de gobernanza económica reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar incentivos y ataques de gobernanza económica, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar incentivos y ataques de gobernanza económica.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-009 - Analizar MEV, ordenamiento y sandwich risk

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si analizar mev, ordenamiento y sandwich risk reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con analizar mev, ordenamiento y sandwich risk, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden analizar mev, ordenamiento y sandwich risk.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-010 - Ejecutar simulaciones históricas y de estrés

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar simulaciones históricas y de estrés reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar simulaciones históricas y de estrés, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar simulaciones históricas y de estrés.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-011 - Validar insolvencia y socialización de pérdidas

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar insolvencia y socialización de pérdidas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar insolvencia y socialización de pérdidas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar insolvencia y socialización de pérdidas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-DEF-012 - Comprobar alertas de manipulación económica

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar alertas de manipulación económica reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar alertas de manipulación económica, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar alertas de manipulación económica.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-DEF-001` Manipulación de precio y extracción de valor: Actor externo, interno o automatizado intenta provocar manipulación de precio y extracción de valor para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-DEF-002` Insolvencia por liquidaciones fallidas: Actor externo, interno o automatizado intenta provocar insolvencia por liquidaciones fallidas para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-DEF-003` Ataque de liquidez temporal: Actor externo, interno o automatizado intenta provocar ataque de liquidez temporal para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-DEF-004` Drenaje por error de contabilidad de shares: Actor externo, interno o automatizado intenta provocar drenaje por error de contabilidad de shares para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-DEF-005` Captura de gobernanza económica: Actor externo, interno o automatizado intenta provocar captura de gobernanza económica para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-DEF-001` Oráculo poco robusto: Condición de diseño, implementación u operación caracterizada por oráculo poco robusto, capaz de facilitar amenazas del dominio DEF.
- `CSPTF-WEAK-DEF-002` Caps inexistentes: Condición de diseño, implementación u operación caracterizada por caps inexistentes, capaz de facilitar amenazas del dominio DEF.
- `CSPTF-WEAK-DEF-003` Supuestos de liquidez irreales: Condición de diseño, implementación u operación caracterizada por supuestos de liquidez irreales, capaz de facilitar amenazas del dominio DEF.
- `CSPTF-WEAK-DEF-004` Redondeo acumulativo: Condición de diseño, implementación u operación caracterizada por redondeo acumulativo, capaz de facilitar amenazas del dominio DEF.
- `CSPTF-WEAK-DEF-005` Dependencia de una sola ruta de liquidación: Condición de diseño, implementación u operación caracterizada por dependencia de una sola ruta de liquidación, capaz de facilitar amenazas del dominio DEF.

## 12.9 CSPTF-DOM-09 - ORA: Oráculos, datos externos y automatización

**English:** Oracles, External Data and Automation

**Propósito:** Evaluar autenticidad, frescura, disponibilidad, agregación y uso seguro de precios, datos, keepers y automatizaciones off-chain.

**Activos principales:** price feeds, data providers, keepers, relayers, webhooks, time sources, fallbacks, aggregation logic.

### Controles

#### CSPTF-CTRL-ORA-001 - Diversidad y gobernanza de fuentes

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que diversidad y gobernanza de fuentes se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar diversidad y gobernanza de fuentes, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con diversidad y gobernanza de fuentes.

#### CSPTF-CTRL-ORA-002 - Frescura, heartbeat y staleness

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que frescura, heartbeat y staleness se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar frescura, heartbeat y staleness, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con frescura, heartbeat y staleness.

#### CSPTF-CTRL-ORA-003 - Agregación y tolerancia a outliers

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que agregación y tolerancia a outliers se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar agregación y tolerancia a outliers, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con agregación y tolerancia a outliers.

#### CSPTF-CTRL-ORA-004 - Autenticidad e integridad de datos

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que autenticidad e integridad de datos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar autenticidad e integridad de datos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con autenticidad e integridad de datos.

#### CSPTF-CTRL-ORA-005 - Fallbacks y degradación segura

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que fallbacks y degradación segura se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar fallbacks y degradación segura, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con fallbacks y degradación segura.

#### CSPTF-CTRL-ORA-006 - Seguridad de keepers y automatización

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que seguridad de keepers y automatización se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar seguridad de keepers y automatización, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con seguridad de keepers y automatización.

#### CSPTF-CTRL-ORA-007 - Límites de uso y sanity checks

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que límites de uso y sanity checks se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar límites de uso y sanity checks, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con límites de uso y sanity checks.

#### CSPTF-CTRL-ORA-008 - Monitoreo y respuesta de oráculos

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que monitoreo y respuesta de oráculos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar monitoreo y respuesta de oráculos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con monitoreo y respuesta de oráculos.

### Pruebas

#### CSPTF-TEST-ORA-001 - Inventariar fuentes y dependencias

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si inventariar fuentes y dependencias reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con inventariar fuentes y dependencias, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden inventariar fuentes y dependencias.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-002 - Validar frescura y heartbeat

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar frescura y heartbeat reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar frescura y heartbeat, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar frescura y heartbeat.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-003 - Evaluar agregación y outliers

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar agregación y outliers reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar agregación y outliers, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar agregación y outliers.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-004 - Comprobar autenticidad de actualizaciones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar autenticidad de actualizaciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar autenticidad de actualizaciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar autenticidad de actualizaciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-005 - Revisar límites y sanity checks

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar límites y sanity checks reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar límites y sanity checks, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar límites y sanity checks.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-006 - Evaluar fallbacks y modo degradado

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar fallbacks y modo degradado reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar fallbacks y modo degradado, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar fallbacks y modo degradado.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-007 - Comprobar permisos de actualización

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar permisos de actualización reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar permisos de actualización, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar permisos de actualización.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-008 - Revisar keepers, jobs y secretos

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar keepers, jobs y secretos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar keepers, jobs y secretos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar keepers, jobs y secretos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-009 - Simular indisponibilidad de fuente

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si simular indisponibilidad de fuente reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con simular indisponibilidad de fuente, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden simular indisponibilidad de fuente.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-010 - Evaluar manipulación de mercado subyacente

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar manipulación de mercado subyacente reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar manipulación de mercado subyacente, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar manipulación de mercado subyacente.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-011 - Comprobar observabilidad y alertas

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar observabilidad y alertas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar observabilidad y alertas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar observabilidad y alertas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-ORA-012 - Validar recuperación tras datos incorrectos

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar recuperación tras datos incorrectos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar recuperación tras datos incorrectos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar recuperación tras datos incorrectos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-ORA-001` Manipulación de feed: Actor externo, interno o automatizado intenta provocar manipulación de feed para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-ORA-002` Uso de datos obsoletos: Actor externo, interno o automatizado intenta provocar uso de datos obsoletos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-ORA-003` Compromiso de updater o keeper: Actor externo, interno o automatizado intenta provocar compromiso de updater o keeper para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-ORA-004` Indisponibilidad coordinada de fuentes: Actor externo, interno o automatizado intenta provocar indisponibilidad coordinada de fuentes para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-ORA-005` Desviación de mercado de referencia: Actor externo, interno o automatizado intenta provocar desviación de mercado de referencia para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-ORA-001` Fuente única: Condición de diseño, implementación u operación caracterizada por fuente única, capaz de facilitar amenazas del dominio ORA.
- `CSPTF-WEAK-ORA-002` Staleness no controlado: Condición de diseño, implementación u operación caracterizada por staleness no controlado, capaz de facilitar amenazas del dominio ORA.
- `CSPTF-WEAK-ORA-003` Agregación débil: Condición de diseño, implementación u operación caracterizada por agregación débil, capaz de facilitar amenazas del dominio ORA.
- `CSPTF-WEAK-ORA-004` Fallback inseguro: Condición de diseño, implementación u operación caracterizada por fallback inseguro, capaz de facilitar amenazas del dominio ORA.
- `CSPTF-WEAK-ORA-005` Límites de precio ausentes: Condición de diseño, implementación u operación caracterizada por límites de precio ausentes, capaz de facilitar amenazas del dominio ORA.

## 12.10 CSPTF-DOM-10 - BRG: Bridges, cross-chain e interoperabilidad

**English:** Bridges, Cross-chain and Interoperability

**Propósito:** Evaluar bloqueo, mint, burn, release, validación de mensajes, relayers, verificadores, finalidad y coherencia entre dominios.

**Activos principales:** bridge contracts, validators, relayers, light clients, message queues, wrapped assets, proofs, source/destination chains.

### Controles

#### CSPTF-CTRL-BRG-001 - Modelo de confianza cross-chain

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que modelo de confianza cross-chain se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar modelo de confianza cross-chain, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con modelo de confianza cross-chain.

#### CSPTF-CTRL-BRG-002 - Autenticidad y unicidad de mensajes

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que autenticidad y unicidad de mensajes se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar autenticidad y unicidad de mensajes, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con autenticidad y unicidad de mensajes.

#### CSPTF-CTRL-BRG-003 - Finalidad y manejo de reorganizaciones

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que finalidad y manejo de reorganizaciones se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar finalidad y manejo de reorganizaciones, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con finalidad y manejo de reorganizaciones.

#### CSPTF-CTRL-BRG-004 - Custodia y respaldo de activos

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que custodia y respaldo de activos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar custodia y respaldo de activos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con custodia y respaldo de activos.

#### CSPTF-CTRL-BRG-005 - Validadores, relayers y quorum

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que validadores, relayers y quorum se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar validadores, relayers y quorum, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con validadores, relayers y quorum.

#### CSPTF-CTRL-BRG-006 - Coherencia semántica entre cadenas

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que coherencia semántica entre cadenas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar coherencia semántica entre cadenas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con coherencia semántica entre cadenas.

#### CSPTF-CTRL-BRG-007 - Rate limits, caps y pausas

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que rate limits, caps y pausas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar rate limits, caps y pausas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con rate limits, caps y pausas.

#### CSPTF-CTRL-BRG-008 - Monitoreo y reconciliación cross-chain

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que monitoreo y reconciliación cross-chain se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar monitoreo y reconciliación cross-chain, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con monitoreo y reconciliación cross-chain.

### Pruebas

#### CSPTF-TEST-BRG-001 - Documentar modelo de confianza del bridge

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si documentar modelo de confianza del bridge reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con documentar modelo de confianza del bridge, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden documentar modelo de confianza del bridge.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-002 - Validar autenticidad de mensajes

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar autenticidad de mensajes reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar autenticidad de mensajes, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar autenticidad de mensajes.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-003 - Comprobar nonce, replay y unicidad

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar nonce, replay y unicidad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar nonce, replay y unicidad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar nonce, replay y unicidad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-004 - Evaluar finalidad y reorganizaciones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar finalidad y reorganizaciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar finalidad y reorganizaciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar finalidad y reorganizaciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-005 - Revisar lock-mint y burn-release

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar lock-mint y burn-release reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar lock-mint y burn-release, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar lock-mint y burn-release.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-006 - Comprobar quorum y rotación de validadores

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar quorum y rotación de validadores reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar quorum y rotación de validadores, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar quorum y rotación de validadores.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-007 - Evaluar coherencia entre contratos de ambos lados

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar coherencia entre contratos de ambos lados reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar coherencia entre contratos de ambos lados, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar coherencia entre contratos de ambos lados.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-008 - Revisar proof verification o light client

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar proof verification o light client reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar proof verification o light client, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar proof verification o light client.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-009 - Validar caps, rate limits y pausas

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar caps, rate limits y pausas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar caps, rate limits y pausas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar caps, rate limits y pausas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-010 - Ejecutar reconciliación de supply y reservas

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar reconciliación de supply y reservas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar reconciliación de supply y reservas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar reconciliación de supply y reservas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-011 - Simular fallo de relayer o cadena

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si simular fallo de relayer o cadena reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con simular fallo de relayer o cadena, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden simular fallo de relayer o cadena.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-BRG-012 - Comprobar monitoreo y respuesta cross-chain

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar monitoreo y respuesta cross-chain reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar monitoreo y respuesta cross-chain, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar monitoreo y respuesta cross-chain.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-BRG-001` Falsificación o replay de mensaje cross-chain: Actor externo, interno o automatizado intenta provocar falsificación o replay de mensaje cross-chain para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-BRG-002` Compromiso del quorum de validadores: Actor externo, interno o automatizado intenta provocar compromiso del quorum de validadores para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-BRG-003` Mint sin respaldo o release duplicado: Actor externo, interno o automatizado intenta provocar mint sin respaldo o release duplicado para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-BRG-004` Fallo por reorganización o finalidad: Actor externo, interno o automatizado intenta provocar fallo por reorganización o finalidad para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-BRG-005` Inconsistencia lógica entre cadenas: Actor externo, interno o automatizado intenta provocar inconsistencia lógica entre cadenas para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-BRG-001` Dominio de mensaje ambiguo: Condición de diseño, implementación u operación caracterizada por dominio de mensaje ambiguo, capaz de facilitar amenazas del dominio BRG.
- `CSPTF-WEAK-BRG-002` Quorum concentrado: Condición de diseño, implementación u operación caracterizada por quorum concentrado, capaz de facilitar amenazas del dominio BRG.
- `CSPTF-WEAK-BRG-003` Reconciliación insuficiente: Condición de diseño, implementación u operación caracterizada por reconciliación insuficiente, capaz de facilitar amenazas del dominio BRG.
- `CSPTF-WEAK-BRG-004` Finalidad asumida incorrectamente: Condición de diseño, implementación u operación caracterizada por finalidad asumida incorrectamente, capaz de facilitar amenazas del dominio BRG.
- `CSPTF-WEAK-BRG-005` Rate limits ausentes: Condición de diseño, implementación u operación caracterizada por rate limits ausentes, capaz de facilitar amenazas del dominio BRG.

## 12.11 CSPTF-DOM-11 - NET: Consenso, validadores, nodos y redes P2P

**English:** Consensus, Validators, Nodes and P2P Networks

**Propósito:** Evaluar seguridad del consenso, operación de nodos, validadores, clientes, mempool, P2P, sincronización y exposición de interfaces.

**Activos principales:** validators, full nodes, consensus clients, execution clients, mempool, P2P network, genesis/config, peer discovery.

### Controles

#### CSPTF-CTRL-NET-001 - Configuración de consenso y génesis

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que configuración de consenso y génesis se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar configuración de consenso y génesis, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con configuración de consenso y génesis.

#### CSPTF-CTRL-NET-002 - Diversidad y endurecimiento de clientes

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que diversidad y endurecimiento de clientes se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar diversidad y endurecimiento de clientes, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con diversidad y endurecimiento de clientes.

#### CSPTF-CTRL-NET-003 - Gestión de identidades de validador

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que gestión de identidades de validador se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gestión de identidades de validador, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gestión de identidades de validador.

#### CSPTF-CTRL-NET-004 - Seguridad P2P y peer management

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que seguridad p2p y peer management se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar seguridad p2p y peer management, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con seguridad p2p y peer management.

#### CSPTF-CTRL-NET-005 - Mempool y propagación de transacciones

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que mempool y propagación de transacciones se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar mempool y propagación de transacciones, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con mempool y propagación de transacciones.

#### CSPTF-CTRL-NET-006 - Sincronización, checkpoints y estado

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que sincronización, checkpoints y estado se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar sincronización, checkpoints y estado, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con sincronización, checkpoints y estado.

#### CSPTF-CTRL-NET-007 - Protección contra slashing y equivocación

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que protección contra slashing y equivocación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar protección contra slashing y equivocación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con protección contra slashing y equivocación.

#### CSPTF-CTRL-NET-008 - Monitoreo, disponibilidad y recuperación

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que monitoreo, disponibilidad y recuperación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar monitoreo, disponibilidad y recuperación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con monitoreo, disponibilidad y recuperación.

### Pruebas

#### CSPTF-TEST-NET-001 - Revisar parámetros de consenso y génesis

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar parámetros de consenso y génesis reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar parámetros de consenso y génesis, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar parámetros de consenso y génesis.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-002 - Validar diversidad y versiones de clientes

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar diversidad y versiones de clientes reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar diversidad y versiones de clientes, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar diversidad y versiones de clientes.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-003 - Evaluar exposición de nodos y puertos

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar exposición de nodos y puertos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar exposición de nodos y puertos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar exposición de nodos y puertos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-004 - Comprobar peer discovery y allowlisting

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar peer discovery y allowlisting reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar peer discovery y allowlisting, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar peer discovery y allowlisting.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-005 - Revisar identidad y claves de validador

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar identidad y claves de validador reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar identidad y claves de validador, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar identidad y claves de validador.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-006 - Evaluar protección contra double signing

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar protección contra double signing reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar protección contra double signing, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar protección contra double signing.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-007 - Comprobar mempool y políticas de admisión

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar mempool y políticas de admisión reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar mempool y políticas de admisión, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar mempool y políticas de admisión.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-008 - Validar sincronización y checkpoints

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar sincronización y checkpoints reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar sincronización y checkpoints, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar sincronización y checkpoints.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-009 - Evaluar resistencia a particiones en laboratorio

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar resistencia a particiones en laboratorio reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar resistencia a particiones en laboratorio, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar resistencia a particiones en laboratorio.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-010 - Revisar límites de recursos y DoS

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar límites de recursos y dos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar límites de recursos y dos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar límites de recursos y dos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-011 - Comprobar backups y reconstrucción de estado

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar backups y reconstrucción de estado reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar backups y reconstrucción de estado, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar backups y reconstrucción de estado.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-NET-012 - Ejecutar simulación de indisponibilidad de validador

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar simulación de indisponibilidad de validador reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar simulación de indisponibilidad de validador, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar simulación de indisponibilidad de validador.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-NET-001` Partición o eclipse de nodos: Actor externo, interno o automatizado intenta provocar partición o eclipse de nodos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-NET-002` Compromiso de validador: Actor externo, interno o automatizado intenta provocar compromiso de validador para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-NET-003` Double signing o slashing: Actor externo, interno o automatizado intenta provocar double signing o slashing para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-NET-004` Explotación de cliente dominante: Actor externo, interno o automatizado intenta provocar explotación de cliente dominante para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-NET-005` Agotamiento de recursos P2P: Actor externo, interno o automatizado intenta provocar agotamiento de recursos p2p para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-NET-001` Puertos administrativos expuestos: Condición de diseño, implementación u operación caracterizada por puertos administrativos expuestos, capaz de facilitar amenazas del dominio NET.
- `CSPTF-WEAK-NET-002` Clientes sin diversidad: Condición de diseño, implementación u operación caracterizada por clientes sin diversidad, capaz de facilitar amenazas del dominio NET.
- `CSPTF-WEAK-NET-003` Protección anti-slashing insuficiente: Condición de diseño, implementación u operación caracterizada por protección anti-slashing insuficiente, capaz de facilitar amenazas del dominio NET.
- `CSPTF-WEAK-NET-004` Peer management débil: Condición de diseño, implementación u operación caracterizada por peer management débil, capaz de facilitar amenazas del dominio NET.
- `CSPTF-WEAK-NET-005` Recuperación de estado no probada: Condición de diseño, implementación u operación caracterizada por recuperación de estado no probada, capaz de facilitar amenazas del dominio NET.

## 12.12 CSPTF-DOM-12 - L2: Layer 2, rollups, secuenciadores y disponibilidad de datos

**English:** Layer 2, Rollups, Sequencers and Data Availability

**Propósito:** Evaluar pruebas, secuenciación, publicación de datos, puentes canónicos, ventanas de desafío, escape hatches y dependencias L1/L2.

**Activos principales:** sequencers, provers, verifiers, data availability, canonical bridge, fraud proofs, validity proofs, batch inbox.

### Controles

#### CSPTF-CTRL-L2-001 - Modelo de seguridad L1/L2

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que modelo de seguridad l1/l2 se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar modelo de seguridad l1/l2, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con modelo de seguridad l1/l2.

#### CSPTF-CTRL-L2-002 - Integridad de batches y secuenciación

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que integridad de batches y secuenciación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar integridad de batches y secuenciación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con integridad de batches y secuenciación.

#### CSPTF-CTRL-L2-003 - Pruebas de fraude o validez

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que pruebas de fraude o validez se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar pruebas de fraude o validez, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con pruebas de fraude o validez.

#### CSPTF-CTRL-L2-004 - Disponibilidad y publicación de datos

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que disponibilidad y publicación de datos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar disponibilidad y publicación de datos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con disponibilidad y publicación de datos.

#### CSPTF-CTRL-L2-005 - Puente canónico y mensajería

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que puente canónico y mensajería se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar puente canónico y mensajería, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con puente canónico y mensajería.

#### CSPTF-CTRL-L2-006 - Censura, forced inclusion y escape

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que censura, forced inclusion y escape se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar censura, forced inclusion y escape, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con censura, forced inclusion y escape.

#### CSPTF-CTRL-L2-007 - Actualizaciones y claves administrativas

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que actualizaciones y claves administrativas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar actualizaciones y claves administrativas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con actualizaciones y claves administrativas.

#### CSPTF-CTRL-L2-008 - Monitoreo de estado y discrepancias

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que monitoreo de estado y discrepancias se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar monitoreo de estado y discrepancias, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con monitoreo de estado y discrepancias.

### Pruebas

#### CSPTF-TEST-L2-001 - Documentar supuestos L1/L2

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si documentar supuestos l1/l2 reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con documentar supuestos l1/l2, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden documentar supuestos l1/l2.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-002 - Validar construcción y envío de batches

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar construcción y envío de batches reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar construcción y envío de batches, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar construcción y envío de batches.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-003 - Revisar verificación de pruebas

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar verificación de pruebas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar verificación de pruebas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar verificación de pruebas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-004 - Comprobar disponibilidad y reconstrucción de datos

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar disponibilidad y reconstrucción de datos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar disponibilidad y reconstrucción de datos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar disponibilidad y reconstrucción de datos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-005 - Evaluar puente canónico y retiros

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar puente canónico y retiros reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar puente canónico y retiros, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar puente canónico y retiros.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-006 - Validar ventanas de desafío

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar ventanas de desafío reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar ventanas de desafío, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar ventanas de desafío.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-007 - Revisar forced inclusion y resistencia a censura

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar forced inclusion y resistencia a censura reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar forced inclusion y resistencia a censura, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar forced inclusion y resistencia a censura.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-008 - Comprobar roles de secuenciador y prover

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar roles de secuenciador y prover reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar roles de secuenciador y prover, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar roles de secuenciador y prover.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-009 - Evaluar downtime y recuperación

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar downtime y recuperación reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar downtime y recuperación, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar downtime y recuperación.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-010 - Revisar upgrades y timelocks

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar upgrades y timelocks reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar upgrades y timelocks, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar upgrades y timelocks.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-011 - Comprobar coherencia de estado L1/L2

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar coherencia de estado l1/l2 reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar coherencia de estado l1/l2, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar coherencia de estado l1/l2.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-L2-012 - Ejecutar simulación de falla de secuenciador

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar simulación de falla de secuenciador reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar simulación de falla de secuenciador, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar simulación de falla de secuenciador.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-L2-001` Prueba inválida aceptada: Actor externo, interno o automatizado intenta provocar prueba inválida aceptada para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-L2-002` Censura o indisponibilidad del secuenciador: Actor externo, interno o automatizado intenta provocar censura o indisponibilidad del secuenciador para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-L2-003` Pérdida de disponibilidad de datos: Actor externo, interno o automatizado intenta provocar pérdida de disponibilidad de datos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-L2-004` Fraude en puente canónico: Actor externo, interno o automatizado intenta provocar fraude en puente canónico para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-L2-005` Actualización administrativa maliciosa: Actor externo, interno o automatizado intenta provocar actualización administrativa maliciosa para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-L2-001` Escape hatch no probado: Condición de diseño, implementación u operación caracterizada por escape hatch no probado, capaz de facilitar amenazas del dominio L2.
- `CSPTF-WEAK-L2-002` DA centralizada: Condición de diseño, implementación u operación caracterizada por da centralizada, capaz de facilitar amenazas del dominio L2.
- `CSPTF-WEAK-L2-003` Timelock insuficiente: Condición de diseño, implementación u operación caracterizada por timelock insuficiente, capaz de facilitar amenazas del dominio L2.
- `CSPTF-WEAK-L2-004` Dependencia de un solo prover: Condición de diseño, implementación u operación caracterizada por dependencia de un solo prover, capaz de facilitar amenazas del dominio L2.
- `CSPTF-WEAK-L2-005` Monitoreo de discrepancias ausente: Condición de diseño, implementación u operación caracterizada por monitoreo de discrepancias ausente, capaz de facilitar amenazas del dominio L2.

## 12.13 CSPTF-DOM-13 - CEX: Exchanges centralizados, brokers e infraestructura de mercado

**English:** Centralized Exchanges, Brokers and Market Infrastructure

**Propósito:** Evaluar onboarding, cuentas, trading, depósitos, retiros, matching, custodia, reservas, fraude y procesos operacionales de plataformas centralizadas.

**Activos principales:** accounts, matching engine, OMS, deposit services, withdrawal services, custody, market data, treasury.

### Controles

#### CSPTF-CTRL-CEX-001 - Seguridad de cuentas y autenticación

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que seguridad de cuentas y autenticación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar seguridad de cuentas y autenticación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con seguridad de cuentas y autenticación.

#### CSPTF-CTRL-CEX-002 - Integridad de órdenes y matching

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que integridad de órdenes y matching se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar integridad de órdenes y matching, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con integridad de órdenes y matching.

#### CSPTF-CTRL-CEX-003 - Depósitos, confirmaciones y atribución

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que depósitos, confirmaciones y atribución se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar depósitos, confirmaciones y atribución, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con depósitos, confirmaciones y atribución.

#### CSPTF-CTRL-CEX-004 - Retiros, límites y aprobaciones

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que retiros, límites y aprobaciones se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar retiros, límites y aprobaciones, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con retiros, límites y aprobaciones.

#### CSPTF-CTRL-CEX-005 - Custodia y tesorería segregadas

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que custodia y tesorería segregadas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar custodia y tesorería segregadas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con custodia y tesorería segregadas.

#### CSPTF-CTRL-CEX-006 - Market data y prevención de abuso

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que market data y prevención de abuso se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar market data y prevención de abuso, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con market data y prevención de abuso.

#### CSPTF-CTRL-CEX-007 - Reservas, pasivos y reconciliación

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que reservas, pasivos y reconciliación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar reservas, pasivos y reconciliación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con reservas, pasivos y reconciliación.

#### CSPTF-CTRL-CEX-008 - Fraude, monitoreo y continuidad operacional

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que fraude, monitoreo y continuidad operacional se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar fraude, monitoreo y continuidad operacional, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con fraude, monitoreo y continuidad operacional.

### Pruebas

#### CSPTF-TEST-CEX-001 - Evaluar registro, recuperación y MFA

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar registro, recuperación y mfa reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar registro, recuperación y mfa, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar registro, recuperación y mfa.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-002 - Revisar autorización de cuentas y roles

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar autorización de cuentas y roles reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar autorización de cuentas y roles, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar autorización de cuentas y roles.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-003 - Validar integridad del ciclo de órdenes

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar integridad del ciclo de órdenes reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar integridad del ciclo de órdenes, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar integridad del ciclo de órdenes.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-004 - Comprobar idempotencia y concurrencia

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar idempotencia y concurrencia reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar idempotencia y concurrencia, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar idempotencia y concurrencia.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-005 - Evaluar depósitos y políticas de confirmación

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar depósitos y políticas de confirmación reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar depósitos y políticas de confirmación, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar depósitos y políticas de confirmación.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-006 - Revisar retiros, allowlists y cooling-off

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar retiros, allowlists y cooling-off reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar retiros, allowlists y cooling-off, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar retiros, allowlists y cooling-off.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-007 - Validar segregación de custodia y tesorería

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar segregación de custodia y tesorería reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar segregación de custodia y tesorería, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar segregación de custodia y tesorería.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-008 - Comprobar reconciliación de libros y cadena

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar reconciliación de libros y cadena reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar reconciliación de libros y cadena, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar reconciliación de libros y cadena.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-009 - Evaluar manipulación de market data

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar manipulación de market data reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar manipulación de market data, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar manipulación de market data.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-010 - Revisar controles antifraude y abuso interno

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar controles antifraude y abuso interno reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar controles antifraude y abuso interno, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar controles antifraude y abuso interno.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-011 - Simular interrupción del matching en laboratorio

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si simular interrupción del matching en laboratorio reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con simular interrupción del matching en laboratorio, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden simular interrupción del matching en laboratorio.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-CEX-012 - Validar continuidad, reservas y comunicación

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar continuidad, reservas y comunicación reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar continuidad, reservas y comunicación, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar continuidad, reservas y comunicación.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-CEX-001` Toma de cuenta y retiro fraudulento: Actor externo, interno o automatizado intenta provocar toma de cuenta y retiro fraudulento para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-CEX-002` Manipulación o pérdida de órdenes: Actor externo, interno o automatizado intenta provocar manipulación o pérdida de órdenes para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-CEX-003` Atribución incorrecta de depósitos: Actor externo, interno o automatizado intenta provocar atribución incorrecta de depósitos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-CEX-004` Abuso interno de tesorería: Actor externo, interno o automatizado intenta provocar abuso interno de tesorería para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-CEX-005` Descuadre entre reservas y pasivos: Actor externo, interno o automatizado intenta provocar descuadre entre reservas y pasivos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-CEX-001` Recuperación de cuenta débil: Condición de diseño, implementación u operación caracterizada por recuperación de cuenta débil, capaz de facilitar amenazas del dominio CEX.
- `CSPTF-WEAK-CEX-002` Idempotencia insuficiente: Condición de diseño, implementación u operación caracterizada por idempotencia insuficiente, capaz de facilitar amenazas del dominio CEX.
- `CSPTF-WEAK-CEX-003` Límites de retiro inadecuados: Condición de diseño, implementación u operación caracterizada por límites de retiro inadecuados, capaz de facilitar amenazas del dominio CEX.
- `CSPTF-WEAK-CEX-004` Reconciliación tardía: Condición de diseño, implementación u operación caracterizada por reconciliación tardía, capaz de facilitar amenazas del dominio CEX.
- `CSPTF-WEAK-CEX-005` Segregación de funciones deficiente: Condición de diseño, implementación u operación caracterizada por segregación de funciones deficiente, capaz de facilitar amenazas del dominio CEX.

## 12.14 CSPTF-DOM-14 - API: APIs, RPC, WebSocket y plataformas para desarrolladores

**English:** APIs, RPC, WebSocket and Developer Platforms

**Propósito:** Evaluar autenticación, autorización, exposición, rate limiting, seguridad de métodos, datos y disponibilidad en interfaces programáticas.

**Activos principales:** REST APIs, GraphQL, JSON-RPC, WebSocket, API keys, developer portals, webhooks, indexers.

### Controles

#### CSPTF-CTRL-API-001 - Inventario y clasificación de interfaces

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que inventario y clasificación de interfaces se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar inventario y clasificación de interfaces, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con inventario y clasificación de interfaces.

#### CSPTF-CTRL-API-002 - Autenticación y gestión de credenciales

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que autenticación y gestión de credenciales se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar autenticación y gestión de credenciales, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con autenticación y gestión de credenciales.

#### CSPTF-CTRL-API-003 - Autorización por objeto y función

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que autorización por objeto y función se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar autorización por objeto y función, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con autorización por objeto y función.

#### CSPTF-CTRL-API-004 - Métodos RPC y superficies administrativas

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que métodos rpc y superficies administrativas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar métodos rpc y superficies administrativas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con métodos rpc y superficies administrativas.

#### CSPTF-CTRL-API-005 - Rate limiting, cuotas y antiabuso

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que rate limiting, cuotas y antiabuso se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar rate limiting, cuotas y antiabuso, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con rate limiting, cuotas y antiabuso.

#### CSPTF-CTRL-API-006 - Validación de entradas y salidas

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que validación de entradas y salidas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar validación de entradas y salidas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con validación de entradas y salidas.

#### CSPTF-CTRL-API-007 - Webhooks, WebSocket y eventos

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que webhooks, websocket y eventos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar webhooks, websocket y eventos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con webhooks, websocket y eventos.

#### CSPTF-CTRL-API-008 - Observabilidad, versionado y retiro seguro

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que observabilidad, versionado y retiro seguro se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar observabilidad, versionado y retiro seguro, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con observabilidad, versionado y retiro seguro.

### Pruebas

#### CSPTF-TEST-API-001 - Inventariar endpoints, métodos y versiones

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si inventariar endpoints, métodos y versiones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con inventariar endpoints, métodos y versiones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden inventariar endpoints, métodos y versiones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-002 - Evaluar autenticación y ciclo de API keys

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar autenticación y ciclo de api keys reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar autenticación y ciclo de api keys, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar autenticación y ciclo de api keys.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-003 - Comprobar autorización por objeto

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar autorización por objeto reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar autorización por objeto, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar autorización por objeto.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-004 - Revisar métodos RPC sensibles

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar métodos rpc sensibles reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar métodos rpc sensibles, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar métodos rpc sensibles.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-005 - Validar rate limiting y cuotas

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar rate limiting y cuotas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar rate limiting y cuotas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar rate limiting y cuotas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-006 - Evaluar validación de parámetros

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar validación de parámetros reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar validación de parámetros, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar validación de parámetros.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-007 - Comprobar filtrado de datos sensibles

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar filtrado de datos sensibles reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar filtrado de datos sensibles, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar filtrado de datos sensibles.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-008 - Revisar WebSocket, suscripciones y sesiones

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar websocket, suscripciones y sesiones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar websocket, suscripciones y sesiones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar websocket, suscripciones y sesiones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-009 - Validar autenticidad de webhooks

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar autenticidad de webhooks reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar autenticidad de webhooks, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar autenticidad de webhooks.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-010 - Evaluar errores, logs y exposición de stack

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar errores, logs y exposición de stack reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar errores, logs y exposición de stack, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar errores, logs y exposición de stack.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-011 - Comprobar versionado y compatibilidad

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar versionado y compatibilidad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar versionado y compatibilidad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar versionado y compatibilidad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-API-012 - Ejecutar pruebas de resiliencia no destructivas

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar pruebas de resiliencia no destructivas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar pruebas de resiliencia no destructivas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar pruebas de resiliencia no destructivas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-API-001` Abuso de método RPC administrativo: Actor externo, interno o automatizado intenta provocar abuso de método rpc administrativo para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-API-002` Acceso no autorizado a objetos: Actor externo, interno o automatizado intenta provocar acceso no autorizado a objetos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-API-003` Exfiltración de datos por API: Actor externo, interno o automatizado intenta provocar exfiltración de datos por api para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-API-004` Agotamiento de cuota o recursos: Actor externo, interno o automatizado intenta provocar agotamiento de cuota o recursos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-API-005` Falsificación de webhook o evento: Actor externo, interno o automatizado intenta provocar falsificación de webhook o evento para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-API-001` API keys de larga duración: Condición de diseño, implementación u operación caracterizada por api keys de larga duración, capaz de facilitar amenazas del dominio API.
- `CSPTF-WEAK-API-002` Autorización a nivel objeto ausente: Condición de diseño, implementación u operación caracterizada por autorización a nivel objeto ausente, capaz de facilitar amenazas del dominio API.
- `CSPTF-WEAK-API-003` RPC administrativo expuesto: Condición de diseño, implementación u operación caracterizada por rpc administrativo expuesto, capaz de facilitar amenazas del dominio API.
- `CSPTF-WEAK-API-004` Rate limits inconsistentes: Condición de diseño, implementación u operación caracterizada por rate limits inconsistentes, capaz de facilitar amenazas del dominio API.
- `CSPTF-WEAK-API-005` Errores excesivamente informativos: Condición de diseño, implementación u operación caracterizada por errores excesivamente informativos, capaz de facilitar amenazas del dominio API.

## 12.15 CSPTF-DOM-15 - INF: Cloud, contenedores, CI/CD e infraestructura

**English:** Cloud, Containers, CI/CD and Infrastructure

**Propósito:** Evaluar la infraestructura que construye, despliega y opera servicios de activos digitales, incluyendo secretos, IaC, imágenes y pipelines.

**Activos principales:** cloud accounts, Kubernetes, containers, CI/CD, IaC, artifact registries, secrets managers, observability stack.

### Controles

#### CSPTF-CTRL-INF-001 - Arquitectura cloud y segmentación

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que arquitectura cloud y segmentación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar arquitectura cloud y segmentación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con arquitectura cloud y segmentación.

#### CSPTF-CTRL-INF-002 - IAM de infraestructura y privilegios

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que iam de infraestructura y privilegios se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar iam de infraestructura y privilegios, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con iam de infraestructura y privilegios.

#### CSPTF-CTRL-INF-003 - Gestión de secretos y KMS

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que gestión de secretos y kms se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gestión de secretos y kms, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gestión de secretos y kms.

#### CSPTF-CTRL-INF-004 - Endurecimiento de contenedores y orquestación

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que endurecimiento de contenedores y orquestación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar endurecimiento de contenedores y orquestación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con endurecimiento de contenedores y orquestación.

#### CSPTF-CTRL-INF-005 - Integridad de CI/CD y releases

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que integridad de ci/cd y releases se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar integridad de ci/cd y releases, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con integridad de ci/cd y releases.

#### CSPTF-CTRL-INF-006 - IaC, configuración y drift

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que iac, configuración y drift se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar iac, configuración y drift, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con iac, configuración y drift.

#### CSPTF-CTRL-INF-007 - Red, exposición y protección perimetral

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que red, exposición y protección perimetral se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar red, exposición y protección perimetral, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con red, exposición y protección perimetral.

#### CSPTF-CTRL-INF-008 - Respaldo, continuidad y recuperación

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que respaldo, continuidad y recuperación se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar respaldo, continuidad y recuperación, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con respaldo, continuidad y recuperación.

### Pruebas

#### CSPTF-TEST-INF-001 - Revisar cuentas, proyectos y segmentación

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar cuentas, proyectos y segmentación reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar cuentas, proyectos y segmentación, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar cuentas, proyectos y segmentación.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-002 - Evaluar IAM y privilegios cloud

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar iam y privilegios cloud reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar iam y privilegios cloud, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar iam y privilegios cloud.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-003 - Comprobar secretos, KMS y rotación

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar secretos, kms y rotación reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar secretos, kms y rotación, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar secretos, kms y rotación.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-004 - Revisar imágenes y configuración de contenedores

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar imágenes y configuración de contenedores reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar imágenes y configuración de contenedores, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar imágenes y configuración de contenedores.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-005 - Evaluar controles de Kubernetes

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar controles de kubernetes reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar controles de kubernetes, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar controles de kubernetes.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-006 - Comprobar integridad del pipeline y aprobaciones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar integridad del pipeline y aprobaciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar integridad del pipeline y aprobaciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar integridad del pipeline y aprobaciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-007 - Validar firma y procedencia de artefactos

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar firma y procedencia de artefactos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar firma y procedencia de artefactos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar firma y procedencia de artefactos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-008 - Revisar IaC y drift de configuración

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar iac y drift de configuración reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar iac y drift de configuración, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar iac y drift de configuración.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-009 - Evaluar exposición de red y servicios

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar exposición de red y servicios reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar exposición de red y servicios, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar exposición de red y servicios.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-010 - Comprobar logs, métricas y alertas

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar logs, métricas y alertas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar logs, métricas y alertas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar logs, métricas y alertas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-011 - Validar backups y restauración

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar backups y restauración reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar backups y restauración, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar backups y restauración.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-INF-012 - Simular pérdida controlada de un componente

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si simular pérdida controlada de un componente reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con simular pérdida controlada de un componente, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden simular pérdida controlada de un componente.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-INF-001` Compromiso de pipeline de despliegue: Actor externo, interno o automatizado intenta provocar compromiso de pipeline de despliegue para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-INF-002` Exposición de secreto de producción: Actor externo, interno o automatizado intenta provocar exposición de secreto de producción para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-INF-003` Escape o abuso de contenedor: Actor externo, interno o automatizado intenta provocar escape o abuso de contenedor para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-INF-004` Toma de cuenta cloud privilegiada: Actor externo, interno o automatizado intenta provocar toma de cuenta cloud privilegiada para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-INF-005` Pérdida de infraestructura sin recuperación: Actor externo, interno o automatizado intenta provocar pérdida de infraestructura sin recuperación para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-INF-001` Roles cloud excesivos: Condición de diseño, implementación u operación caracterizada por roles cloud excesivos, capaz de facilitar amenazas del dominio INF.
- `CSPTF-WEAK-INF-002` Secretos en variables o repositorios: Condición de diseño, implementación u operación caracterizada por secretos en variables o repositorios, capaz de facilitar amenazas del dominio INF.
- `CSPTF-WEAK-INF-003` Imágenes no firmadas: Condición de diseño, implementación u operación caracterizada por imágenes no firmadas, capaz de facilitar amenazas del dominio INF.
- `CSPTF-WEAK-INF-004` Kubernetes mal endurecido: Condición de diseño, implementación u operación caracterizada por kubernetes mal endurecido, capaz de facilitar amenazas del dominio INF.
- `CSPTF-WEAK-INF-005` Backups no restaurados en pruebas: Condición de diseño, implementación u operación caracterizada por backups no restaurados en pruebas, capaz de facilitar amenazas del dominio INF.

## 12.16 CSPTF-DOM-16 - IAM: Identidad, acceso privilegiado y riesgo interno

**English:** Identity, Privileged Access and Insider Risk

**Propósito:** Evaluar identidades humanas y de máquina, acceso privilegiado, segregación, revisiones, monitoreo y controles frente a fraude o abuso interno.

**Activos principales:** workforce identities, service accounts, PAM, break-glass accounts, admin consoles, signer roles, vendors, joiner-mover-leaver.

### Controles

#### CSPTF-CTRL-IAM-001 - Gobierno del ciclo de identidad

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que gobierno del ciclo de identidad se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gobierno del ciclo de identidad, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gobierno del ciclo de identidad.

#### CSPTF-CTRL-IAM-002 - MFA resistente y autenticación fuerte

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que mfa resistente y autenticación fuerte se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar mfa resistente y autenticación fuerte, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con mfa resistente y autenticación fuerte.

#### CSPTF-CTRL-IAM-003 - Mínimo privilegio y acceso just-in-time

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que mínimo privilegio y acceso just-in-time se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar mínimo privilegio y acceso just-in-time, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con mínimo privilegio y acceso just-in-time.

#### CSPTF-CTRL-IAM-004 - Segregación de funciones críticas

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que segregación de funciones críticas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar segregación de funciones críticas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con segregación de funciones críticas.

#### CSPTF-CTRL-IAM-005 - PAM, sesiones y cuentas break-glass

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que pam, sesiones y cuentas break-glass se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar pam, sesiones y cuentas break-glass, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con pam, sesiones y cuentas break-glass.

#### CSPTF-CTRL-IAM-006 - Identidades de máquina y workloads

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que identidades de máquina y workloads se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar identidades de máquina y workloads, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con identidades de máquina y workloads.

#### CSPTF-CTRL-IAM-007 - Monitoreo de comportamiento privilegiado

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que monitoreo de comportamiento privilegiado se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar monitoreo de comportamiento privilegiado, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con monitoreo de comportamiento privilegiado.

#### CSPTF-CTRL-IAM-008 - Gestión de terceros y salida segura

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que gestión de terceros y salida segura se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gestión de terceros y salida segura, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gestión de terceros y salida segura.

### Pruebas

#### CSPTF-TEST-IAM-001 - Revisar altas, cambios y bajas

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar altas, cambios y bajas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar altas, cambios y bajas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar altas, cambios y bajas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-002 - Evaluar MFA y recuperación de acceso

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar mfa y recuperación de acceso reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar mfa y recuperación de acceso, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar mfa y recuperación de acceso.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-003 - Comprobar privilegios efectivos

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar privilegios efectivos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar privilegios efectivos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar privilegios efectivos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-004 - Validar segregación de funciones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar segregación de funciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar segregación de funciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar segregación de funciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-005 - Revisar PAM y grabación de sesiones

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar pam y grabación de sesiones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar pam y grabación de sesiones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar pam y grabación de sesiones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-006 - Comprobar cuentas break-glass

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar cuentas break-glass reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar cuentas break-glass, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar cuentas break-glass.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-007 - Evaluar identidades de máquina

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar identidades de máquina reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar identidades de máquina, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar identidades de máquina.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-008 - Revisar accesos de terceros

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar accesos de terceros reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar accesos de terceros, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar accesos de terceros.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-009 - Validar recertificación periódica

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar recertificación periódica reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar recertificación periódica, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar recertificación periódica.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-010 - Comprobar monitoreo de acciones críticas

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar monitoreo de acciones críticas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar monitoreo de acciones críticas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar monitoreo de acciones críticas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-011 - Ejecutar tabletop de abuso interno

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar tabletop de abuso interno reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar tabletop de abuso interno, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar tabletop de abuso interno.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IAM-012 - Validar revocación y preservación de evidencia

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar revocación y preservación de evidencia reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar revocación y preservación de evidencia, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar revocación y preservación de evidencia.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-IAM-001` Abuso de administrador o firmante: Actor externo, interno o automatizado intenta provocar abuso de administrador o firmante para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-IAM-002` Toma de cuenta privilegiada: Actor externo, interno o automatizado intenta provocar toma de cuenta privilegiada para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-IAM-003` Persistencia de excolaborador o tercero: Actor externo, interno o automatizado intenta provocar persistencia de excolaborador o tercero para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-IAM-004` Colusión entre funciones críticas: Actor externo, interno o automatizado intenta provocar colusión entre funciones críticas para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-IAM-005` Uso no autorizado de identidad de máquina: Actor externo, interno o automatizado intenta provocar uso no autorizado de identidad de máquina para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-IAM-001` Privilegios permanentes: Condición de diseño, implementación u operación caracterizada por privilegios permanentes, capaz de facilitar amenazas del dominio IAM.
- `CSPTF-WEAK-IAM-002` MFA recuperable por canal débil: Condición de diseño, implementación u operación caracterizada por mfa recuperable por canal débil, capaz de facilitar amenazas del dominio IAM.
- `CSPTF-WEAK-IAM-003` Segregación de funciones incompleta: Condición de diseño, implementación u operación caracterizada por segregación de funciones incompleta, capaz de facilitar amenazas del dominio IAM.
- `CSPTF-WEAK-IAM-004` Cuentas compartidas: Condición de diseño, implementación u operación caracterizada por cuentas compartidas, capaz de facilitar amenazas del dominio IAM.
- `CSPTF-WEAK-IAM-005` Recertificación insuficiente: Condición de diseño, implementación u operación caracterizada por recertificación insuficiente, capaz de facilitar amenazas del dominio IAM.

## 12.17 CSPTF-DOM-17 - SUP: Cadena de suministro, dependencias e integridad de construcción

**English:** Supply Chain, Dependencies and Build Integrity

**Propósito:** Evaluar componentes, repositorios, compiladores, paquetes, artefactos, proveedores y procedencia del software y firmware.

**Activos principales:** source repositories, dependencies, package registries, compilers, build runners, artifacts, firmware, vendors.

### Controles

#### CSPTF-CTRL-SUP-001 - Inventario SBOM y dependencias

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que inventario sbom y dependencias se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar inventario sbom y dependencias, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con inventario sbom y dependencias.

#### CSPTF-CTRL-SUP-002 - Gobierno de repositorios y ramas

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que gobierno de repositorios y ramas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gobierno de repositorios y ramas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gobierno de repositorios y ramas.

#### CSPTF-CTRL-SUP-003 - Verificación de paquetes y procedencia

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que verificación de paquetes y procedencia se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar verificación de paquetes y procedencia, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con verificación de paquetes y procedencia.

#### CSPTF-CTRL-SUP-004 - Entornos de construcción aislados

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que entornos de construcción aislados se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar entornos de construcción aislados, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con entornos de construcción aislados.

#### CSPTF-CTRL-SUP-005 - Firmas, reproducibilidad y releases

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que firmas, reproducibilidad y releases se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar firmas, reproducibilidad y releases, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con firmas, reproducibilidad y releases.

#### CSPTF-CTRL-SUP-006 - Gestión de vulnerabilidades de terceros

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que gestión de vulnerabilidades de terceros se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gestión de vulnerabilidades de terceros, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gestión de vulnerabilidades de terceros.

#### CSPTF-CTRL-SUP-007 - Firmware y hardware de confianza

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que firmware y hardware de confianza se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar firmware y hardware de confianza, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con firmware y hardware de confianza.

#### CSPTF-CTRL-SUP-008 - Respuesta a compromiso de supply chain

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que respuesta a compromiso de supply chain se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar respuesta a compromiso de supply chain, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con respuesta a compromiso de supply chain.

### Pruebas

#### CSPTF-TEST-SUP-001 - Generar y revisar SBOM

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si generar y revisar sbom reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con generar y revisar sbom, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden generar y revisar sbom.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-002 - Validar protección de ramas y revisiones

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar protección de ramas y revisiones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar protección de ramas y revisiones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar protección de ramas y revisiones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-003 - Evaluar dependencias directas y transitivas

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar dependencias directas y transitivas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar dependencias directas y transitivas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar dependencias directas y transitivas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-004 - Comprobar pinning, hashes y registries

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar pinning, hashes y registries reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar pinning, hashes y registries, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar pinning, hashes y registries.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-005 - Revisar runners y entornos de build

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar runners y entornos de build reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar runners y entornos de build, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar runners y entornos de build.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-006 - Validar firma y procedencia de artefactos

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar firma y procedencia de artefactos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar firma y procedencia de artefactos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar firma y procedencia de artefactos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-007 - Comprobar builds reproducibles donde aplique

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar builds reproducibles donde aplique reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar builds reproducibles donde aplique, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar builds reproducibles donde aplique.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-008 - Evaluar compiladores y toolchains

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar compiladores y toolchains reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar compiladores y toolchains, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar compiladores y toolchains.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-009 - Revisar firmware y actualizaciones

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar firmware y actualizaciones reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar firmware y actualizaciones, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar firmware y actualizaciones.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-010 - Validar riesgo y acceso de proveedores

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar riesgo y acceso de proveedores reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar riesgo y acceso de proveedores, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar riesgo y acceso de proveedores.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-011 - Simular revocación de componente comprometido

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si simular revocación de componente comprometido reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con simular revocación de componente comprometido, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden simular revocación de componente comprometido.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-SUP-012 - Comprobar detección de cambios no autorizados

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar detección de cambios no autorizados reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar detección de cambios no autorizados, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar detección de cambios no autorizados.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-SUP-001` Paquete o dependencia maliciosa: Actor externo, interno o automatizado intenta provocar paquete o dependencia maliciosa para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-SUP-002` Compromiso de repositorio o maintainer: Actor externo, interno o automatizado intenta provocar compromiso de repositorio o maintainer para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-SUP-003` Manipulación del pipeline de build: Actor externo, interno o automatizado intenta provocar manipulación del pipeline de build para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-SUP-004` Firmware o dispositivo adulterado: Actor externo, interno o automatizado intenta provocar firmware o dispositivo adulterado para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-SUP-005` Actualización comprometida distribuida: Actor externo, interno o automatizado intenta provocar actualización comprometida distribuida para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-SUP-001` Dependencias sin pinning: Condición de diseño, implementación u operación caracterizada por dependencias sin pinning, capaz de facilitar amenazas del dominio SUP.
- `CSPTF-WEAK-SUP-002` Artefactos no firmados: Condición de diseño, implementación u operación caracterizada por artefactos no firmados, capaz de facilitar amenazas del dominio SUP.
- `CSPTF-WEAK-SUP-003` Runners compartidos y privilegiados: Condición de diseño, implementación u operación caracterizada por runners compartidos y privilegiados, capaz de facilitar amenazas del dominio SUP.
- `CSPTF-WEAK-SUP-004` SBOM ausente: Condición de diseño, implementación u operación caracterizada por sbom ausente, capaz de facilitar amenazas del dominio SUP.
- `CSPTF-WEAK-SUP-005` Proveedores sin evaluación continua: Condición de diseño, implementación u operación caracterizada por proveedores sin evaluación continua, capaz de facilitar amenazas del dominio SUP.

## 12.18 CSPTF-DOM-18 - REG: Privacidad, cumplimiento, AML/KYT y protección de datos

**English:** Privacy, Compliance, AML/KYT and Data Protection

**Propósito:** Evaluar obligaciones aplicables, minimización, trazabilidad, privacidad, controles AML/KYT y tratamiento seguro de datos personales y financieros.

**Activos principales:** PII, KYC records, transaction monitoring, sanctions screening, travel rule data, audit records, privacy notices, retention systems.

### Controles

#### CSPTF-CTRL-REG-001 - Inventario de obligaciones y jurisdicciones

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que inventario de obligaciones y jurisdicciones se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar inventario de obligaciones y jurisdicciones, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con inventario de obligaciones y jurisdicciones.

#### CSPTF-CTRL-REG-002 - Minimización y propósito de datos

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que minimización y propósito de datos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar minimización y propósito de datos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con minimización y propósito de datos.

#### CSPTF-CTRL-REG-003 - Seguridad de KYC y datos sensibles

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que seguridad de kyc y datos sensibles se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar seguridad de kyc y datos sensibles, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con seguridad de kyc y datos sensibles.

#### CSPTF-CTRL-REG-004 - AML, KYT y screening basado en riesgo

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que aml, kyt y screening basado en riesgo se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar aml, kyt y screening basado en riesgo, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con aml, kyt y screening basado en riesgo.

#### CSPTF-CTRL-REG-005 - Travel Rule y transferencia segura

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que travel rule y transferencia segura se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar travel rule y transferencia segura, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con travel rule y transferencia segura.

#### CSPTF-CTRL-REG-006 - Retención, borrado y derechos

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que retención, borrado y derechos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar retención, borrado y derechos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con retención, borrado y derechos.

#### CSPTF-CTRL-REG-007 - Trazabilidad y evidencia regulatoria

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que trazabilidad y evidencia regulatoria se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar trazabilidad y evidencia regulatoria, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con trazabilidad y evidencia regulatoria.

#### CSPTF-CTRL-REG-008 - Privacidad por diseño en datos on-chain

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que privacidad por diseño en datos on-chain se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar privacidad por diseño en datos on-chain, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con privacidad por diseño en datos on-chain.

### Pruebas

#### CSPTF-TEST-REG-001 - Identificar obligaciones y alcance regulatorio

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si identificar obligaciones y alcance regulatorio reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con identificar obligaciones y alcance regulatorio, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden identificar obligaciones y alcance regulatorio.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-002 - Revisar inventario y clasificación de datos

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar inventario y clasificación de datos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar inventario y clasificación de datos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar inventario y clasificación de datos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-003 - Validar minimización y propósito

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar minimización y propósito reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar minimización y propósito, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar minimización y propósito.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-004 - Evaluar protección de datos KYC

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar protección de datos kyc reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar protección de datos kyc, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar protección de datos kyc.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-005 - Comprobar controles AML y KYT

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar controles aml y kyt reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar controles aml y kyt, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar controles aml y kyt.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-006 - Revisar screening y manejo de falsos positivos

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar screening y manejo de falsos positivos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar screening y manejo de falsos positivos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar screening y manejo de falsos positivos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-007 - Validar Travel Rule y transferencias

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar travel rule y transferencias reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar travel rule y transferencias, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar travel rule y transferencias.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-008 - Comprobar retención y eliminación

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar retención y eliminación reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar retención y eliminación, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar retención y eliminación.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-009 - Evaluar privacidad y linkability on-chain

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar privacidad y linkability on-chain reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar privacidad y linkability on-chain, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar privacidad y linkability on-chain.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-010 - Revisar accesos y trazabilidad regulatoria

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar accesos y trazabilidad regulatoria reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar accesos y trazabilidad regulatoria, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar accesos y trazabilidad regulatoria.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-011 - Validar respuesta a solicitudes de titulares

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar respuesta a solicitudes de titulares reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar respuesta a solicitudes de titulares, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar respuesta a solicitudes de titulares.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-REG-012 - Ejecutar tabletop de incidente de datos

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar tabletop de incidente de datos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar tabletop de incidente de datos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar tabletop de incidente de datos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-REG-001` Exposición de datos KYC: Actor externo, interno o automatizado intenta provocar exposición de datos kyc para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-REG-002` Evasión de monitoreo transaccional: Actor externo, interno o automatizado intenta provocar evasión de monitoreo transaccional para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-REG-003` Transferencia regulada sin datos requeridos: Actor externo, interno o automatizado intenta provocar transferencia regulada sin datos requeridos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-REG-004` Reidentificación o linkability indebida: Actor externo, interno o automatizado intenta provocar reidentificación o linkability indebida para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-REG-005` Retención o uso incompatible de datos: Actor externo, interno o automatizado intenta provocar retención o uso incompatible de datos para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-REG-001` Datos KYC sobreexpuestos: Condición de diseño, implementación u operación caracterizada por datos kyc sobreexpuestos, capaz de facilitar amenazas del dominio REG.
- `CSPTF-WEAK-REG-002` Reglas AML estáticas: Condición de diseño, implementación u operación caracterizada por reglas aml estáticas, capaz de facilitar amenazas del dominio REG.
- `CSPTF-WEAK-REG-003` Minimización insuficiente: Condición de diseño, implementación u operación caracterizada por minimización insuficiente, capaz de facilitar amenazas del dominio REG.
- `CSPTF-WEAK-REG-004` Cifrado o tokenización inadecuados: Condición de diseño, implementación u operación caracterizada por cifrado o tokenización inadecuados, capaz de facilitar amenazas del dominio REG.
- `CSPTF-WEAK-REG-005` Obligaciones no mapeadas por jurisdicción: Condición de diseño, implementación u operación caracterizada por obligaciones no mapeadas por jurisdicción, capaz de facilitar amenazas del dominio REG.

## 12.19 CSPTF-DOM-19 - MON: Monitoreo, detección, analítica on-chain y fraude

**English:** Monitoring, Detection, On-chain Analytics and Fraud

**Propósito:** Evaluar cobertura, calidad, correlación y respuesta de telemetría off-chain/on-chain frente a fraude, compromiso y anomalías económicas.

**Activos principales:** SIEM, on-chain analytics, fraud rules, wallet monitoring, node logs, contract events, alerting, case management.

### Controles

#### CSPTF-CTRL-MON-001 - Estrategia y cobertura de telemetría

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que estrategia y cobertura de telemetría se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar estrategia y cobertura de telemetría, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con estrategia y cobertura de telemetría.

#### CSPTF-CTRL-MON-002 - Calidad, tiempo y sincronización de logs

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que calidad, tiempo y sincronización de logs se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar calidad, tiempo y sincronización de logs, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con calidad, tiempo y sincronización de logs.

#### CSPTF-CTRL-MON-003 - Detecciones on-chain y off-chain

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que detecciones on-chain y off-chain se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar detecciones on-chain y off-chain, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con detecciones on-chain y off-chain.

#### CSPTF-CTRL-MON-004 - Monitoreo de wallets y contratos críticos

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que monitoreo de wallets y contratos críticos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar monitoreo de wallets y contratos críticos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con monitoreo de wallets y contratos críticos.

#### CSPTF-CTRL-MON-005 - Detección de fraude y abuso

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que detección de fraude y abuso se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar detección de fraude y abuso, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con detección de fraude y abuso.

#### CSPTF-CTRL-MON-006 - Correlación, enriquecimiento y atribución

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que correlación, enriquecimiento y atribución se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar correlación, enriquecimiento y atribución, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con correlación, enriquecimiento y atribución.

#### CSPTF-CTRL-MON-007 - Gestión de alertas y casos

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que gestión de alertas y casos se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar gestión de alertas y casos, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con gestión de alertas y casos.

#### CSPTF-CTRL-MON-008 - Validación continua de detecciones

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que validación continua de detecciones se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar validación continua de detecciones, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con validación continua de detecciones.

### Pruebas

#### CSPTF-TEST-MON-001 - Mapear telemetría a activos y amenazas

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si mapear telemetría a activos y amenazas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con mapear telemetría a activos y amenazas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden mapear telemetría a activos y amenazas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-002 - Validar fuentes, integridad y retención de logs

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar fuentes, integridad y retención de logs reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar fuentes, integridad y retención de logs, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar fuentes, integridad y retención de logs.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-003 - Comprobar sincronización temporal

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar sincronización temporal reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar sincronización temporal, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar sincronización temporal.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-004 - Evaluar eventos de contratos y nodos

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar eventos de contratos y nodos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar eventos de contratos y nodos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar eventos de contratos y nodos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-005 - Revisar monitoreo de wallets críticas

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar monitoreo de wallets críticas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar monitoreo de wallets críticas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar monitoreo de wallets críticas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-006 - Probar detecciones de cambios administrativos

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si probar detecciones de cambios administrativos reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con probar detecciones de cambios administrativos, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden probar detecciones de cambios administrativos.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-007 - Evaluar reglas de fraude y anomalías

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar reglas de fraude y anomalías reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar reglas de fraude y anomalías, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar reglas de fraude y anomalías.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-008 - Comprobar correlación on-chain/off-chain

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar correlación on-chain/off-chain reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar correlación on-chain/off-chain, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar correlación on-chain/off-chain.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-009 - Validar enriquecimiento y contexto

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar enriquecimiento y contexto reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar enriquecimiento y contexto, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar enriquecimiento y contexto.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-010 - Revisar SLAs y escalamiento

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar slas y escalamiento reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar slas y escalamiento, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar slas y escalamiento.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-011 - Ejecutar emulación segura de señales

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar emulación segura de señales reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar emulación segura de señales, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar emulación segura de señales.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-MON-012 - Medir cobertura, precisión y mejora continua

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si medir cobertura, precisión y mejora continua reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con medir cobertura, precisión y mejora continua, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden medir cobertura, precisión y mejora continua.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-MON-001` Actividad maliciosa no detectada: Actor externo, interno o automatizado intenta provocar actividad maliciosa no detectada para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-MON-002` Supresión o manipulación de telemetría: Actor externo, interno o automatizado intenta provocar supresión o manipulación de telemetría para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-MON-003` Falsos positivos que ocultan señales reales: Actor externo, interno o automatizado intenta provocar falsos positivos que ocultan señales reales para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-MON-004` Fraude coordinado multicanal: Actor externo, interno o automatizado intenta provocar fraude coordinado multicanal para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-MON-005` Respuesta tardía a drenaje o compromiso: Actor externo, interno o automatizado intenta provocar respuesta tardía a drenaje o compromiso para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-MON-001` Logs críticos ausentes: Condición de diseño, implementación u operación caracterizada por logs críticos ausentes, capaz de facilitar amenazas del dominio MON.
- `CSPTF-WEAK-MON-002` Eventos sin contexto de negocio: Condición de diseño, implementación u operación caracterizada por eventos sin contexto de negocio, capaz de facilitar amenazas del dominio MON.
- `CSPTF-WEAK-MON-003` Alertas sin owner: Condición de diseño, implementación u operación caracterizada por alertas sin owner, capaz de facilitar amenazas del dominio MON.
- `CSPTF-WEAK-MON-004` Cobertura no medida: Condición de diseño, implementación u operación caracterizada por cobertura no medida, capaz de facilitar amenazas del dominio MON.
- `CSPTF-WEAK-MON-005` Retención insuficiente para investigación: Condición de diseño, implementación u operación caracterizada por retención insuficiente para investigación, capaz de facilitar amenazas del dominio MON.

## 12.20 CSPTF-DOM-20 - IRR: Respuesta a incidentes, recuperación, reservas y resiliencia

**English:** Incident Response, Recovery, Reserves and Resilience

**Propósito:** Evaluar preparación, contención, recuperación, reconciliación, comunicación, evidencia, reservas y continuidad ante incidentes de activos digitales.

**Activos principales:** incident plans, war room, pause mechanisms, recovery keys, reserve ledgers, communications, forensic data, business continuity.

### Controles

#### CSPTF-CTRL-IRR-001 - Planes específicos por escenario

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que planes específicos por escenario se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar planes específicos por escenario, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con planes específicos por escenario.

#### CSPTF-CTRL-IRR-002 - Autoridad, coordinación y comunicaciones

- **Perfil mínimo:** AP1
- **Objetivo:** Asegurar que autoridad, coordinación y comunicaciones se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar autoridad, coordinación y comunicaciones, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con autoridad, coordinación y comunicaciones.

#### CSPTF-CTRL-IRR-003 - Contención on-chain y off-chain

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que contención on-chain y off-chain se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar contención on-chain y off-chain, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con contención on-chain y off-chain.

#### CSPTF-CTRL-IRR-004 - Preservación de evidencia y forense

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que preservación de evidencia y forense se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar preservación de evidencia y forense, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con preservación de evidencia y forense.

#### CSPTF-CTRL-IRR-005 - Recuperación de claves y servicios

- **Perfil mínimo:** AP2
- **Objetivo:** Asegurar que recuperación de claves y servicios se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar recuperación de claves y servicios, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con recuperación de claves y servicios.

#### CSPTF-CTRL-IRR-006 - Reconciliación de activos y reservas

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que reconciliación de activos y reservas se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar reconciliación de activos y reservas, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con reconciliación de activos y reservas.

#### CSPTF-CTRL-IRR-007 - Continuidad, liquidez y obligaciones

- **Perfil mínimo:** AP3
- **Objetivo:** Asegurar que continuidad, liquidez y obligaciones se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar continuidad, liquidez y obligaciones, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con continuidad, liquidez y obligaciones.

#### CSPTF-CTRL-IRR-008 - Lecciones aprendidas y validación periódica

- **Perfil mínimo:** AP4
- **Objetivo:** Asegurar que lecciones aprendidas y validación periódica se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.
- **Requisito:** La organización DEBE definir, aprobar, implementar, monitorear y revisar lecciones aprendidas y validación periódica, manteniendo evidencia trazable y excepciones formalmente aceptadas.
- **Evidencia:** Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con lecciones aprendidas y validación periódica.

### Pruebas

#### CSPTF-TEST-IRR-001 - Revisar playbooks por escenario

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar playbooks por escenario reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar playbooks por escenario, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar playbooks por escenario.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-002 - Validar contactos, roles y autoridad

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar contactos, roles y autoridad reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar contactos, roles y autoridad, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar contactos, roles y autoridad.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-003 - Comprobar mecanismos de pausa y contención

- **Perfil mínimo:** AP1
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar mecanismos de pausa y contención reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar mecanismos de pausa y contención, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar mecanismos de pausa y contención.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-004 - Evaluar preservación de evidencia

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar preservación de evidencia reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar preservación de evidencia, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar preservación de evidencia.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-005 - Simular compromiso de clave

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si simular compromiso de clave reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con simular compromiso de clave, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden simular compromiso de clave.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-006 - Simular exploit de contrato o bridge

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si simular exploit de contrato o bridge reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con simular exploit de contrato o bridge, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden simular exploit de contrato o bridge.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-007 - Validar restauración de servicios

- **Perfil mínimo:** AP2
- **Tipo:** Revisión y validación controlada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar restauración de servicios reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar restauración de servicios, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar restauración de servicios.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-008 - Comprobar reconciliación de balances

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si comprobar reconciliación de balances reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con comprobar reconciliación de balances, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden comprobar reconciliación de balances.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-009 - Evaluar reservas y liquidez de crisis

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si evaluar reservas y liquidez de crisis reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con evaluar reservas y liquidez de crisis, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden evaluar reservas y liquidez de crisis.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-010 - Revisar comunicación a clientes y reguladores

- **Perfil mínimo:** AP3
- **Tipo:** Simulación técnica autorizada
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si revisar comunicación a clientes y reguladores reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con revisar comunicación a clientes y reguladores, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden revisar comunicación a clientes y reguladores.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-011 - Ejecutar ejercicio integral de crisis

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si ejecutar ejercicio integral de crisis reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con ejecutar ejercicio integral de crisis, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden ejecutar ejercicio integral de crisis.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

#### CSPTF-TEST-IRR-012 - Validar remediación y lecciones aprendidas

- **Perfil mínimo:** AP4
- **Tipo:** Ejercicio avanzado en laboratorio/fork
- **Objetivo:** Determinar, mediante evidencia verificable y validación no destructiva, si validar remediación y lecciones aprendidas reduce el riesgo esperado.
- **Procedimiento resumido:** Revisar diseño y configuración relacionados con validar remediación y lecciones aprendidas, contrastarlos con invariantes y requisitos, y validar su eficacia mediante consultas de solo lectura, datos sintéticos, simulación o reproducción segura.
- **Evidencia:** Capturas o exportaciones fechadas; configuración; hashes/IDs de artefactos; consultas; resultados de prueba; logs; decisión de pass/fail; limitaciones y responsables.
- **Pass:** Existe diseño aprobado, la implementación coincide con el diseño, la evidencia demuestra eficacia y no se identifican rutas razonables que invaliden validar remediación y lecciones aprendidas.
- **Fail:** Falta de control, evidencia insuficiente, configuración inconsistente, bypass reproducible en entorno autorizado o dependencia no tratada.

### Amenazas y debilidades

**Amenazas:**

- `CSPTF-THRT-IRR-001` Contención tardía de drenaje: Actor externo, interno o automatizado intenta provocar contención tardía de drenaje para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-IRR-002` Pérdida de evidencia forense: Actor externo, interno o automatizado intenta provocar pérdida de evidencia forense para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-IRR-003` Recuperación con claves comprometidas: Actor externo, interno o automatizado intenta provocar recuperación con claves comprometidas para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-IRR-004` Descuadre de reservas tras incidente: Actor externo, interno o automatizado intenta provocar descuadre de reservas tras incidente para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.
- `CSPTF-THRT-IRR-005` Comunicación errónea que amplifica impacto: Actor externo, interno o automatizado intenta provocar comunicación errónea que amplifica impacto para obtener acceso, control, beneficio económico, fraude, interrupción o ventaja estratégica.

**Debilidades:**

- `CSPTF-WEAK-IRR-001` Playbooks genéricos: Condición de diseño, implementación u operación caracterizada por playbooks genéricos, capaz de facilitar amenazas del dominio IRR.
- `CSPTF-WEAK-IRR-002` Pausas no ensayadas: Condición de diseño, implementación u operación caracterizada por pausas no ensayadas, capaz de facilitar amenazas del dominio IRR.
- `CSPTF-WEAK-IRR-003` Dependencia de personas únicas: Condición de diseño, implementación u operación caracterizada por dependencia de personas únicas, capaz de facilitar amenazas del dominio IRR.
- `CSPTF-WEAK-IRR-004` Reconciliación manual lenta: Condición de diseño, implementación u operación caracterizada por reconciliación manual lenta, capaz de facilitar amenazas del dominio IRR.
- `CSPTF-WEAK-IRR-005` Backups y claves de recuperación no validados: Condición de diseño, implementación u operación caracterizada por backups y claves de recuperación no validados, capaz de facilitar amenazas del dominio IRR.

# 13. Mapeos y fuentes

Los mapeos de v0.1 son temáticos y no prueban conformidad con las fuentes relacionadas. Véase `mappings/domain-crosswalk.csv`.

## Registro de fuentes

- `REF-001` MITRE (2025), *MITRE AADAPT: Adversarial Actions in Digital Asset Payment Technologies*, MITRE. https://aadapt.mitre.org/
- `REF-002` MITRE (2025), *MITRE Introduces AADAPT Cybersecurity Framework for Cryptocurrency*, MITRE. https://www.mitre.org/news-insights/news-release/mitre-introduces-aadapt-cybersecurity-framework-cryptocurrency
- `REF-003` OWASP Foundation (2026), *OWASP Smart Contract Security Testing Guide (SCSTG)*, OWASP SCS. https://scs.owasp.org/SCSTG/
- `REF-004` OWASP Foundation (2026), *OWASP Smart Contract Security Verification Standard (SCSVS)*, OWASP SCS. https://scs.owasp.org/SCSVS/
- `REF-005` OWASP Foundation (2026), *OWASP Smart Contract Weakness Enumeration (SCWE)*, OWASP SCS. https://scs.owasp.org/SCWE/
- `REF-006` Enterprise Ethereum Alliance (2025), *EEA EthTrust Security Levels Specification Version 3*, EEA. https://entethalliance.org/specs/ethtrust-sl/v3/
- `REF-007` Scarfone, Souppaya, Cody, Orebaugh (2008), *NIST SP 800-115: Technical Guide to Information Security Testing and Assessment*, NIST. https://doi.org/10.6028/NIST.SP.800-115
- `REF-008` NIST (2024), *Cybersecurity Framework 2.0*, NIST. https://doi.org/10.6028/NIST.CSWP.29
- `REF-009` Yaga, Mell, Roby, Scarfone (2018), *NISTIR 8202: Blockchain Technology Overview*, NIST. https://doi.org/10.6028/NIST.IR.8202
- `REF-010` NIST (2023), *FIPS 186-5: Digital Signature Standard*, NIST. https://doi.org/10.6028/NIST.FIPS.186-5
- `REF-011` NIST (2022), *SP 800-218: Secure Software Development Framework (SSDF)*, NIST. https://doi.org/10.6028/NIST.SP.800-218
- `REF-012` MITRE (2026), *MITRE ATT&CK*, MITRE. https://attack.mitre.org/
- `REF-013` MITRE (2026), *MITRE D3FEND*, MITRE. https://d3fend.mitre.org/
- `REF-014` OWASP Foundation (2026), *OWASP Web Security Testing Guide*, OWASP. https://owasp.org/www-project-web-security-testing-guide/
- `REF-015` Atzei, Bartoletti, Cimoli (2017), *A Survey of Attacks on Ethereum Smart Contracts (SoK)*, POST 2017. https://doi.org/10.1007/978-3-662-54455-6_8
- `REF-016` Luu, Chu, Olickel, Saxena, Hobor (2016), *Making Smart Contracts Smarter*, ACM CCS 2016. https://doi.org/10.1145/2976749.2978309
- `REF-017` Tsankov et al. (2018), *Securify: Practical Security Analysis of Smart Contracts*, ACM CCS 2018. https://doi.org/10.1145/3243734.3243780
- `REF-018` Nikolic et al. (2018), *Finding The Greedy, Prodigal, and Suicidal Contracts at Scale*, ACSAC 2018. https://doi.org/10.1145/3274694.3274743
- `REF-019` Durieux, Ferreira, Abreu, Cruz (2020), *Empirical Review of Automated Analysis Tools on 47,587 Ethereum Smart Contracts*, ICSE 2020. https://doi.org/10.1145/3377811.3380364
- `REF-020` Daian et al. (2020), *Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability*, IEEE S&P 2020. https://doi.org/10.1109/SP40000.2020.00040
- `REF-021` Qin et al. (2021), *Attacking the DeFi Ecosystem with Flash Loans for Fun and Profit*, Financial Cryptography 2021. https://doi.org/10.1007/978-3-662-64331-0_1
- `REF-022` Su et al. (2021), *Evil Under the Sun: Understanding and Discovering Attacks on Ethereum Decentralized Applications*, USENIX Security 2021. https://www.usenix.org/conference/usenixsecurity21/presentation/su
- `REF-023` So, Hong, Oh (2021), *SmarTest: Effectively Hunting Vulnerable Transaction Sequences in Smart Contracts*, USENIX Security 2021. https://www.usenix.org/conference/usenixsecurity21/presentation/so
- `REF-024` He et al. (2021), *EOSAFE: Security Analysis of EOSIO Smart Contracts*, USENIX Security 2021. https://www.usenix.org/conference/usenixsecurity21/presentation/he-ningyu
- `REF-025` Liao et al. (2024), *SmartAxe: Detecting Cross-Chain Vulnerabilities in Bridge Smart Contracts via Fine-Grained Static Analysis*, arXiv. https://arxiv.org/abs/2406.15999
- `REF-026` Augusto et al. (2024), *XChainWatcher: Monitoring and Identifying Attacks in Cross-Chain Bridges*, arXiv. https://arxiv.org/abs/2410.02029
- `REF-027` Wu et al. (2024), *Safeguarding Blockchain Ecosystem: Understanding and Detecting Attack Transactions on Cross-chain Bridges*, arXiv. https://arxiv.org/abs/2410.14493
- `REF-028` OASIS (2024), *STIX Version 2.1*, OASIS Open. https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html
- `REF-029` FIRST (2023), *Common Vulnerability Scoring System Version 4.0*, FIRST. https://www.first.org/cvss/v4.0/
- `REF-030` OpenSSF (2026), *Supply-chain Levels for Software Artifacts (SLSA)*, OpenSSF. https://slsa.dev/
- `REF-031` OWASP Foundation (2026), *CycloneDX Specification*, OWASP. https://cyclonedx.org/specification/overview/
- `REF-032` FATF (2021), *Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs*, FATF. https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html
- `REF-033` European Union (2023), *Regulation (EU) 2023/1114 on Markets in Crypto-assets (MiCA)*, EUR-Lex. https://eur-lex.europa.eu/eli/reg/2023/1114/oj
- `REF-034` European Union (2022), *Regulation (EU) 2022/2554 on digital operational resilience for the financial sector (DORA)*, EUR-Lex. https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- `REF-035` Bitcoin Improvement Proposals (2026), *BIP-32: Hierarchical Deterministic Wallets*, Bitcoin BIPs. https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki
- `REF-036` Bitcoin Improvement Proposals (2026), *BIP-39: Mnemonic code for generating deterministic keys*, Bitcoin BIPs. https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
- `REF-037` Ethereum Improvement Proposals (2026), *EIP-712: Typed structured data hashing and signing*, Ethereum EIPs. https://eips.ethereum.org/EIPS/eip-712
- `REF-038` Ethereum Improvement Proposals (2026), *ERC-1967: Proxy Storage Slots*, Ethereum EIPs. https://eips.ethereum.org/EIPS/eip-1967
- `REF-039` Satoshi Nakamoto (2008), *Bitcoin: A Peer-to-Peer Electronic Cash System*, Bitcoin.org. https://bitcoin.org/bitcoin.pdf
- `REF-040` Gavin Wood et al. (2026), *Ethereum Yellow Paper*, Ethereum. https://ethereum.github.io/yellowpaper/paper.pdf

# 14. Validación requerida

El detalle documental no constituye validación por sí solo. CSPTF requiere varias líneas de evidencia antes de declarar una versión estable.

## Etapa 1 - Validez de contenido

Convocar especialistas en contratos inteligentes, custodia, DeFi, bridges, exchanges centralizados, infraestructura, criptografía, cumplimiento y respuesta a incidentes. Medir acuerdo sobre relevancia, claridad y completitud.

## Etapa 2 - Validez de los mapeos

Revisar de forma independiente los mapeos con AADAPT, ATT&CK, OWASP, EEA y NIST. Registrar desacuerdos y nivel de confianza de cada relación.

## Etapa 3 - Cobertura mediante estudios de caso

Aplicar CSPTF retrospectivamente a incidentes públicos y prospectivamente a ambientes de prueba autorizados. Medir si identifica la ruta causal, los controles afectados, la evidencia y las brechas de recuperación.

## Etapa 4 - Confiabilidad entre evaluadores

Dos o más equipos deben delimitar y valorar de manera independiente el mismo sistema. Se medirá el acuerdo sobre aplicabilidad, resultados de pruebas, nivel de evidencia, confianza y banda de riesgo.

## Etapa 5 - Calibración del scoring

Comparar las dimensiones preliminares con pérdidas históricas, indisponibilidad, usuarios afectados, contagio y recuperación. Ajustar pesos y umbrales sin ocultar la incertidumbre.

## Etapa 6 - Usabilidad y eficiencia

Medir tiempo, carga de evidencia, rutas de alto riesgo omitidas, duplicación y retroalimentación de evaluadores por perfil de aseguramiento.

## Criterios de aceptación antes de v1.0

- resolución pública de comentarios;
- revisión experta independiente en todos los dominios críticos;
- estudios de caso documentados;
- confiabilidad entre evaluadores aceptable;
- modelo de riesgo calibrado o eliminación de precisión numérica no sustentada;
- identificadores estables y política de migración;
- revisión legal, ética y de seguridad operacional.
