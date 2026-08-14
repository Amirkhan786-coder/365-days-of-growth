DAY 20 — PYTHON ADVANCED

ITERATORS • GENERATORS • DECORATORS


1. ITERABLES

An iterable is an object that can be iterated over one
element at a time.

Examples:

• list
• tuple
• string
• set
• dictionary
• range

Example:

numbers = [10, 20, 30]

for number in numbers:
    print(number)


2. ITERATORS

An iterator is an object that produces values one at a time
and keeps track of its current position.

An iterator provides two important methods:

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


3. iter()

The iter() function converts an iterable into an iterator.

Example:

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))


4. next()

The next() function returns the next value from an iterator.

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


5. StopIteration

When an iterator has no more values,
next() raises the StopIteration exception.

Example:

numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

# The following would raise StopIteration:
# print(next(iterator))


6. ITERABLE VS ITERATOR

Iterable:

An object that can provide an iterator.

Examples:

list
tuple
string
set
dictionary
range

Iterator:

An object that produces values using next().

Example:

numbers = [1, 2, 3]

# Iterable
print(numbers)

# Iterator
iterator = iter(numbers)

print(next(iterator))


7. HOW A FOR LOOP USES AN ITERATOR

Example:

numbers = [10, 20, 30]

for number in numbers:
    print(number)

Conceptually, Python does something similar to:

iterator = iter(numbers)

while True:

    try:
        number = next(iterator)
        print(number)

    except StopIteration:
        break


8. CUSTOM ITERATOR

We can create our own iterator using a class.

Example:

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


counter = Count(1, 5)

for number in counter:
    print(number)

Output:

1
2
3
4
5


9. GENERATORS

A generator is a special type of iterator.

Generators produce values one at a time instead of
creating and storing all values at once.

Generators are created using the yield keyword.


10. yield

The yield keyword produces a value from a generator and
pauses the function.

The function can continue from the same point later.

Example:

def numbers():

    yield 1
    yield 2
    yield 3


generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))

Output:

1
2
3


11. yield VS return

return:

• Terminates the function.
• Returns a final value.
• Execution stops.

yield:

• Produces a value.
• Pauses the function.
• Preserves the function state.
• Execution can continue later.

Example:

def normal_function():

    return 10


def generator_function():

    yield 10
    yield 20


12. GENERATOR WITH FOR LOOP

Example:

def numbers():

    for i in range(1, 6):
        yield i


for number in numbers():
    print(number)

Output:

1
2
3
4
5


13. GENERATOR MEMORY EFFICIENCY

Generators are memory efficient because they produce values
only when they are needed.

Example:

def generate_numbers():

    for i in range(1000000):
        yield i


numbers = generate_numbers()

print(next(numbers))
print(next(numbers))

This approach is useful when working with large datasets.


14. GENERATOR EXPRESSION

A generator expression is similar to a list comprehension.

List comprehension:

numbers = [x * 2 for x in range(5)]


Generator expression:

numbers = (x * 2 for x in range(5))


The generator expression produces values lazily.


15. LIST VS GENERATOR

List:

numbers = [x for x in range(1000000)]

The values are created and stored in memory.

Generator:

numbers = (x for x in range(1000000))

Values are generated when required.

Generators are useful for:

• Large datasets
• Large files
• Data pipelines
• Streaming data


16. send() WITH GENERATORS

Generators can receive values using send().

Example:

def calculator():

    value = yield

    print("Received:", value)


gen = calculator()

next(gen)

gen.send(100)

Output:

Received: 100


17. DECORATORS

A decorator is a function that modifies or extends the
behavior of another function without changing its original
source code.

Common uses:

• Logging
• Authentication
• Validation
• Timing
• Monitoring
• Access control
• Caching


18. FUNCTIONS AS OBJECTS

In Python, functions are first-class objects.

A function can be:

• Stored in a variable
• Passed as an argument
• Returned from another function

Example:

def greet():

    print("Hello")


message = greet

message()

Output:

Hello


19. FUNCTION AS AN ARGUMENT

A function can be passed as an argument to another function.

Example:

def greet():

    print("Hello")


def execute(function):

    function()


execute(greet)


20. NESTED FUNCTIONS

A function defined inside another function is called a
nested function.

Example:

def outer():

    def inner():

        print("Inside inner function")

    inner()


outer()


21. BASIC DECORATOR

Example:

def decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")

    return wrapper


@decorator
def greet():

    print("Hello")


greet()

Output:

Before function
Hello
After function


22. HOW @decorator WORKS

This:

@decorator
def greet():
    print("Hello")

is equivalent to:

def greet():
    print("Hello")

greet = decorator(greet)


23. DECORATOR WITH *args AND **kwargs

Using *args and **kwargs allows a decorator to work with
different types and numbers of arguments.

Example:

def decorator(function):

    def wrapper(*args, **kwargs):

        print("Function started")

        result = function(
            *args,
            **kwargs
        )

        print("Function finished")

        return result

    return wrapper


@decorator
def add(a, b):

    return a + b


print(add(10, 20))


24. RETURNING VALUES FROM A DECORATOR

A decorator should return the result of the original
function when required.

Example:

def decorator(function):

    def wrapper(*args, **kwargs):

        result = function(
            *args,
            **kwargs
        )

        return result

    return wrapper


@decorator
def multiply(a, b):

    return a * b


print(multiply(5, 4))

Output:

20


25. functools.wraps

functools.wraps preserves important metadata of the original
function.

Example:

from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        return function(
            *args,
            **kwargs
        )

    return wrapper


@decorator
def greet():

    """This function greets the user."""

    print("Hello")


print(greet.__name__)
print(greet.__doc__)


26. TIMER DECORATOR

A timer decorator can measure the execution time of a
function.

Example:

import time


def timer(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(
            *args,
            **kwargs
        )

        end = time.time()

        print(
            "Execution time:",
            end - start
        )

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for i in range(100000):

        total += i

    return total


print(calculate())


27. LOGGING DECORATOR

A logging decorator can display information whenever a
function is called.

Example:

def logger(function):

    def wrapper(*args, **kwargs):

        print(
            "Calling:",
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


@logger
def greet(name):

    print("Hello", name)


greet("Amir")


28. DECORATOR WITH ARGUMENT

A decorator can also accept its own arguments.

Example:

def repeat(times):

    def decorator(function):

        def wrapper(*args, **kwargs):

            for _ in range(times):

                function(
                    *args,
                    **kwargs
                )

        return wrapper

    return decorator


@repeat(3)
def greet():

    print("Hello")


greet()

Output:

Hello
Hello
Hello


29. MULTIPLE DECORATORS

Multiple decorators can be applied to the same function.

Example:

def first(function):

    def wrapper():

        print("First")

        function()

    return wrapper


def second(function):

    def wrapper():

        print("Second")

        function()

    return wrapper


@first
@second
def greet():

    print("Hello")


greet()


Decorators are applied from bottom to top.

Conceptually:

greet = first(second(greet))


30. DECORATOR + GENERATOR

Decorators and generators can also be combined.

Example:

def logger(function):

    def wrapper(*args, **kwargs):

        print("Generator started")

        return function(
            *args,
            **kwargs
        )

    return wrapper


@logger
def numbers():

    for i in range(1, 6):

        yield i


for number in numbers():

    print(number)


31. REAL-WORLD USES OF DECORATORS

Decorators are commonly used for:

• Logging
• Authentication
• Authorization
• Timing
• Validation
• Caching
• Error handling
• Monitoring
• Access control
• API request processing


32. REAL-WORLD USES OF GENERATORS

Generators are commonly used for:

• Large files
• Large datasets
• Data pipelines
• Streaming data
• Log processing
• Database records
• Memory-efficient processing
• Infinite sequences


33. GENERATOR FOR FILE PROCESSING

Generators are useful when processing large files.

Example:

def read_lines(filename):

    with open(filename, "r") as file:

        for line in file:

            yield line.strip()


for line in read_lines("data.txt"):

    print(line)

Only one line needs to be processed at a time.


34. INFINITE GENERATOR

A generator can produce an unlimited sequence of values.

Example:

def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1


numbers = infinite_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))

Output:

1
2
3


35. IMPORTANT DIFFERENCES

Iterable:

An object that can be iterated over.

Iterator:

An object that produces values using next().

Generator:

A convenient way to create an iterator using yield.

Decorator:

A function that modifies another function's behavior.


36. ITERATOR VS GENERATOR

Iterator:

• Uses __iter__()
• Uses __next__()
• Can be implemented using a class.
• Keeps track of its current state.

Generator:

• Uses yield.
• Automatically behaves like an iterator.
• Easier to write.
• Maintains its state automatically.


37. LIST VS GENERATOR

List:

• Stores all values.
• Uses more memory for large data.
• Values are immediately created.

Generator:

• Produces values one at a time.
• More memory efficient.
• Values are created when needed.


38. yield VS return

yield:

• Pauses execution.
• Preserves state.
• Can produce multiple values.
• Used in generators.

return:

• Ends function execution.
• Returns a final result.
• Does not resume the function.


39. DAY 20 QUICK REVISION

ITERATORS

iter()
next()
__iter__()
__next__()
StopIteration


GENERATORS

yield
generator()
generator expression
send()
memory efficiency


DECORATORS

@decorator
wrapper()
*args
**kwargs
functools.wraps


PRACTICAL DECORATORS

Timer
Logger
Validation
Authentication
Caching


40. DAY 20 LEARNING GOAL

By the end of Day 20, you should be able to:

1. Explain iterable and iterator.
2. Create and use iterators.
3. Understand iter() and next().
4. Handle StopIteration.
5. Create custom iterators.
6. Create generator functions.
7. Use yield correctly.
8. Explain yield vs return.
9. Use generator expressions.
10. Explain generator memory efficiency.
11. Create decorators.
12. Use @decorator syntax.
13. Use *args and **kwargs in decorators.
14. Use functools.wraps.
15. Create timer and logging decorators.
16. Create decorators with arguments.
17. Understand multiple decorators.
18. Combine generators and decorators.


