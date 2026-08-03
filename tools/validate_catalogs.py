#!/usr/bin/env python3
"""Validate CSPTF catalog structure, IDs, counts, references and JSON schemas."""
from __future__ import annotations
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
