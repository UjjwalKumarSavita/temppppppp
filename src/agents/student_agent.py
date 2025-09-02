from ..core.types import State
from .base import Agent

class StudentAgent(Agent):
    def act(self, state: State) -> State:
        return state
