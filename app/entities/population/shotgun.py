import random
from .population import Population


class Shotgun(Population):

    def __init__(self):
        super().__init__()
        self.generation = self.make_gen_shotgun()

    def make_gen_shotgun(self):
        generation = []
        length = int(len(range(self.minimum, self.maximum, 1))/2)+1
        for i in range(length):
            generation.append(random.randrange(self.minimum, self.maximum))
        return generation
