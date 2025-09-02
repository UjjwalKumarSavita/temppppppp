from .core.orchestrator import Orchestrator

class DynamicSystem:
    def __init__(self):
        self.o = Orchestrator()
    def solve(self, problem: str):
        return self.o.run(problem)

