class MiniEnv:
    def reset(self): return 'init'
    def step(self, action): return 'next', 1.0, False
