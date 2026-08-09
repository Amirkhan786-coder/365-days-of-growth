# Q23. Implement an abstract method using a Dog class.

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()
dog1.sound()