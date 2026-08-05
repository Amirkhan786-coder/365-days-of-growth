# Question:
# Create a custom module named 'calculator.py' with add(), subtract(),
# multiply(), and divide() functions, then use all functions in main.py.

# calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by Zero is not Allowed!"
    return a / b