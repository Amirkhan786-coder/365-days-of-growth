# DAY 21 — PYTHON ADVANCED
# 30 SEPARATE PRACTICE CODES
# Context Managers, Modules, Type Hints, Dataclasses,
# Lambda, map(), filter(), reduce(), enumerate(), zip(),
# Shallow Copy and Deep Copy


# ------------------------------
# Q1. READ FILE USING CONTEXT MANAGER
# ------------------------------

with open("data.txt", "r") as file:

    content = file.read()

print(content)


# ------------------------------
# Q2. CUSTOM CONTEXT MANAGER
# ------------------------------

class MyContext:

    def __enter__(self):

        print("Entering context")

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        print("Exiting context")


with MyContext():

    print("Inside context")


# ------------------------------
# Q3. START AND FINISH CONTEXT MANAGER
# ------------------------------

class Process:

    def __enter__(self):

        print("Starting process")

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        print("Finished process")


with Process():

    print("Processing data...")


# ------------------------------
# Q4. CONTEXT MANAGER TIMER
# ------------------------------

import time


class Timer:

    def __enter__(self):

        self.start = time.perf_counter()

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        self.end = time.perf_counter()

        print(
            "Execution Time:",
            self.end - self.start,
            "seconds"
        )


with Timer():

    total = 0

    for number in range(1, 1000000):

        total += number

    print("Total:", total)


# ------------------------------
# Q5. @contextmanager
# ------------------------------

from contextlib import contextmanager


@contextmanager
def my_context():

    print("Context started")

    yield

    print("Context finished")


with my_context():

    print("Inside context")


# ------------------------------
# Q6. MATH MODULE
# ------------------------------

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


def multiply(a, b):

    return a * b


def divide(a, b):

    if b == 0:

        return "Cannot divide by zero"

    return a / b


print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))


# ------------------------------
# Q7. IMPORT STYLE EXAMPLE
# ------------------------------

import math


print(
    math.sqrt(25)
)

print(
    math.pow(2, 3)
)


from math import factorial


print(
    factorial(5)
)


# ------------------------------
# Q8. PACKAGE STRUCTURE EXAMPLE
# ------------------------------

# Create this structure:
#
# utilities/
#     __init__.py
#     math_utils.py
#     string_utils.py
#
# math_utils.py:
#
# def add(a, b):
#     return a + b
#
# string_utils.py:
#
# def uppercase(text):
#     return text.upper()
#
# main.py:
#
# from utilities.math_utils import add
# from utilities.string_utils import uppercase
#
# print(add(10, 20))
# print(uppercase("python"))


# ------------------------------
# Q9. IMPORT VS FROM IMPORT
# ------------------------------

import math


print(
    math.sqrt(16)
)


from math import sqrt


print(
    sqrt(16)
)


# ------------------------------
# Q10. __name__ == "__main__"
# ------------------------------

def main():

    print("Program started")

    print("Python Advanced")


if __name__ == "__main__":

    main()


# ------------------------------
# Q11. TYPE HINT — ADDITION
# ------------------------------

def add(
    a: int,
    b: int
) -> int:

    return a + b


result = add(10, 20)

print(result)


# ------------------------------
# Q12. TYPE HINT — AVERAGE
# ------------------------------

def average(
    numbers: list[int]
) -> float:

    return sum(numbers) / len(numbers)


marks = [80, 90, 70, 85]

print(
    average(marks)
)


# ------------------------------
# Q13. TYPE HINT — BOOLEAN
# ------------------------------

def is_adult(
    age: int
) -> bool:

    return age >= 18


print(
    is_adult(20)
)

print(
    is_adult(15)
)


# ------------------------------
# Q14. TYPE HINT — STUDENT DICTIONARY
# ------------------------------

student: dict[str, object] = {

    "name": "Amir",

    "age": 20,

    "marks": 85
}


print(student)


# ------------------------------
# Q15. LONGEST STRING
# ------------------------------

def longest_string(
    words: list[str]
) -> str:

    return max(
        words,
        key=len
    )


words = [
    "Python",
    "Programming",
    "AI",
    "Developer"
]


print(
    longest_string(words)
)


# ------------------------------
# Q16. STUDENT DATACLASS
# ------------------------------

from dataclasses import dataclass


@dataclass
class Student:

    name: str
    age: int
    course: str


student = Student(
    "Amir",
    20,
    "CSE"
)


print(student)


# ------------------------------
# Q17. PRODUCT DATACLASS
# ------------------------------

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
    "Total:",
    product.total_price()
)


# ------------------------------
# Q18. DATACLASS WITH DEFAULT
# ------------------------------

@dataclass
class Employee:

    name: str
    department: str = "IT"
    salary: float = 30000


employee = Employee(
    "Amir"
)


print(employee)


# ------------------------------
# Q19. LIST OF DATACLASS OBJECTS
# ------------------------------

@dataclass
class StudentRecord:

    name: str
    marks: int


students = [

    StudentRecord("Amir", 90),

    StudentRecord("Rahul", 85),

    StudentRecord("Aman", 78),

    StudentRecord("Riya", 92),

    StudentRecord("Neha", 88)
]


for student in students:

    print(
        student.name,
        student.marks
    )


# ------------------------------
# Q20. BANK ACCOUNT DATACLASS
# ------------------------------

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

account.withdraw(1000)


print(
    "Balance:",
    account.balance
)


# ------------------------------
# Q21. LAMBDA — SQUARES
# ------------------------------

numbers = list(
    range(1, 11)
)


squares = list(
    map(
        lambda x: x ** 2,
        numbers
    )
)


print(squares)


# ------------------------------
# Q22. MAP — CELSIUS TO FAHRENHEIT
# ------------------------------

celsius = [
    0,
    10,
    20,
    30,
    40
]


fahrenheit = list(
    map(
        lambda c: (c * 9 / 5) + 32,
        celsius
    )
)


print(fahrenheit)


# ------------------------------
# Q23. FILTER — EVEN NUMBERS
# ------------------------------

numbers = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]


even_numbers = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)


print(even_numbers)


# ------------------------------
# Q24. FILTER — LONG STRINGS
# ------------------------------

words = [
    "Python",
    "AI",
    "Programming",
    "Code",
    "Developer"
]


long_words = list(
    filter(
        lambda word: len(word) > 5,
        words
    )
)


print(long_words)


# ------------------------------
# Q25. REDUCE — PRODUCT
# ------------------------------

from functools import reduce


numbers = [
    1, 2, 3, 4, 5
]


product = reduce(
    lambda a, b: a * b,
    numbers
)


print(product)


# ------------------------------
# Q26. ENUMERATE — STUDENT NAMES
# ------------------------------

names = [
    "Amir",
    "Rahul",
    "Aman",
    "Riya"
]


for number, name in enumerate(
    names,
    start=1
):

    print(
        number,
        name
    )


# ------------------------------
# Q27. ZIP — NAMES AND MARKS
# ------------------------------

names = [
    "Amir",
    "Rahul",
    "Aman"
]

marks = [
    90,
    85,
    88
]


for name, mark in zip(
    names,
    marks
):

    print(
        name,
        mark
    )


# ------------------------------
# Q28. ZIP — CREATE DICTIONARY
# ------------------------------

keys = [
    "name",
    "age",
    "course"
]

values = [
    "Amir",
    20,
    "CSE"
]


student = dict(
    zip(
        keys,
        values
    )
)


print(student)


# ------------------------------
# Q29. SHALLOW VS DEEP COPY
# ------------------------------

import copy


original = [
    [1, 2],
    [3, 4]
]


shallow = copy.copy(
    original
)

deep = copy.deepcopy(
    original
)


original[0][0] = 100


print(
    "Original:",
    original
)

print(
    "Shallow:",
    shallow
)

print(
    "Deep:",
    deep
)


# ------------------------------
# Q30. CLEAN CODE + PEP 8 + DRY
# ------------------------------

def calculate_total(
    price: float,
    quantity: int
) -> float:

    return price * quantity


def display_product(
    name: str,
    price: float,
    quantity: int
):

    total = calculate_total(
        price,
        quantity
    )

    print(
        f"{name}: ₹{total}"
    )


products = [

    ("Laptop", 50000, 1),

    ("Mouse", 1000, 2),

    ("Keyboard", 2000, 1)
]


for name, price, quantity in products:

    display_product(
        name,
        price,
        quantity
    )


