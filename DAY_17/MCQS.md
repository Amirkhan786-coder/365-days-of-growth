
# 🧠 DAY 17 / 365 — PYTHON ITERATORS & GENERATORS
# 📝 MCQs

> Multiple Choice Questions for Day 17 — Iterators & Generators 🚀

---

## Q1. What is an iterator?

A. A variable that stores data  
B. An object that produces values one at a time  
C. A function that creates classes  
D. A Python module  

**Answer: B**

---

## Q2. Which function is used to create an iterator from an iterable?

A. `next()`  
B. `iterator()`  
C. `iter()`  
D. `create()`  

**Answer: C**

---

## Q3. Which function is used to get the next value from an iterator?

A. `next()`  
B. `iter()`  
C. `yield()`  
D. `continue()`  

**Answer: A**

---

## Q4. What exception indicates that an iterator has no more values?

A. `ValueError`  
B. `IndexError`  
C. `StopIteration`  
D. `IteratorError`  

**Answer: C**

---

## Q5. Which two methods are commonly used to implement a custom iterator?

A. `__start__()` and `__stop__()`  
B. `__iter__()` and `__next__()`  
C. `__begin__()` and `__end__()`  
D. `__loop__()` and `__next__()`  

**Answer: B**

---

## Q6. What keyword is used to create a generator?

A. `generate`  
B. `generator`  
C. `yield`  
D. `return`  

**Answer: C**

---

## Q7. A generator is a special type of:

A. List  
B. Dictionary  
C. Iterator  
D. Class  

**Answer: C**

---

## Q8. What does `yield` do?

A. Terminates the program  
B. Pauses the generator and produces a value  
C. Deletes a variable  
D. Creates a class  

**Answer: B**

---

## Q9. What happens when a generator function is called?

A. It executes completely immediately  
B. It returns a generator object  
C. It returns a list  
D. It returns `None`  

**Answer: B**

---

## Q10. Which is a generator expression?

A. `[x * 2 for x in range(10)]`  
B. `{x * 2 for x in range(10)}`  
C. `(x * 2 for x in range(10))`  
D. `{x: x * 2 for x in range(10)}`  

**Answer: C**

---

## Q11. Which is generally more memory efficient for processing a large sequence?

A. List  
B. Generator  
C. Tuple  
D. String  

**Answer: B**

---

## Q12. What is lazy evaluation?

A. Calculating everything immediately  
B. Calculating values only when needed  
C. Deleting unused values  
D. Sorting values automatically  

**Answer: B**

---

## Q13. What will this code print?

```python
def numbers():
    yield 10
    yield 20

generator = numbers()

print(next(generator))
````

A. `20`
B. `10`
C. `None`
D. Error

**Answer: B**

---

## Q14. What will this code print?

```python
def numbers():
    yield 10
    yield 20

generator = numbers()

print(next(generator))
print(next(generator))
```

A.

```text
10
20
```

B.

```text
20
10
```

C.

```text
10
10
```

D. Error

**Answer: A**

---

## Q15. What happens when `next()` is called after a generator is exhausted?

A. It returns `None`
B. It starts again
C. It raises `StopIteration`
D. It returns `0`

**Answer: C**

---

## Q16. Which statement about `yield` is correct?

A. It always terminates the function
B. It pauses execution and remembers the state
C. It can only be used outside functions
D. It creates a list

**Answer: B**

---

## Q17. Which of the following is iterable?

A. List
B. String
C. Tuple
D. All of the above

**Answer: D**

---

## Q18. Is every iterable an iterator?

A. Yes
B. No
C. Only lists
D. Only strings

**Answer: B**

---

## Q19. Is every iterator a generator?

A. Yes
B. No
C. Only in Python 3
D. Only custom iterators

**Answer: B**

---

## Q20. What is the output?

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
```

A. `20`
B. `30`
C. `10`
D. Error

**Answer: C**

---

## Q21. What is the output?

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

A.

```text
10
20
```

B.

```text
20
30
```

C.

```text
10
30
```

D.

```text
30
20
```

**Answer: A**

---

## Q22. Which statement is true about a list?

A. A list is always an iterator
B. A list is iterable
C. A list cannot be iterated
D. A list is a generator

**Answer: B**

---

## Q23. Which code correctly creates an iterator?

A.

```python
numbers = [1, 2, 3]
iterator = next(numbers)
```

B.

```python
numbers = [1, 2, 3]
iterator = iter(numbers)
```

C.

```python
numbers = [1, 2, 3]
iterator = yield(numbers)
```

D.

```python
numbers = [1, 2, 3]
iterator = iterator(numbers)
```

**Answer: B**

---

## Q24. Which keyword is commonly used instead of `return` in a generator?

A. `break`
B. `yield`
C. `pass`
D. `continue`

**Answer: B**

---

## Q25. What is the main benefit of generators?

A. They always run faster
B. They reduce memory usage by generating values when needed
C. They automatically sort data
D. They convert data into lists

**Answer: B**

---

## Q26. What does `__iter__()` usually return in a custom iterator?

A. A string
B. A list
C. An iterator
D. An integer

**Answer: C**

---

## Q27. What should `__next__()` raise when there are no more values?

A. `ValueError`
B. `StopIteration`
C. `IndexError`
D. `TypeError`

**Answer: B**

---

## Q28. Which one creates an infinite generator?

A.

```python
def numbers():
    for i in range(10):
        yield i
```

B.

```python
def numbers():
    while True:
        yield 1
```

C.

```python
def numbers():
    return 1
```

D.

```python
def numbers():
    print(1)
```

**Answer: B**

---

## Q29. Which is better for processing millions of values one at a time?

A. Generator
B. Large list
C. Large tuple
D. Set

**Answer: A**

---

## Q30. What does this generator produce?

```python
def squares():
    for number in range(1, 4):
        yield number ** 2
```

A.

```text
1
2
3
```

B.

```text
1
4
9
```

C.

```text
2
4
6
```

D.

```text
1
8
27
```

**Answer: B**

---

## Q31. What does this generator produce?

```python
def even_numbers():
    for number in range(2, 7, 2):
        yield number
```

A.

```text
1
3
5
```

B.

```text
2
4
6
```

C.

```text
2
3
4
```

D.

```text
0
2
4
6
```

**Answer: B**

---

## Q32. Which of these uses lazy evaluation?

A. Generator
B. Normal integer
C. String literal
D. Boolean

**Answer: A**

---

## Q33. What is the difference between `return` and `yield`?

A. There is no difference
B. `return` ends the function, while `yield` pauses a generator
C. `yield` ends the function permanently
D. `return` creates an iterator

**Answer: B**

---

## Q34. Which syntax creates a generator expression?

A.

```python
[x for x in range(10)]
```

B.

```python
(x for x in range(10))
```

C.

```python
{x for x in range(10)}
```

D.

```python
{x: x for x in range(10)}
```

**Answer: B**

---

## Q35. What happens to a generator after it is exhausted?

A. It automatically restarts
B. It remains exhausted
C. It becomes a list
D. It becomes an integer

**Answer: B**

---

## Q36. Can a generator be used inside a `for` loop?

A. Yes
B. No
C. Only with lists
D. Only with tuples

**Answer: A**

---

## Q37. Which of the following is NOT a generator keyword?

A. `yield`
B. `return`
C. `next`
D. All of the above

**Answer: D**

---

## Q38. What is a generator pipeline?

A. A sequence of generators processing data step by step
B. A Python installation method
C. A type of database
D. A class inheritance technique

**Answer: A**

---

## Q39. Which real-world task is a good use case for generators?

A. Processing a huge file line by line
B. Changing a variable name
C. Creating a simple integer
D. Printing one message

**Answer: A**

---

## Q40. What is the most important advantage of lazy evaluation?

A. It uses more memory
B. It calculates everything immediately
C. It calculates values only when required
D. It deletes all values

**Answer: C**

---

# 🏆 SCORE YOURSELF

```text
35–40  → 🔥 Excellent
30–34  → 🚀 Very Good
25–29  → 💪 Good
20–24  → 📚 Need More Practice
Below 20 → 🔄 Revise Day 17
```

---

# 🎯 DAY 17 MCQ REVISION

```text
Iterable
    ↓
Iterator
    ↓
iter()
    ↓
next()
    ↓
StopIteration
    ↓
Generator
    ↓
yield
    ↓
Lazy Evaluation
    ↓
Memory Efficiency
    ↓
Generator Expression
```

---

# 🏆 DAY 17 MCQs COMPLETED

**40 MCQs — Python Iterators & Generators ✅**

**17 / 365 — Keep Growing 🚀**

