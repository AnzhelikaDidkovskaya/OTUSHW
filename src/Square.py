from src.Figure import Figure


class Square(Figure):

    def __init__(self, name, a):
        super().__init__(name)
        self.a = a

    def calc_area(self):
        return self.a ** 2

    def calc_perimeter(self):
        return self.a * 4

    def add_area(self, figure):
        return self.calc_area() + figure.calc_area()
