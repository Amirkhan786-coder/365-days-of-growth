# Q14. Decorator with Arguments
# Create a decorator that works with a function
# accepting a name.


def decorator(function):

    def wrapper(name):

        print("Function is starting")

        function(name)

        print("Function is finished")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Amir")