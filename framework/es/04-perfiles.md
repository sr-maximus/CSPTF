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
