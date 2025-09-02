from typing import Any, List
from sympy import symbols, Eq, solve, simplify, diff, integrate, limit, E, pi, sin, cos, tan, log, sqrt, expand_trig
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

T = standard_transformations + (convert_xor, implicit_multiplication_application)
LOCAL = {"e": E, "pi": pi, "sin": sin, "cos": cos, "tan": tan, "log": log, "ln": log, "sqrt": sqrt}

class MathTools:
    def __init__(self):
        self.default_var = symbols("x")
    def _sym(self, s):
        if isinstance(s, str):
            return parse_expr(s, transformations=T, evaluate=True, local_dict=LOCAL)
        return s
    def evaluate(self, expr: str) -> Any:
        return simplify(self._sym(expr))
    def derivative(self, expr: str, var: str = "x") -> Any:
        return diff(self._sym(expr), symbols(var))
    def derivative_expanded(self, expr: str, var: str = "x") -> Any:
        return expand_trig(diff(self._sym(expr), symbols(var)))
    def integral(self, expr: str, var: str = "x") -> Any:
        return simplify(integrate(self._sym(expr), symbols(var)))
    def solve_equation(self, equation: str, var: str = "x") -> List[Any]:
        if "=" in equation:
            l, r = equation.split("=", 1)
            return solve(Eq(self._sym(l), self._sym(r)), symbols(var))
        return solve(self._sym(equation), symbols(var))
    def limit_of(self, expr: str, var: str = "x", to: str = "0") -> Any:
        return simplify(limit(self._sym(expr), symbols(var), self._sym(to)))
    def verify_solution(self, equation: str, sols: List[Any], var: str = "x") -> bool:
        if not sols:
            return False
        v = symbols(var)
        if "=" in equation:
            l, r = equation.split("=", 1)
            L = self._sym(l)
            R = self._sym(r)
            ok = True
            for s in sols:
                ok = ok and simplify(L.subs(v, s) - R.subs(v, s)) == 0
            return ok
        expr = self._sym(equation)
        ok = True
        for s in sols:
            ok = ok and simplify(expr.subs(v, s)) == 0
        return ok
