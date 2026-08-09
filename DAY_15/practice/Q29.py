# Q29. Create an Employee system using Developer and Designer classes.

class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working")


class Developer(Employee):

    def work(self):
        print(self.name, "is developing software")


class Designer(Employee):

    def work(self):
        print(self.name, "is designing UI")


developer = Developer("Amir")
designer = Designer("Rahul")

developer.work()
designer.work()