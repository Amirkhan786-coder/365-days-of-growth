# Q24. Create an abstract Shape class and implement Circle.

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


circle1 = Circle(5)

print("Area:", circle1.area())