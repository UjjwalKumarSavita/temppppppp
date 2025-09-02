from .servers.computation import ComputationMCP
from .servers.theorem_finder import TheoremFinder
from .servers.math_knowledge import MathKnowledge
from .servers.community_check import CommunityCheck

class MCPClient:
    def __init__(self):
        self.compute = ComputationMCP()
        self.theorems = TheoremFinder()
        self.knowledge = MathKnowledge()
        self.community = CommunityCheck()
