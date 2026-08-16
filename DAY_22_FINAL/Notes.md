DAY 22 — PYTHON ADVANCED
FINAL REVISION NOTES


1. EXCEPTION HANDLING

Exception handling is used to handle runtime errors without
crashing the complete program.

Basic structure:

try:
    # risky code

except:
    # error handling

else:
    # runs when no exception occurs

finally:
    # always runs


Example:

try:

    number = int(input("Enter a number: "))

    result = 100 / number

    print(result)

except ValueError:

    print("Please enter a valid number.")

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    print("Program finished.")


Important keywords:

try
except
else
finally
raise


2. CUSTOM EXCEPTIONS

We can create our own exception classes.

Example:

class InvalidAgeError(Exception):

    pass


age = 15

if age < 18:

    raise InvalidAgeError(
        "Age must be 18 or above."
    )


3. ITERATORS

An iterator is an object that allows us to access elements
one at a time.

Important methods:

__iter__()
__next__()


Example:

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


Output:

10
20
30


When there are no more elements, next() raises StopIteration.


4. GENERATORS

Generators produce values one at a time instead of storing
all values in memory.

They use the yield keyword.

Example:

def numbers():

    for i in range(1, 6):

        yield i


for number in numbers():

    print(number)


Advantages:

- Memory efficient
- Useful for large datasets
- Values are generated when needed
- Supports lazy evaluation


5. DECORATORS

A decorator modifies or extends the behavior of a function
without changing its original code.

Example:

def decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")

    return wrapper


@decorator
def hello():

    print("Hello Python")


hello()


Common uses:

- Logging
- Authentication
- Timing
- Validation
- Access control


6. CONTEXT MANAGERS

Context managers manage resources safely.

The most common syntax is:

with


Example:

with open(
    "data.txt",
    "r"
) as file:

    content = file.read()


The file is automatically closed after the block.


7. CUSTOM CONTEXT MANAGER

A custom context manager can use:

__enter__()
__exit__()


Example:

class Manager:

    def __enter__(self):

        print("Resource opened")

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        print("Resource closed")


with Manager():

    print("Working...")


8. contextlib

Python provides the contextlib module for creating
context managers more easily.

Example:

from contextlib import contextmanager


@contextmanager
def manager():

    print("Start")

    yield

    print("End")


with manager():

    print("Inside")


9. MODULES

A module is a Python file containing reusable code.

Example:

math_utils.py

def add(a, b):

    return a + b


Importing the module:

import math_utils


print(
    math_utils.add(10, 20)
)


10. FROM IMPORT

A specific function can be imported directly.

Example:

from math import sqrt

print(
    sqrt(25)
)


11. PACKAGES

A package is a collection of related Python modules.

Example:

project/

    utilities/

        __init__.py

        math_utils.py

        string_utils.py


Packages help organize large projects.


12. __name__

Python provides the special variable:

__name__


When a file is executed directly:

__name__ == "__main__"


Example:

def main():

    print("Program started")


if __name__ == "__main__":

    main()


This prevents the main code from automatically running when
the file is imported.


13. TYPE HINTS

Type hints indicate the expected type of data.

Example:

def add(
    a: int,
    b: int
) -> int:

    return a + b


Type hints improve:

- Readability
- Documentation
- IDE support
- Static analysis


Important:

Type hints generally do NOT enforce types at runtime.


14. DATACLASSES

Dataclasses are useful for classes that mainly store data.

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


Advantages:

- Less boilerplate
- Automatic __init__()
- Automatic __repr__()
- Easy data representation
- Works well with type hints


15. LAMBDA FUNCTIONS

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


16. map()

map() applies a function to every item of an iterable.

Example:

numbers = [1, 2, 3, 4, 5]

squares = list(
    map(
        lambda x: x ** 2,
        numbers
    )
)

print(squares)


17. filter()

filter() selects elements according to a condition.

Example:

numbers = [
    1, 2, 3, 4, 5, 6
]

even_numbers = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print(even_numbers)


18. reduce()

reduce() repeatedly combines elements and produces one result.

It is available from functools.

Example:

from functools import reduce


numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)


Output:

15


19. enumerate()

enumerate() provides both the index and value.

Example:

names = [
    "Amir",
    "Rahul",
    "Aman"
]


for index, name in enumerate(
    names,
    start=1
):

    print(
        index,
        name
    )


Output:

1 Amir
2 Rahul
3 Aman


20. zip()

zip() combines elements from multiple iterables.

Example:

names = [
    "Amir",
    "Rahul"
]

marks = [
    90,
    85
]


for name, mark in zip(
    names,
    marks
):

    print(
        name,
        mark
    )


21. SHALLOW COPY

A shallow copy creates a new outer object, but nested objects
may still be shared.

Example:

import copy


original = [
    [1, 2],
    [3, 4]
]


new_list = copy.copy(
    original
)


22. DEEP COPY

A deep copy creates independent copies of nested objects.

Example:

import copy


original = [
    [1, 2],
    [3, 4]
]


new_list = copy.deepcopy(
    original
)


Important difference:

Shallow Copy
→ Outer object copied
→ Nested objects may be shared

Deep Copy
→ Outer object copied
→ Nested objects also copied


23. PEP 8

PEP 8 is Python's style guide.

Important practices:

- Use proper indentation.
- Use meaningful names.
- Use consistent spacing.
- Keep code readable.
- Organize imports.
- Avoid unnecessarily long lines.


Example:

Good:

student_name = "Amir"


Bad:

sn="Amir"


24. DRY PRINCIPLE

DRY means:

Don't Repeat Yourself


Instead of repeating code:

print(price * 2)
print(price * 3)
print(price * 4)


Create reusable logic:

def calculate_price(
    price,
    quantity
):

    return price * quantity


25. CLEAN CODE

Clean code should be:

- Readable
- Simple
- Organized
- Reusable
- Maintainable


Good practices:

- Meaningful variable names
- Small functions
- Avoid unnecessary duplication
- Proper comments
- Clear project structure


26. ADVANCED PYTHON REVISION TABLE

Exception Handling
→ Handle runtime errors

Iterators
→ Access values one at a time

Generators
→ Generate values lazily

Decorators
→ Modify function behavior

Context Managers
→ Manage resources safely

Modules
→ Reusable Python files

Packages
→ Collections of modules

Type Hints
→ Indicate expected data types

Dataclasses
→ Simplify data-focused classes

Lambda
→ Small anonymous functions

map()
→ Transform elements

filter()
→ Select elements

reduce()
→ Combine elements

enumerate()
→ Index + value

zip()
→ Combine iterables

Shallow Copy
→ Nested objects may be shared

Deep Copy
→ Nested objects independently copied

PEP 8
→ Python style guide

DRY
→ Don't Repeat Yourself

Clean Code
→ Readable and maintainable code


27. FINAL PYTHON ADVANCED ROADMAP

Python Basics
      ↓
Functions
      ↓
OOP
      ↓
Exception Handling
      ↓
File Handling
      ↓
Iterators
      ↓
Generators
      ↓
Decorators
      ↓
Context Managers
      ↓
Modules & Packages
      ↓
Type Hints
      ↓
Dataclasses
      ↓
Functional Programming
      ↓
Copying
      ↓
Clean Code
      ↓
Problem Solving
      ↓
Projects


28. FINAL TAKEAWAY

Advanced Python is not only about learning more syntax.

The goal is to write code that is:

Readable
Reusable
Reliable
Maintainable
Efficient
Well organized

The concepts learned across Days 19–22 provide a strong
foundation for moving toward real-world Python development.


