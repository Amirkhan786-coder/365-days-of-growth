
# Smart Function Toolkit

## Day 20 — Python Advanced Mini Project

Smart Function Toolkit is a Python-based utility project
created to demonstrate advanced Python concepts such as
decorators, generators, iterators, validation, logging,
execution-time measurement, and data processing.

---

## Project Overview

The main purpose of this project is to understand how advanced
Python features can be combined to create reusable and
efficient programs.

The project processes a collection of numbers and generates
useful statistics while applying multiple decorators.

---

## Features

### 1. Function Logger

The logger decorator displays:

- Function name
- Arguments
- Function execution status
- Result

### 2. Execution Timer

The timer decorator measures the approximate execution time
of a function.

### 3. Input Validation

The validation decorator checks that:

- The input is not empty.
- Only numeric values are provided.
- All numbers are positive.

### 4. Generator-Based Processing

The project uses a generator to process numbers one at a time.

This demonstrates lazy evaluation and memory-efficient
processing.

### 5. Statistics

The project calculates:

- Total numbers
- Even numbers
- Odd numbers
- Sum
- Average
- Minimum
- Maximum

### 6. Multiple Decorators

The `process_numbers()` function uses multiple decorators:

```python
@logger
@timer
@validate_positive
def process_numbers(numbers):
    ...
````

This demonstrates how decorators can be combined.

---

## Technologies Used

* Python 3
* `functools`
* `collections`
* `time`

---

## Python Concepts Used

This project covers:

* Functions
* First-class functions
* Decorators
* Multiple decorators
* `@decorator` syntax
* `*args`
* `**kwargs`
* `functools.wraps`
* Generators
* `yield`
* Iteration
* `Counter`
* Exception handling
* Input validation
* Performance measurement

---

## Project Structure

```text
smart_function_toolkit/
│
├── main.py
├── README.md
└── mini_project.md
```

---

## Program Flow

```text
Input Numbers
      ↓
Validation
      ↓
Generator
      ↓
Number Processing
      ↓
Statistics Calculation
      ↓
Logger
      ↓
Timer
      ↓
Final Report
```

---

## How the Generator Works

The project contains the following generator:

```python
def number_generator(numbers):

    for number in numbers:

        print("Generated:", number)

        yield number
```

The `yield` keyword allows the program to produce one
number at a time.

This is useful when processing large datasets because all
values do not need to be generated at once.

---

## How the Logger Works

The logger decorator records information about function
execution.

Example:

```python
@logger
def process_numbers(numbers):
    ...
```

It displays the function name, arguments, and result.

---

## How the Timer Works

The timer decorator uses `time.perf_counter()` to measure
execution time.

Example:

```python
@timer
def process_numbers(numbers):
    ...
```

This helps understand the performance of a function.

---

## How Validation Works

The validation decorator checks the input before the main
function executes.

Example:

```python
@validate_positive
def process_numbers(numbers):
    ...
```

If invalid data is provided, the program raises an
appropriate error.

---

## Example Input

```python
numbers = [10, 15, 20, 25, 30]
```

---

## Example Processing

The generator processes the numbers one at a time:

```text
Generated: 10
Generated: 15
Generated: 20
Generated: 25
Generated: 30
```

---

## Example Output

```text
SMART FUNCTION TOOLKIT

Function Started: process_numbers
Arguments: ([10, 15, 20, 25, 30],)

Generated: 10
Generated: 15
Generated: 20
Generated: 25
Generated: 30

Execution Time: 0.0000 seconds

Function Completed: process_numbers

SMART FUNCTION TOOLKIT
------------------------------
Total Numbers: 5
Even Numbers: 3
Odd Numbers: 2
Sum: 100
Average: 20.0
Minimum: 10
Maximum: 30
```

The exact execution time may be different on different
computers.

---

## Error Handling

The project handles invalid input using exceptions.

For example:

```python
numbers = [10, -5, 20]
```

This will produce a validation error because negative numbers
are not allowed.

Another invalid example:

```python
numbers = [10, "20", 30]
```

This will produce a type error because the project expects
numeric values.

---

## Why Generators Are Used

Generators are useful because they:

* Produce values one at a time.
* Save memory.
* Support lazy evaluation.
* Work well with large datasets.
* Are useful in data-processing pipelines.

---

## Why Decorators Are Used

Decorators allow additional functionality to be added to
functions without modifying the main function logic.

In this project they are used for:

* Logging
* Timing
* Validation

This makes the code more modular and reusable.

---

## Learning Outcomes

After completing this project, I learned how to:

* Create custom decorators.
* Apply multiple decorators.
* Use `functools.wraps`.
* Create generator functions.
* Use `yield`.
* Process data lazily.
* Use `Counter`.
* Validate function input.
* Measure execution time.
* Handle exceptions.
* Build reusable Python utilities.

---

## Possible Future Improvements

The project can be extended with:

* User input from the terminal.
* File-based data processing.
* CSV support.
* JSON support.
* Data visualization.
* Menu-driven interface.
* More statistical calculations.
* Exporting reports.
* Database integration.

---

## Difficulty Level

**Intermediate → Advanced**

---

## Project Purpose

This project was created as part of my **365 Days of Growth**
Python learning journey.

The main goal was to move from basic Python programming
towards advanced and practical Python development.

---

## Day 20 Status

* [x] Iterators
* [x] Generators
* [x] Decorators
* [x] `yield`
* [x] `iter()`
* [x] `next()`
* [x] `StopIteration`
* [x] `*args`
* [x] `**kwargs`
* [x] `functools.wraps`
* [x] Mini Project

---

## Author

**Md Amir Khan**

Python Advanced Learning Journey

365 Days of Growth

