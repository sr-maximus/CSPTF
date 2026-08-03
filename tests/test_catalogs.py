import json
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

if __name__=="__main__":
    unittest.main()
