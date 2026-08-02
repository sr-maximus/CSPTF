# 02 - Rules of Engagement (RoE)

## Mandatory authorization

No CSPTF test begins without a signed authorization identifying the owner, tester, systems, environments, dates, contacts, techniques and limits. Authorization MUST be specific enough that an independent reviewer can decide whether an action was permitted.

## Environment priority

Use the safest environment that can answer the question:

1. static review and documentation;
2. local unit/integration environment;
3. isolated simulation;
4. deterministic fork or shadow environment;
5. testnet;
6. staging/pre-production;
7. read-only production observation;
8. explicitly authorized active production testing.

Moving down the list requires a documented reason and increased controls.

## Production safeguards

Active production testing requires:

- itemized test IDs;
- named approver and stop authority;
- live monitoring and communications channel;
- backups, rollback or compensating recovery;
- zero customer-fund use by default;
- transaction, gas, volume and time limits;
- rate and concurrency limits;
- pre- and post-test balance reconciliation;
- emergency termination criteria;
- incident conversion procedure;
- evidence handling and disclosure plan.

## Default prohibited actions

Unless individually authorized in writing, the assessor MUST NOT:

- move, lock, burn or expose real customer assets;
- degrade consensus, availability or market integrity;
- manipulate prices or create deceptive market activity;
- use stolen credentials, seeds or keys;
- create uncontrolled persistence;
- bypass legal identity, sanctions or financial-crime controls;
- access data unrelated to the test objective;
- publish an unremediated vulnerability that materially increases risk.

## Stop conditions

Stop immediately when:

- unexpected asset movement occurs;
- integrity, availability, consensus or solvency may be affected;
- scope or ownership becomes uncertain;
- monitoring is unavailable;
- sensitive third-party data is exposed;
- a real attacker may be active;
- rollback or reconciliation cannot be assured;
- the named stop authority instructs termination.

## Evidence and cleanup

Every active action MUST be logged with operator, time, target, purpose, expected effect, observed effect and cleanup status. Test identities, allowances, roles, contracts, data and infrastructure MUST be removed or revoked after validation.
