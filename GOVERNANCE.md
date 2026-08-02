# CSPTF governance

## Roles

- **Founding maintainer:** stewards vision, releases and governance.
- **Maintainer:** merges routine changes and enforces quality gates.
- **Domain editor:** reviews one or more technical domains.
- **Reviewer:** provides documented expert review.
- **Contributor:** submits accepted changes.

## Decision model

Routine editorial and additive changes use lazy consensus after review. Normative changes to identifiers, assurance profiles, scoring, conformance or safety require:

1. a public design issue;
2. evidence and alternatives;
3. two independent reviews;
4. a recorded maintainer decision;
5. a deprecation or migration plan where relevant.

## Releases

- Patch: corrections with no normative semantic change.
- Minor: additive controls, tests, mappings or tooling.
- Major: incompatible change to structure, meaning, scoring or conformance.

Draft identifiers are stable within a minor line but may change before v1.0. Released identifiers are never reused.

## Independence and conflicts

Reviewers disclose employment, commercial relationships or authorship that could materially affect judgment. No vendor may claim exclusive conformance, certification rights or endorsement by CSPTF.

## Certification

CSPTF v0.1 does not operate a certification program. Any future certification requires independent governance, assessor criteria, quality assurance, appeals and surveillance.
