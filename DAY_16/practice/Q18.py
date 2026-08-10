# Q18. Return Value
# Create a decorator that preserves and returns
# the result of the decorated function.


def decorator(function):

    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs)

        return result

    return wrapper


@decorator
def multiply(a, b):
    return a * b


result = multiply(5, 6)

print("Result:", result)