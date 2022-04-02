from .population import Population


class Blanket(Population):
    def __init__(self):
        super().__init__()
        self.generation = self.make_gen_blanket()

    def make_gen_blanket(self):
        generation = []
        for i in range(self.minimum, self.maximum, 1):
            generation.append(i)
        return generation
