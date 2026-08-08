# Q34. Create a utility module.

# File: utils.py

def square(number):
    return number * number


def cube(number):
    return number * number * number


def is_even(number):
    return number % 2 == 0


# File: main.py

import utils

print("Square:", utils.square(5))
print("Cube:", utils.cube(3))
print("Is Even:", utils.is_even(10))