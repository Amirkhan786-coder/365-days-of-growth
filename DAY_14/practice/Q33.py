# Calculate Average Marks

class Student:

    def __init__(self, name, python, math, english):
        self.name = name
        self.python = python
        self.math = math
        self.english = english

    def calculate_average(self):
        average = (self.python + self.math + self.english) / 3
        return average


student1 = Student("Amir", 85, 90, 80)

print("Name:", student1.name)
print("Average Marks:", student1.calculate_average())