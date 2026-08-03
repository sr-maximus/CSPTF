#!/usr/bin/env python3
"""Calculate the CSPTF v0.1 draft risk score."""
from __future__ import annotations
import argparse
import math

def band(score:int)->str:
    if score<=9:return "Informational"
    if score<=29:return "Low"
    if score<=49:return "Medium"
    if score<=69:return "High"
    if score<=89:return "Critical"
    return "Systemic"

def main()->int:
    p=argparse.ArgumentParser()
    for k in "FIAPGSR":
        p.add_argument(f"--{k.lower()}",type=float,required=True)
    for k in "EXQMC":
        p.add_argument(f"--{k.lower()}",type=float,required=True)
    a=p.parse_args()
    vals=vars(a)
    if any(v<0 or v>5 for v in vals.values()):
        p.error("all dimensions must be between 0 and 5")
    impact=.25*a.f+.15*a.i+.10*a.a+.10*a.p+.10*a.g+.15*a.s+.15*a.r
    likelihood=.30*a.e+.20*a.x+.15*a.q+.20*a.m+.15*a.c
    score=math.floor(100*(impact/5)*(likelihood/5)+0.5)
    print(f"Impact={impact:.2f}/5")
    print(f"Likelihood={likelihood:.2f}/5")
    print(f"Risk={score}/100 ({band(score)})")
    print("Draft model: calibration required.")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
