#!/usr/bin/env python3
"""Generate a profile-tailored CSPTF checklist in CSV."""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LEVEL={"AP1":1,"AP2":2,"AP3":3,"AP4":4}

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--profile",choices=LEVEL,required=True)
    ap.add_argument("--output",required=True)
    ap.add_argument("--domain",action="append",help="Repeatable domain code filter")
    args=ap.parse_args()
    tests=json.loads((ROOT/"catalogs/tests.json").read_text(encoding="utf-8"))
    selected=[t for t in tests if LEVEL[t["minimum_profile"]] <= LEVEL[args.profile]]
    if args.domain:
        allowed={d.upper() for d in args.domain}
        selected=[t for t in selected if t["domain_code"] in allowed]
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    fields=["id","domain_code","title_es","minimum_profile","related_controls","status","result","evidence_id","finding_id","notes"]
    with out.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n"); w.writeheader()
        for t in selected:
            w.writerow({**{k:t.get(k,"") for k in fields},"result":"not-tested"})
    print(f"Wrote {len(selected)} tests to {out}")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
