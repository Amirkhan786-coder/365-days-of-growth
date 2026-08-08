# Q23. Use alias with a custom module.

# File: calculator.py

def square(number):
    return number * number


# File: main.py

import calculator as calc

print("Square:", calc.square(8))