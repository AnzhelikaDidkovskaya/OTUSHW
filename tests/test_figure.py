import pytest

from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize('triangle', [
    (Triangle(name='3an', a=0, b=0, c=0)),
    (Triangle(name='3an', a=0, b=10, c=20)),
    (Triangle(name='3an', a=11, b=0, c=22)),
    (Triangle(name='3an', a=111, b=222, c=0)),
    (Triangle(name='3an', a=-9, b=-46, c=-23)),
    (Triangle(name='3an', a=-10, b=6, c=3)),
    (Triangle(name='3an', a=12, b=-3, c=13)),
    (Triangle(name='3an', a=15, b=64, c=-4)),
    (Triangle(name='3an', a=2, b=1, c=7)),
    (Triangle(name='3an', a=4, b=17, c=5)),
    (Triangle(name='3an', a=30, b=9, c=8)),
    (Triangle(name='3an', a=14, b=15, c=29)),
    (Triangle(name='3an', a=15, b=31, c=16)),
    (Triangle(name='3an', a=35, b=17, c=18)),
])
def test_triangle_not_exist(triangle):
    with pytest.raises(ValueError):
        triangle.create_not_valid_triangle()


def test_calc_area_rectangle(default_rectangle):
    default_rectangle.calc_area()
    assert default_rectangle.calc_area() == 6


def test_calc_perimeter_rectangle(default_rectangle):
    default_rectangle.calc_perimeter()
    assert default_rectangle.calc_perimeter() == 10


def test_calc_area_square(default_square):
    default_square.calc_area()
    assert default_square.calc_area() == 25


def test_calc_perimeter_square(default_square):
    default_square.calc_perimeter()
    assert default_square.calc_perimeter() == 20


def test_calc_area_triangle(default_triangle):
    default_triangle.calc_area()
    assert default_triangle.calc_area() == 20.662465970933866


def test_calc_perimeter_triangle(default_triangle):
    default_triangle.calc_perimeter()
    assert default_triangle.calc_perimeter() == 23


def test_calc_area_circle(default_circle):
    default_circle.calc_area()
    assert default_circle.calc_area() == 254.34


def test_calc_perimeter_circle(default_circle):
    default_circle.calc_perimeter()
    assert default_circle.calc_perimeter() == 56.52


@pytest.mark.parametrize('area_figure1, area_figure2, sum_area', [
    (Rectangle(name='Rect', a=2, b=3), Square(name='Sc', a=5), 31),
    (Rectangle(name='Rect', a=2, b=3), Triangle(name='3an', a=10, b=6, c=7), 26.662465970933866),
    (Rectangle(name='Rect', a=2, b=3), Circle(name='Cir', a=9), 260.34000000000003),
    (Rectangle(name='Rect', a=2, b=3), Rectangle(name='Rect', a=2, b=3), 12),
    (Square(name='Sc', a=5), Triangle(name='3an', a=10, b=6, c=7), 45.662465970933866),
    (Square(name='Sc', a=5), Circle(name='Cir', a=9), 279.34000000000003),
    (Square(name='Sc', a=5), Square(name='Sc', a=5), 50),
    (Triangle(name='3an', a=10, b=6, c=7), Circle(name='Cir', a=9), 275.0024659709339),
    (Triangle(name='3an', a=10, b=6, c=7), Triangle(name='3an', a=10, b=6, c=7), 41.32493194186773),
    (Circle(name='Cir', a=9), Circle(name='Cir', a=9), 508.68)
])
def test_add_area(area_figure1, area_figure2, sum_area):
    if not isinstance(area_figure1, Figure):
        raise ValueError('The Object' + ' \'' + area_figure1 + '\' ' + 'is not an instance of the class "Figure"')
    elif not isinstance(area_figure2, Figure):
        raise ValueError('The Object' + ' \'' + area_figure2 + '\' ' + 'is not an instance of the class "Figure"')
    else:
        area_figure1.add_area(area_figure2)
        assert area_figure1.add_area(area_figure2) == sum_area
        print(area_figure1.add_area(area_figure2))
