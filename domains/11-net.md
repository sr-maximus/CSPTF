# CSPTF-DOM-11 - NET: Consenso, validadores, nodos y redes P2P

**English:** Consensus, Validators, Nodes and P2P Networks

## Purpose

Evaluar seguridad del consenso, operación de nodos, validadores, clientes, mempool, P2P, sincronización y exposición de interfaces.

## Principal assets

- validators
- full nodes
- consensus clients
- execution clients
- mempool
- P2P network
- genesis/config
- peer discovery

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-NET-001 | Configuración de consenso y génesis | AP1 |
| CSPTF-CTRL-NET-002 | Diversidad y endurecimiento de clientes | AP1 |
| CSPTF-CTRL-NET-003 | Gestión de identidades de validador | AP2 |
| CSPTF-CTRL-NET-004 | Seguridad P2P y peer management | AP2 |
| CSPTF-CTRL-NET-005 | Mempool y propagación de transacciones | AP2 |
| CSPTF-CTRL-NET-006 | Sincronización, checkpoints y estado | AP3 |
| CSPTF-CTRL-NET-007 | Protección contra slashing y equivocación | AP3 |
| CSPTF-CTRL-NET-008 | Monitoreo, disponibilidad y recuperación | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-NET-001 | Revisar parámetros de consenso y génesis | AP1 | Revisión y validación controlada |
| CSPTF-TEST-NET-002 | Validar diversidad y versiones de clientes | AP1 | Revisión y validación controlada |
| CSPTF-TEST-NET-003 | Evaluar exposición de nodos y puertos | AP1 | Revisión y validación controlada |
| CSPTF-TEST-NET-004 | Comprobar peer discovery y allowlisting | AP2 | Revisión y validación controlada |
| CSPTF-TEST-NET-005 | Revisar identidad y claves de validador | AP2 | Revisión y validación controlada |
| CSPTF-TEST-NET-006 | Evaluar protección contra double signing | AP2 | Revisión y validación controlada |
| CSPTF-TEST-NET-007 | Comprobar mempool y políticas de admisión | AP2 | Revisión y validación controlada |
| CSPTF-TEST-NET-008 | Validar sincronización y checkpoints | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-NET-009 | Evaluar resistencia a particiones en laboratorio | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-NET-010 | Revisar límites de recursos y DoS | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-NET-011 | Comprobar backups y reconstrucción de estado | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-NET-012 | Ejecutar simulación de indisponibilidad de validador | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-NET-001 | Partición o eclipse de nodos |
| CSPTF-THRT-NET-002 | Compromiso de validador |
| CSPTF-THRT-NET-003 | Double signing o slashing |
| CSPTF-THRT-NET-004 | Explotación de cliente dominante |
| CSPTF-THRT-NET-005 | Agotamiento de recursos P2P |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-NET-001 | Puertos administrativos expuestos |
| CSPTF-WEAK-NET-002 | Clientes sin diversidad |
| CSPTF-WEAK-NET-003 | Protección anti-slashing insuficiente |
| CSPTF-WEAK-NET-004 | Peer management débil |
| CSPTF-WEAK-NET-005 | Recuperación de estado no probada |

## Crosswalk

- MITRE AADAPT tactics: Resource Development, Initial Access, Execution, Lateral Movement, Impact
- NIST CSF 2.0 functions: PR, DE, RC
- OWASP alignment: OWASP scope is partial; CSPTF extension

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
