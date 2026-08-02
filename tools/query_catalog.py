#!/usr/bin/env python3
"""Query CSPTF catalogs by domain and object kind."""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True, help="Domain code, e.g. BRG")
    ap.add_argument("--kind", choices=["controls","tests","threats","weaknesses"], default="tests")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    rows=json.loads((ROOT/"catalogs"/f"{args.kind}.json").read_text(encoding="utf-8"))
    rows=[r for r in rows if r["domain_code"].upper()==args.domain.upper()]
    if args.json:
        print(json.dumps(rows,ensure_ascii=False,indent=2))
    else:
        for r in rows:
            print(f"{r['id']}\t{r['title_es']}")
    return 0 if rows else 2
if __name__=="__main__":
    raise SystemExit(main())
