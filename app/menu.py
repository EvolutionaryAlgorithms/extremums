from .entities.crossing.mask_cross import MaskCross
from .entities.crossing.one_point_cross import OnePointCross
from .entities.crossing.two_point_cross import TwoPointCross
from .modules.extremum_values import ExtremumValues
from .entities.population.blanket import Blanket
from .entities.population.selective import Selective
from .entities.population.shotgun import Shotgun
from .entities.selection.roulette import Roulette
from .entities.selection.tournament import Tournament


class Menu:
    POPULATION = {
        0: "Blanket",
        1: "Selective",
        2: "Shotgun"
    }
    SELECTION = {
        0: "Tournament",
        1: "Roulette"
    }
    CROSSING = {
        0: "OnePointCross",
        1: "TwoPointCross",
        2: "MaskCross"
    }

    def __init__(self):
        self.extremum = 0
        self.population = 0
        self.selection = 0
        self.crossing = 0

    @staticmethod
    def __return_input(input_number):
        if input_number.isdigit():
            input_number = int(input_number)
        return input_number

    def __choose_extremum(self):
        while True:
            print("Select one of the values: ")
            print("Enter:\n\t 0 - You search MINIMUM value\n\t 1 - You search MAXIMUM value")
            inp = self.__return_input(input())
            if inp == 0:
                self.extremum = inp
                print("You search MINIMUM value\n")
                break
            elif inp == 1:
                self.extremum = inp
                print("You search MAXIMUM value\n")
                break
            else:
                print("Wrong argument\n")

    def __choose_population(self):
        while True:
            print("Select one of the values: ")
            print("Enter:\n\t 0 - For BLANKET\n\t 1 - For SELECTIVE\n\t 2 - For SHOTGUN")
            inp = self.__return_input(input())
            if inp == 0:
                self.population = inp
                print("You select BLANKET population\n")
                break
            elif inp == 1:
                self.population = inp
                print("You select SELECTIVE population\n")
                break
            elif inp == 2:
                self.population = inp
                print("You select SHOTGUN population\n")
                break
            else:
                print("Wrong argument\n")

    def __choose_selection(self):
        while True:
            print("Select one of the values: ")
            print("Enter:\n\t 0 - For TOURNAMENT\n\t 1 - For ROULETTE")
            inp = self.__return_input(input())
            if inp == 0:
                self.selection = inp
                print("You select TOURNAMENT selection\n")
                break
            elif inp == 1:
                self.selection = inp
                print("You select ROULETTE selection\n")
                break
            else:
                print("Wrong argument\n")

    def __choose_crossing(self):
        while True:
            print("Select one of the values: ")
            print("Enter:\n\t 0 - For ONE_POINT_CROSS\n\t 1 - For TWO_POINT_CROSS\n\t 2 - For MASK_CROSS")
            inp = self.__return_input(input())
            if inp == 0:
                self.crossing = inp
                print("You select ONE_POINT_CROSS crossing\n")
                break
            elif inp == 1:
                self.crossing = inp
                print("You select TWO_POINT_CROSS crossing\n")
                break
            elif inp == 2:
                self.crossing = inp
                print("You select MASK_CROSS crossing\n")
                break
            else:
                print("Wrong argument\n")

    def __print_value_of_function(self, result):
        if self.extremum:
            print("The MAXIMUM value of function = ", str(result), "\n")
        else:
            print("The MINIMUM value of function = ", str(result), "\n")

    @staticmethod
    def __choose_range():
        while True:
            print("Enter the number of iterations: ")
            inp = input()
            if inp.isdigit():
                print("You enter ", inp, "iterations\n")
                return int(inp)
            else:
                print("Wrong argument\n")

    def main(self):
        extremum_value = ExtremumValues()
        self.__choose_extremum()
        self.__choose_population()
        self.__choose_selection()
        self.__choose_crossing()
        number_of_iterations = self.__choose_range()

        generation = eval(self.POPULATION[self.population])().generation
        print("Initial population: ", generation)
        result = extremum_value.value(generation, self.extremum, print_el=True)
        self.__print_value_of_function(result)

        for i in range(number_of_iterations):
            new_generation = eval(self.CROSSING[self.crossing])(
                eval(self.SELECTION[self.selection])(self.extremum, generation).selection
            ).new_generation
            print(new_generation)

            generation = new_generation
            result = extremum_value.value(generation, self.extremum, print_el=True)
            self.__print_value_of_function(result)
