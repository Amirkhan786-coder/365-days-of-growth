# Q17. Flexible Decorator
# Create a decorator using both *args and **kwargs.


def decorator(function):

    def wrapper(*args, **kwargs):

        print("Function started")

        result = function(*args, **kwargs)

        print("Function completed")

        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print("Result:", add(10, 20))