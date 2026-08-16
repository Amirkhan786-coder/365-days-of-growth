# DAY 22 — PYTHON ADVANCED
30 SEPARATE PRACTICE CODES


# ============================================================
# Q1. DIVISION WITH EXCEPTION HANDLING
# ============================================================

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    result = first_number / second_number

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")


# ============================================================
# Q2. HANDLE INVALID INTEGER INPUT
# ============================================================

try:
    number = int(input("Enter an integer: "))

    print("Number:", number)

except ValueError:
    print("Invalid input. Please enter an integer.")


# ============================================================
# Q3. CUSTOM EXCEPTION FOR INVALID MARKS
# ============================================================

class InvalidMarksError(Exception):
    pass


marks = 105

try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )

    print("Valid marks:", marks)

except InvalidMarksError as error:
    print("Error:", error)


# ============================================================
# Q4. TRY, EXCEPT, ELSE AND FINALLY
# ============================================================

try:
    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")


# ============================================================
# Q5. AGE VALIDATION WITH CUSTOM EXCEPTION
# ============================================================

class InvalidAgeError(Exception):
    pass


def validate_age(age: int) -> None:

    if age < 0 or age > 120:
        raise InvalidAgeError(
            "Invalid age."
        )

    print("Valid age:", age)


try:
    validate_age(150)

except InvalidAgeError as error:
    print("Error:", error)


# ============================================================
# Q6. CUSTOM ITERATOR
# ============================================================

class NumberIterator:

    def __init__(self, limit: int):

        self.current = 1
        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current

            self.current += 1

            return value

        raise StopIteration


numbers = NumberIterator(10)

for number in numbers:

    print(number)


# ============================================================
# Q7. GENERATOR FOR EVEN NUMBERS
# ============================================================

def even_numbers(limit: int):

    for number in range(2, limit + 1, 2):

        yield number


for number in even_numbers(20):

    print(number)


# ============================================================
# Q8. FIBONACCI GENERATOR
# ============================================================

def fibonacci(count: int):

    first = 0
    second = 1

    for _ in range(count):

        yield first

        first, second = (
            second,
            first + second
        )


for number in fibonacci(10):

    print(number)


# ============================================================
# Q9. FILE READING GENERATOR
# ============================================================

def read_lines(filename: str):

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            yield line.strip()


# Example:
#
# for line in read_lines("data.txt"):
#     print(line)


# ============================================================
# Q10. SQUARE GENERATOR
# ============================================================

def square_generator():

    for number in range(1, 21):

        yield number ** 2


for square in square_generator():

    print(square)


# ============================================================
# Q11. BASIC DECORATOR
# ============================================================

def message_decorator(function):

    def wrapper():

        print("Function Started")

        function()

        print("Function Finished")

    return wrapper


@message_decorator
def greet():

    print("Hello Python!")


greet()


# ============================================================
# Q12. EXECUTION TIME DECORATOR
# ============================================================

import time


def timer_decorator(function):

    def wrapper():

        start_time = time.perf_counter()

        function()

        end_time = time.perf_counter()

        print(
            "Execution Time:",
            end_time - start_time,
            "seconds"
        )

    return wrapper


@timer_decorator
def calculate():

    total = 0

    for number in range(1, 100000):

        total += number

    print("Total:", total)


calculate()


# ============================================================
# Q13. FUNCTION NAME LOGGER
# ============================================================

def log_function(function):

    def wrapper():

        print(
            "Executing:",
            function.__name__
        )

        return function()

    return wrapper


@log_function
def hello():

    print("Hello!")


hello()


# ============================================================
# Q14. POSITIVE NUMBER DECORATOR
# ============================================================

def positive_only(function):

    def wrapper(number):

        if number <= 0:

            print(
                "Number must be positive."
            )

            return

        return function(number)

    return wrapper


@positive_only
def square(number):

    print(
        "Square:",
        number ** 2
    )


square(5)
square(-2)


# ============================================================
# Q15. FUNCTION CALL COUNTER
# ============================================================

def count_calls(function):

    count = 0

    def wrapper():

        nonlocal count

        count += 1

        print(
            "Call number:",
            count
        )

        return function()

    return wrapper


@count_calls
def say_hello():

    print("Hello!")


say_hello()
say_hello()
say_hello()


# ============================================================
# Q16. CUSTOM FILE CONTEXT MANAGER
# ============================================================

class FileManager:

    def __init__(self, filename, mode):

        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):

        self.file = open(
            self.filename,
            self.mode,
            encoding="utf-8"
        )

        return self.file

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        self.file.close()


with FileManager(
    "example.txt",
    "w"
) as file:

    file.write(
        "Python Advanced"
    )


# ============================================================
# Q17. SIMPLE CONTEXT MANAGER
# ============================================================

class ProcessManager:

    def __enter__(self):

        print("Start")

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        print("End")


with ProcessManager():

    print("Processing...")


# ============================================================
# Q18. @contextmanager
# ============================================================

from contextlib import contextmanager


@contextmanager
def temporary_message():

    print("Temporary state started")

    try:

        yield

    finally:

        print("Original state restored")


with temporary_message():

    print("Inside context")


# ============================================================
# Q19. CALCULATOR MODULE EXAMPLE
# ============================================================

# calculator.py
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b


# main.py
#
# from calculator import add
#
# print(add(10, 20))


# ============================================================
# Q20. PACKAGE EXAMPLE
# ============================================================

# Project structure:
#
# utilities/
#     __init__.py
#     math_utils.py
#     string_utils.py
#
#
# math_utils.py
#
# def add(a, b):
#     return a + b
#
#
# string_utils.py
#
# def uppercase(text):
#     return text.upper()
#
#
# main.py
#
# from utilities.math_utils import add
# from utilities.string_utils import uppercase
#
# print(add(10, 20))
# print(uppercase("python"))


# ============================================================
# Q21. TYPE HINT — MAXIMUM VALUE
# ============================================================

def maximum(
    numbers: list[int]
) -> int:

    return max(numbers)


numbers = [10, 50, 30, 90, 20]

print(
    maximum(numbers)
)


# ============================================================
# Q22. TYPE HINT — STUDENT AVERAGE
# ============================================================

def average_marks(
    students: dict[str, int]
) -> float:

    return sum(
        students.values()
    ) / len(students)


students = {
    "Amir": 90,
    "Rahul": 80,
    "Aman": 70
}


print(
    average_marks(students)
)


# ============================================================
# Q23. STUDENT DATACLASS
# ============================================================

from dataclasses import dataclass


@dataclass
class Student:

    name: str
    marks: list[int]

    def average(self) -> float:

        return sum(self.marks) / len(self.marks)


student = Student(
    "Amir",
    [85, 90, 80, 95]
)


print(
    student.name
)

print(
    student.average()
)


# ============================================================
# Q24. PRODUCT DATACLASS
# ============================================================

@dataclass
class Product:

    name: str
    price: float
    quantity: int

    def total_price(self) -> float:

        return self.price * self.quantity


product = Product(
    "Laptop",
    50000,
    2
)


print(
    product.total_price()
)


# ============================================================
# Q25. BANK ACCOUNT DATACLASS
# ============================================================

@dataclass
class BankAccount:

    account_holder: str
    balance: float = 0

    def deposit(
        self,
        amount: float
    ):

        self.balance += amount

    def withdraw(
        self,
        amount: float
    ):

        if amount > self.balance:

            print("Insufficient balance")

        else:

            self.balance -= amount


account = BankAccount(
    "Amir",
    5000
)


account.deposit(2000)

account.withdraw(1500)


print(
    "Balance:",
    account.balance
)


# ============================================================
# Q26. LAMBDA + MAP — CUBES
# ============================================================

numbers = list(
    range(1, 11)
)


cubes = list(
    map(
        lambda x: x ** 3,
        numbers
    )
)


print(cubes)


# ============================================================
# Q27. FILTER — DIVISIBLE BY 3
# ============================================================

numbers = [
    3, 5, 6, 8, 9,
    12, 14, 15, 20
]


result = list(
    filter(
        lambda x: x % 3 == 0,
        numbers
    )
)


print(result)


# ============================================================
# Q28. REDUCE — SUM
# ============================================================

from functools import reduce


numbers = [
    10, 20, 30, 40
]


total = reduce(
    lambda a, b: a + b,
    numbers
)


print(
    "Total:",
    total
)


# ============================================================
# Q29. ENUMERATE + ZIP
# ============================================================

names = [
    "Amir",
    "Rahul",
    "Aman",
    "Riya"
]

marks = [
    95,
    88,
    82,
    91
]


combined = sorted(
    zip(names, marks),
    key=lambda item: item[1],
    reverse=True
)


for rank, (
    name,
    mark
) in enumerate(
    combined,
    start=1
):

    print(
        rank,
        name,
        mark
    )


# ============================================================
# Q30. FINAL STUDENT RESULT SYSTEM
# ============================================================

from dataclasses import dataclass
from functools import reduce
from contextlib import contextmanager


class InvalidMarksError(Exception):
    pass


@dataclass
class StudentResult:

    name: str
    marks: list[int]

    def total(self) -> int:

        return reduce(
            lambda a, b: a + b,
            self.marks
        )

    def average(self) -> float:

        return self.total() / len(
            self.marks
        )

    def grade(self) -> str:

        average = self.average()

        if average >= 90:
            return "A+"

        elif average >= 80:
            return "A"

        elif average >= 70:
            return "B"

        elif average >= 60:
            return "C"

        elif average >= 50:
            return "D"

        return "F"

    def status(self) -> str:

        if self.average() >= 40:

            return "PASS"

        return "FAIL"


def validate_marks(
    marks: list[int]
) -> None:

    for mark in marks:

        if mark < 0 or mark > 100:

            raise InvalidMarksError(
                "Marks must be between 0 and 100."
            )


@contextmanager
def report_manager(filename: str):

    file = open(
        filename,
        "w",
        encoding="utf-8"
    )

    try:

        yield file

    finally:

        file.close()


students = [

    StudentResult(
        "Amir",
        [90, 85, 88, 92, 95]
    ),

    StudentResult(
        "Rahul",
        [78, 82, 75, 80, 77]
    ),

    StudentResult(
        "Aman",
        [55, 60, 58, 62, 57]
    ),

    StudentResult(
        "Riya",
        [95, 96, 92, 94, 98]
    )
]


try:

    for student in students:

        validate_marks(
            student.marks
        )


    ranked_students = sorted(
        students,
        key=lambda student: student.average(),
        reverse=True
    )


    print(
        "\nSTUDENT RESULT SYSTEM"
    )

    print(
        "-" * 40
    )


    for rank, student in enumerate(
        ranked_students,
        start=1
    ):

        print(
            f"{rank}. "
            f"{student.name} | "
            f"Total: {student.total()} | "
            f"Average: {student.average():.2f} | "
            f"Grade: {student.grade()} | "
            f"Status: {student.status()}"
        )


    passed_students = list(
        filter(
            lambda student: student.status() == "PASS",
            students
        )
    )


    print(
        "\nPASSED STUDENTS:"
    )

    for student in passed_students:

        print(
            student.name
        )


    with report_manager(
        "final_result.txt"
    ) as file:

        file.write(
            "STUDENT RESULT REPORT\n"
        )

        file.write(
            "-" * 40 + "\n"
        )

        for rank, student in enumerate(
            ranked_students,
            start=1
        ):

            file.write(
                f"{rank}. "
                f"{student.name} | "
                f"Total: {student.total()} | "
                f"Average: "
                f"{student.average():.2f} | "
                f"Grade: {student.grade()} | "
                f"Status: {student.status()}\n"
            )


    print(
        "\nReport saved to final_result.txt"
    )


except InvalidMarksError as error:

    print(
        "Error:",
        error
    )

