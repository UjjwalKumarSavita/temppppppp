from .core.orchestrator import Orchestrator

def solve(problem: str):
    o = Orchestrator()
    s = o.run(problem)
    return {"problem": s.problem, "domain": s.domain, "solution": s.solution, "verified": s.verified, "explanation": s.explanation}

