# Q15. Decorator with *args
# Create a decorator that can handle any number
# of positional arguments.


def decorator(function):

    def wrapper(*args):

        print("Arguments:", args)

        return function(*args)

    return wrapper


@decorator
def add(a, b, c):
    return a + b + c


result = add(10, 20, 30)

print("Result:", result)