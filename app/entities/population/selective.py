import random
from .population import Population


class Selective(Population):
    def __init__(self):
        super().__init__()
        self.generation = self.make_gen_selective()

    def make_gen_selective(self):
        generation = []
        length = 8

        for i in range(length):
            generation.append(random.randrange(self.minimum, self.maximum))
        return generation
