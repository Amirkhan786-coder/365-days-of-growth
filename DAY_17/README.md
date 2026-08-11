
# 🚀 DAY 17 / 365 — PYTHON ITERATORS & GENERATORS

> Continuing my 365 Days of Growth journey 🚀

---

## 📅 Day 17

Today I learned about **Python Iterators and Generators**.

I learned how Python processes data one element at a time and how generators can produce values efficiently without storing all values in memory.

---

# 📚 TOPICS COVERED

- Iterable
- Iterator
- Iterable vs Iterator
- `iter()`
- `next()`
- `StopIteration`
- Custom Iterators
- `__iter__()`
- `__next__()`
- Generators
- `yield`
- Generator Functions
- Generator Expressions
- `yield` vs `return`
- Lazy Evaluation
- Memory Efficiency
- Infinite Generators
- Real-World Applications

---

# 🧠 WHAT I LEARNED

## 1. Iterable

An iterable is an object that can be iterated over one element at a time.

Examples:

```text
List
Tuple
String
Set
Dictionary
Range
````

Example:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

---

## 2. Iterator

An iterator is an object that produces values one at a time.

Python provides:

```python
iter()
```

and:

```python
next()
```

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

---

## 3. StopIteration

When an iterator has no more values, Python raises the `StopIteration` exception.

Example:

```python
numbers = [10, 20]

iterator = iter(numbers)

try:

    while True:

        print(next(iterator))

except StopIteration:

    print("Iteration completed")
```

---

## 4. Custom Iterator

Python allows us to create custom iterators using classes.

A custom iterator normally implements:

```python
__iter__()
```

and:

```python
__next__()
```

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

## 5. Generator

A generator is a special type of iterator.

Generators use the `yield` keyword.

Example:

```python
def numbers():

    yield 1
    yield 2
    yield 3
```

Using the generator:

```python
for number in numbers():

    print(number)
```

---

## 6. `yield`

The `yield` keyword produces a value and pauses the generator.

The generator remembers its state and continues from where it stopped.

Example:

```python
def count():

    for number in range(1, 6):

        yield number
```

---

## 7. Generator Expression

A generator expression is similar to a list comprehension.

List comprehension:

```python
numbers = [x * x for x in range(10)]
```

Generator expression:

```python
numbers = (x * x for x in range(10))
```

Generator expressions are useful when values should be generated only when needed.

---

## 8. Lazy Evaluation

Lazy evaluation means calculating values only when they are needed.

Generators use lazy evaluation.

This makes them useful for large datasets.

---

## 9. Memory Efficiency

Generators do not store all values at once.

For example:

```python
numbers = (x for x in range(1000000))
```

Values are generated one at a time.

This can reduce memory usage compared with creating a list containing all values.

---

## 10. Infinite Generator

Generators can produce values indefinitely.

Example:

```python
def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1
```

---

# 🧪 PRACTICE COMPLETED

During Day 17, I practiced:

* Iterators
* `iter()`
* `next()`
* `StopIteration`
* Custom Iterators
* `__iter__()`
* `__next__()`
* Generator Functions
* `yield`
* Generator Expressions
* Lazy Evaluation
* Infinite Generators
* Generator Pipelines

---

# 💻 PRACTICE EXAMPLES

## Even Number Generator

```python
def even_numbers(limit):

    for number in range(2, limit + 1, 2):

        yield number


for number in even_numbers(20):

    print(number)
```

---

## Fibonacci Generator

```python
def fibonacci(count):

    first = 0
    second = 1

    for _ in range(count):

        yield first

        first, second = second, first + second


for number in fibonacci(10):

    print(number)
```

---

# 🚀 MINI PROJECT

## Smart Data Processor Using Iterators & Generators

For today's mini project, I created a:

**Smart Data Processor**

The project demonstrates how iterators and generators can be used to process data efficiently.

---

# ✨ MINI PROJECT FEATURES

### 1. Iterator Processing

Converts a list into an iterator using:

```python
iter()
```

and processes values using:

```python
next()
```

---

### 2. Even Number Filtering

The project generates only even numbers.

---

### 3. Square Calculation

The project generates squares of numbers using `yield`.

---

### 4. Data Filtering

The project filters values greater than `100`.

---

### 5. Running Total

The project calculates running totals using a generator.

Example:

```text
10
30
60
100
```

---

### 6. Generator Expression

The project also demonstrates generator expressions.

---

### 7. Generator Pipeline

The project uses multiple generator functions together:

```text
Input
  ↓
Even Numbers
  ↓
Square
  ↓
Greater Than 100
  ↓
Final Output
```

---

# 🛠️ TECHNOLOGIES USED

```text
Python
Python Iterators
Python Generators
iter()
next()
yield
StopIteration
Generator Expressions
Lazy Evaluation
Data Processing
```

---

# 📂 PROJECT STRUCTURE

```text
Day17/
│
├── README.md
├── notes.md
├── practice_questions.md
├── practice_codes.py
├── interview_questions.md
│
└── mini_project/
    │
    └── main.py
```

---

# ▶️ HOW TO RUN

## Step 1

Open the project folder in VS Code.

## Step 2

Open the terminal.

## Step 3

Go to the mini project folder:

```bash
cd mini_project
```

## Step 4

Run the Python program:

```bash
python main.py
```

---

# 💻 SAMPLE PROJECT FLOW

```text
============================================================
      SMART DATA PROCESSOR
   ITERATORS & GENERATORS
============================================================

Original Data:
[12, 5, 28, 7, 44, 19, 60, 3, 72, 15, 90, 21, 36, 8, 55]

------------------------------------------------------------
Iterator Processing
------------------------------------------------------------

12
5
28
7
44
19
60
3
72
15
90
21
36
8
55

------------------------------------------------------------
Even Numbers
------------------------------------------------------------

12
28
44
60
72
90
36
8
```

The exact output may vary depending on the program version and data.

---

# 🧠 KEY CONCEPTS

## Iterable

An object that can be iterated over.

---

## Iterator

An object that produces values one at a time.

---

## `iter()`

Converts an iterable into an iterator.

---

## `next()`

Returns the next value from an iterator.

---

## `StopIteration`

Indicates that the iterator has no more values.

---

## Generator

A special type of iterator created using `yield`.

---

## `yield`

Produces a value and pauses execution.

---

## Lazy Evaluation

Values are calculated only when needed.

---

# 🌍 REAL-WORLD APPLICATIONS

Iterators and generators can be used in:

* Large File Processing
* Data Streaming
* Log Processing
* Database Processing
* API Data Processing
* Machine Learning Pipelines
* Large Dataset Processing
* Memory-Efficient Applications
* Infinite Data Streams
* Data Transformation Pipelines

---

# 🎯 LEARNING OUTCOMES

After completing Day 17, I can:

* [x] Explain Iterables
* [x] Explain Iterators
* [x] Use `iter()`
* [x] Use `next()`
* [x] Handle `StopIteration`
* [x] Create Custom Iterators
* [x] Use `__iter__()`
* [x] Use `__next__()`
* [x] Create Generator Functions
* [x] Use `yield`
* [x] Create Generator Expressions
* [x] Understand Lazy Evaluation
* [x] Understand Memory Efficiency
* [x] Create Infinite Generators
* [x] Build Generator Pipelines

---

# 🎯 INTERVIEW PREPARATION

I prepared interview questions related to:

```text
Iterable
Iterator
iter()
next()
StopIteration
Custom Iterator
__iter__()
__next__()
Generator
yield
Generator Function
Generator Expression
Lazy Evaluation
Memory Efficiency
Infinite Generator
Generator Pipeline
Real-World Applications
```

---

# 📊 DAY 17 PROGRESS

```text
Notes                  ✅ Completed
Practice Questions     ✅ Completed
Practice Codes         ✅ Completed
Interview Questions    ✅ Completed
Mini Project           ✅ Completed
README                 ✅ Completed
```

---

# 🏆 DAY 17 ACHIEVEMENT

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
Generator Expressions
       ↓
Lazy Evaluation
       ↓
Memory Efficiency
       ↓
Mini Project
       ↓
Day 17 Completed ✅
```

---

# 📈 365 DAYS OF GROWTH

**Day 17 / 365**

```text
████░░░░░░░░░░░░░░░░  4.7%
```

---

# 💡 KEY LEARNING

> Iterators help process data one element at a time, while generators make it easier and more memory-efficient to create such sequences.

---

# 🔥 MY GOAL

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

**17 / 365 — Keep Growing 🚀**

