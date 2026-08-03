# Publishing CSPTF to GitHub

Target repository: `sr-maximus/CSPTF`

## Preferred: Codex

Open the repository in Codex, upload this project package, and request:

> Replace the repository working tree with the contents of the `CSPTF` folder. Preserve `.git`, create branch `agent/publish-csptf-v0.1`, run `python tools/validate_catalogs.py` and `python -m pytest`, commit as `Publish CSPTF v0.1.0 draft`, push the branch, and open a draft pull request against `main`. Do not publish credentials, local environment files, caches, or generated temporary files.

## Local Git alternative

From the extracted `CSPTF` directory:

```bash
./scripts/publish-to-github.sh
```

The script clones the public repository, creates a branch, replaces the working tree with the complete framework, commits, and pushes. GitHub authentication must already be available in the terminal.

## Expected release inventory

- 20 security assessment domains
- 160 controls
- 240 authorized test cases
- 100 threats
- 100 weaknesses
- Paper and full framework specification in PDF and DOCX
- JSON/CSV catalogs, schemas, examples, validation tools, and MkDocs configuration

## Safety and authorization

CSPTF is intended only for assessments with explicit written authorization. Destructive, economic, consensus, availability, and real-fund tests must be performed only in controlled environments with approved stop conditions.
