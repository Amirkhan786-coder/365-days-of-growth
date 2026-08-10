# Q21. Multiple Decorators
# Create two decorators and apply both to the same function.


def decorator_one(function):

    def wrapper():

        print("Decorator One")

        function()

    return wrapper


def decorator_two(function):

    def wrapper():

        print("Decorator Two")

        function()

    return wrapper


@decorator_one
@decorator_two
def greet():

    print("Hello!")


greet()