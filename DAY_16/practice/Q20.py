# Q20. Execution Time
# Create a decorator that measures the execution time
# of a function using the time module.


import time


def performance(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start, "seconds")

        return result

    return wrapper


@performance
def calculate():

    total = 0

    for i in range(1000000):
        total += i

    return total


print("Result:", calculate())