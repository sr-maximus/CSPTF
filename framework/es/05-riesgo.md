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
