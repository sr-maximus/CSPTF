# 09 - Conformance

CSPTF v0.1 supports **assessment conformance**, not product certification.

An assessment MAY claim `CSPTF Assessment Conformant - Draft` only when it:

1. identifies framework version;
2. has written authorization and RoE;
3. states system archetype and scope;
4. assigns assurance profile per domain;
5. records applicable, excluded and not-tested items;
6. uses CSPTF IDs;
7. preserves evidence level and confidence;
8. applies the risk model or documents a transparent alternative;
9. reports limitations and residual risk;
10. includes remediation and retest status;
11. passes structural validation of the assessment manifest.

It MUST NOT claim:

- CSPTF certification;
- security guarantee;
- framework endorsement;
- compliance with mapped standards solely because a thematic mapping exists.

## Coverage metrics

Report separately:

- control coverage;
- test execution coverage;
- evidence coverage;
- threat coverage;
- domain coverage;
- retest closure.

A single combined percentage is discouraged because it can hide omitted critical paths.
