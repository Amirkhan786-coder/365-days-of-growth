# Q27. functools.wraps
# Create a decorator using functools.wraps and preserve
# the original function's name and docstring.


from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        return function(*args, **kwargs)

    return wrapper


@decorator
def greet():

    """This function greets the user."""

    print("Hello!")


greet()

print("Function Name:", greet.__name__)
print("Docstring:", greet.__doc__)