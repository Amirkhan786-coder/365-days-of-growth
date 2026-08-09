# Q15. Demonstrate polymorphism using a common function.

class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)