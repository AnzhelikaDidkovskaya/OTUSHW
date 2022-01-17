from src.Figure import Figure


class Circle(Figure):
    pi = 3.14

    def __init__(self, name, a):
        super().__init__(name)
        self.a = a

    def calc_area(self):
        return (self.a * self.a) * self.pi

    def calc_perimeter(self):
        return self.a * self.pi * 2

    def add_area(self, figure):
        return self.calc_area() + figure.calc_area()
