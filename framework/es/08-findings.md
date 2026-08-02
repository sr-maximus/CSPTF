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
