from .selection import Selection


class Tournament(Selection):
    def __init__(self, target, gen):
        super().__init__()
        self.selection = self.__selection(target, gen)

    def __selection(self, target, gen):
        ext = self.extremum_value.value(gen, target)
        fitness_result = {}
        result = []
        for i in range(len(gen)):
            fitness_result[i] = self.extremum_value.my_func(gen[i]) / ext
        for i in range(0, len(gen) - 1, 2):
            if fitness_result[i] >= fitness_result[i + 1]:
                result.append(gen[i])
            else:
                result.append(gen[i + 1])
        return result
