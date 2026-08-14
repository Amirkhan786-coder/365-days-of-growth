DAY 20 — PYTHON ADVANCED
PART 3 — 30 INTERVIEW QUESTIONS


Q1. What is an iterable in Python?

Answer:

An iterable is an object whose elements can be accessed one
by one during iteration.

Examples:

list
tuple
string
set
dictionary
range


Q2. What is an iterator?

Answer:

An iterator is an object that produces values one at a time.

It implements:

__iter__()
__next__()


Q3. What is the difference between an iterable and an iterator?

Answer:

Iterable:

An object that can return an iterator.

Iterator:

An object that keeps its current state and returns the next
value using next().


Q4. What does iter() do?

Answer:

iter() converts an iterable into an iterator.

Example:

numbers = [10, 20, 30]

iterator = iter(numbers)


Q5. What does next() do?

Answer:

next() retrieves the next value from an iterator.

Example:

iterator = iter([10, 20, 30])

print(next(iterator))

Output:

10


Q6. What is StopIteration?

Answer:

StopIteration is an exception raised when an iterator or
generator has no more values to return.


Q7. How does a for loop work internally?

Answer:

A for loop internally obtains an iterator using iter()
and repeatedly calls next() until StopIteration occurs.

Conceptually:

iterator = iter(collection)

while True:

    try:
        value = next(iterator)

    except StopIteration:
        break


Q8. How can you create a custom iterator?

Answer:

A custom iterator can be created using a class containing
__iter__() and __next__() methods.

Example:

class Count:

    def __init__(self):
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.number <= 5:

            value = self.number
            self.number += 1

            return value

        raise StopIteration


Q9. What is a generator?

Answer:

A generator is a special type of iterator that produces
values lazily using the yield keyword.


Q10. How do you create a generator?

Answer:

A generator is created using a function containing yield.

Example:

def numbers():

    yield 1
    yield 2
    yield 3


Q11. What is the difference between yield and return?

Answer:

return:

• Terminates the function.
• Returns a final result.

yield:

• Produces a value.
• Pauses execution.
• Preserves the function's state.
• Allows the function to continue later.


Q12. Why are generators memory efficient?

Answer:

Generators do not store all generated values in memory.
They produce one value at a time when requested.

This makes them useful for large datasets and large files.


Q13. What is lazy evaluation?

Answer:

Lazy evaluation means that a value is calculated only when
it is needed.

Generators use lazy evaluation.


Q14. What is a generator expression?

Answer:

A generator expression is a compact way to create a
generator.

Example:

numbers = (x * 2 for x in range(5))


Q15. What is the difference between list comprehension and
generator expression?

Answer:

List comprehension:

numbers = [x * 2 for x in range(5)]

Creates and stores all values.

Generator expression:

numbers = (x * 2 for x in range(5))

Produces values one at a time.


Q16. Can a generator be iterated more than once?

Answer:

Normally, no.

Once a generator is exhausted, it cannot be restarted.

A new generator must be created to iterate again.


Q17. What happens when next() is called on an exhausted
generator?

Answer:

It raises StopIteration.


Q18. What is a decorator?

Answer:

A decorator is a function that modifies or extends the
behavior of another function without changing its original
source code.


Q19. Why are decorators used?

Answer:

Decorators are commonly used for:

• Logging
• Authentication
• Authorization
• Validation
• Timing
• Caching
• Monitoring
• Access control


Q20. What does the @ symbol mean in decorators?

Answer:

The @ symbol provides a convenient syntax for applying a
decorator to a function.

Example:

@decorator
def greet():
    pass

It is equivalent to:

greet = decorator(greet)


Q21. What are first-class functions?

Answer:

In Python, functions are first-class objects.

They can be:

• Assigned to variables
• Passed as arguments
• Returned from functions
• Stored in collections


Q22. What is a nested function?

Answer:

A nested function is a function defined inside another
function.

Example:

def outer():

    def inner():
        print("Hello")

    inner()


Q23. Why are *args and **kwargs useful in decorators?

Answer:

They allow the wrapper function to accept different numbers
of positional and keyword arguments.

Example:

def decorator(function):

    def wrapper(*args, **kwargs):

        return function(
            *args,
            **kwargs
        )

    return wrapper


Q24. What is functools.wraps?

Answer:

functools.wraps is a decorator used inside decorators to
preserve metadata of the original function.

It can preserve:

• Function name
• Documentation string
• Other function metadata


Q25. What happens if functools.wraps is not used?

Answer:

The wrapper function may replace the original function's
metadata.

For example:

function.__name__

may show:

wrapper

instead of the original function name.


Q26. Can a decorator accept arguments?

Answer:

Yes.

A decorator can be designed as a function that returns
another decorator.

Example:

def repeat(times):

    def decorator(function):

        def wrapper():

            for _ in range(times):
                function()

        return wrapper

    return decorator


Q27. Can multiple decorators be applied to one function?

Answer:

Yes.

Example:

@first
@second
def greet():
    pass

They are applied from the bottom decorator upward.

Conceptually:

greet = first(second(greet))


Q28. What are some real-world uses of generators?

Answer:

Generators are useful for:

• Large file processing
• Database records
• Data pipelines
• Streaming data
• Log processing
• Large datasets
• Infinite sequences


Q29. What are some real-world uses of decorators?

Answer:

Decorators are widely used for:

• Authentication
• Authorization
• Logging
• Execution timing
• Validation
• Caching
• Error handling
• API request handling


Q30. Why are iterators, generators, and decorators important
in real-world Python development?

Answer:

They help create efficient, reusable, and maintainable code.

Iterators:

Provide controlled sequential access to data.

Generators:

Allow memory-efficient processing of large or streaming
data.

Decorators:

Allow reusable behavior to be added to functions without
modifying their core implementation.


INTERVIEW QUICK REVISION

ITERATOR

iter()
next()
__iter__()
__next__()
StopIteration


GENERATOR

yield
lazy evaluation
memory efficiency
generator expression
send()


DECORATOR

@
wrapper function
*args
**kwargs
functools.wraps


IMPORTANT DIFFERENCES

Iterable
→ Can be iterated.

Iterator
→ Produces the next value.

Generator
→ Convenient way to create an iterator.

Decorator
→ Modifies or extends function behavior.


