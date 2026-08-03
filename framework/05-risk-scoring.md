# 05 - Draft risk-scoring model

> This model is a v0.1 hypothesis. Weights and bands require empirical calibration and inter-rater validation before any certification use.

## Impact dimensions (0-5)

- **F - Financial:** direct and indirect asset loss.
- **I - Integrity:** unauthorized state, transaction or record change.
- **A - Availability:** disruption and recovery time.
- **P - Privacy:** exposure, linkability or misuse of sensitive data.
- **G - Governance:** capture of administrative or decision authority.
- **S - Systemic:** contagion across protocols, markets or institutions.
- **R - Irreversibility:** difficulty of rollback, clawback or restoration.

```text
Impact = 0.25F + 0.15I + 0.10A + 0.10P + 0.10G + 0.15S + 0.15R
```

## Likelihood dimensions (0-5)

- **E - Exploitability:** complexity, reliability and access.
- **X - Exposure:** reachability and attack-surface prevalence.
- **Q - Preconditions:** score is higher when fewer preconditions exist.
- **M - Incentive:** economic or strategic attractiveness.
- **C - Composability:** amplification through dependencies and atomicity.

```text
Likelihood = 0.30E + 0.20X + 0.15Q + 0.20M + 0.15C
RawRisk = 100 * (Impact / 5) * (Likelihood / 5)
Risk = floor(RawRisk + 0.5)  # deterministic half-up rounding
```

## Draft bands

| Score | Band |
|---:|---|
| 0-9 | Informational |
| 10-29 | Low |
| 30-49 | Medium |
| 50-69 | High |
| 70-89 | Critical |
| 90-100 | Systemic |

## Overrides

A finding cannot be below High when credible exploitation can directly compromise a root signer, unrestricted mint, bridge validator majority, reserve ledger or irreversible high-value withdrawal. Overrides MUST be explained, not hidden.

## Confidence and evidence

Risk and confidence are separate. A plausible but weakly evidenced scenario may have high potential impact and low confidence. The report shows both.

## Aggregation

Do not average findings into a single “security score” without preserving:

- maximum risk;
- asset concentration;
- shared root causes;
- correlated dependencies;
- unresolved critical paths;
- uncertainty.

## Example

Dimensions `F=5, I=4, A=2, P=1, G=4, S=4, R=5` produce Impact 3.90.  
Dimensions `E=3, X=4, Q=3, M=5, C=4` produce Likelihood 3.75.  
Draft risk is `floor(100 × 3.90/5 × 3.75/5 + 0.5) = 59`, High.
