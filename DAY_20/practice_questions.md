DAY 20 — PYTHON ADVANCED

PART 4 — 30 PRACTICE QUESTIONS


ITERATORS


Q1. Create an iterator from the following list and print all
elements using next():

numbers = [10, 20, 30, 40, 50]


Q2. Write a program that manually iterates over a tuple using
iter() and next().


Q3. Write a program that catches StopIteration when an
iterator is exhausted.


Q4. Create a custom iterator class that generates numbers
from 1 to 10.


Q5. Create a custom iterator that generates even numbers from
2 to 20.


Q6. Create a custom iterator that generates the first 10
square numbers.

Expected sequence:

1, 4, 9, 16, ...


Q7. Create a custom iterator that counts backward from 10 to 1.


Q8. Create an iterator for a string and print each character
using next().


Q9. Create an iterator for a dictionary and print all its keys
using next().


Q10. Write a program that checks whether an object is iterable
or not.


GENERATORS


Q11. Create a generator that produces numbers from 1 to 10.


Q12. Create a generator that produces only even numbers from
1 to 20.


Q13. Create a generator that produces the squares of numbers
from 1 to 10.


Q14. Create a generator that produces the cubes of numbers
from 1 to 10.


Q15. Create a generator that produces Fibonacci numbers.


Q16. Create an infinite generator that produces numbers
starting from 1.


Q17. Create a generator that reads a file line by line.


Q18. Create a generator that receives a list and yields only
positive numbers.


Q19. Create a generator that receives a list and yields only
even numbers.


Q20. Create a generator expression that produces the squares
of numbers from 1 to 20.


DECORATORS


Q21. Create a basic decorator that prints "Function Started"
before executing a function.


Q22. Create a decorator that prints "Function Completed"
after executing a function.


Q23. Create a decorator that prints the name of the function
being executed.


Q24. Create a decorator that accepts *args and **kwargs.


Q25. Create a decorator that measures the execution time of
a function.


Q26. Create a logging decorator that prints:

Function name
Arguments
Result


Q27. Create a decorator that allows a function to execute only
if a condition is True.


Q28. Create a decorator that runs a function three times.


Q29. Create two decorators and apply both to the same function.


Q30. Create a complete program combining:

• Generator
• Decorator
• Counter

The program should generate numbers, process them using a
decorated function, and count the generated values.


CHALLENGE QUESTIONS


Challenge 1:

Create a generator that produces Fibonacci numbers
indefinitely.

Use next() to print the first 15 numbers.


Challenge 2:

Create a timer decorator and apply it to a function that
calculates the sum of numbers from 1 to 1,000,000.


Challenge 3:

Create a custom iterator that generates prime numbers.

Generate the first 10 prime numbers.


Challenge 4:

Create a decorator called @validate_positive that allows a
function to execute only when all numeric arguments are
positive.


Challenge 5:

Create a generator that reads a large text file and yields
only lines containing the word "ERROR".


