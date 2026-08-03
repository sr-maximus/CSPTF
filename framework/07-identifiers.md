# 07 - Identifier system

Identifiers are immutable after stable release.

| Object | Pattern | Example |
|---|---|---|
| Domain | `CSPTF-DOM-NN` | `CSPTF-DOM-10` |
| Control | `CSPTF-CTRL-CODE-NNN` | `CSPTF-CTRL-BRG-004` |
| Test | `CSPTF-TEST-CODE-NNN` | `CSPTF-TEST-BRG-009` |
| Threat | `CSPTF-THRT-CODE-NNN` | `CSPTF-THRT-KEY-001` |
| Weakness | `CSPTF-WEAK-CODE-NNN` | `CSPTF-WEAK-SCT-002` |
| Finding | `CSPTF-FIND-NNNN` | `CSPTF-FIND-0042` |
| Evidence | `CSPTF-EVID-NNNN` | `CSPTF-EVID-0088` |

## Rules

- IDs do not encode severity.
- Titles may evolve; IDs remain stable.
- Deleted items are deprecated, never reused.
- Chain-specific annexes append a namespace rather than replacing core IDs.
- Mappings include status: proposed, reviewed, verified or deprecated.
