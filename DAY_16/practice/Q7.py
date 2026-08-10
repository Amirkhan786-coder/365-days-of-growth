# Q7. Multiplication Function
# Create a multiply() function and execute it through
# another function.


def multiply(a, b):
    return a * b


def execute(function, a, b):
    return function(a, b)


result = execute(multiply, 5, 6)

print("Multiplication:", result)