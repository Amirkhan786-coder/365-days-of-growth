from functools import wraps
from collections import Counter
import time


# ------------------------------
# LOGGER DECORATOR
# ------------------------------

def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("\nFunction Started:", function.__name__)

        print("Arguments:", args)

        result = function(
            *args,
            **kwargs
        )

        print("Function Completed:", function.__name__)

        print("Result:", result)

        return result

    return wrapper


# ------------------------------
# TIMER DECORATOR
# ------------------------------

def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(
            *args,
            **kwargs
        )

        end = time.perf_counter()

        execution_time = end - start

        print(
            f"Execution Time: {execution_time:.6f} seconds"
        )

        return result

    return wrapper


# ------------------------------
# POSITIVE NUMBER VALIDATOR
# ------------------------------

def validate_positive(function):

    @wraps(function)
    def wrapper(numbers):

        if not numbers:

            raise ValueError(
                "Numbers list cannot be empty."
            )

        for number in numbers:

            if not isinstance(number, (int, float)):

                raise TypeError(
                    "Only numbers are allowed."
                )

            if number <= 0:

                raise ValueError(
                    "All numbers must be positive."
                )

        return function(numbers)

    return wrapper


# ------------------------------
# NUMBER GENERATOR
# ------------------------------

def number_generator(numbers):

    for number in numbers:

        print(
            "Generated:",
            number
        )

        yield number


# ------------------------------
# PROCESS NUMBERS
# ------------------------------

@logger
@timer
@validate_positive
def process_numbers(numbers):

    counter = Counter()

    total_sum = 0

    minimum = None

    maximum = None

    for number in number_generator(numbers):

        counter["total"] += 1

        total_sum += number

        if number % 2 == 0:

            counter["even"] += 1

        else:

            counter["odd"] += 1

        if minimum is None or number < minimum:

            minimum = number

        if maximum is None or number > maximum:

            maximum = number

    total = counter["total"]

    average = total_sum / total

    return {
        "total": total,
        "even": counter["even"],
        "odd": counter["odd"],
        "sum": total_sum,
        "average": average,
        "minimum": minimum,
        "maximum": maximum
    }


# ------------------------------
# DISPLAY REPORT
# ------------------------------

def display_report(statistics):

    print("\n")
    print("SMART FUNCTION TOOLKIT")
    print("-" * 30)

    print(
        "Total Numbers:",
        statistics["total"]
    )

    print(
        "Even Numbers:",
        statistics["even"]
    )

    print(
        "Odd Numbers:",
        statistics["odd"]
    )

    print(
        "Sum:",
        statistics["sum"]
    )

    print(
        "Average:",
        statistics["average"]
    )

    print(
        "Minimum:",
        statistics["minimum"]
    )

    print(
        "Maximum:",
        statistics["maximum"]
    )


# ------------------------------
# MAIN PROGRAM
# ------------------------------

def main():

    print("SMART FUNCTION TOOLKIT")

    print("-" * 30)

    numbers = [10, 15, 20, 25, 30]

    try:

        statistics = process_numbers(numbers)

        display_report(statistics)

    except ValueError as error:

        print(
            "Validation Error:",
            error
        )

    except TypeError as error:

        print(
            "Type Error:",
            error
        )


# ------------------------------
# PROGRAM START
# ------------------------------

if __name__ == "__main__":

    main()