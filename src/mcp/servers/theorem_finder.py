import json, os

class TheoremFinder:
    def __init__(self, path=None):
        self.path = path or os.path.join(os.path.dirname(__file__), "../../../data/theorems.json")
        with open(self.path, "r", encoding="utf-8") as f:
            self.theorems = json.load(f)
    def find_theorem(self, query: str):
        q = query.lower()
        hits = []
        for t in self.theorems:
            if any(k in q for k in t.get("keywords", [])):
                hits.append({"name": t["name"], "statement": t["statement"]})
        return hits[:3]
