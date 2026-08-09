# Q7. Use super() to call a parent class method.

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog1 = Dog()
dog1.sound()