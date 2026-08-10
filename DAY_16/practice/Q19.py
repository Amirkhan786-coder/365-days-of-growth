# Q19. Addition Decorator
# Create a decorator for an addition function.
# The decorator should print "Calculating..."
# before the calculation.


def calculation_message(function):

    def wrapper(*args, **kwargs):

        print("Calculating...")

        result = function(*args, **kwargs)

        print("Calculation completed.")

        return result

    return wrapper


@calculation_message
def add(a, b):
    return a + b


print("Answer:", add(20, 30))