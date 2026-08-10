# Q24. Repeat Decorator
# Create a decorator that executes a function
# a specified number of times.


def repeat(times):

    def decorator(function):

        def wrapper():

            for i in range(times):
                function()

        return wrapper

    return decorator


@repeat(3)
def hello():

    print("Hello!")


hello()