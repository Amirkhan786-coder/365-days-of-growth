# Day 20 — Python Advanced

## Iterators, Generators & Decorators

Day 20 of my **365 Days of Growth** journey focuses on
advanced Python programming concepts.

Today I learned how Python handles iteration, lazy evaluation,
function wrapping, and reusable function behavior.

---

## Topics Covered

### Iterators

- Iterable vs Iterator
- `iter()`
- `next()`
- `__iter__()`
- `__next__()`
- `StopIteration`
- Custom Iterators

### Generators

- Generator Functions
- `yield`
- `yield` vs `return`
- Generator Expressions
- Lazy Evaluation
- Memory Efficiency
- `send()`
- Infinite Generators

### Decorators

- Functions as Objects
- Nested Functions
- Decorators
- `@decorator` Syntax
- Wrapper Functions
- `*args`
- `**kwargs`
- `functools.wraps`
- Multiple Decorators
- Decorators with Arguments

### Practical Decorators

- Logging
- Execution Timer
- Input Validation
- Function Monitoring

---

## Mini Project

### Smart Function Toolkit

The Day 20 mini project combines multiple advanced Python
concepts into one practical application.

The project processes numbers and generates useful statistics
while using generators and decorators.

---

## Project Features

- Function logging
- Execution-time measurement
- Positive-number validation
- Generator-based processing
- Even-number counting
- Odd-number counting
- Total calculation
- Sum calculation
- Average calculation
- Minimum and maximum calculation
- Multiple decorators
- Exception handling

---

## Project Structure

```text
Day-20/
│
├── notes.md
├── mcqs.md
├── interview_questions.md
├── practice_questions.md
├── practice_codes.py
├── mini_project.md
├── main.py
├── reflection.md
└── README.md
````

---

## Technologies Used

**Language**

Python 3

**Modules**

* `functools`
* `collections`
* `time`

---

## Concepts Used

The project demonstrates:

```text
Functions
   ↓
Decorators
   ↓
Validation
   ↓
Generators
   ↓
Data Processing
   ↓
Statistics
   ↓
Final Report
```

---

## Example Code

### Generator

```python
def number_generator(numbers):

    for number in numbers:

        yield number
```

### Decorator

```python
def logger(function):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = function(
            *args,
            **kwargs
        )

        print("Function Completed")

        return result

    return wrapper
```

---

## Example Input

```python
numbers = [10, 15, 20, 25, 30]
```

---

## Example Output

```text
SMART FUNCTION TOOLKIT

Generated: 10
Generated: 15
Generated: 20
Generated: 25
Generated: 30

Total Numbers: 5
Even Numbers: 3
Odd Numbers: 2
Sum: 100
Average: 20.0
Minimum: 10
Maximum: 30
```

The execution time may vary depending on the computer.

---

## Learning Outcomes

After completing Day 20, I can:

* Create custom iterators.
* Use `iter()` and `next()`.
* Handle `StopIteration`.
* Create generator functions.
* Use `yield`.
* Explain lazy evaluation.
* Create generator expressions.
* Build custom decorators.
* Use `@decorator` syntax.
* Work with `*args` and `**kwargs`.
* Use `functools.wraps`.
* Create multiple decorators.
* Build timer and logging decorators.
* Validate function input.
* Combine advanced Python concepts in a project.

---

## Why This Matters

Iterators and generators are useful when working with large
amounts of data because they allow values to be processed
efficiently.

Decorators are useful for creating reusable functionality
such as logging, authentication, validation, timing, and
monitoring.

These concepts are commonly encountered in professional
Python development.

---

## Challenges

The most challenging topics were:

* Understanding iterator state.
* Understanding how `yield` pauses execution.
* Understanding decorator wrapping.
* Working with multiple decorators.
* Using `*args` and `**kwargs`.

Regular coding practice helped me understand these concepts
better.

---

## Day 20 Checklist

* [x] Advanced Python Notes
* [x] 30 MCQs
* [x] 30 Interview Questions
* [x] 30 Practice Questions
* [x] 30 Practice Codes
* [x] Mini Project
* [x] `mini_project.md`
* [x] `reflection.md`
* [x] `README.md`

---

## 365 Days of Growth

**Day 20 completed successfully.**

Continuing the journey toward becoming a stronger Python
developer and building practical, industry-ready projects.

---

## Author

**Md Amir Khan**

