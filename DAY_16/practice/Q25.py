# Q25. Validation Decorator
# Create a decorator that checks whether a number
# is positive before executing the function.


def positive_only(function):

    def wrapper(number):

        if number > 0:
            return function(number)

        print("Number must be positive.")

    return wrapper


@positive_only
def square(number):

    print("Square:", number * number)


square(5)
square(-2)