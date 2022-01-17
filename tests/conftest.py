import pytest

from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(name='Rect', a=2, b=3)
    return rectangle


@pytest.fixture
def default_square():
    square = Square(name='Sc', a=5)
    return square


@pytest.fixture
def default_triangle():
    triangle = Triangle(name='3an', a=10, b=6, c=7)
    return triangle


@pytest.fixture
def default_circle():
    circle = Circle(name='Cir', a=9)
    return circle
