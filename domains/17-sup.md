# CSPTF-DOM-17 - SUP: Cadena de suministro, dependencias e integridad de construcción

**English:** Supply Chain, Dependencies and Build Integrity

## Purpose

Evaluar componentes, repositorios, compiladores, paquetes, artefactos, proveedores y procedencia del software y firmware.

## Principal assets

- source repositories
- dependencies
- package registries
- compilers
- build runners
- artifacts
- firmware
- vendors

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-SUP-001 | Inventario SBOM y dependencias | AP1 |
| CSPTF-CTRL-SUP-002 | Gobierno de repositorios y ramas | AP1 |
| CSPTF-CTRL-SUP-003 | Verificación de paquetes y procedencia | AP2 |
| CSPTF-CTRL-SUP-004 | Entornos de construcción aislados | AP2 |
| CSPTF-CTRL-SUP-005 | Firmas, reproducibilidad y releases | AP2 |
| CSPTF-CTRL-SUP-006 | Gestión de vulnerabilidades de terceros | AP3 |
| CSPTF-CTRL-SUP-007 | Firmware y hardware de confianza | AP3 |
| CSPTF-CTRL-SUP-008 | Respuesta a compromiso de supply chain | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-SUP-001 | Generar y revisar SBOM | AP1 | Revisión y validación controlada |
| CSPTF-TEST-SUP-002 | Validar protección de ramas y revisiones | AP1 | Revisión y validación controlada |
| CSPTF-TEST-SUP-003 | Evaluar dependencias directas y transitivas | AP1 | Revisión y validación controlada |
| CSPTF-TEST-SUP-004 | Comprobar pinning, hashes y registries | AP2 | Revisión y validación controlada |
| CSPTF-TEST-SUP-005 | Revisar runners y entornos de build | AP2 | Revisión y validación controlada |
| CSPTF-TEST-SUP-006 | Validar firma y procedencia de artefactos | AP2 | Revisión y validación controlada |
| CSPTF-TEST-SUP-007 | Comprobar builds reproducibles donde aplique | AP2 | Revisión y validación controlada |
| CSPTF-TEST-SUP-008 | Evaluar compiladores y toolchains | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-SUP-009 | Revisar firmware y actualizaciones | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-SUP-010 | Validar riesgo y acceso de proveedores | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-SUP-011 | Simular revocación de componente comprometido | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-SUP-012 | Comprobar detección de cambios no autorizados | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-SUP-001 | Paquete o dependencia maliciosa |
| CSPTF-THRT-SUP-002 | Compromiso de repositorio o maintainer |
| CSPTF-THRT-SUP-003 | Manipulación del pipeline de build |
| CSPTF-THRT-SUP-004 | Firmware o dispositivo adulterado |
| CSPTF-THRT-SUP-005 | Actualización comprometida distribuida |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-SUP-001 | Dependencias sin pinning |
| CSPTF-WEAK-SUP-002 | Artefactos no firmados |
| CSPTF-WEAK-SUP-003 | Runners compartidos y privilegiados |
| CSPTF-WEAK-SUP-004 | SBOM ausente |
| CSPTF-WEAK-SUP-005 | Proveedores sin evaluación continua |

## Crosswalk

- MITRE AADAPT tactics: Resource Development, Initial Access, Execution, Defense Evasion, Impact
- NIST CSF 2.0 functions: GV, ID, PR
- OWASP alignment: OWASP Software Component Verification Standard themes

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
