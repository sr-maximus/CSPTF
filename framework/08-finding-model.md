# 08 - Finding model

A finding is a testable claim supported by evidence.

## Required fields

- finding ID and title;
- affected assets, versions, networks and addresses;
- related test, control, threat and weakness IDs;
- observation and expected property;
- reproducible safe validation;
- prerequisites and exploit path;
- impact dimensions;
- likelihood dimensions;
- risk band and any override;
- evidence level and confidence;
- root cause;
- remediation;
- compensating controls;
- owner and target date;
- disclosure restrictions;
- retest status;
- residual risk.

## Finding states

`draft -> validated -> accepted -> remediation in progress -> ready for retest -> closed`

Alternative terminal states:

- risk accepted;
- duplicate;
- not applicable;
- false positive;
- superseded.

State changes require actor, time, rationale and evidence.

## Root-cause rule

Do not create one finding per scanner line when several observations share one cause. Conversely, do not merge unrelated risks merely because they affect the same component.
