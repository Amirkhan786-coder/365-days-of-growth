# Q21. Import a specific function from a custom module.

# File: calculator.py

def add(a, b):
    return a + b


# File: main.py

from calculator import add

result = add(20, 10)

print("Result:", result)