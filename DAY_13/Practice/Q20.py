# Q20. Create and use a custom module.

# File: calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# File: main.py

import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))