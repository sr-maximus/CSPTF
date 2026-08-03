# CSPTF-CTRL-API-005 - Rate limiting, cuotas y antiabuso

- **Domain:** API
- **Minimum assurance:** AP2
- **Status:** draft

## Objective

Asegurar que rate limiting, cuotas y antiabuso se diseñe, implemente, opere y evidencie de forma proporcional al riesgo del ecosistema de activos digitales.

## Normative requirement

La organización DEBE definir, aprobar, implementar, monitorear y revisar rate limiting, cuotas y antiabuso, manteniendo evidencia trazable y excepciones formalmente aceptadas.

## Required evidence

Política o diseño aprobado; configuración o artefacto técnico; registro operativo; evidencia de revisión; prueba de eficacia relacionada con rate limiting, cuotas y antiabuso.

## Implementation considerations

- define accountable owner and review frequency;
- document normal and emergency paths;
- automate preventive or detective evidence where feasible;
- separate implementation evidence from assertions;
- record exceptions, expiry and compensating controls;
- retest after material change.

## Crosswalk

- AADAPT tactics: Reconnaissance; Initial Access; Execution; Credential Access; Collection; Impact
- NIST CSF 2.0: PR; DE
- OWASP/related: OWASP API Security Top 10; SCSTG RPC interactions

## Assessment note

This control is technology-neutral. Chain-specific details belong in an annex or assessment profile and must not weaken the core property.
