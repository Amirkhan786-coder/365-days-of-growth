# Q11. Basic Decorator
# Create a decorator that prints:
# Before Function
# After Function
# around another function.


def decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper


@decorator
def greet():
    print("Hello!")


greet()