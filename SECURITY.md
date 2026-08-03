# Security policy and responsible disclosure

## Scope

Report vulnerabilities in CSPTF tooling, schemas, examples, documentation supply chain, release artifacts or the project website privately before public disclosure.

Do not place secrets, customer data, private incident evidence or a working exploit against a live third-party system in a public issue.

## Report contents

- affected version and component;
- impact and prerequisites;
- safe reproduction in an isolated environment;
- supporting evidence;
- suggested remediation;
- disclosure constraints.

## Framework safety

CSPTF is intended only for systems the assessor owns or is explicitly authorized to test. A framework test case is not authorization. Production-active testing must be itemized in the Rules of Engagement.

The default prohibitions are:

- movement or loss of real customer funds;
- destructive changes;
- denial-of-service or consensus disruption;
- market manipulation;
- bypass of sanctions, KYC or other legal controls;
- use of stolen credentials or keys;
- disclosure of unpatched vulnerabilities before coordination.

Use forks, testnets, staging, synthetic identities and test assets whenever possible.
