# Q12. Greeting Decorator
# Create a decorator that prints "Welcome!"
# before executing a greeting function.


def welcome_decorator(function):

    def wrapper():

        print("Welcome!")

        function()

    return wrapper


@welcome_decorator
def greet():
    print("Hello, Amir!")


greet()