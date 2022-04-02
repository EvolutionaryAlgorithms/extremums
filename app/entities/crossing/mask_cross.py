import random
from .crossing import Crossing


class MaskCross(Crossing):
    def __init__(self, father):
        super().__init__()
        self.new_generation = self.__new_generation(father)

    def __init_child(self, mask):
        for j in range(len(mask)):
            if mask[j] == "1":
                self.child1 += self.mom[j]
                self.child2 += self.dad[j]
            elif mask[j] == "0":
                self.child1 += self.dad[j]
                self.child2 += self.mom[j]

    def __new_generation(self, father):
        mask = ""
        for i in range(8):
            mask += "".join(str(random.randrange(0, 2)))
        print("crossing mask: ", mask)
        binary_population = {}
        new_generation = []
        temporary_generation = []
        for i in range(len(father)):
            binary_population[i] = bin(father[i])
        for i in range(0, len(binary_population), 2):
            self.child1 = ""
            self.child2 = ""
            init_child = self.__init_child
            if binary_population[i][0:1] == "-" and binary_population[i + 1][0:1] == "-":
                remove_binary = self.remove_binary_when_minus_minus
                add_binary = self.when_minus_minus
                self.make_crossing(remove_binary, binary_population, i, mask, temporary_generation, init_child, add_binary)
            elif binary_population[i][0:1] == "-" and binary_population[i + 1][0:1] != "-":
                remove_binary = self.remove_binary_when_minus_plus
                add_binary = self.when_minus_plus
                self.make_crossing(remove_binary, binary_population, i, mask, temporary_generation, init_child, add_binary)
            elif binary_population[i][0:1] != "-" and binary_population[i + 1][0:1] == "-":
                remove_binary = self.remove_binary_when_plus_minus
                add_binary = self.when_plus_minus
                self.make_crossing(remove_binary, binary_population, i, mask, temporary_generation, init_child, add_binary)
            else:
                remove_binary = self.remove_binary_when_plus_plus
                add_binary = self.when_plus_plus
                self.make_crossing(remove_binary, binary_population, i, mask, temporary_generation, init_child, add_binary)
        for i in range(len(temporary_generation)):
            new_generation.append(int(temporary_generation[i], 2))
        return new_generation
