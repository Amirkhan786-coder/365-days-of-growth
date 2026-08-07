# Q11. Safe Division Function
# Question:
# Create a function divide(a, b).
# Return the result when division is valid.
# Handle division by zero.

def divide(a, b):

    try:
        result = a / b
        return result

    except ZeroDivisionError:
        return "Cannot divide by zero."


print(divide(10, 2))
print(divide(10, 0))