import random
from .selection import Selection


class Roulette(Selection):
    def __init__(self, target, gen):
        super().__init__()
        self.selection = self.__selection(target, gen)

    @staticmethod
    def __get_key(val, dictionary):
        for key, value in dictionary.items():
            if val == value:
                return key

        return "key doesn't exist"

    def __selection(self, target, gen):
        ext_value = self.extremum_value.value(gen, target)
        fitness_result = {}
        result = []
        for i in range(len(gen)):
            fitness_result[i] = self.extremum_value.my_func(gen[i]) / ext_value
        fitness_result_sorted = sorted(fitness_result.values(), reverse=True)
        length = int(len(gen) / 2)
        for j in range(length):
            choice = random.uniform(fitness_result_sorted[len(fitness_result_sorted) - 1], 1.0)
            for i in range(len(gen)):
                if i == len(gen) - 1:
                    if fitness_result_sorted[i] >= choice >= fitness_result_sorted[len(fitness_result_sorted) - 1]:
                        key = self.__get_key(fitness_result_sorted[i], fitness_result)
                        result.append(gen[key])
                else:
                    if fitness_result_sorted[i] >= choice >= fitness_result_sorted[i + 1]:
                        key = self.__get_key(fitness_result_sorted[i], fitness_result)
                        result.append(gen[key])
        return result
