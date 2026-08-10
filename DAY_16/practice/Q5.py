# Q5. Higher-Order Function
# Create a higher-order function that accepts a function
# and a number, then applies the function to the number.


def double(number):
    return number * 2


def apply_function(function, value):
    return function(value)


result = apply_function(double, 10)

print("Result:", result)