DAY 20 — PYTHON ADVANCED
PART 2 — 30 MCQs


Q1. What is an iterator in Python?

A. A function that returns a list
B. An object that produces values one at a time
C. A module used for file handling
D. A variable that stores strings

Answer: B


Q2. Which function converts an iterable into an iterator?

A. next()
B. iterator()
C. iter()
D. convert()

Answer: C


Q3. Which function retrieves the next value from an iterator?

A. next()
B. get()
C. iter()
D. value()

Answer: A


Q4. Which exception is raised when an iterator has no more values?

A. ValueError
B. IndexError
C. StopIteration
D. IteratorError

Answer: C


Q5. Which methods are required for a custom iterator?

A. __start__() and __stop__()
B. __iter__() and __next__()
C. __begin__() and __end__()
D. start() and next()

Answer: B


Q6. Which keyword is used to create a generator?

A. generate
B. return
C. yield
D. produce

Answer: C


Q7. What happens when yield is executed?

A. The function terminates permanently
B. The function pauses and preserves its state
C. The program terminates
D. The variable is deleted

Answer: B


Q8. Which statement is TRUE about generators?

A. They always store all values in memory
B. They produce values lazily
C. They cannot be iterated
D. They can only produce one value

Answer: B


Q9. What is the output?

def numbers():
    yield 10
    yield 20

g = numbers()

print(next(g))

A. 10
B. 20
C. None
D. Error

Answer: A


Q10. What does a generator expression use?

A. {}
B. []
C. ()
D. <>

Answer: C


Q11. Which is a generator expression?

A. [x for x in range(5)]
B. (x for x in range(5))
C. {x for x in range(5)}
D. <x for x in range(5)>

Answer: B


Q12. What is the main advantage of generators?

A. Faster syntax
B. Better graphics
C. Memory efficiency
D. Automatic debugging

Answer: C


Q13. What is a decorator?

A. A variable
B. A function that modifies another function
C. A Python package
D. A data type

Answer: B


Q14. Which symbol is commonly used to apply a decorator?

A. #
B. $
C. @
D. &

Answer: C


Q15. What does this syntax mean?

@decorator
def greet():
    pass

A. decorator is ignored
B. greet is passed to decorator
C. decorator is a variable
D. greet becomes a class

Answer: B


Q16. Which concept allows functions to be passed as arguments?

A. First-class functions
B. Encapsulation
C. Inheritance
D. Polymorphism

Answer: A


Q17. What is a nested function?

A. A function inside another function
B. A function inside a class only
C. A function inside a loop
D. A function imported from another file

Answer: A


Q18. Why are *args commonly used in decorators?

A. To accept multiple positional arguments
B. To create a generator
C. To create a class
D. To stop a function

Answer: A


Q19. Why is **kwargs used in decorators?

A. To accept multiple keyword arguments
B. To create tuples
C. To create iterators
D. To handle exceptions

Answer: A


Q20. Which module provides functools.wraps?

A. collections
B. functools
C. itertools
D. decorators

Answer: B


Q21. What is the purpose of functools.wraps?

A. Creates a generator
B. Preserves metadata of the original function
C. Converts a list to tuple
D. Stops recursion

Answer: B


Q22. Which decorator can be used to measure execution time?

A. timer
B. iterator
C. generator
D. counter

Answer: A


Q23. What does the following return?

def test():
    yield 1
    yield 2

print(test())

A. 1
B. 2
C. A generator object
D. None

Answer: C


Q24. Which statement about return is correct?

A. It pauses a function
B. It terminates the current function
C. It creates an iterator
D. It creates a decorator

Answer: B


Q25. Which statement about yield is correct?

A. It permanently terminates the generator
B. It pauses the generator
C. It deletes the generator
D. It converts the generator into a list

Answer: B


Q26. What happens when next() is called repeatedly after a
generator is exhausted?

A. It starts again
B. It returns None
C. It raises StopIteration
D. It creates a new generator

Answer: C


Q27. Which is better for processing a huge dataset one item
at a time?

A. List
B. Generator
C. Tuple
D. String

Answer: B


Q28. What is the output?

def gen():
    yield 1
    yield 2
    yield 3

g = gen()

print(next(g))
print(next(g))

A. 1, 1
B. 1, 2
C. 2, 3
D. 1, 3

Answer: B


Q29. What does a logging decorator commonly do?

A. Deletes logs
B. Records information about function execution
C. Converts logs into generators
D. Creates database tables

Answer: B


Q30. Which statement best describes the relationship between
a generator and an iterator?

A. They are completely unrelated
B. A generator is a convenient way to create an iterator
C. An iterator is always a decorator
D. A generator cannot be iterated

Answer: B


QUICK ANSWER KEY

1.  B
2.  C
3.  A
4.  C
5.  B
6.  C
7.  B
8.  B
9.  A
10. C
11. B
12. C
13. B
14. C
15. B
16. A
17. A
18. A
19. A
20. B
21. B
22. A
23. C
24. B
25. B
26. C
27. B
28. B
29. B
30. B


