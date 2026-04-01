from figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        Figure.validate_value(side_a)
        Figure.validate_value(side_b)
        Figure.validate_value(side_c)

        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError(f'Triangle with sides {side_a}, {side_b}, {side_c} does not exist.'
                             f'Each side must be less than sum of two others.')

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def half_perimeter(self):
        return (self.side_a + self.side_b + self.side_c) / 2

    @property
    def area(self):
        p = self.half_perimeter()
        return sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
