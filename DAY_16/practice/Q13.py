# Q13. Logging Decorator
# Create a decorator that prints the name of the function
# whenever it is called.


def logger(function):

    def wrapper():

        print("Function called:", function.__name__)

        function()

    return wrapper


@logger
def greet():
    print("Hello!")


greet()