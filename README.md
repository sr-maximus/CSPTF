# CSPTF - Crypto Security Penetration Testing Framework

<p align="center"><img src="docs/assets/csptf-logo.svg" alt="CSPTF" width="760"></p>


> **Status:** `0.1.0-draft` - foundational public draft, not a certification.

CSPTF is an open, evidence-informed framework for **authorized security assessment and penetration testing** of cryptocurrency, blockchain, Web3, DeFi, CeFi, wallets, custody, bridges, smart contracts, nodes, Layer 2 systems, APIs, cloud infrastructure, governance, monitoring, and operational resilience.

CSPTF is designed as an integration layer rather than a replacement for specialized sources. It combines:

- the adversary-behavior perspective of **MITRE AADAPT** and MITRE ATT&CK;
- the smart-contract depth of **OWASP SCSVS, SCSTG and SCWE**;
- the Solidity assurance requirements of **EEA EthTrust**;
- the assessment discipline of **NIST SP 800-115**;
- secure development, supply-chain, privacy, compliance, detection and resilience practices.

## Why CSPTF

Existing bodies of knowledge are valuable but usually focus on one layer: adversary TTPs, smart contracts, Solidity verification, application testing, or general information-security assessment. Digital-asset systems combine **irreversible transactions, economic incentives, composability, custody, distributed consensus, off-chain infrastructure and regulatory obligations**. CSPTF provides one traceable operating model across those layers.

## Draft inventory

| Component | Count |
|---|---:|
| Security domains | 20 |
| Normative controls | 160 |
| Authorized test cases | 240 |
| Threat scenarios | 100 |
| Weakness patterns | 100 |
| Assurance profiles | 4 |
| Evidence levels | 6 |

## Core principles

1. **Authorization before technique.**
2. **Testnets, forks and staging before production.**
3. **No customer assets by default.**
4. **Invariants and flows of value before vulnerability labels.**
5. **Economic, systemic and irreversibility impact are first-class risk dimensions.**
6. **Evidence, reproducibility and retesting are mandatory.**
7. **Automated tools support - but never replace - expert validation.**
8. **Safety, responsible disclosure and legal compliance are part of technical quality.**

## Repository map

```text
framework/      Core methodology, lifecycle, risk, assurance and conformance
domains/        Twenty security domains
catalogs/       Controls, tests, threats and weaknesses in Markdown/CSV/JSON
mappings/       Crosswalks to AADAPT, ATT&CK, OWASP, NIST, EEA and regulations
research/       Literature method, gap analysis, source register and validation plan
paper/          Publishable Spanish paper and technical specification
templates/      Rules of engagement, findings, reports, retest and disclosure
schemas/        Machine-readable JSON schemas
tools/          Catalog validator and query/checklist utilities
examples/       Safe example assessment package
publication/    LinkedIn article and release material
```

## Publication artifacts

- [Spanish technical paper (PDF)](paper/CSPTF_Paper_ES.pdf)
- [Spanish technical paper (DOCX)](paper/CSPTF_Paper_ES.docx)
- [Spanish consolidated specification (PDF)](paper/CSPTF_Specification_v0.1_ES.pdf)
- [Spanish consolidated specification (DOCX)](paper/CSPTF_Specification_v0.1_ES.docx)
- [LinkedIn article in Spanish](publication/linkedin-article-es.md)
- [Release validation report](publication/validation-report-v0.1.0-draft.md)

## Getting started

```bash
python tools/validate_catalogs.py
python tools/query_catalog.py --domain BRG --kind tests
python tools/generate_checklist.py --profile AP2 --output build/checklist-ap2.csv
```

Read these first:

1. [`framework/00-charter.md`](framework/00-charter.md)
2. [`framework/02-rules-of-engagement.md`](framework/02-rules-of-engagement.md)
3. [`framework/03-assessment-lifecycle.md`](framework/03-assessment-lifecycle.md)
4. [`framework/05-risk-scoring.md`](framework/05-risk-scoring.md)
5. [`domains/README.md`](domains/README.md)

## Assurance profiles

- **AP1 - Baseline:** low-complexity or limited-value systems.
- **AP2 - Enhanced:** production systems with meaningful assets or dependencies.
- **AP3 - Critical:** custody, exchanges, bridges, DeFi, validators or high-value services.
- **AP4 - Systemic:** material market, institutional, cross-chain or public-infrastructure impact.

Profiles define the minimum depth of evidence and testing; they do not certify that a system is secure.

## Responsible use

CSPTF is for systems you own or are explicitly authorized to test. Production-active, destructive, denial-of-service, consensus-disrupting, market-manipulating or fund-moving tests require itemized written authorization, monitoring, limits and stop authority. See [`SECURITY.md`](SECURITY.md) and the Rules of Engagement.

## Language

The normative draft is currently **Spanish-first**. An English normative translation is planned for v0.2. The repository structure and identifiers are language-neutral.

## Citation

See [`CITATION.cff`](CITATION.cff). Suggested citation:

> Peñuela Camacho, E. J. (2026). *CSPTF: Crypto Security Penetration Testing Framework, v0.1.0-draft*. GitHub repository.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).

## Maintainer

**Edwin Javier Peñuela Camacho** (GitHub: `@sr-maximus`)
