class SymbolEncoder:
    def encode(self, x):
        return hash(x) % 1000
