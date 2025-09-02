class KnowledgeBase:
    def __init__(self):
        self.shared = {}
    def write(self, key, value):
        self.shared[key] = value
    def read(self, key, default=None):
        return self.shared.get(key, default)
