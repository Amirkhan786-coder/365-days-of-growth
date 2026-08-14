# DAY 20 — PYTHON ADVANCED
# ITERATORS + GENERATORS + DECORATORS
# 30 SEPARATE PRACTICE CODES


# ------------------------------
# Q1. CREATE AN ITERATOR FROM A LIST
# ------------------------------

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ------------------------------
# Q2. ITERATE OVER A TUPLE
# ------------------------------

numbers = (10, 20, 30, 40)

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# ------------------------------
# Q3. HANDLE StopIteration
# ------------------------------

numbers = [1, 2, 3]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        print("Iterator exhausted.")
        break


# ------------------------------
# Q4. CUSTOM ITERATOR — 1 TO 10
# ------------------------------

class Count:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.end:

            value = self.current
            self.current += 1

            return value

        raise StopIteration


counter = Count(1, 10)

for number in counter:
    print(number)


# ------------------------------
# Q5. CUSTOM ITERATOR — EVEN NUMBERS
# ------------------------------

class EvenNumbers:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        while self.current <= self.end:

            number = self.current
            self.current += 1

            if number % 2 == 0:
                return number

        raise StopIteration


numbers = EvenNumbers(1, 20)

for number in numbers:
    print(number)


# ------------------------------
# Q6. CUSTOM ITERATOR — SQUARES
# ------------------------------

class Squares:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current ** 2
            self.current += 1

            return value

        raise StopIteration


squares = Squares(10)

for value in squares:
    print(value)


# ------------------------------
# Q7. CUSTOM ITERATOR — COUNTDOWN
# ------------------------------

class Countdown:

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= 1:

            value = self.current
            self.current -= 1

            return value

        raise StopIteration


countdown = Countdown(10)

for number in countdown:
    print(number)


# ------------------------------
# Q8. STRING ITERATOR
# ------------------------------

text = "Python"

iterator = iter(text)

while True:
    try:
        print(next(iterator))

    except StopIteration:
        break


# ------------------------------
# Q9. DICTIONARY KEY ITERATOR
# ------------------------------

student = {
    "name": "Amir",
    "age": 20,
    "course": "CSE"
}

iterator = iter(student)

while True:
    try:
        key = next(iterator)
        print(key)

    except StopIteration:
        break


# ------------------------------
# Q10. CHECK WHETHER OBJECT IS ITERABLE
# ------------------------------

from collections.abc import Iterable

items = [
    [1, 2, 3],
    (1, 2, 3),
    "Python",
    100
]

for item in items:

    if isinstance(item, Iterable):
        print(item, "is iterable")

    else:
        print(item, "is not iterable")


# ------------------------------
# Q11. GENERATOR — 1 TO 10
# ------------------------------

def numbers():

    for number in range(1, 11):
        yield number


for number in numbers():
    print(number)


# ------------------------------
# Q12. GENERATOR — EVEN NUMBERS
# ------------------------------

def even_numbers():

    for number in range(1, 21):

        if number % 2 == 0:
            yield number


for number in even_numbers():
    print(number)


# ------------------------------
# Q13. GENERATOR — SQUARES
# ------------------------------

def squares():

    for number in range(1, 11):
        yield number ** 2


for value in squares():
    print(value)


# ------------------------------
# Q14. GENERATOR — CUBES
# ------------------------------

def cubes():

    for number in range(1, 11):
        yield number ** 3


for value in cubes():
    print(value)


# ------------------------------
# Q15. FIBONACCI GENERATOR
# ------------------------------

def fibonacci(limit):

    a = 0
    b = 1

    for _ in range(limit):

        yield a

        a, b = b, a + b


for number in fibonacci(10):
    print(number)


# ------------------------------
# Q16. INFINITE GENERATOR
# ------------------------------

def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1


numbers = infinite_numbers()

for _ in range(10):
    print(next(numbers))


# ------------------------------
# Q17. FILE READING GENERATOR
# ------------------------------

def read_file(filename):

    with open(filename, "r") as file:

        for line in file:
            yield line.strip()


# Example:
# for line in read_file("data.txt"):
#     print(line)


# ------------------------------
# Q18. GENERATOR — POSITIVE NUMBERS
# ------------------------------

def positive_numbers(numbers):

    for number in numbers:

        if number > 0:
            yield number


values = [-5, 10, -2, 20, 0, 30]

for number in positive_numbers(values):
    print(number)


# ------------------------------
# Q19. GENERATOR — EVEN NUMBERS
# ------------------------------

def even_numbers(numbers):

    for number in numbers:

        if number % 2 == 0:
            yield number


values = [1, 2, 3, 4, 5, 6, 7, 8]

for number in even_numbers(values):
    print(number)


# ------------------------------
# Q20. GENERATOR EXPRESSION
# ------------------------------

squares = (
    number ** 2
    for number in range(1, 21)
)

for value in squares:
    print(value)


# ------------------------------
# Q21. BASIC DECORATOR
# ------------------------------

def start_message(function):

    def wrapper():

        print("Function Started")

        function()

    return wrapper


@start_message
def greet():

    print("Hello!")


greet()


# ------------------------------
# Q22. COMPLETION DECORATOR
# ------------------------------

def completion_message(function):

    def wrapper():

        function()

        print("Function Completed")

    return wrapper


@completion_message
def greet():

    print("Hello!")


greet()


# ------------------------------
# Q23. FUNCTION NAME DECORATOR
# ------------------------------

def show_function_name(function):

    def wrapper(*args, **kwargs):

        print(
            "Function:",
            function.__name__
        )

        return function(
            *args,
            **kwargs
        )

    return wrapper


@show_function_name
def add(a, b):

    return a + b


print(add(10, 20))


# ------------------------------
# Q24. DECORATOR WITH *args AND **kwargs
# ------------------------------

def decorator(function):

    def wrapper(*args, **kwargs):

        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)

        return function(
            *args,
            **kwargs
        )

    return wrapper


@decorator
def introduce(name, age):

    print(
        f"My name is {name} and I am {age} years old."
    )


introduce(
    "Amir",
    age=20
)


# ------------------------------
# Q25. TIMER DECORATOR
# ------------------------------

import time


def timer(function):

    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(
            *args,
            **kwargs
        )

        end = time.perf_counter()

        print(
            "Execution Time:",
            end - start,
            "seconds"
        )

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for number in range(1, 1000000):
        total += number

    return total


print(
    "Result:",
    calculate()
)


# ------------------------------
# Q26. LOGGING DECORATOR
# ------------------------------

def logger(function):

    def wrapper(*args, **kwargs):

        print(
            "Calling:",
            function.__name__
        )

        print(
            "Arguments:",
            args
        )

        result = function(
            *args,
            **kwargs
        )

        print(
            "Result:",
            result
        )

        return result

    return wrapper


@logger
def multiply(a, b):

    return a * b


multiply(5, 10)


# ------------------------------
# Q27. CONDITIONAL DECORATOR
# ------------------------------

def require_positive(function):

    def wrapper(number):

        if number > 0:

            return function(number)

        print(
            "Number must be positive."
        )

    return wrapper


@require_positive
def square(number):

    print(
        "Square:",
        number ** 2
    )


square(5)
square(-5)


# ------------------------------
# Q28. REPEAT FUNCTION THREE TIMES
# ------------------------------

def repeat_three(function):

    def wrapper(*args, **kwargs):

        for _ in range(3):

            function(
                *args,
                **kwargs
            )

    return wrapper


@repeat_three
def greet(name):

    print(
        "Hello",
        name
    )


greet("Amir")


# ------------------------------
# Q29. MULTIPLE DECORATORS
# ------------------------------

def first(function):

    def wrapper():

        print("First decorator")

        function()

    return wrapper


def second(function):

    def wrapper():

        print("Second decorator")

        function()

    return wrapper


@first
@second
def greet():

    print("Hello")


greet()


# ------------------------------
# Q30. GENERATOR + DECORATOR + COUNTER
# ------------------------------

from collections import Counter
from functools import wraps


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(
            "\nStarting:",
            function.__name__
        )

        result = function(
            *args,
            **kwargs
        )

        print(
            "Completed:",
            function.__name__
        )

        return result

    return wrapper


def number_generator(limit):

    for number in range(1, limit + 1):
        yield number


@logger
def process_numbers(limit):

    numbers = number_generator(limit)

    counter = Counter()

    for number in numbers:

        print(
            "Generated:",
            number
        )

        counter["numbers"] += 1

        if number % 2 == 0:
            counter["even"] += 1

        else:
            counter["odd"] += 1

    return counter


result = process_numbers(10)

print("\nFinal Count:")

print(
    "Total:",
    result["numbers"]
)

print(
    "Even:",
    result["even"]
)

print(
    "Odd:",
    result["odd"]
)