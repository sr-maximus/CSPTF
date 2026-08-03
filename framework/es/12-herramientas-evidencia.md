# 12 - Herramientas y evidencia

Las herramientas ayudan a ejecutar actividades de CSPTF, pero no otorgan
autorizacion y no reemplazan el criterio experto. Un resultado de herramienta se
acepta solo cuando esta asociado a una prueba aprobada, un activo especifico, un
entorno, una fecha, una version, un operador, una declaracion de limitaciones y
una decision de revision.

## Regla de evidencia

La misma herramienta puede producir distintos niveles de evidencia segun su uso:

| Uso de herramientas | Evidencia maxima antes de revision | Que falta validar |
|---|---:|---|
| Cuestionario, inventario de politicas o exportacion de arquitectura | E1 | confirmacion del responsable y mapeo al alcance |
| Analizador estatico, dependencias, SBOM, IaC o configuracion exportada | E2 | alcanzabilidad, explotabilidad o eficacia del control |
| Logs, consultas on-chain, telemetria, CI o configuracion observada | E3 | frescura, procedencia y correlacion |
| Fuzzing autorizado, pruebas de propiedades, simulacion en fork, replay harness o laboratorio | E4 | precondiciones acotadas, limpieza y reproducibilidad |
| Repeticion independiente por otro equipo calificado o atestacion externa | E5 | resolucion de conflictos y aprobacion final |

La salida de un scanner no debe cerrar por si sola un finding ni demostrar que
un control funciona. Puede abrir una investigacion, apoyar un finding o apoyar
una decision de pass solo si la propiedad esperada y las limitaciones quedan
documentadas.

## Matriz actividad-herramienta

| Actividad CSPTF | Dominios principales | Valida | Clases de herramientas y ejemplos | Evidencia tipica | Notas de seguridad |
|---|---|---|---|---|---|
| Modelado de sistema y amenazas | GOV, ARC, DEF, BRG, IRR | activos, fronteras de confianza, flujos de valor, abuso e invariantes | diagramas, threat modeling, ADR, arboles de ataque | diagramas, supuestos, notas de revision, invariantes aceptados | no inferir alcance productivo solo desde diagramas |
| Revision de contratos inteligentes | SCT, DAP, TOK, BRG, ORA | propiedades de codigo, autorizacion, upgrades, aritmetica, llamadas externas y estandares | Slither, Semgrep, CodeQL, Mythril, warnings de compilador, revision manual | version fuente, compilador, salida de detectores, triage | los hallazgos estaticos son E2 hasta validarse |
| Pruebas de propiedades y fuzzing | SCT, DAP, TOK, DEF, BRG | invariantes, transiciones de estado, conservacion de valor, acceso y fallas | Foundry, Echidna, Medusa, Halmos, Hardhat tests | suite, seed, traza, cobertura, entrada fallida, replay | usar activos sinteticos y estado aislado |
| Fork, simulacion y trazas de transacciones | DEF, BRG, ORA, L2, CEX, IRR | rutas economicas, liquidacion, oraculos, replay, finalidad y dependencias | Foundry Anvil, Hardhat Network, Tenderly, forks locales, consultas de indexador | bloque del fork, chain ID, traza, diff de estado, reconciliacion | no mover fondos reales sin autorizacion escrita excepcional |
| Pruebas API y aplicacion | API, CEX, DAP, IAM, INF | autenticacion, autorizacion, entradas, sesiones y logica de negocio | OWASP ZAP, Burp Suite, clientes API, contract tests, validadores de schema | request/response, limites, prueba de autorizacion, version afectada | respetar presupuestos de tasa y ventanas aprobadas |
| Cadena de suministro y dependencias | SUP, INF, SCT, API | dependencias vulnerables, SBOM, procedencia de build e integridad | OSV-Scanner, Syft, CycloneDX, Trivy, lockfiles | SBOM, reporte de dependencias, advisory, hash de build | presencia de CVE no equivale a explotabilidad |
| Cloud, infraestructura e IaC | INF, IAM, NET, MON, IRR | exposicion, minimo privilegio, rutas de red, secretos, backup y recuperacion | Checkov, Trivy IaC, Prowler, cloud CLIs, Kubernetes y containers | configuracion exportada, politicas, inventario, evidencia de fix | preferir recoleccion read-only salvo change control aprobado |
| Identidad, custodia y llaves | KEY, IAM, CEX, GOV | autoridad de firmantes, ceremonias, HSM/KMS, politicas de wallet y emergencia | logs HSM/KMS, analizadores IAM, exportes de politica, access reviews | roles, set de firmantes, ceremonia, workflow de aprobacion | nunca solicitar ni exponer private keys, seeds o mnemonics |
| Monitoreo y deteccion | MON, IRR, NET, CEX, BRG | cobertura de alertas, calidad de telemetria, triage, contencion y recuperacion | SIEM, Sigma, Prometheus, Grafana, monitores on-chain, tabletop | alerta, query, dashboard, timeline, ticket | usar senales seguras y etiquetas acordadas |
| Reporte, remediacion y retest | todos | causa raiz, eficacia del fix, riesgo residual y cierre | issue trackers, scripts de retest, CI, repositorio de evidencia, templates | finding, plan, salida de retest, aceptacion de riesgo residual | retestar la misma ruta y modos de falla adyacentes |

## Herramientas minimas por perfil

| Perfil | Expectativa minima |
|---|---|
| AP1 Baseline | revision estructurada, checklist de catalogo, evidencia de configuracion/fuente y al menos una validacion reproducible para controles seleccionados |
| AP2 Enhanced | AP1 mas evidencia runtime observada, revision de dependencias/SBOM, prueba API o integracion cuando aplique y triage independiente del implementador |
| AP3 Critical | AP2 mas validacion adversarial en lab/fork/testnet, fuzzing o propiedades para invariantes criticos, validacion de deteccion y revision especialista independiente |
| AP4 Systemic | AP3 mas repeticion multi-equipo, simulacion economica/sistemica, ejercicio de crisis, analisis de contagio e impugnacion independiente de evidencia |

## Criterios de seleccion

Una herramienta es aceptable para CSPTF cuando el registro de evaluacion indica:

- version, configuracion y entorno de ejecucion;
- alcance exacto, objetivos y activos excluidos;
- referencia de autorizacion y criterios de detencion;
- datos de entrada e identidades sinteticas usadas;
- ubicacion de salida y hash de integridad cuando aplique;
- limitaciones conocidas de falsos positivos y falsos negativos;
- conclusion del revisor e IDs de control, prueba y finding relacionados.

Herramientas comerciales, open-source e internas pueden ser validas. CSPTF
registra su idoneidad para una actividad concreta; no endosa un proveedor ni
implica que una herramienta establezca certificacion.
