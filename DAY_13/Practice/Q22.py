# Q22. Nested try-except
# Question:
# Create a program with an outer try-except
# and an inner try-except.
# Handle different exceptions at different levels.

try:

    number = int(input("Enter a number: "))

    try:

        result = 100 / number

        print("Result:", result)

    except ZeroDivisionError:

        print("Cannot divide by zero.")

except ValueError:

    print("Please enter a valid integer.")