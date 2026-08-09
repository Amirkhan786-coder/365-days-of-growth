# Q8. Demonstrate method overriding using Animal and Dog.

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()
dog1.sound()