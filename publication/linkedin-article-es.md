# CSPTF: una propuesta abierta para estandarizar el pentesting de criptomonedas, blockchain y Web3

Las evaluaciones de seguridad en ecosistemas de activos digitales suelen fragmentarse. Un equipo revisa contratos inteligentes; otro valida cloud y APIs; otro analiza custodia; y un tercero observa fraude, liquidez o cumplimiento. El resultado puede ser técnicamente competente y, aun así, dejar sin analizar la relación entre una clave, un contrato, un bridge, un oráculo, un proceso de retiro y la capacidad real de responder a una crisis.

Por esa razón desarrollé **CSPTF - Crypto Security Penetration Testing Framework**, un borrador abierto que propone evaluar el sistema digital completo, no solamente su código on-chain.

## El punto de partida

La industria ya cuenta con referentes importantes:

- MITRE AADAPT estructura tácticas y técnicas adversarias para tecnologías de pagos y activos digitales.
- OWASP SCSVS, SCSTG y SCWE profundizan en requisitos, pruebas y debilidades de contratos inteligentes.
- EEA EthTrust define niveles y requisitos para revisiones de contratos Solidity.
- NIST SP 800-115 aporta disciplina para planear, ejecutar, analizar y cerrar evaluaciones técnicas.

CSPTF no pretende reemplazarlos. Su objetivo es conectarlos dentro de un ciclo de evaluación que abarque arquitectura, criptografía, custodia, contratos, dApps, tokens, DeFi, oráculos, bridges, consenso, Layer 2, exchanges centralizados, APIs, cloud, identidad, supply chain, privacidad, fraude, monitoreo y respuesta a incidentes.

## Qué contiene el borrador v0.1

La versión inicial incluye:

- 20 dominios de seguridad;
- 160 controles normativos;
- 240 casos de prueba autorizados;
- 100 escenarios de amenaza;
- 100 patrones de debilidad;
- cuatro perfiles de aseguramiento;
- seis niveles de evidencia;
- un modelo de riesgo que incorpora impacto financiero, gobernanza, contagio sistémico e irreversibilidad;
- plantillas, esquemas JSON, validadores y mapeos;
- un paper y una especificación técnica.

## La diferencia más importante: autorización y seguridad operacional

En blockchain, una prueba mal ejecutada puede ser irreversible. Por ello CSPTF parte de una regla sencilla: **una técnica nunca sustituye la autorización**.

El framework prioriza revisión estática, ambientes locales, simulación, forks determinísticos, testnets y staging. Las pruebas activas en producción se consideran excepcionales y exigen autorización individual, presupuesto de transacciones y pérdida, monitoreo, reconciliación, rollback o recuperación compensatoria y autoridad clara de detención.

El uso de fondos reales de clientes, la manipulación de mercado, la disrupción del consenso y las pruebas destructivas se prohíben por defecto.

## Evaluar propiedades, no solo vulnerabilidades

CSPTF propone comenzar por invariantes:

- ¿El supply siempre corresponde a las reglas autorizadas?
- ¿Un mensaje cross-chain puede procesarse una sola vez?
- ¿Los activos custodiados permanecen respaldados y reconciliados?
- ¿Una actualización conserva almacenamiento, permisos y lógica esperada?
- ¿Un fallo de oráculo lleva al sistema a un modo seguro?
- ¿Una clave comprometida puede revocarse antes de producir una pérdida irreversible?
- ¿La organización detecta y contiene la anomalía?

Después se seleccionan controles, pruebas y evidencia para demostrar o refutar esas propiedades.

## Un scoring distinto

Una vulnerabilidad en activos digitales no puede medirse únicamente por confidencialidad, integridad y disponibilidad. El borrador añade dimensiones como:

- pérdida financiera;
- captura de gobernanza;
- impacto sistémico;
- incentivos económicos;
- composabilidad;
- irreversibilidad.

El modelo numérico se publica como hipótesis de trabajo. Antes de considerarlo estable debe calibrarse con incidentes, estudios de caso y concordancia entre evaluadores.

## Qué falta para convertirlo en un estándar estable

CSPTF v0.1 es una base completa, pero todavía no una certificación. El siguiente paso es someterlo a revisión de expertos, validar mapeos, aplicar estudios de caso, medir confiabilidad entre evaluadores y calibrar los pesos de riesgo.

La meta no es crear otra lista de vulnerabilidades. La meta es construir un lenguaje común para planear, ejecutar, documentar, comparar y mejorar evaluaciones de seguridad sobre ecosistemas cripto completos.

El proyecto se publica bajo Apache 2.0 para permitir revisión, reutilización y contribuciones.

**Autor:** Edwin Javier Peñuela Camacho  
**Repositorio:** GitHub `@sr-maximus/CSPTF`  
**Versión:** 0.1.0-draft
