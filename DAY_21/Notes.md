DAY 21 — PYTHON ADVANCED
COMPLETE NOTES

Topics:
Context Managers
Modules & Packages
Type Hints
Dataclasses
Lambda
map()
filter()
reduce()
enumerate()
zip()
Shallow Copy & Deep Copy
Python Best Practices


────────────────────────────────

1. CONTEXT MANAGERS

A context manager is a Python feature used to manage resources
properly.

Common examples:

• Files
• Database connections
• Locks
• Network connections

The most common syntax is:

with


Example:

with open("data.txt", "r") as file:

    data = file.read()

    print(data)

The file is automatically closed after the with block.

This is safer than manually opening and closing a file.


────────────────────────────────

2. WHY USE CONTEXT MANAGERS?

Without a context manager:

file = open("data.txt", "r")

data = file.read()

file.close()


With a context manager:

with open("data.txt", "r") as file:

    data = file.read()


Advantages:

• Automatic resource cleanup
• Cleaner code
• Safer resource management
• Less chance of forgetting close()


────────────────────────────────

3. __enter__() AND __exit__()

A custom context manager can be created using a class.

Example:

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


Usage:

with MyContext():

    print("Inside context")


Output:

Entering context
Inside context
Exiting context


────────────────────────────────

4. contextlib

Python provides the contextlib module to make context managers
easier to create.

Example:

from contextlib import contextmanager


@contextmanager
def my_context():

    print("Starting")

    yield

    print("Ending")


with my_context():

    print("Inside")


The yield separates the setup and cleanup parts.


────────────────────────────────

5. MODULES

A module is a Python file containing reusable code.

Example:

math_utils.py

def add(a, b):

    return a + b


Another file can import it:

import math_utils


print(
    math_utils.add(10, 20)
)


Advantages:

• Code reuse
• Better organization
• Easier maintenance
• Separation of functionality


────────────────────────────────

6. IMPORT STATEMENTS

Import complete module:

import math


Import specific function:

from math import sqrt


Import multiple functions:

from math import sqrt, pow


Create an alias:

import numpy as np


Now we can use:

np.array()


────────────────────────────────

7. __name__

Python provides a special variable:

__name__


When a file is executed directly:

__name__ == "__main__"


Example:

def main():

    print("Program started")


if __name__ == "__main__":

    main()


This allows a Python file to work both as:

• An executable script
• An imported module


────────────────────────────────

8. PACKAGES

A package is a directory containing Python modules.

Example:

project/
│
├── main.py
│
└── utilities/
    │
    ├── __init__.py
    ├── math_utils.py
    └── file_utils.py


Packages help organize large projects.


────────────────────────────────

9. __init__.py

The __init__.py file is traditionally used to mark a directory
as a Python package.

It can also contain package initialization code.

Example:

utilities/
│
├── __init__.py
└── math_utils.py


────────────────────────────────

10. TYPE HINTS

Type hints allow developers to indicate expected data types.

Example:

def add(
    a: int,
    b: int
) -> int:

    return a + b


Here:

a: int

means a should be an integer.

-> int

means the function is expected to return an integer.


────────────────────────────────

11. TYPE HINTS WITH STRINGS

Example:

def greet(
    name: str
) -> str:

    return f"Hello {name}"


Type hints improve:

• Readability
• Code documentation
• IDE support
• Error detection


Type hints do not automatically enforce types at runtime.


────────────────────────────────

12. COMMON TYPE HINTS

int

str

float

bool

list

tuple

dict

set


Example:

def calculate(
    numbers: list[int]
) -> float:

    return sum(numbers) / len(numbers)


────────────────────────────────

13. DATACLASSES

Dataclasses provide an easier way to create classes mainly
used for storing data.

Example:

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


Dataclasses automatically provide useful methods such as
__init__() and __repr__().


────────────────────────────────

14. DATACLASS WITH DEFAULT VALUES

Example:

from dataclasses import dataclass


@dataclass
class Student:

    name: str
    age: int
    course: str = "CSE"


student = Student(
    "Amir",
    20
)


print(student)


The default course will be:

CSE


────────────────────────────────

15. DATACLASS VS NORMAL CLASS

Normal class:

class Student:

    def __init__(
        self,
        name,
        age
    ):

        self.name = name
        self.age = age


Dataclass:

@dataclass
class Student:

    name: str
    age: int


Dataclasses reduce boilerplate code.


────────────────────────────────

16. LAMBDA FUNCTIONS

A lambda is a small anonymous function.

Syntax:

lambda arguments: expression


Example:

square = lambda x: x ** 2


print(
    square(5)
)


Output:

25


Lambda functions are commonly used with:

• map()
• filter()
• sorted()


────────────────────────────────

17. map()

map() applies a function to every item of an iterable.

Example:

numbers = [1, 2, 3, 4, 5]


squares = map(
    lambda x: x ** 2,
    numbers
)


print(
    list(squares)
)


Output:

[1, 4, 9, 16, 25]


────────────────────────────────

18. filter()

filter() selects elements based on a condition.

Example:

numbers = [1, 2, 3, 4, 5, 6]


even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)


print(
    list(even_numbers)
)


Output:

[2, 4, 6]


────────────────────────────────

19. reduce()

reduce() repeatedly combines elements to produce one result.

It is available in functools.

Example:

from functools import reduce


numbers = [1, 2, 3, 4]


result = reduce(
    lambda a, b: a + b,
    numbers
)


print(result)


Output:

10


────────────────────────────────

20. enumerate()

enumerate() provides both index and value while iterating.

Example:

names = [
    "Amir",
    "Rahul",
    "Aman"
]


for index, name in enumerate(names):

    print(
        index,
        name
    )


Output:

0 Amir
1 Rahul
2 Aman


You can start from another index:

for index, name in enumerate(
    names,
    start=1
):

    print(
        index,
        name
    )


────────────────────────────────

21. zip()

zip() combines multiple iterables.

Example:

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


Output:

Amir 90
Rahul 85
Aman 88


────────────────────────────────

22. SHALLOW COPY

A shallow copy creates a new outer object but nested objects
may still be shared.

Example:

import copy


original = [
    [1, 2],
    [3, 4]
]


shallow = copy.copy(
    original
)


The outer list is different, but nested lists can still refer
to the same objects.


────────────────────────────────

23. DEEP COPY

A deep copy creates a completely independent copy including
nested objects.

Example:

import copy


original = [
    [1, 2],
    [3, 4]
]


deep = copy.deepcopy(
    original
)


Changes to nested objects in the deep copy do not affect the
original.


────────────────────────────────

24. SHALLOW COPY VS DEEP COPY

Shallow Copy:

• Copies outer object
• Nested objects may be shared
• Faster in many cases


Deep Copy:

• Recursively copies nested objects
• Creates independent nested structures
• Can use more memory


────────────────────────────────

25. PEP 8

PEP 8 is Python's style guide.

It provides recommendations for writing readable Python code.

Examples:

Use meaningful variable names:

student_name = "Amir"


Instead of:

x = "Amir"


Use proper indentation:

if age >= 18:

    print("Adult")


Avoid unnecessarily long lines.


────────────────────────────────

26. CLEAN CODE

Clean code should be:

• Readable
• Simple
• Organized
• Reusable
• Maintainable


Example:

def calculate_average(numbers):

    return sum(numbers) / len(numbers)


This is better than putting the entire calculation inside a
large block of unrelated code.


────────────────────────────────

27. DRY PRINCIPLE

DRY means:

Don't Repeat Yourself


Instead of writing the same logic multiple times, create a
reusable function.

Bad approach:

print(a + b)

print(c + d)

print(e + f)


Better:

def add(a, b):

    return a + b


────────────────────────────────

28. MEANINGFUL NAMING

Use descriptive names.

Good:

total_marks = 450

student_name = "Amir"

average_score = 90


Poor:

x = 450

n = "Amir"

a = 90


Meaningful names make programs easier to understand.


────────────────────────────────

29. REUSABLE FUNCTIONS

A reusable function should perform a clear task.

Example:

def calculate_average(
    numbers: list[int]
) -> float:

    return sum(numbers) / len(numbers)


The function can be reused anywhere in the project.


────────────────────────────────

30. ADVANCED PYTHON TOOLKIT

Important functions to remember:

enumerate()
→ Index + value

zip()
→ Combine iterables

map()
→ Transform elements

filter()
→ Select elements

reduce()
→ Combine elements into one result

lambda
→ Small anonymous function

iter()
→ Create iterator

next()
→ Get next value

yield
→ Create generator


────────────────────────────────

31. CONTEXT MANAGER QUICK REVISION

with

__enter__()

__exit__()

contextlib

@contextmanager


Purpose:

Resource management


────────────────────────────────

32. MODULE QUICK REVISION

Module:

A Python file containing reusable code.


Important:

import

from ... import

__name__


────────────────────────────────

33. PACKAGE QUICK REVISION

Package:

A directory containing Python modules.


Common structure:

package/
│
├── __init__.py
└── module.py


────────────────────────────────

34. TYPE HINT QUICK REVISION

Example:

def add(
    a: int,
    b: int
) -> int:

    return a + b


Type hints improve readability and development tools.


────────────────────────────────

35. DATACLASS QUICK REVISION

Example:

from dataclasses import dataclass


@dataclass
class Product:

    name: str
    price: float


Dataclasses are useful for data-focused classes.


────────────────────────────────

36. IMPORTANT INTERVIEW DIFFERENCES

Iterable vs Iterator

Iterable:
Can provide an iterator.

Iterator:
Produces the next value.


Iterator vs Generator

Iterator:
Usually created using a class.

Generator:
Usually created using a function with yield.


Shallow Copy vs Deep Copy

Shallow:
Nested objects may be shared.

Deep:
Nested objects are copied independently.


map() vs filter()

map():
Transforms values.

filter():
Selects values.


────────────────────────────────

37. BEST PRACTICES

Always try to:

• Write readable code.
• Use meaningful names.
• Keep functions focused.
• Avoid unnecessary repetition.
• Use comments where useful.
• Handle exceptions properly.
• Use type hints when helpful.
• Organize code into modules.
• Use virtual environments for projects.
• Keep dependencies documented.
• Write a clear README.


────────────────────────────────

38. DAY 21 FINAL REVISION

Context Managers
        ↓
Modules
        ↓
Packages
        ↓
Type Hints
        ↓
Dataclasses
        ↓
Lambda
        ↓
map()
        ↓
filter()
        ↓
reduce()
        ↓
enumerate()
        ↓
zip()
        ↓
Shallow Copy
        ↓
Deep Copy
        ↓
Clean Code
        ↓
PEP 8
        ↓
Python Advanced Complete


────────────────────────────────
