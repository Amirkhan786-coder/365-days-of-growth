# Q35. Create a custom module and use it.

# ============================================
# File: my_module.py
# ============================================

def greet(name):
    return f"Hello, {name}!"


def square(number):
    return number * number


def add(a, b):
    return a + b


# ============================================
# File: main.py
# ============================================

import my_module

name = input("Enter your name: ")
number = int(input("Enter a number: "))

print(my_module.greet(name))
print("Square:", my_module.square(number))
print("Addition:", my_module.add(number, 10))