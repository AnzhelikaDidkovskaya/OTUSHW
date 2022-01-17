from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    def calc_area(self):
        return self.a * self.b

    def calc_perimeter(self):
        return (self.a + self.b) * 2

    def add_area(self, figure):
        return self.calc_area() + figure.calc_area()
