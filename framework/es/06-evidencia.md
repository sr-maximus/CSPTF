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
