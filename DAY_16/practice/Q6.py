# Q6. Addition Function
# Create an add() function and pass it to another function.


def add(a, b):
    return a + b


def calculate(function, a, b):
    return function(a, b)


result = calculate(add, 10, 20)

print("Addition:", result)