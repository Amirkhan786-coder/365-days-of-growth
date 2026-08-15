DAY 21 — PYTHON ADVANCED
30 INTERVIEW QUESTIONS


Q1. What is a context manager in Python?

Answer:

A context manager manages resources and ensures that cleanup
operations are performed properly.

The most common syntax is:

with


Example:

with open("data.txt", "r") as file:

    data = file.read()


Q2. Why is the with statement useful?

Answer:

The with statement automatically handles resource cleanup.

For example, when working with a file, it automatically closes
the file after the with block finishes.


Q3. What are __enter__() and __exit__()?

Answer:

They are special methods used to create custom context
managers.

__enter__():

Runs when entering the with block.

__exit__():

Runs when leaving the with block.


Q4. How can you create a context manager using contextlib?

Answer:

The contextlib module provides the @contextmanager decorator.

Example:

from contextlib import contextmanager


@contextmanager
def manager():

    print("Start")

    yield

    print("End")


Q5. What happens if an exception occurs inside a context
manager?

Answer:

The __exit__() method is called, allowing the context manager
to perform cleanup.

Depending on how __exit__() is implemented, the exception can
either be propagated or suppressed.


Q6. What is a Python module?

Answer:

A module is a Python file containing reusable code such as
functions, classes, and variables.

Example:

math_utils.py


Q7. What is a Python package?

Answer:

A package is a directory used to organize related Python
modules.

Example:

project/
    utilities/
        __init__.py
        math_utils.py
        file_utils.py


Q8. What is the purpose of __init__.py?

Answer:

It is used to initialize a package and can contain package-level
code.

It also traditionally identifies a directory as a Python
package.


Q9. What is the difference between import and from import?

Answer:

import:

import math

The complete module is imported.

from import:

from math import sqrt

A specific object is imported from the module.


Q10. What is __name__ == "__main__"?

Answer:

It checks whether the Python file is being executed directly.

Example:

if __name__ == "__main__":

    main()

This prevents main() from automatically running when the file
is imported as a module.


Q11. What are type hints?

Answer:

Type hints indicate the expected data types of variables,
function parameters, and return values.

Example:

def add(
    a: int,
    b: int
) -> int:

    return a + b


Q12. Do type hints enforce data types at runtime?

Answer:

No.

Python generally does not automatically enforce type hints at
runtime.

They mainly improve:

- Readability
- Documentation
- IDE support
- Static analysis


Q13. What is a dataclass?

Answer:

A dataclass is a class designed mainly for storing data.

It automatically provides useful methods such as __init__()
and __repr__().

Example:

from dataclasses import dataclass


@dataclass
class Student:

    name: str
    age: int


Q14. What are the advantages of dataclasses?

Answer:

Dataclasses:

- Reduce boilerplate code.
- Automatically generate common methods.
- Improve readability.
- Work well with type hints.
- Are useful for data-focused objects.


Q15. What is a lambda function?

Answer:

A lambda is a small anonymous function written in a single
expression.

Example:

square = lambda x: x ** 2


Q16. When are lambda functions commonly used?

Answer:

They are commonly used with:

- map()
- filter()
- sorted()
- Small callback functions


Q17. What does map() do?

Answer:

map() applies a function to every item in an iterable.

Example:

numbers = [1, 2, 3]

result = map(
    lambda x: x * 2,
    numbers
)

print(list(result))


Q18. What does filter() do?

Answer:

filter() selects elements from an iterable based on a
condition.

Example:

numbers = [1, 2, 3, 4]

result = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(list(result))


Q19. What is reduce()?

Answer:

reduce() repeatedly applies a function to elements of an
iterable and produces a single result.

It is available in functools.

Example:

from functools import reduce


result = reduce(
    lambda a, b: a + b,
    [1, 2, 3, 4]
)


Q20. What does enumerate() do?

Answer:

enumerate() provides both the index and value while iterating
over an iterable.

Example:

names = ["Amir", "Aman"]


for index, name in enumerate(names):

    print(index, name)


Q21. What does zip() do?

Answer:

zip() combines elements from multiple iterables.

Example:

names = ["Amir", "Aman"]

marks = [90, 85]


for name, mark in zip(
    names,
    marks
):

    print(name, mark)


Q22. What happens when zipped iterables have different lengths?

Answer:

zip() stops when the shortest iterable is exhausted.

Example:

list(
    zip(
        [1, 2, 3],
        ["A", "B"]
    )
)

Result:

[(1, "A"), (2, "B")]


Q23. What is shallow copy?

Answer:

A shallow copy creates a new outer object, but nested objects
may still be shared between the original and the copy.

Example:

import copy

new_list = copy.copy(old_list)


Q24. What is deep copy?

Answer:

A deep copy creates an independent copy of the object and its
nested objects.

Example:

import copy

new_list = copy.deepcopy(old_list)


Q25. What is the difference between shallow copy and deep copy?

Answer:

Shallow copy:

- Copies the outer object.
- Nested objects may be shared.

Deep copy:

- Recursively copies nested objects.
- Changes to nested objects do not affect the original.


Q26. What is PEP 8?

Answer:

PEP 8 is the official Python style guide.

It provides recommendations for:

- Naming
- Indentation
- Spacing
- Line length
- Code organization
- Readability


Q27. What does DRY mean in programming?

Answer:

DRY means:

Don't Repeat Yourself.

The principle encourages developers to avoid unnecessary
duplication and create reusable code.


Q28. What is clean code?

Answer:

Clean code is code that is:

- Easy to read
- Easy to understand
- Easy to maintain
- Properly organized
- Reusable

Meaningful names and small focused functions are examples of
clean-code practices.


Q29. Why should large Python projects be divided into modules
and packages?

Answer:

Dividing a project into modules and packages:

- Improves organization.
- Makes code reusable.
- Makes debugging easier.
- Allows different functionality to be separated.
- Makes large projects easier to maintain.


Q30. Which advanced Python concepts are important for
professional development?

Answer:

Important concepts include:

- Context managers
- Iterators
- Generators
- Decorators
- Modules
- Packages
- Type hints
- Dataclasses
- Lambda functions
- map()
- filter()
- reduce()
- enumerate()
- zip()
- Shallow and deep copying
- Exception handling
- Clean code
- PEP 8


INTERVIEW QUICK REVISION

CONTEXT MANAGER
→ Resource management

__enter__()
→ Setup

__exit__()
→ Cleanup


MODULE
→ Reusable Python file


PACKAGE
→ Collection of related modules


TYPE HINT
→ Indicates expected data type


DATACLASS
→ Simplifies data-focused classes


LAMBDA
→ Small anonymous function


map()
→ Transform


filter()
→ Select


reduce()
→ Combine


enumerate()
→ Index + value


zip()
→ Combine multiple iterables


SHALLOW COPY
→ Nested objects may be shared


DEEP COPY
→ Nested objects are independently copied


PEP 8
→ Python style guide


DRY
→ Don't Repeat Yourself
