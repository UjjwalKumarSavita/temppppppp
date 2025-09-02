from ..core.types import State
from .base import Agent
from ..core.llm import build_llm
from ..skills.math_tools import MathTools

class ExplainerAgent(Agent):
    def __init__(self, name="explainer"):
        super().__init__(name)
        self.llm = build_llm()
        self.mt = MathTools()
    def act(self, state: State) -> State:
        prompt = f"Problem: {state.problem}\nApproach: {state.approach}\nSolution: {state.solution}\nWrite a clear step-by-step explanation for a student."
        txt = self.llm.ask("You are a precise math tutor.", prompt)
        if txt:
            state.explanation = txt
            return state
        if state.domain == "calculus_derivative":
            expr = state.problem.replace("Find derivative of"," ").replace("derivative of"," ").replace("differentiate"," ").strip()
            expanded = self.mt.derivative_expanded(expr, "x")
            state.explanation = f"Let f(x) = {expr}. Using chain rule, d/dx(f(x)) = {expanded}."
        else:
            state.explanation = f"Approach used: {state.approach}. Final answer: {state.solution}."
        return state
