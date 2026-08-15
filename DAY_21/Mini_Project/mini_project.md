
# Student Performance Analyzer

## Day 21 — Python Advanced Mini Project

Student Performance Analyzer is a Python project that analyzes
student marks and generates a performance report.

This project combines multiple advanced Python concepts into
one practical application.

## Project Objective

The main objective is to practice:

- Dataclasses
- Type hints
- Context managers
- Lambda functions
- `map()`
- `filter()`
- `reduce()`
- `enumerate()`
- `zip()`
- Sorting
- File handling
- Clean code

## Features

The project can:

- Store student information.
- Store marks for multiple subjects.
- Calculate total marks.
- Calculate average marks.
- Determine pass/fail status.
- Rank students.
- Filter passed students.
- Perform subject-wise analysis.
- Calculate grand total marks.
- Save the final report to a text file.

## Technologies Used

- Python 3
- `dataclasses`
- `contextlib`
- `functools`
- `typing`

## Python Concepts Used

### 1. Dataclass

The `Student` dataclass stores:

- Student name
- Student marks

It also contains methods for calculating total marks,
average marks, and pass/fail status.

### 2. Type Hints

Type hints are used throughout the project.

Example:

```python
def average_marks(self) -> float:
````

This improves code readability and development support.

### 3. Lambda Functions

Lambda functions are used for:

* Sorting students.
* Filtering students.
* Reducing values.

Example:

```python
key=lambda student: student.average_marks()
```

### 4. reduce()

`reduce()` is used to calculate total marks.

```python
reduce(
    lambda a, b: a + b,
    self.marks
)
```

### 5. filter()

`filter()` is used to find students who passed.

```python
filter(
    lambda student: student.is_passed(),
    students
)
```

### 6. enumerate()

`enumerate()` is used to assign rankings.

```python
for rank, student in enumerate(
    ranked_students,
    start=1
):
```

### 7. zip()

`zip()` combines subject names with their indexes.

```python
for subject, index in zip(
    subject_names,
    range(len(subject_names))
):
```

### 8. Context Manager

A custom context manager is used to safely create and close
the report file.

```python
with report_file(
    "student_report.txt"
) as file:
```

The file is automatically closed after the block finishes.

## Project Structure

```text
Day-21/
│
├── main.py
├── mini_project.md
├── reflection.md
└── README.md
```

## Program Flow

```text
Student Data
     ↓
Dataclass
     ↓
Calculate Total
     ↓
Calculate Average
     ↓
Determine Pass/Fail
     ↓
Sort Students
     ↓
Generate Ranking
     ↓
Filter Passed Students
     ↓
Subject Analysis
     ↓
Generate Report
     ↓
Save File
```

## Sample Student Data

```python
Student(
    "Amir",
    [85, 90, 78, 88, 92]
)
```

## Sample Output

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

The exact output depends on the student data provided.

## Passing Rule

The project considers a student passed when their average is
greater than or equal to 40.

```python
return self.average_marks() >= 40
```

## Generated File

The program creates:

```text
student_report.txt
```

The file contains:

* Student rankings
* Total marks
* Average marks
* Pass/fail status
* Grand total

## Why This Project Is Useful

This project demonstrates how several Python concepts can work
together in a realistic application.

Instead of practicing each concept separately, the project
combines them into a single workflow.

## Learning Outcomes

After completing this project, I learned how to:

* Create dataclasses.
* Use type hints.
* Create reusable methods.
* Use lambda functions.
* Use `reduce()`.
* Use `filter()`.
* Use `enumerate()`.
* Use `zip()`.
* Sort objects using a key function.
* Create custom context managers.
* Safely handle files.
* Organize a Python project.
* Combine multiple advanced concepts.

## Future Improvements

Possible improvements include:

* User input system.
* Interactive menu.
* CSV file support.
* JSON file support.
* Database integration.
* Graphs and charts.
* Grade calculation.
* Subject-wise ranking.
* Attendance analysis.
* GUI interface.
* Web-based dashboard.

## Difficulty Level

Intermediate → Advanced

## Day 21 Mini Project Status

* [x] Dataclass
* [x] Type Hints
* [x] Lambda
* [x] reduce()
* [x] filter()
* [x] enumerate()
* [x] zip()
* [x] Context Manager
* [x] File Handling
* [x] Ranking
* [x] Report Generation

## Conclusion

Student Performance Analyzer provided practical experience
with advanced Python concepts.

The project demonstrates how modern Python features can be
combined to create clean, reusable, and maintainable
applications.

## Author

**Md Amir Khan**

