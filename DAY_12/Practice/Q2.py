# Q2. Handle ZeroDivisionError
# Question:
# Take two numbers from the user and divide them.
# Handle division by zero.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")