# 04 - Assurance profiles

Profiles determine minimum depth, evidence and independence. They do not rank the business or certify security.

| Profile | Typical use | Minimum evidence | Testing depth | Independence |
|---|---|---|---|---|
| AP1 Baseline | prototypes, internal tools, low-value pilots | E2 configuration | review + bounded functional validation | qualified internal review |
| AP2 Enhanced | production dApps and services with material assets | E3 observed | threat-informed dynamic testing | reviewer independent of implementation |
| AP3 Critical | custody, CEX, bridges, validators, major DeFi | E4 adversarial | simulation, property testing, failure exercises | independent specialist team |
| AP4 Systemic | material market/institutional or cross-chain impact | E5 independent | multi-team review, crisis exercise, economic/systemic modeling | organizationally independent assurance |

## Selection factors

Score each 0-5:

- asset value at risk;
- transaction volume;
- user and institutional concentration;
- irreversibility;
- composability and dependency depth;
- custody or privileged signing;
- consensus or market impact;
- regulatory/systemic significance;
- novelty and change velocity;
- recovery difficulty.

AP1 is not appropriate when any single factor is 4-5 without a documented compensating rationale.

## Profile inheritance

Higher profiles inherit lower-profile requirements. A control MAY require a higher profile than the system baseline due to local criticality.

## Mixed profiles

A system may use AP3 for custody and bridge domains, AP2 for APIs and AP1 for a non-production documentation portal. The assessment report MUST show the profile by domain and justify differences.
