from abc import abstractmethod


class Figure:
    def __init__(self, name):
        """Class constructor"""
        self.name = name

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_perimeter(self):
        pass

    @abstractmethod
    def add_area(self, figure):
        pass
