
DAY 22 — PYTHON ADVANCED
30 INTERVIEW QUESTIONS


Q1. What is exception handling in Python?

Answer:
Exception handling is a mechanism used to handle runtime
errors without terminating the entire program.

The main keywords are:

try
except
else
finally
raise


Q2. What is the difference between `except` and `finally`?

Answer:
`except` runs when a matching exception occurs.

`finally` runs whether an exception occurs or not.

Example:

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Execution completed")


Q3. What is the purpose of the `raise` keyword?

Answer:
`raise` is used to manually generate an exception.

Example:

age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")


Q4. What is an iterator?

Answer:
An iterator is an object that allows values to be accessed
one at a time.

It implements:

__iter__()
__next__()


Q5. What is a generator?

Answer:
A generator is a special type of iterator that produces values
one at a time using the `yield` keyword.

Example:

def numbers():
    for i in range(5):
        yield i


Q6. What is the difference between `return` and `yield`?

Answer:

`return`:
- Ends the function.
- Returns a result.
- Does not preserve the function's execution state.

`yield`:
- Produces a value.
- Pauses the function.
- Preserves its state.
- Allows execution to continue later.


Q7. Why are generators memory efficient?

Answer:
Generators do not store all generated values in memory at
once. They produce values only when requested.

This makes them useful for large datasets and streams of data.


Q8. What is a decorator?

Answer:
A decorator is a function that modifies or extends the
behavior of another function without changing its original
code.

Example:

def decorator(function):

    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper


Q9. What are common uses of decorators?

Answer:

Decorators are commonly used for:

- Logging
- Authentication
- Authorization
- Timing
- Validation
- Caching
- Access control


Q10. What is a context manager?

Answer:
A context manager manages resources and ensures that cleanup
operations are performed properly.

The `with` statement is commonly used with context managers.

Example:

with open("data.txt", "r") as file:
    content = file.read()


Q11. What are `__enter__()` and `__exit__()`?

Answer:

`__enter__()` runs when entering a context.

`__exit__()` runs when leaving the context.

They are commonly used to create custom context managers.


Q12. What is `contextlib`?

Answer:
`contextlib` is a Python standard-library module that provides
utilities for working with context managers.

One commonly used feature is:

```python
@contextmanager
````

Q13. What is a Python module?

Answer:
A module is a Python file containing reusable code such as
functions, classes, and variables.

Example:

math_utils.py

Q14. What is a Python package?

Answer:
A package is a collection of related Python modules organized
in a directory.

Packages help structure large applications.

Q15. What is the purpose of `__name__ == "__main__"`?

Answer:
It allows code to run only when the Python file is executed
directly, rather than when it is imported as a module.

Example:

if **name** == "**main**":
main()

Q16. What are type hints?

Answer:
Type hints indicate the expected data types of variables,
parameters, and return values.

Example:

def add(a: int, b: int) -> int:
return a + b

Q17. Do type hints enforce types at runtime?

Answer:
Normally, no.

Python's type hints mainly provide information for developers,
IDEs, linters, and static type-checking tools.

Q18. What is a dataclass?

Answer:
A dataclass is a class designed mainly for storing data.

It can automatically generate methods such as:

* `__init__()`
* `__repr__()`
* `__eq__()`

Example:

from dataclasses import dataclass

@dataclass
class Student:
name: str
age: int

Q19. Why use dataclasses instead of regular classes?

Answer:
Dataclasses reduce boilerplate code and make data-focused
classes easier to create and maintain.

Q20. What is a lambda function?

Answer:
A lambda function is a small anonymous function written using
the `lambda` keyword.

Example:

square = lambda x: x ** 2

Q21. What is the difference between `map()` and `filter()`?

Answer:

`map()` transforms every applicable element.

`filter()` selects elements that satisfy a condition.

Example:

map():
[1, 2, 3] → [2, 4, 6]

filter():
[1, 2, 3, 4] → [2, 4]

Q22. What is `reduce()`?

Answer:
`reduce()` repeatedly applies a function to the elements of an
iterable and produces a single accumulated result.

It is available in:

```python
functools
```

Example:

from functools import reduce

result = reduce(
lambda a, b: a + b,
[1, 2, 3, 4]
)

Q23. What does `enumerate()` do?

Answer:
`enumerate()` allows us to iterate over values while also
getting their indexes.

Example:

names = ["Amir", "Rahul"]

for index, name in enumerate(names):
print(index, name)

Q24. What does `zip()` do?

Answer:
`zip()` combines corresponding elements from multiple
iterables.

Example:

names = ["Amir", "Rahul"]
marks = [90, 85]

for name, mark in zip(names, marks):
print(name, mark)

Q25. What is shallow copy?

Answer:
A shallow copy creates a new outer object, but nested objects
may still be shared between the original and copied object.

Example:

import copy

new_list = copy.copy(original)

Q26. What is deep copy?

Answer:
A deep copy creates a new object and recursively copies nested
objects as well.

Example:

import copy

new_list = copy.deepcopy(original)

Q27. What is the main difference between shallow copy and deep
copy?

Answer:

Shallow Copy:

* New outer object.
* Nested objects may be shared.

Deep Copy:

* New outer object.
* Nested objects are copied independently.

Q28. What is PEP 8?

Answer:
PEP 8 is the official style guide for Python code.

It provides recommendations for:

* Naming
* Indentation
* Spacing
* Imports
* Line length
* Code organization

Q29. What does DRY mean in programming?

Answer:
DRY means:

Don't Repeat Yourself.

The principle encourages developers to avoid unnecessary
duplication by creating reusable functions, classes, and
components.

Q30. How would you write maintainable Python code?

Answer:

I would focus on:

* Meaningful variable and function names
* Small reusable functions
* Type hints
* Proper exception handling
* Following PEP 8
* Avoiding duplicate code
* Using appropriate data structures
* Writing clear documentation
* Organizing modules and packages
* Testing the code regularly

QUICK INTERVIEW REVISION

Exception Handling
→ Handle runtime errors.

Iterator
→ Produces values one at a time.

Generator
→ Uses yield for lazy value generation.

Decorator
→ Extends or modifies function behavior.

Context Manager
→ Safely manages resources.

Module
→ Reusable Python file.

Package
→ Collection of related modules.

Type Hint
→ Indicates expected data types.

Dataclass
→ Simplifies data-focused classes.

Lambda
→ Small anonymous function.

map()
→ Transform data.

filter()
→ Select data.

reduce()
→ Produce one accumulated result.

enumerate()
→ Index + value.

zip()
→ Combine iterables.

Shallow Copy
→ Nested objects may be shared.

Deep Copy
→ Nested objects copied independently.

PEP 8
→ Python coding style guide.

DRY
→ Don't Repeat Yourself.

Clean Code
→ Readable, reusable, maintainable code.

