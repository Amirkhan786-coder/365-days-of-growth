
# 🚀 DAY 17 / 365 — PYTHON ITERATORS & GENERATORS
# 🎯 INTERVIEW QUESTIONS & ANSWERS

> Interview preparation for Python Iterators and Generators 🚀

---

# 🟢 BASIC QUESTIONS

## Q1. What is an iterable?

An iterable is an object that can be traversed or iterated over one element at a time.

Examples include:

- List
- Tuple
- String
- Set
- Dictionary
- Range

---

## Q2. What is an iterator?

An iterator is an object that produces values one at a time.

An iterator implements:

```python
__iter__()
````

and:

```python
__next__()
```

---

## Q3. What is the difference between an iterable and an iterator?

An iterable is an object from which we can obtain an iterator.

An iterator is the object that actually produces the next value.

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
```

Here:

```text
numbers → Iterable
iterator → Iterator
```

---

## Q4. What is `iter()`?

`iter()` is a built-in Python function that converts an iterable into an iterator.

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)
```

---

## Q5. What is `next()`?

`next()` is a built-in function used to retrieve the next value from an iterator.

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
```

---

## Q6. What is `StopIteration`?

`StopIteration` is an exception raised when an iterator has no more values to return.

Example:

```python
numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

The third call raises:

```text
StopIteration
```

---

## Q7. What is a generator?

A generator is a special type of iterator that generates values one at a time.

Generators are created using the `yield` keyword.

Example:

```python
def numbers():

    yield 1
    yield 2
    yield 3
```

---

## Q8. What is `yield`?

`yield` is used inside a generator function to produce a value.

Unlike `return`, `yield` pauses the function and remembers its state.

---

## Q9. What is a generator function?

A generator function is a function that contains at least one `yield` statement.

Example:

```python
def count():

    for number in range(1, 6):

        yield number
```

---

## Q10. What happens when a generator function is called?

Calling a generator function does not immediately execute the function.

Instead, it returns a generator object.

Example:

```python
def numbers():

    yield 1
    yield 2

generator = numbers()

print(generator)
```

The function starts executing when values are requested.

---

# 🟡 INTERMEDIATE QUESTIONS

## Q11. What is the difference between `yield` and `return`?

### `return`

* Ends the function.
* Sends a value back.
* Function execution stops.

### `yield`

* Produces a value.
* Pauses the function.
* Remembers the function state.
* Can continue execution later.

Example:

```python
def example():

    yield 10
    yield 20
```

---

## Q12. Why are generators memory efficient?

Generators do not store all generated values in memory.

They produce values only when required.

Example:

```python
numbers = (x for x in range(1000000))
```

The values are generated one at a time.

---

## Q13. What is lazy evaluation?

Lazy evaluation means calculating values only when they are needed.

Generators use lazy evaluation.

Example:

```python
def numbers():

    for number in range(1, 6):

        yield number
```

The numbers are generated only when requested.

---

## Q14. Can a generator be used with `next()`?

Yes.

Example:

```python
def numbers():

    yield 10
    yield 20
    yield 30

generator = numbers()

print(next(generator))
print(next(generator))
```

Output:

```text
10
20
```

---

## Q15. Can a generator be used in a `for` loop?

Yes.

Example:

```python
def numbers():

    yield 1
    yield 2
    yield 3

for number in numbers():

    print(number)
```

---

## Q16. What are `__iter__()` and `__next__()`?

`__iter__()` returns an iterator.

`__next__()` returns the next value from the iterator.

A custom iterator normally implements both methods.

---

## Q17. What should `__next__()` do when there are no more values?

It should raise:

```python
StopIteration
```

Example:

```python
def __next__(self):

    if self.current <= self.limit:

        value = self.current

        self.current += 1

        return value

    raise StopIteration
```

---

## Q18. What is a custom iterator?

A custom iterator is an iterator created by the programmer using a class.

Example:

```python
class Counter:

    def __init__(self, limit):

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
```

---

## Q19. What is a generator expression?

A generator expression is a compact way of creating a generator.

Example:

```python
squares = (x * x for x in range(10))
```

---

## Q20. What is the difference between a list comprehension and a generator expression?

### List Comprehension

```python
numbers = [x * x for x in range(1000000)]
```

Stores all values in memory.

### Generator Expression

```python
numbers = (x * x for x in range(1000000))
```

Produces values when required.

Therefore, generator expressions are generally more memory efficient.

---

# 🟠 ADVANCED QUESTIONS

## Q21. Why does `yield` remember its state?

When a generator reaches `yield`, execution pauses instead of ending.

Python remembers:

* Local variables
* Current execution position
* Generator state

When `next()` is called again, execution continues from that point.

---

## Q22. Can a generator have multiple `yield` statements?

Yes.

Example:

```python
def numbers():

    yield 10
    yield 20
    yield 30
```

---

## Q23. Can a generator run forever?

Yes.

An infinite generator can use `while True`.

Example:

```python
def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1
```

---

## Q24. How do you stop an infinite generator?

You can stop requesting values or use a condition in the loop consuming the generator.

Example:

```python
generator = infinite_numbers()

for _ in range(5):

    print(next(generator))
```

---

## Q25. What is the main advantage of generators?

The main advantage is **memory efficiency**.

Generators are especially useful when processing large amounts of data.

---

## Q26. Where are generators used in real-world applications?

Generators can be used for:

* Large file processing
* Data streaming
* Log processing
* Database records
* API responses
* Machine learning pipelines
* Large datasets
* Infinite sequences

---

## Q27. Is every iterator a generator?

No.

A generator is a type of iterator, but not every iterator is a generator.

Custom iterator classes are also iterators.

---

## Q28. Is every iterable an iterator?

No.

For example:

```python
numbers = [10, 20, 30]
```

The list is iterable but is not itself an iterator.

We can create an iterator using:

```python
iterator = iter(numbers)
```

---

## Q29. Can a list be directly used with `next()`?

No.

This will produce an error:

```python
numbers = [10, 20, 30]

next(numbers)
```

We first need:

```python
iterator = iter(numbers)

next(iterator)
```

---

## Q30. Why does a `for` loop work with iterables?

Internally, a `for` loop obtains an iterator from the iterable and repeatedly calls `next()` until `StopIteration` occurs.

Conceptually:

```text
Iterable
   ↓
iter()
   ↓
Iterator
   ↓
next()
   ↓
Value
   ↓
next()
   ↓
Value
   ↓
StopIteration
```

---

# 🔵 PRACTICAL INTERVIEW QUESTIONS

## Q31. Write a generator for even numbers.

```python
def even_numbers(limit):

    for number in range(2, limit + 1, 2):

        yield number
```

---

## Q32. Write a generator for squares.

```python
def squares(limit):

    for number in range(1, limit + 1):

        yield number * number
```

---

## Q33. Write a Fibonacci generator.

```python
def fibonacci(count):

    first = 0
    second = 1

    for _ in range(count):

        yield first

        first, second = second, first + second
```

---

## Q34. Write an infinite number generator.

```python
def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1
```

---

## Q35. Write a generator that filters even numbers from a list.

```python
def even_numbers(numbers):

    for number in numbers:

        if number % 2 == 0:

            yield number
```

---

# 🔴 TRICKY INTERVIEW QUESTIONS

## Q36. Does calling a generator function execute its code immediately?

No.

Calling a generator function returns a generator object.

The function begins executing when the generator is iterated or `next()` is called.

---

## Q37. What happens after a generator is exhausted?

Once a generator has no more values, calling `next()` again raises:

```text
StopIteration
```

---

## Q38. Can a generator be restarted?

A generator object cannot be restarted after it is exhausted.

A new generator object must be created by calling the generator function again.

Example:

```python
def numbers():

    yield 1
    yield 2

generator = numbers()

for number in generator:

    print(number)

generator = numbers()
```

---

## Q39. Why are generators useful for large files?

A generator can process a file one line at a time instead of loading the entire file into memory.

This reduces memory usage.

---

## Q40. What is a generator pipeline?

A generator pipeline connects multiple generators together.

Example:

```text
Input
  ↓
Filter
  ↓
Transform
  ↓
Final Output
```

Each stage processes values lazily.

---

# 🟣 SCENARIO-BASED QUESTIONS

## Q41. You need to process a file containing millions of lines. Would you use a list or generator?

A generator is generally a better choice because it can process one line at a time and reduce memory usage.

---

## Q42. You need to generate Fibonacci numbers forever. What would you use?

An infinite generator using `yield` and `while True`.

---

## Q43. You have one million numbers but only need to process them one by one. What would you use?

A generator or iterator would be appropriate because values can be processed one at a time.

---

## Q44. Why would you use a custom iterator instead of a generator?

A custom iterator can be useful when you need a class with more complex state or behavior.

Generators are usually simpler when the iteration logic is straightforward.

---

## Q45. Which is easier to implement: a custom iterator or a generator?

A generator is generally easier because Python automatically handles the iterator protocol.

---

# 🏆 QUICK REVISION

```text
Iterable
   ↓
Can be iterated

Iterator
   ↓
Produces values one at a time

iter()
   ↓
Creates an iterator

next()
   ↓
Gets the next value

StopIteration
   ↓
No values remaining

Generator
   ↓
Special type of iterator

yield
   ↓
Produces and pauses

Lazy Evaluation
   ↓
Calculate only when needed

Generator Expression
   ↓
Compact generator creation
```

---

# 🎯 MOST IMPORTANT INTERVIEW POINTS

Remember these points:

1. An iterable can provide an iterator.
2. An iterator produces values one at a time.
3. `iter()` creates an iterator.
4. `next()` gets the next value.
5. `StopIteration` indicates the end.
6. Custom iterators use `__iter__()` and `__next__()`.
7. Generators are a special type of iterator.
8. Generators use `yield`.
9. `yield` pauses and remembers state.
10. `return` ends the function.
11. Generators use lazy evaluation.
12. Generators are memory efficient.
13. Generator expressions use parentheses.
14. Infinite generators can use `while True`.
15. Generators are useful for large data processing.

---

# 🏆 DAY 17 INTERVIEW PREPARATION

```text
40+ Interview Questions
        ↓
Basic Concepts
        ↓
Iterators
        ↓
Generators
        ↓
yield
        ↓
Lazy Evaluation
        ↓
Memory Efficiency
        ↓
Custom Iterators
        ↓
Real-World Scenarios
        ↓
Interview Ready 🚀
```

---

# 🔥 365 DAYS OF GROWTH

**Day 17 — Interview Preparation Completed ✅**

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

**Day 17 — Keep Growing 🚀**

