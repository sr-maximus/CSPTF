import json
import csv
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class CatalogTests(unittest.TestCase):
    def load(self,name):
        return json.loads((ROOT/"catalogs"/f"{name}.json").read_text(encoding="utf-8"))
    def test_counts(self):
        self.assertEqual(len(self.load("domains")),20)
        self.assertEqual(len(self.load("controls")),160)
        self.assertEqual(len(self.load("tests")),240)
        self.assertEqual(len(self.load("threats")),100)
        self.assertEqual(len(self.load("weaknesses")),100)
    def test_unique_ids(self):
        ids=[]
        for name in ["domains","controls","tests","threats","weaknesses"]:
            ids += [x["id"] for x in self.load(name)]
        self.assertEqual(len(ids),len(set(ids)))
    def test_related_controls(self):
        controls={x["id"] for x in self.load("controls")}
        self.assertTrue(all(t["related_controls"] in controls for t in self.load("tests")))
    def test_tooling_register_covers_all_domains(self):
        domains={x["code"] for x in self.load("domains")}
        with (ROOT/"research/tooling-register.csv").open(encoding="utf-8",newline="") as f:
            rows=list(csv.DictReader(f))
        covered=set()
        for row in rows:
            covered.update(row["primary_domains"].split(";"))
        self.assertEqual(domains-covered,set())
    def test_evidence_matrix_fixture_matches_ap2_scope(self):
        tests=[x for x in self.load("tests") if x["minimum_profile"] in {"AP1","AP2"}]
        with (ROOT/"build/evidence-matrix-ap2.csv").open(encoding="utf-8",newline="") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),len(tests))
        self.assertTrue({"test_id","example_tools","minimum_evidence"}.issubset(rows[0].keys()))

if __name__=="__main__":
    unittest.main()
