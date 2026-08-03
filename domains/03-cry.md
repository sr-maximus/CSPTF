# CSPTF-DOM-03 - CRY: Criptografía, aleatoriedad y material criptográfico

**English:** Cryptography, Randomness and Cryptographic Material

## Purpose

Verificar selección, implementación, uso y ciclo de vida de primitivas criptográficas, fuentes de entropía, firmas y pruebas.

## Principal assets

- algoritmos
- parámetros
- entropía
- nonce
- firmas
- hashes
- cifrado
- pruebas de conocimiento cero

## Security questions

- What value, authority or state can be lost, forged, frozen or misdirected?
- Which trust assumptions are external, centralized, economic or time-dependent?
- Which invariants must remain true under failure and adversarial behavior?
- What can be validated safely in a fork, testnet or isolated lab?
- Which signals prove prevention, detection, containment and recovery?

## Controls

| ID | Control | Profile |
|---|---|---|
| CSPTF-CTRL-CRY-001 | Primitivas y parámetros aprobados | AP1 |
| CSPTF-CTRL-CRY-002 | Generación de entropía y aleatoriedad | AP1 |
| CSPTF-CTRL-CRY-003 | Gestión segura de nonces | AP2 |
| CSPTF-CTRL-CRY-004 | Validación canónica de firmas | AP2 |
| CSPTF-CTRL-CRY-005 | Separación de dominios criptográficos | AP2 |
| CSPTF-CTRL-CRY-006 | Protección contra replay y malleability | AP3 |
| CSPTF-CTRL-CRY-007 | Agilidad y migración criptográfica | AP3 |
| CSPTF-CTRL-CRY-008 | Verificación de implementaciones y bibliotecas | AP4 |

## Tests

| ID | Test | Profile | Type |
|---|---|---|---|
| CSPTF-TEST-CRY-001 | Inventariar primitivas y parámetros | AP1 | Revisión y validación controlada |
| CSPTF-TEST-CRY-002 | Revisar fuentes de entropía | AP1 | Revisión y validación controlada |
| CSPTF-TEST-CRY-003 | Validar generación y reutilización de nonces | AP1 | Revisión y validación controlada |
| CSPTF-TEST-CRY-004 | Comprobar validación de firmas | AP2 | Revisión y validación controlada |
| CSPTF-TEST-CRY-005 | Evaluar separación de dominios | AP2 | Revisión y validación controlada |
| CSPTF-TEST-CRY-006 | Probar controles anti-replay en entorno autorizado | AP2 | Revisión y validación controlada |
| CSPTF-TEST-CRY-007 | Revisar serialización y codificación canónica | AP2 | Revisión y validación controlada |
| CSPTF-TEST-CRY-008 | Comprobar manejo de claves públicas inválidas | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-CRY-009 | Evaluar bibliotecas y compilación criptográfica | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-CRY-010 | Revisar custodia de secretos criptográficos | AP3 | Simulación técnica autorizada |
| CSPTF-TEST-CRY-011 | Validar plan de migración y agilidad | AP4 | Ejercicio avanzado en laboratorio/fork |
| CSPTF-TEST-CRY-012 | Ejecutar pruebas de interoperabilidad criptográfica | AP4 | Ejercicio avanzado en laboratorio/fork |

## Threat scenarios

| ID | Threat |
|---|---|
| CSPTF-THRT-CRY-001 | Predicción o sesgo de aleatoriedad |
| CSPTF-THRT-CRY-002 | Reutilización de nonce y exposición de clave |
| CSPTF-THRT-CRY-003 | Replay de mensajes firmados |
| CSPTF-THRT-CRY-004 | Degradación de algoritmo o parámetro |
| CSPTF-THRT-CRY-005 | Fallo de validación criptográfica |

## Weakness patterns

| ID | Weakness |
|---|---|
| CSPTF-WEAK-CRY-001 | Entropía insuficiente |
| CSPTF-WEAK-CRY-002 | Dominio de firma ambiguo |
| CSPTF-WEAK-CRY-003 | Parámetros obsoletos |
| CSPTF-WEAK-CRY-004 | Comparaciones no constantes |
| CSPTF-WEAK-CRY-005 | Manejo incorrecto de serialización |

## Crosswalk

- MITRE AADAPT tactics: Credential Access, Execution, Defense Evasion, Impact, Fraud
- NIST CSF 2.0 functions: PR
- OWASP alignment: SCSTG cryptography; SCSVS cryptography

## Domain completion criteria

The domain is complete only when applicability is justified, selected controls are evidenced, tests are executed or explicitly deferred, findings are reviewed, and high-risk remediation has an owner and retest plan.
