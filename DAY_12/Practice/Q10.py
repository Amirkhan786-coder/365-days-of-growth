# Q10. Multiple Exceptions
# Question:
# Handle ValueError and ZeroDivisionError
# using separate except blocks.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")