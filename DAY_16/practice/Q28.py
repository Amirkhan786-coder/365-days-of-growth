# Q28. Logging to File
# Create a decorator that writes the function name
# and arguments to logs.txt.


from functools import wraps


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        with open("logs.txt", "a") as file:

            file.write(
                f"Function: {function.__name__}\n"
            )

            file.write(
                f"Arguments: {args}, {kwargs}\n"
            )

        return function(*args, **kwargs)

    return wrapper


@logger
def greet(name):

    print("Hello", name)


greet("Amir")

print("Log saved successfully.")