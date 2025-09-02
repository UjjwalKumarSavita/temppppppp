from .mcp.client import MCPClient

class MCPIntegration:
    def __init__(self):
        self.client = MCPClient()
    def compute(self, task):
        return self.client.compute.compute_math(task)
    def find_theorem(self, query):
        return self.client.theorems.find_theorem(query)
    def lookup(self, query):
        return self.client.knowledge.serp_math_lookup(query)
    def community_check(self, problem, solution):
        return self.client.community.community_solution_check(problem, solution)
