class TransitionModel:
    def __init__(self):
        self.graph = {}

    def add_transition(self, s1, s2):
        self.graph.setdefault(s1, set()).add(s2)

    def get_successors(self, state):
        return list(self.graph.get(state, []))
