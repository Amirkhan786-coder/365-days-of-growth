# Q5. Create an Employee class and a Developer child class.

class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee:", self.name)


class Developer(Employee):

    def code(self):
        print(self.name, "is coding")


developer1 = Developer("Amir")
developer1.display()
developer1.code()