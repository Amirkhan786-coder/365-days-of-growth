
# Day 21 — Python Advanced

## Context Managers, Modules, Type Hints, Dataclasses & Functional Programming

Day 21 is the final major day of my Python Advanced learning
journey.

Today I learned how to combine advanced Python concepts to
write cleaner, reusable, organized, and maintainable programs.

## Topics Covered

### Context Managers

- `with` statement
- `__enter__()`
- `__exit__()`
- Custom Context Managers
- `contextlib`
- `@contextmanager`

### Modules & Packages

- Python Modules
- Python Packages
- `import`
- `from ... import`
- `__init__.py`
- `__name__`
- `if __name__ == "__main__"`

### Type Hints

- Function Type Hints
- Parameter Type Hints
- Return Type Hints
- `list[int]`
- `list[str]`
- `dict`
- Type-hinted classes

### Dataclasses

- `@dataclass`
- Dataclass fields
- Default values
- Dataclass methods
- Dataclass vs normal class

### Functional Programming

- Lambda Functions
- `map()`
- `filter()`
- `reduce()`

### Useful Built-in Functions

- `enumerate()`
- `zip()`

### Copying

- Shallow Copy
- Deep Copy
- `copy.copy()`
- `copy.deepcopy()`

### Python Best Practices

- PEP 8
- DRY Principle
- Clean Code
- Meaningful Naming
- Reusable Functions
- Project Organization

## Mini Project

# Student Performance Analyzer

The Day 21 mini project is a Python application that analyzes
student performance.

It combines multiple advanced Python concepts into one
practical project.

## Features

The project can:

- Store student information.
- Store subject marks.
- Calculate total marks.
- Calculate average marks.
- Determine pass/fail status.
- Rank students.
- Filter passed students.
- Perform subject-wise analysis.
- Calculate grand total.
- Generate a report.
- Save the report to a text file.

## Technologies Used

- Python 3
- `dataclasses`
- `contextlib`
- `functools`
- `typing`

## Concepts Used in the Project

```text
Dataclass
    ↓
Type Hints
    ↓
Lambda
    ↓
reduce()
    ↓
filter()
    ↓
sorted()
    ↓
enumerate()
    ↓
zip()
    ↓
Context Manager
    ↓
File Handling
    ↓
Report Generation
````

## Project Structure

```text
Day-21/
│
├── main.py
├── mini_project.md
├── reflection.md
└── README.md
```

## Example Student

```python
Student(
    "Amir",
    [85, 90, 78, 88, 92]
)
```

## Example Output

```text
STUDENT PERFORMANCE ANALYZER
----------------------------------------
1. Riya | Total: 460 | Average: 92.00 | Status: PASS
2. Amir | Total: 433 | Average: 86.60 | Status: PASS
3. Rahul | Total: 362 | Average: 72.40 | Status: PASS
4. Neha | Total: 292 | Average: 58.40 | Status: PASS
5. Aman | Total: 200 | Average: 40.00 | Status: PASS

PASSED STUDENTS
Riya
Amir
Rahul
Aman
Neha

Grand Total Marks: 1747

SUBJECT-WISE ANALYSIS
Python: 67.40
SQL: 70.40
DSA: 69.00
Math: 72.00
AI: 71.00

Report saved to student_report.txt
```

The exact output depends on the input data.

## Generated Report

The project creates:

```text
student_report.txt
```

The report contains:

* Student ranking
* Total marks
* Average marks
* Pass/fail status
* Grand total marks

## Learning Outcomes

After completing Day 21, I can:

* Create custom context managers.
* Use the `with` statement.
* Create and organize modules.
* Create Python packages.
* Use `__name__`.
* Write type-hinted functions.
* Create dataclasses.
* Use lambda functions.
* Transform data using `map()`.
* Filter data using `filter()`.
* Combine values using `reduce()`.
* Use `enumerate()`.
* Use `zip()`.
* Understand shallow and deep copies.
* Follow PEP 8.
* Apply the DRY principle.
* Write cleaner Python code.
* Build practical Python projects.

## Challenges

The most challenging concepts were:

* Custom context managers
* `reduce()`
* Shallow vs deep copy
* Combining multiple functional programming tools
* Integrating multiple advanced concepts into one project

## What I Improved

I improved my ability to:

* Structure Python programs.
* Write reusable functions.
* Work with data-focused classes.
* Manage resources safely.
* Process collections efficiently.
* Follow clean-code practices.

## Python Advanced Journey

```text
Exception Handling
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
Lambda
        ↓
map()
        ↓
filter()
        ↓
reduce()
        ↓
enumerate()
        ↓
zip()
        ↓
Shallow & Deep Copy
        ↓
Clean Code
        ↓
Python Advanced Complete
```

## Day 21 Checklist

* [x] Complete Notes
* [x] 30 MCQs
* [x] 30 Interview Questions
* [x] 30 Practice Questions
* [x] 30 Separate Practice Codes
* [x] Mini Project
* [x] `mini_project.md`
* [x] `reflection.md`
* [x] `README.md`

## Python Advanced Completion

Python Advanced has now been completed as part of my
**365 Days of Growth** journey.

This phase helped me move from learning Python syntax to
building more structured and practical applications.

## Next Step

Continue the 365 Days of Growth journey by applying Python
knowledge to:

* Data Structures
* Problem Solving
* SQL
* Data Analysis
* AI/ML
* Real-world Projects

## Author

**Md Amir Khan**