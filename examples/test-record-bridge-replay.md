# CSPTF Test Record - Fictional Bridge Replay

- Test ID: `CSPTF-TEST-BRG-003`
- Test title: Comprobar nonce, replay y unicidad
- Assessment ID: `CSPTF-ASMT-DEMO-0001`
- Operator: demo security team
- Date/time/timezone: 2026-07-31 14:20 America/Bogota
- Authorization reference: `DEMO-ROE-TESTNET-001`
- Asset/environment/version: fictional bridge lab v0.0-test on local fork
- Related control: `CSPTF-CTRL-BRG-002`
- Expected invariant: a consumed cross-chain message identifier cannot be accepted twice
- Preconditions: synthetic token, mock relayer, no production network, no real funds
- Limits and stop conditions: stop on unexpected external RPC call, non-demo asset movement or uncontrolled state change

## Procedure performed

1. Started a local fork and loaded only the fictional bridge lab contracts.
2. Submitted a synthetic message with identifier `DEMO-MSG-0001` through the mock relayer.
3. Confirmed the first synthetic message changed only local test balances.
4. Reset the mock relayer process without resetting bridge contract state.
5. Replayed the same synthetic message identifier.
6. Compared bridge state, event logs and local balances before and after replay.

## Evidence

| Evidence ID | Description | Source | Hash/location | Sensitivity |
|---|---|---|---|---|
| `CSPTF-EVID-DEMO-0001` | replay harness output and state diff | fictional local fork | `examples/evidence-record.json` | public demo |

## Result

- result: fail
- observation: the fictional lab accepted a duplicate message after mock relayer restart
- deviation from plan: none
- side effects: local synthetic state only
- cleanup and reconciliation: fork discarded; no external state changed
- related finding: `CSPTF-FIND-0001`
- reviewer: demo reviewer

## Limitations

This is a safe fictional example. It does not demonstrate a vulnerability in any
real bridge or protocol.
