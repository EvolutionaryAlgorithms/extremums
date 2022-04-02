import random
from .crossing import Crossing


class TwoPointCross(Crossing):
    def __init__(self, father):
        super().__init__()
        self.new_generation = self.__new_generation(father)

    def __init_child(self, crossing_points):
        for j in range(crossing_points[0]):
            self.child1 += self.mom[j]
            self.child2 += self.dad[j]
        for j in range(crossing_points[0], crossing_points[1]):
            self.child1 += self.dad[j]
            self.child2 += self.mom[j]
        for j in range(crossing_points[1], len(self.dad)):
            self.child1 += self.mom[j]
            self.child2 += self.dad[j]

    def __new_generation(self, father):
        temporary_point_1 = random.randrange(1, 6)
        temporary_point_2 = random.randrange(1, 6)
        while temporary_point_1 == temporary_point_2:
            temporary_point_2 = random.randrange(1, 6)
        crossing_points = [temporary_point_1, temporary_point_2]
        crossing_points.sort()
        print("Cross Points: ", crossing_points)
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
                self.make_crossing(remove_binary, binary_population, i, crossing_points, temporary_generation, init_child, add_binary)
            elif binary_population[i][0:1] == "-" and binary_population[i + 1][0:1] != "-":
                remove_binary = self.remove_binary_when_minus_plus
                add_binary = self.when_minus_plus
                self.make_crossing(remove_binary, binary_population, i, crossing_points, temporary_generation, init_child, add_binary)
            elif binary_population[i][0:1] != "-" and binary_population[i + 1][0:1] == "-":
                remove_binary = self.remove_binary_when_plus_minus
                add_binary = self.when_plus_minus
                self.make_crossing(remove_binary, binary_population, i, crossing_points, temporary_generation, init_child, add_binary)
            else:
                remove_binary = self.remove_binary_when_plus_plus
                add_binary = self.when_plus_plus
                self.make_crossing(remove_binary, binary_population, i, crossing_points, temporary_generation, init_child, add_binary)
        for i in range(len(temporary_generation)):
            new_generation.append(int(temporary_generation[i], 2))
        return new_generation
