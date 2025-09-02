class CommunityCheck:
    def community_solution_check(self, problem: str, solution: str):
        score = 0.7 if len(solution) > 0 else 0.0
        verdict = "plausible" if score >= 0.6 else "uncertain"
        return {"score": score, "verdict": verdict}
