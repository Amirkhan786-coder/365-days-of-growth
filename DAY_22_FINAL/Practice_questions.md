DAY 22 — PYTHON ADVANCED
PART 4 — 30 FINAL CODING QUESTIONS


EXCEPTION HANDLING

Q1. Write a program that accepts two numbers and handles
division by zero.

Q2. Write a program that accepts an integer from the user and
handles invalid input using ValueError.

Q3. Create a custom exception called InvalidMarksError.
Raise it when marks are below 0 or above 100.

Q4. Write a program that uses try, except, else, and finally
together.

Q5. Create a function that validates a user's age and raises
a custom exception if the age is invalid.


ITERATORS AND GENERATORS

Q6. Create a custom iterator that generates numbers from 1 to
10.

Q7. Create a generator that produces the first 10 even numbers.

Q8. Create a generator that generates Fibonacci numbers.

Q9. Create a generator that reads a large text file line by
line.

Q10. Create a generator that produces squares of numbers from
1 to 20.


DECORATORS

Q11. Create a decorator that prints "Function Started" before
a function and "Function Finished" after it.

Q12. Create a decorator that measures the execution time of a
function.

Q13. Create a decorator that logs the name of the function
being executed.

Q14. Create a decorator that checks whether a number passed to
a function is positive.

Q15. Create a decorator that counts how many times a function
has been called.


CONTEXT MANAGERS

Q16. Create a custom context manager for opening and closing a
file.

Q17. Create a context manager that prints "Start" when entering
and "End" when leaving the context.

Q18. Create a context manager using @contextmanager that
temporarily changes a variable and restores its original value
after the block.


MODULES AND TYPE HINTS

Q19. Create a module named calculator.py containing functions
for addition, subtraction, multiplication, and division.

Q20. Create a package containing:

math_utils.py
string_utils.py

Import and use functions from both modules.

Q21. Create a function using type hints that accepts a list of
integers and returns the maximum value.

Q22. Create a function using type hints that accepts a
dictionary of student names and marks and returns the average
marks.


DATACLASSES

Q23. Create a Student dataclass containing:

name
age
course
marks

Add a method that calculates average marks.

Q24. Create a Product dataclass containing:

name
price
quantity

Add a method that calculates total price.

Q25. Create a BankAccount dataclass with deposit and withdrawal
methods.


FUNCTIONAL PROGRAMMING

Q26. Use lambda and map() to calculate the cubes of numbers
from 1 to 10.

Q27. Use filter() to find all numbers divisible by 3 from a
list.

Q28. Use reduce() to calculate the sum of all numbers in a list.

Q29. Use enumerate() and zip() together to display student
rankings with their names and marks.


FINAL CHALLENGE

Q30. Build a complete "Student Result Management System".

The project should:

- Use a dataclass for student information.
- Accept student names and marks.
- Validate marks using exception handling.
- Calculate total marks.
- Calculate average marks.
- Assign grades.
- Determine pass/fail status.
- Rank students.
- Use lambda functions.
- Use filter().
- Use reduce().
- Use enumerate().
- Use zip().
- Use a custom context manager.
- Save the final result to a text file.
- Use type hints.
- Follow PEP 8.
- Avoid repeated code using the DRY principle.


FINAL CHALLENGE REQUIREMENTS

Student fields:

name
marks


The program should calculate:

Total
Average
Grade
Status
Rank


Suggested grading:

90–100 → A+
80–89  → A
70–79  → B
60–69  → C
50–59  → D
Below 50 → F


Suggested passing rule:

Average >= 40 → PASS

Average < 40 → FAIL


EXPECTED PROJECT FLOW

User Input
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
Determine Pass/Fail
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


FINAL DAY 22 PRACTICE CHECKLIST

[ ] Exception Handling
[ ] Custom Exceptions
[ ] Iterators
[ ] Generators
[ ] Decorators
[ ] Context Managers
[ ] Modules
[ ] Packages
[ ] Type Hints
[ ] Dataclasses
[ ] Lambda
[ ] map()
[ ] filter()
[ ] reduce()
[ ] enumerate()
[ ] zip()
[ ] File Handling
[ ] PEP 8
[ ] DRY
[ ] Clean Code
[ ] Final Project
