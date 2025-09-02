from ..core.types import State
from .base import Agent
from ..mcp.client import MCPClient
from ..skills.math_tools import MathTools

class StrategistAgent(Agent):
    def __init__(self, name="strategist"):
        super().__init__(name)
        self.mcp = MCPClient()
        self.mt = MathTools()
    def act(self, state: State) -> State:
        d = state.domain
        if d == "calculus_integral":
            r = self.mcp.compute.compute_math({"type": "integral", "expr": state.problem.replace("Integrate"," ").replace("integrate"," ").strip(), "var": "x"})
            state.solution = r.get("result")
            state.approach = "symbolic_integration"
        elif d == "calculus_derivative":
            expr = state.problem.replace("Find derivative of"," ").replace("derivative of"," ").replace("differentiate"," ").strip()
            r = self.mcp.compute.compute_math({"type": "derivative", "expr": expr, "var": "x"})
            try:
                expanded = self.mt.derivative_expanded(expr, "x")
                state.solution = str(expanded)
            except Exception:
                state.solution = r.get("result")
            state.approach = "symbolic_differentiation"
        elif d == "algebra_equation":
            eq = state.problem.replace("Solve"," ").replace("solve"," ").strip()
            r = self.mcp.compute.compute_math({"type": "solve", "equation": eq, "var": "x"})
            state.solution = r.get("result")
            state.approach = "equation_solving"
        else:
            r = self.mcp.compute.compute_math({"type": "evaluate", "expr": state.problem})
            state.solution = r.get("result")
            state.approach = "simplification"
        return state
