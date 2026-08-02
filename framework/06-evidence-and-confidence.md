# 06 - Evidence and confidence

## Evidence levels

| Level | Name | Meaning |
|---|---|---|
| E0 | Declarative | unverified statement or questionnaire answer |
| E1 | Documentary | policy, diagram, ticket or design record |
| E2 | Configuration | configuration, source, build or control artifact |
| E3 | Observed | direct observation, logs, queries or runtime output |
| E4 | Adversarial | controlled test reproduces the security property or failure |
| E5 | Independent | independently repeated or externally attested evidence |

Higher evidence is not automatically better if it is stale, incomplete or unrelated.

## Evidence record

Each artifact MUST record:

- evidence ID;
- source and owner;
- collection date/time and timezone;
- environment and version;
- collector;
- integrity hash where appropriate;
- sensitivity and handling restrictions;
- related control/test/finding;
- limitations;
- retention and deletion date.

## Confidence levels

- **C1 Low:** material assumptions remain unverified.
- **C2 Moderate:** multiple indicators support the conclusion but gaps remain.
- **C3 High:** direct, repeatable evidence supports the conclusion.
- **C4 Very high:** independent reproduction and complete traceability.

## Contradictory evidence

Conflicts are not resolved by choosing the most convenient artifact. The assessor documents the conflict, assesses freshness and provenance, seeks reproduction, and lowers confidence until resolved.

## Tool output

Scanner output alone is E2 at most unless the assessor validates reachability, preconditions and impact. Tool disagreement is expected and requires expert triage.
