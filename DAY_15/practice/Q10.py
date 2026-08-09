# Q10. Demonstrate multilevel inheritance using Grandparent -> Parent -> Child.

class Grandparent:

    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):

    def car(self):
        print("Parent's car")


class Child(Parent):

    def bike(self):
        print("Child's bike")


child1 = Child()

child1.house()
child1.car()
child1.bike()