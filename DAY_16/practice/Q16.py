# Q16. Decorator with **kwargs
# Create a decorator that can handle keyword arguments.


def decorator(function):

    def wrapper(**kwargs):

        print("Keyword Arguments:", kwargs)

        return function(**kwargs)

    return wrapper


@decorator
def introduce(name, age):

    print("Name:", name)
    print("Age:", age)


introduce(name="Amir", age=19)