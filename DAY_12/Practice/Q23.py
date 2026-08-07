# Q23. Exception Propagation
# Question:
# Create a function that generates an exception.
# Do not handle the exception inside the function.
# Handle it in the calling code.

def divide():

    number = 10 / 0

    return number


try:

    divide()

except ZeroDivisionError:

    print("Exception handled outside the function.")