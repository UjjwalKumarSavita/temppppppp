from typing import Any, Dict
from ...skills.math_tools import MathTools

class ComputationMCP:
    def __init__(self):
        self.mt = MathTools()
    def compute_math(self, task: Dict[str, Any]) -> Dict[str, Any]:
        t = task.get("type", "evaluate")
        if t == "evaluate":
            res = self.mt.evaluate(task["expr"])
            return {"ok": True, "result": str(res), "kind": "evaluate"}
        if t == "derivative":
            res = self.mt.derivative(task["expr"], task.get("var", "x"))
            return {"ok": True, "result": str(res), "kind": "derivative"}
        if t == "integral":
            res = self.mt.integral(task["expr"], task.get("var", "x"))
            return {"ok": True, "result": str(res), "kind": "integral"}
        if t == "solve":
            res = self.mt.solve_equation(task["equation"], task.get("var", "x"))
            return {"ok": True, "result": [str(x) for x in res], "kind": "solve"}
        if t == "limit":
            res = self.mt.limit_of(task["expr"], task.get("var", "x"), task.get("to", "0"))
            return {"ok": True, "result": str(res), "kind": "limit"}
        return {"ok": False, "error": "unknown task"}
