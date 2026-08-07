# Q16. Multiple Exception Handling
# Question:
# Create a program that can generate:
# ValueError
# TypeError
# ZeroDivisionError
# Handle each exception separately.

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:

    print("ValueError: Please enter valid numbers.")

except ZeroDivisionError:

    print("ZeroDivisionError: Cannot divide by zero.")

except TypeError:

    print("TypeError: Invalid data type.")