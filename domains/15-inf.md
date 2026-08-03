# CSPTF-DOM-15 - INF: Cloud, contenedores, CI/CD e infraestructura

**English:** Cloud, Containers, CI/CD and Infrastructure

## Purpose

Evaluar la infraestructura que construye, despliega y opera servicios de activos digitales, incluyendo secretos, IaC, imágenes y pipelines.

## Principal assets

- cloud accounts
- Kubernetes
- containers
- CI/CD
- IaC
- artifact registries
- secrets managers
- observability stack

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-INF-001 | Arquitectura cloud y segmentación | AP1 |
| CSPTF-CTRL-INF-002 | IAM de infraestructura y privilegios | AP1 |
| CSPTF-CTRL-INF-003 | Gestión de secretos y KMS | AP2 |
| CSPTF-CTRL-INF-004 | Endurecimiento de contenedores y orquestación | AP2 |
| CSPTF-CTRL-INF-005 | Integridad de CI/CD y releases | AP2 |
| CSPTF-CTRL-INF-006 | IaC, configuración y drift | AP3 |
| CSPTF-CTRL-INF-007 | Red, exposición y protección perimetral | AP3 |
| CSPTF-CTRL-INF-008 | Respaldo, continuidad y recuperación | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-INF-001 | Revisar cuentas, proyectos y segmentación | AP1 | Revisión y validación controlada |
| CSPTF-TEST-INF-002 | Evaluar IAM y privilegios cloud | AP1 | Revisión y validación controlada |
| CSPTF-TEST-INF-003 | Comprobar secretos, KMS y rotación | AP1 | Revisión y validación controlada |
| CSPTF-TEST-INF-004 | Revisar imágenes y configuración de contenedores | AP2 | Revisión y validación controlada |
| CSPTF-TEST-INF-005 | Evaluar controles de Kubernetes | AP2 | Revisión y validación controlada |
| CSPTF-TEST-INF-006 | Comprobar integridad del pipeline y aprobaciones | AP2 | Revisión y validación controlada |
| CSPTF-TEST-INF-007 | Validar firma y procedencia de artefactos | AP2 | Revisión y validación controlada |
| CSPTF-TEST-INF-008 | Revisar IaC y drift de configuración | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-INF-009 | Evaluar exposición de red y servicios | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-INF-010 | Comprobar logs, métricas y alertas | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-INF-011 | Validar backups y restauración | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-INF-012 | Simular pérdida controlada de un componente | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-INF-001 | Compromiso de pipeline de despliegue |
| CSPTF-THRT-INF-002 | Exposición de secreto de producción |
| CSPTF-THRT-INF-003 | Escape o abuso de contenedor |
| CSPTF-THRT-INF-004 | Toma de cuenta cloud privilegiada |
| CSPTF-THRT-INF-005 | Pérdida de infraestructura sin recuperación |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-INF-001 | Roles cloud excesivos |
| CSPTF-WEAK-INF-002 | Secretos en variables o repositorios |
| CSPTF-WEAK-INF-003 | Imágenes no firmadas |
| CSPTF-WEAK-INF-004 | Kubernetes mal endurecido |
| CSPTF-WEAK-INF-005 | Backups no restaurados en pruebas |

## Crosswalk

- MITRE AADAPT tactics: Initial Access, Execution, Privilege Escalation, Credential Access, Lateral Movement, Impact
- NIST CSF 2.0 functions: PR, DE, RC
- OWASP alignment: OWASP DevSecOps and supply-chain practices

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
