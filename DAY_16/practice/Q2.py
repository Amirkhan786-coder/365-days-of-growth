# Q2. Function as Argument
# Create a square() function and pass it as an argument
# to another function.


def square(number):
    return number * number


def calculate(function, number):
    return function(number)


result = calculate(square, 5)

print("Square:", result)