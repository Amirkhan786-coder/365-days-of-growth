DAY 21 — PYTHON ADVANCED
30 PRACTICE QUESTIONS


CONTEXT MANAGERS

Q1. Write a program using the `with` statement to read a text
file.

Q2. Create a custom context manager using `__enter__()` and
`__exit__()`.

Q3. Create a context manager that prints "Starting" when
entering and "Finished" when leaving the context.

Q4. Create a context manager that measures the execution time
of a block of code.

Q5. Use `@contextmanager` from the `contextlib` module to
create a custom context manager.


MODULES AND PACKAGES

Q6. Create a module named `math_utils.py` containing functions
for addition, subtraction, multiplication, and division.

Q7. Import the functions from `math_utils.py` into another
Python file and use them.

Q8. Create a package named `utilities` containing two modules:
`math_utils.py` and `string_utils.py`.

Q9. Write a program demonstrating the difference between
`import module` and `from module import function`.

Q10. Create a Python file containing a `main()` function and
use `if __name__ == "__main__":` correctly.


TYPE HINTS

Q11. Write a function that accepts two integers and returns
their sum using type hints.

Q12. Write a function that accepts a list of integers and
returns their average using type hints.

Q13. Create a function that accepts a string and returns a
boolean using type hints.

Q14. Create a dictionary with type hints representing a
student's name, age, and marks.

Q15. Create a function using type hints that accepts a list of
strings and returns the longest string.


DATACLASSES

Q16. Create a `Student` dataclass with:

name
age
course

Create and display a student object.

Q17. Create a `Product` dataclass with:

name
price
quantity

Calculate the total price.

Q18. Create a dataclass with default values.

Q19. Create a list containing five dataclass objects and print
their information.

Q20. Create a `BankAccount` dataclass containing:

account_holder
balance

Add methods for deposit and withdrawal.


LAMBDA, MAP, FILTER AND REDUCE

Q21. Use a lambda function to calculate the square of every
number from 1 to 10.

Q22. Use `map()` to convert a list of Celsius temperatures to
Fahrenheit.

Q23. Use `filter()` to extract all even numbers from a list.

Q24. Use `filter()` to extract all strings longer than five
characters.

Q25. Use `reduce()` to calculate the product of all numbers in
a list.


ENUMERATE AND ZIP

Q26. Use `enumerate()` to print student names with numbers
starting from 1.

Q27. Use `zip()` to combine a list of names and marks and print
each student's information.

Q28. Use `zip()` to create a dictionary from two lists:

keys
values


COPYING AND CLEAN CODE

Q29. Create a program demonstrating the difference between
shallow copy and deep copy using a nested list.

Q30. Create a small Python program that follows PEP 8 and DRY
principles.

The program should:

- Use meaningful variable names.
- Use reusable functions.
- Use type hints.
- Avoid repeated code.
- Handle invalid input.
- Keep the code organized.


CHALLENGE TASK

Build a small "Student Performance Analyzer" that combines:

- Dataclass
- Type hints
- Lambda
- map()
- filter()
- enumerate()
- zip()
- reduce()
- Context manager

The program should:

1. Store student information using a dataclass.
2. Accept student marks.
3. Calculate average marks.
4. Filter students who passed.
5. Display students with their ranking.
6. Calculate total marks.
7. Save the final report to a file using a context manager.

