from ..core.types import State
from .base import Agent

class AnalyzerAgent(Agent):
    def act(self, state: State) -> State:
        p = state.problem.lower()
        if any(k in p for k in ["integrate", "∫"]):
            state.domain = "calculus_integral"
        elif any(k in p for k in ["derivative", "differentiate", "d/dx"]):
            state.domain = "calculus_derivative"
        elif "=" in p or "solve" in p:
            state.domain = "algebra_equation"
        else:
            state.domain = "algebra_expression"
        return state
