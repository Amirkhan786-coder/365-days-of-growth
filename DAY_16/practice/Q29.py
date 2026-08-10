# Q29. Performance Monitor
# Create a decorator that:
# 1. Records start time
# 2. Executes the function
# 3. Records end time
# 4. Calculates execution time
# 5. Prints execution time


import time
from functools import wraps


def performance(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        execution_time = end - start

        print(
            "Execution Time:",
            execution_time,
            "seconds"
        )

        return result

    return wrapper


@performance
def calculate():

    total = 0

    for i in range(1000000):
        total += i

    return total


print("Result:", calculate())