import math

from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def create_not_valid_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError('Triangle does not exist')
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError('Triangle does not exist')

    def calc_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def calc_perimeter(self):
        return self.a + self.b + self.c

    def add_area(self, figure):
        return self.calc_area() + figure.calc_area()
