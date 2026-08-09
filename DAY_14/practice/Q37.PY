# Circle

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


circle1 = Circle(7)

print("Radius:", circle1.radius)
print("Area:", circle1.area())