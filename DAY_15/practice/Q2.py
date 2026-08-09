# Q2. Create a Dog class that inherits from Animal.

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()
dog1.eat()
dog1.bark()