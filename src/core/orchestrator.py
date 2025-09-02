from .types import State
from ..agents.student_agent import StudentAgent
from ..agents.analyzer_agent import AnalyzerAgent
from ..agents.strategist_agent import StrategistAgent
from ..agents.verifier_agent import VerifierAgent
from ..agents.explainer_agent import ExplainerAgent

class Orchestrator:
    def __init__(self):
        self.student = StudentAgent("student")
        self.analyzer = AnalyzerAgent("analyzer")
        self.strategist = StrategistAgent()
        self.verifier = VerifierAgent()
        self.explainer = ExplainerAgent()
    def run(self, problem: str) -> State:
        s = State(problem=problem)
        s = self.student.act(s)
        s = self.analyzer.act(s)
        s = self.strategist.act(s)
        if not s.verified:
            s = self.strategist.act(s)
            s = self.verifier.act(s)
        else:
            s = self.verifier.act(s)
        s = self.explainer.act(s)
        return s
