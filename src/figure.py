from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @staticmethod
    def validate_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'{value} must be a number (int or float)')
        if value <= 0:
            raise ValueError(f'{value} must be above zero')
        return value

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f'Argument figure must be instance of Figure class')
        return self.area + figure.area
