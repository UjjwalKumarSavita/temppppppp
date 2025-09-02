from ..core.types import State
from .base import Agent
from ..skills.math_tools import MathTools
from sympy import simplify

class VerifierAgent(Agent):
    def __init__(self, name="verifier"):
        super().__init__(name)
        self.mt = MathTools()
    def act(self, state: State) -> State:
        d = state.domain
        ok = False
        if d == "algebra_equation":
            sols = state.solution if isinstance(state.solution, list) else [state.solution]
            ok = self.mt.verify_solution(state.problem.replace("Solve"," ").replace("solve"," "), [self.mt._sym(s) for s in sols])
        elif d == "calculus_integral":
            F = self.mt._sym(str(state.solution))
            f = self.mt._sym(state.problem.replace("Integrate"," ").replace("integrate"," ").strip())
            ok = simplify(self.mt.derivative(str(F)) - self.mt._sym(f)) == 0
        elif d == "calculus_derivative":
            expr = state.problem.replace("Find derivative of"," ").replace("derivative of"," ").replace("differentiate"," ").strip()
            ok = simplify(self.mt.derivative(expr) - self.mt._sym(state.solution)) == 0
        else:
            ok = True
        state.verified = bool(ok)
        return state
