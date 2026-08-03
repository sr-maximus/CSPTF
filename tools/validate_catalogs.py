#!/usr/bin/env python3
"""Validate CSPTF catalog structure, IDs, counts, references and JSON schemas."""
from __future__ import annotations
import csv
import json
import re
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"domains":20, "controls":160, "tests":240, "threats":100, "weaknesses":100}

def load(name: str):
    return json.loads((ROOT / "catalogs" / f"{name}.json").read_text(encoding="utf-8"))

def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)

def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def parse_ref_tokens(value: str) -> set[str]:
    refs: set[str] = set()
    for match in re.finditer(r"REF-(\d{3})(?:\s+to\s+REF-(\d{3}))?", value):
        start = int(match.group(1))
        end = int(match.group(2) or match.group(1))
        refs.update(f"REF-{idx:03d}" for idx in range(start, end + 1))
    return refs

def main() -> int:
    errors: list[str] = []
    data = {name: load(name) for name in EXPECTED}
    for name, expected in EXPECTED.items():
        if len(data[name]) != expected:
            fail(f"{name}: expected {expected}, got {len(data[name])}", errors)

    domain_codes = {d["code"] for d in data["domains"]}
    if len(domain_codes) != 20:
        fail("domain codes are not unique", errors)

    all_ids: set[str] = set()
    for name, rows in data.items():
        for row in rows:
            item_id = row["id"]
            if item_id in all_ids:
                fail(f"duplicate ID: {item_id}", errors)
            all_ids.add(item_id)
            if name != "domains" and row["domain_code"] not in domain_codes:
                fail(f"{item_id}: unknown domain {row['domain_code']}", errors)

    schemas = {
        "controls": json.loads((ROOT/"schemas/control.schema.json").read_text()),
        "tests": json.loads((ROOT/"schemas/test.schema.json").read_text()),
    }
    for name, schema in schemas.items():
        validator = Draft202012Validator(schema)
        for row in data[name]:
            for err in validator.iter_errors(row):
                fail(f"{row.get('id')}: schema: {err.message}", errors)

    example_schemas = {
        "assessment-manifest.json": "assessment.schema.json",
        "finding.json": "finding.schema.json",
        "evidence-record.json": "evidence.schema.json",
    }
    for example_name, schema_name in example_schemas.items():
        example = json.loads((ROOT / "examples" / example_name).read_text(encoding="utf-8"))
        schema = json.loads((ROOT / "schemas" / schema_name).read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema)
        for err in validator.iter_errors(example):
            fail(f"examples/{example_name}: schema: {err.message}", errors)

    control_ids = {c["id"] for c in data["controls"]}
    for test in data["tests"]:
        if test["related_controls"] not in control_ids:
            fail(f"{test['id']}: missing related control {test['related_controls']}", errors)

    markdown_counts = {
        "controls": len(list((ROOT/"catalogs/controls").glob("CSPTF-CTRL-*.md"))),
        "tests": len(list((ROOT/"catalogs/tests").glob("CSPTF-TEST-*.md"))),
        "threats": len(list((ROOT/"catalogs/threats").glob("CSPTF-THRT-*.md"))),
        "weaknesses": len(list((ROOT/"catalogs/weaknesses").glob("CSPTF-WEAK-*.md"))),
    }
    for name, expected in EXPECTED.items():
        if name == "domains":
            continue
        if markdown_counts[name] != expected:
            fail(f"{name}: expected {expected} markdown records, got {markdown_counts[name]}", errors)

    forbidden = [r"\bmainnet exploit\b", r"\bstolen private key\b", r"\bdrain real funds\b"]
    for p in (ROOT/"catalogs/tests").glob("*.md"):
        txt = p.read_text(encoding="utf-8").lower()
        for pat in forbidden:
            if re.search(pat, txt):
                fail(f"{p.name}: prohibited unsafe phrase matched {pat}", errors)

    source_rows = read_csv(ROOT / "research/source-register.csv")
    source_ids = {row["id"] for row in source_rows}
    if len(source_ids) != len(source_rows):
        fail("research/source-register.csv has duplicate IDs", errors)
    for row in source_rows:
        if not row["url"].startswith("https://"):
            fail(f"{row['id']}: source URL must use https", errors)

    claims = read_csv(ROOT / "research/claims-evidence.csv")
    claim_ids = {row["claim_id"] for row in claims}
    if len(claim_ids) != len(claims):
        fail("research/claims-evidence.csv has duplicate claim IDs", errors)
    for claim in claims:
        missing = parse_ref_tokens(claim["supporting_refs"]) - source_ids
        if missing:
            fail(f"{claim['claim_id']}: missing source refs {sorted(missing)}", errors)

    tooling = read_csv(ROOT / "research/tooling-register.csv")
    tool_ids = {row["tool_id"] for row in tooling}
    if len(tool_ids) != len(tooling):
        fail("research/tooling-register.csv has duplicate tool IDs", errors)
    for row in tooling:
        if not row["official_reference"].startswith("https://"):
            fail(f"{row['tool_id']}: tooling reference must use https", errors)
        for code in row["primary_domains"].split(";"):
            if code not in domain_codes:
                fail(f"{row['tool_id']}: unknown tooling domain {code}", errors)
        if row["max_evidence_without_review"] not in {"E1", "E2", "E3", "E4", "E5"}:
            fail(f"{row['tool_id']}: invalid evidence limit", errors)

    if errors:
        print("CSPTF validation FAILED")
        for e in errors:
            print(f"- {e}")
        return 1
    print("CSPTF validation PASSED")
    print("Counts:", ", ".join(f"{k}={len(v)}" for k,v in data.items()))
    print(f"Unique IDs: {len(all_ids)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
