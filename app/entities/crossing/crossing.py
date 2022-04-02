import random


class Crossing:
    def __init__(self):
        self.dad = ""
        self.mom = ""
        self.child1 = ""
        self.child2 = ""

    def remove_binary_when_minus_minus(self, binary_population, i):
        self.dad = binary_population[i][3:].zfill(8)
        self.mom = binary_population[i + 1][3:].zfill(8)

    def remove_binary_when_minus_plus(self, binary_population, i):
        self.dad = binary_population[i][3:].zfill(8)
        self.mom = binary_population[i + 1][2:].zfill(8)

    def remove_binary_when_plus_minus(self, binary_population, i):
        self.dad = binary_population[i][2:].zfill(8)
        self.mom = binary_population[i + 1][3:].zfill(8)

    def remove_binary_when_plus_plus(self, binary_population, i):
        self.dad = binary_population[i][2:].zfill(8)
        self.mom = binary_population[i + 1][2:].zfill(8)

    def when_minus_minus(self):
        self.dad = "-0b" + self.dad
        self.mom = "-0b" + self.mom
        self.child1 = "-0b" + self.child1
        self.child2 = "-0b" + self.child2

    def when_minus_plus(self):
        self.dad = "-0b" + self.dad
        self.mom = "0b" + self.mom
        self.child1 = "0b" + self.child1
        self.child2 = "-0b" + self.child2

    def when_plus_minus(self):
        self.dad = "0b" + self.dad
        self.mom = "-0b" + self.mom
        self.child1 = "-0b" + self.child1
        self.child2 = "0b" + self.child2

    def when_plus_plus(self):
        self.dad = "0b" + self.dad
        self.mom = "0b" + self.mom
        self.child1 = "0b" + self.child1
        self.child2 = "0b" + self.child2

    def make_crossing(self, remove_binary, binary_population, i, cross, temporary_generation, init_child, add_binary):
        remove_binary(binary_population, i)
        init_child(cross)
        self.__mutate_person()
        add_binary()
        self.__append_generation(temporary_generation)

    def __append_generation(self, generation):
        generation.append(self.dad)
        generation.append(self.mom)
        generation.append(self.child1)
        generation.append(self.child2)
        print("mom: ", self.mom, "dad: ", self.dad, "\tchild1: ", self.child1, "child2: ", self.child2)

    def __mutate_person(self):
        person = random.randrange(0, 4)
        if person == 0:
            self.dad = self.__mutate(self.dad)
        elif person == 1:
            self.mom = self.__mutate(self.mom)
        elif person == 2:
            self.child1 = self.__mutate(self.child1)
        elif person == 3:
            self.child2 = self.__mutate(self.child2)

    @staticmethod
    def __mutate(person):
        position = random.randrange(0, 7)
        temp_person = ""
        for i in range(len(person)):
            if i == position and person[i] == '1':
                temp_person += "".join('0')

            elif i == position and person[i] == '0':
                temp_person += "".join('1')
            else:
                temp_person += "".join(person[i])
        return temp_person
