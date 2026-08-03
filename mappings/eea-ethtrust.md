# Mapping to EEA EthTrust

EEA EthTrust Security Levels v3 defines requirements for reviewing Solidity smart contracts and distinguishes S, M and Q review levels.

CSPTF treats EthTrust as a specialized Solidity assurance source. Approximate conceptual alignment:

- EthTrust S: automated and baseline checks, often supporting AP1/AP2;
- EthTrust M: manual review depth, often supporting AP2/AP3;
- EthTrust Q: logic and documentation review, often supporting AP3/AP4.

This is not a formal equivalence. CSPTF assurance profiles also include non-Solidity layers, evidence, operational exercises and independence requirements.
