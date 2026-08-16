
## Day 22 — Python Advanced Final Mini Project

Student Result Management System is a Python application that
analyzes student marks, calculates results, generates rankings,
and creates a final result report.

This project combines the major Python Advanced concepts learned
throughout Days 19–22.

## Project Objective

The objective of this project is to apply advanced Python
concepts in one practical application.

The project demonstrates:

- Dataclasses
- Type hints
- Exception handling
- Custom exceptions
- Lambda functions
- `reduce()`
- `filter()`
- `enumerate()`
- Sorting
- Context managers
- File handling
- Clean code
- DRY principle

## Features

The application can:

- Store student information.
- Store marks for multiple subjects.
- Validate marks.
- Calculate total marks.
- Calculate average marks.
- Assign grades.
- Determine pass/fail status.
- Rank students.
- Filter passed students.
- Generate a result report.
- Save the report to a text file.
- Handle invalid data safely.

## Technologies Used

- Python 3
- `dataclasses`
- `functools`
- `contextlib`

## Concepts Used

### 1. Dataclasses

The `Student` dataclass stores student information and marks.

Example:

```python
@dataclass
class Student:

    name: str
    marks: list[int]
````

The class also contains methods for:

* Total marks
* Average marks
* Grade
* Pass/fail status

## 2. Type Hints

Type hints are used to make the code easier to understand.

Example:

```python
def total_marks(self) -> int:
```

and:

```python
def average_marks(self) -> float:
```

## 3. Exception Handling

The project uses `try` and `except` to handle errors safely.

Example:

```python
try:

    validate_marks(student.marks)

except InvalidMarksError as error:

    print(error)
```

This prevents invalid data from breaking the program.

## 4. Custom Exception

A custom exception is created for invalid marks.

```python
class InvalidMarksError(Exception):

    pass
```

Marks must be between 0 and 100.

## 5. Lambda Functions

Lambda functions are used when sorting students.

```python
sorted(
    students,
    key=lambda student: student.average_marks(),
    reverse=True
)
```

Students are ranked according to their average marks.

## 6. reduce()

`reduce()` is used to calculate total marks.

```python
reduce(
    lambda first, second: first + second,
    self.marks
)
```

## 7. filter()

`filter()` is used to find students who passed.

```python
filter(
    lambda student: student.status() == "PASS",
    students
)
```

## 8. enumerate()

`enumerate()` is used to generate student rankings.

```python
for rank, student in enumerate(
    ranked_students,
    start=1
):
```

## 9. Context Manager

A custom context manager is used while generating the report.

```python
@contextmanager
def report_file(filename):

    ...
```

It ensures that the report file is properly closed.

## 10. File Handling

The project creates:

```text
student_result_report.txt
```

The report contains:

* Student ranking
* Marks
* Total
* Average
* Grade
* Status
* Passed students
* Grand total

## Grading System

The project uses the following grading system:

|  Average | Grade |
| -------: | :---: |
|   90–100 |   A+  |
|    80–89 |   A   |
|    70–79 |   B   |
|    60–69 |   C   |
|    50–59 |   D   |
| Below 50 |   F   |

## Passing Rule

```text
Average >= 40
→ PASS

Average < 40
→ FAIL
```

## Project Flow

```text
Student Data
     ↓
Validate Marks
     ↓
Create Student Objects
     ↓
Calculate Total
     ↓
Calculate Average
     ↓
Assign Grade
     ↓
Determine Status
     ↓
Sort Students
     ↓
Generate Ranking
     ↓
Filter Passed Students
     ↓
Generate Report
     ↓
Save Report
```

## Sample Student Data

```python
students = [

    Student(
        "Amir",
        [90, 85, 88, 92, 95]
    ),

    Student(
        "Rahul",
        [78, 82, 75, 80, 77]
    ),

    Student(
        "Aman",
        [35, 42, 38, 40, 36]
    ),

    Student(
        "Riya",
        [95, 96, 92, 94, 98]
    )
]
```

## Sample Output

```text
STUDENT RESULT MANAGEMENT SYSTEM
=============================================

1. Riya | Total: 475 | Average: 95.00 | Grade: A+ | Status: PASS
2. Amir | Total: 450 | Average: 90.00 | Grade: A+ | Status: PASS
3. Rahul | Total: 392 | Average: 78.40 | Grade: B | Status: PASS
4. Aman | Total: 191 | Average: 38.20 | Grade: F | Status: FAIL

PASSED STUDENTS
--------------------
Amir
Rahul
Riya

Creating report: student_result_report.txt
Report file closed.

Report saved successfully to student_result_report.txt
```

## Generated Report

The program generates:

```text
student_result_report.txt
```

Example:

```text
STUDENT RESULT MANAGEMENT SYSTEM
=============================================

1. Riya
   Marks: [95, 96, 92, 94, 98]
   Total: 475
   Average: 95.00
   Grade: A+
   Status: PASS

2. Amir
   Marks: [90, 85, 88, 92, 95]
   Total: 450
   Average: 90.00
   Grade: A+
   Status: PASS
```

## Project Structure

```text
Day-22/
│
├── main.py
├── mini_project.md
├── reflection.md
└── README.md
```

## How to Run

Open the Day-22 folder in VS Code.

Run:

```bash
python main.py
```

The program will display the student results in the terminal
and create the result report automatically.

## Learning Outcomes

After completing this project, I can:

* Create dataclasses.
* Use type hints.
* Create custom exceptions.
* Handle runtime errors.
* Use lambda functions.
* Use `reduce()`.
* Use `filter()`.
* Use `enumerate()`.
* Sort objects using custom keys.
* Create custom context managers.
* Work with files.
* Generate reports.
* Organize code into reusable functions.
* Apply clean-code principles.

## Challenges

The main challenges were:

1. Combining multiple advanced Python concepts.
2. Creating a custom exception.
3. Creating a custom context manager.
4. Using `reduce()` correctly.
5. Ranking objects using `sorted()` and lambda.
6. Generating a formatted report.
7. Keeping the project organized and readable.

## Future Improvements

The project can be improved by adding:

* User input.
* Interactive menu.
* CSV support.
* JSON support.
* Database integration.
* Subject-wise analysis.
* Attendance tracking.
* GUI interface.
* Web dashboard.
* Login system.
* Student search.
* Result editing.
* Result deletion.

## Advanced Concepts Checklist

* [x] Exception Handling
* [x] Custom Exception
* [x] Dataclass
* [x] Type Hints
* [x] Lambda
* [x] reduce()
* [x] filter()
* [x] enumerate()
* [x] sorted()
* [x] Context Manager
* [x] File Handling
* [x] Report Generation
* [x] Clean Code
* [x] DRY Principle

## Final Result

The Student Result Management System successfully combines
multiple Python Advanced concepts into a practical project.

This project helped me understand how individual Python
features can work together to build a structured application.

## Python Advanced Completion

Day 22 marks the completion of my Python Advanced phase in the
365 Days of Growth journey.

I am now ready to move forward toward:

* Data Structures
* Problem Solving
* SQL
* Data Analysis
* AI/ML
* Real-world Projects

## Author

**Md Amir Khan**


