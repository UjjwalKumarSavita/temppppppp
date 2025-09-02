def classify(problem: str) -> str:
    p = problem.lower()
    if any(k in p for k in ["integrate", "∫"]):
        return "calculus_integral"
    if any(k in p for k in ["derivative", "differentiate", "d/dx"]):
        return "calculus_derivative"
    if "=" in p or "solve" in p:
        return "algebra_equation"
    return "algebra_expression"

