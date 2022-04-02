class ExtremumValues:
    def value(self, gen, ext, print_el=False):
        element = gen[0]
        ext_value = self.my_func(element)
        for i in range(len(gen)):
            value = self.my_func(gen[i])
            if ext:
                if ext_value < value:
                    ext_value = value
                    element = gen[i]
            else:
                if ext_value > value:
                    ext_value = value
                    element = gen[i]
        if print_el:
            print("Element: ", element)
        return ext_value

    @staticmethod
    def my_func(person):
        value = -1 * ((person ** 2) - 4 * person + 15)**2 / 256

        return value
