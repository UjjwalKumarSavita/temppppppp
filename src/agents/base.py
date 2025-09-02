from ..core.types import State

class Agent:
    def __init__(self, name):
        self.name = name
    def act(self, state: State) -> State:
        return state
