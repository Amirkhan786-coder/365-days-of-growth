

## 📅 Day 17

Today I learned about **Python Iterators and Generators**.

I learned how Python processes data one element at a time and how generators can produce values efficiently without storing all values in memory.

---

# 📚 TOPICS COVERED

1. Iterable
2. Iterator
3. Iterable vs Iterator
4. `iter()`
5. `next()`
6. `StopIteration`
7. Custom Iterators
8. `__iter__()`
9. `__next__()`
10. Generators
11. `yield`
12. Generator Functions
13. Generator Expressions
14. `next()` with Generators
15. `yield` vs `return`
16. Lazy Evaluation
17. Memory Efficiency
18. Infinite Generators
19. Real-World Applications

---

# 🧠 1. ITERABLE

An iterable is an object that can be iterated over one element at a time.

Common examples of iterables are:

- List
- Tuple
- String
- Set
- Dictionary
- Range

### Example

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
````

### Output

```text
10
20
30
40
```

---

# 🧠 2. ITERATOR

An iterator is an object that produces values one at a time.

An iterator remembers its current position and provides the next value when requested.

Python commonly uses:

```python
iter()
```

and:

```python
next()
```

---

# 🧠 3. ITERABLE VS ITERATOR

An **iterable** is an object that can provide an iterator.

An **iterator** is an object that produces values one by one.

### Example

```python
numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
```

### Output

```text
10
20
30
40
```

---

# 🧠 4. `iter()`

The `iter()` function converts an iterable into an iterator.

### Example

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
```

### Output

```text
10
```

---

# 🧠 5. `next()`

The `next()` function returns the next available value from an iterator.

### Example

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

### Output

```text
10
20
30
```

---

# 🧠 6. STOPITERATION

When there are no more values available, Python raises the `StopIteration` exception.

### Example

```python
numbers = [10, 20]

iterator = iter(numbers)

try:

    while True:

        print(next(iterator))

except StopIteration:

    print("Iteration completed")
```

### Output

```text
10
20
Iteration completed
```

---

# 🧠 7. CUSTOM ITERATORS

Python allows us to create our own iterator classes.

A custom iterator generally contains:

```python
__iter__()
```

and:

```python
__next__()
```

### Example

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


counter = Counter(5)

for number in counter:

    print(number)
```

### Output

```text
1
2
3
4
5
```

---

# 🧠 8. `__iter__()`

The `__iter__()` method returns an iterator.

For an iterator object, it normally returns itself.

### Example

```python
def __iter__(self):

    return self
```

---

# 🧠 9. `__next__()`

The `__next__()` method returns the next value from an iterator.

When there are no more values, it should raise `StopIteration`.

### Example

```python
def __next__(self):

    if self.current <= self.limit:

        value = self.current

        self.current += 1

        return value

    raise StopIteration
```

---

# 🧠 10. GENERATORS

A generator is a special type of iterator.

Generators provide an easier way to create iterators without manually implementing `__iter__()` and `__next__()`.

Generators use the `yield` keyword.

---

# 🧠 11. `yield`

The `yield` keyword produces a value from a generator and pauses its execution.

The generator remembers its state and continues from where it stopped when another value is requested.

### Example

```python
def numbers():

    yield 1
    yield 2
    yield 3


for number in numbers():

    print(number)
```

### Output

```text
1
2
3
```

---

# 🧠 12. GENERATOR FUNCTION

A function containing the `yield` keyword is called a generator function.

### Example

```python
def count():

    for number in range(1, 6):

        yield number


for value in count():

    print(value)
```

### Output

```text
1
2
3
4
5
```

The values are generated one at a time.

---

# 🧠 13. GENERATOR EXPRESSIONS

A generator expression is similar to a list comprehension.

The main difference is that generator expressions use parentheses.

### List Comprehension

```python
numbers = [x * x for x in range(5)]

print(numbers)
```

### Generator Expression

```python
numbers = (x * x for x in range(5))

for number in numbers:

    print(number)
```

Generator expressions are useful when we do not need all values stored in memory at once.

---

# 🧠 14. `next()` WITH GENERATORS

Generators can also be used with `next()`.

### Example

```python
def numbers():

    yield 10
    yield 20
    yield 30


generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))
```

### Output

```text
10
20
30
```

---

# 🧠 15. `yield` VS `return`

## `return`

The `return` statement sends a value back and ends the function.

### Example

```python
def example():

    return 10
```

Once `return` executes, the function ends.

---

## `yield`

The `yield` statement produces a value and pauses the generator.

### Example

```python
def example():

    yield 10
    yield 20
    yield 30
```

The generator can continue from where it stopped.

### Main Difference

```text
return
   ↓
Ends the function

yield
   ↓
Produces a value
   ↓
Pauses execution
   ↓
Remembers state
   ↓
Continues later
```

---

# 🧠 16. LAZY EVALUATION

Lazy evaluation means that values are calculated only when they are needed.

Generators use lazy evaluation.

### Example

```python
def numbers():

    for number in range(1, 6):

        print("Generating:", number)

        yield number


generator = numbers()

print(next(generator))
print(next(generator))
```

### Output

```text
Generating: 1
1
Generating: 2
2
```

Only the requested values are generated.

---

# 🧠 17. MEMORY EFFICIENCY

Generators are memory efficient because they do not store all values at once.

### List

```python
numbers = [x for x in range(1000000)]
```

This creates and stores all one million values.

### Generator

```python
numbers = (x for x in range(1000000))
```

The values are generated only when needed.

This makes generators useful for large datasets and large files.

---

# 🧠 18. INFINITE GENERATORS

A generator can produce values indefinitely.

### Example

```python
def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1


generator = infinite_numbers()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
```

### Output

```text
1
2
3
4
```

The generator continues producing values as long as we request them.

---

# 🧠 19. REAL-WORLD APPLICATIONS

Iterators and generators are useful in:

* Large File Processing
* Data Processing
* Data Streaming
* Log Processing
* Machine Learning Pipelines
* Reading Large Datasets
* API Data Processing
* Database Records
* Memory-Efficient Applications
* Infinite Sequences

---

# 🔥 COMPLETE ITERATOR EXAMPLE

```python
numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

while True:

    try:

        value = next(iterator)

        print(value)

    except StopIteration:

        break
```

### Output

```text
10
20
30
40
50
```

---

# 🔥 COMPLETE GENERATOR EXAMPLE

```python
def even_numbers(limit):

    for number in range(2, limit + 1, 2):

        yield number


for number in even_numbers(10):

    print(number)
```

### Output

```text
2
4
6
8
10
```

---

# 🧠 ITERABLE VS ITERATOR VS GENERATOR

| Feature                   | Iterable  | Iterator | Generator |
| ------------------------- | --------- | -------- | --------- |
| Can be iterated           | ✅         | ✅        | ✅         |
| Can use `iter()`          | ✅         | ✅        | ✅         |
| Can use `next()` directly | ❌         | ✅        | ✅         |
| Uses `yield`              | ❌         | ❌        | ✅         |
| Memory efficient          | Depends   | Usually  | ✅         |
| Custom implementation     | Sometimes | ✅        | Easy      |

---

# 💡 KEY LEARNING

The basic iterator workflow is:

```text
Iterable
   ↓
iter()
   ↓
Iterator
   ↓
next()
   ↓
Next Value
```

The generator workflow is:

```text
Generator Function
       ↓
      yield
       ↓
Generate Value
       ↓
Pause
       ↓
Resume
       ↓
Generate Next Value
```

---

# 🎯 DAY 17 LEARNING OUTCOMES

After completing today's learning, I can:

* [x] Explain Iterables
* [x] Explain Iterators
* [x] Differentiate Iterable and Iterator
* [x] Use `iter()`
* [x] Use `next()`
* [x] Understand `StopIteration`
* [x] Create Custom Iterators
* [x] Use `__iter__()`
* [x] Use `__next__()`
* [x] Create Generator Functions
* [x] Use `yield`
* [x] Create Generator Expressions
* [x] Understand Lazy Evaluation
* [x] Understand Memory Efficiency
* [x] Create Infinite Generators
* [x] Apply Generators to Real-World Problems

---

# 🏆 DAY 17 GOAL

```text
Python Iterators
       ↓
iter()
       ↓
next()
       ↓
StopIteration
       ↓
Custom Iterators
       ↓
Generators
       ↓
yield
       ↓
Lazy Evaluation
       ↓
Memory Efficiency
       ↓
Real-World Applications
```

---

# 🚀 365 DAYS OF GROWTH

**Day 17 / 365**

```text
████░░░░░░░░░░░░░░░░  4.7%
```

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

**Day 17 — Keep Growing 🚀**


