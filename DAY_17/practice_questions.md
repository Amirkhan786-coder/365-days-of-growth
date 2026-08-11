
# 🚀 DAY 17 / 365 — PYTHON ITERATORS & GENERATORS
# 🧪 PRACTICE QUESTIONS

> Practice is the key to turning knowledge into skill. 🚀

---

# 📚 TOPICS

1. Iterable
2. Iterator
3. `iter()`
4. `next()`
5. `StopIteration`
6. Custom Iterators
7. `__iter__()`
8. `__next__()`
9. Generators
10. `yield`
11. Generator Functions
12. Generator Expressions
13. Lazy Evaluation
14. Memory Efficiency
15. Infinite Generators

---

# 🟢 LEVEL 1 — BASIC QUESTIONS

## Q1. What is an iterable?

Write a short explanation of an iterable and give three examples.

---

## Q2. What is an iterator?

Explain what an iterator does.

---

## Q3. What is the purpose of `iter()`?

Write a program that converts a list into an iterator.

---

## Q4. What is the purpose of `next()`?

Create an iterator and print its first three values using `next()`.

---

## Q5. Create an iterator from a tuple.

Given:

```python
numbers = (10, 20, 30, 40, 50)
````

Convert it into an iterator and print all values using `next()`.

---

## Q6. What happens when `next()` is called after the iterator is exhausted?

Explain the `StopIteration` exception.

---

## Q7. Write a program that safely handles `StopIteration`.

Use `try` and `except`.

---

## Q8. Create an iterator from a string.

Given:

```python
name = "PYTHON"
```

Print every character using an iterator.

---

## Q9. Create an iterator from a range.

Create an iterator for:

```python
range(1, 6)
```

Print all values.

---

## Q10. What is the difference between an iterable and an iterator?

Explain with an example.

---

# 🟡 LEVEL 2 — INTERMEDIATE QUESTIONS

## Q11. Create a custom iterator that prints numbers from 1 to 10.

Your class should contain:

```python
__iter__()
__next__()
```

---

## Q12. Create a custom iterator for even numbers.

The iterator should generate:

```text
2
4
6
8
10
```

---

## Q13. Create a custom iterator for odd numbers.

The iterator should generate:

```text
1
3
5
7
9
```

---

## Q14. Create a custom iterator that counts backwards.

For example:

```text
10
9
8
7
6
...
1
```

---

## Q15. Create a custom iterator that generates the first 10 natural numbers.

Expected output:

```text
1
2
3
4
5
6
7
8
9
10
```

---

## Q16. Create a generator that generates numbers from 1 to 10.

Use `yield`.

---

## Q17. Create a generator that generates even numbers from 2 to 20.

---

## Q18. Create a generator that generates odd numbers from 1 to 19.

---

## Q19. Create a generator for the multiplication table of a number.

Example:

```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

## Q20. Create a generator that generates squares from 1 to 10.

Expected values:

```text
1
4
9
16
25
...
100
```

---

# 🟠 LEVEL 3 — GENERATOR PRACTICE

## Q21. Create a generator for cubes.

Generate cubes from 1 to 10.

---

## Q22. Create a generator for Fibonacci numbers.

Generate the first 10 Fibonacci numbers.

Expected output:

```text
0
1
1
2
3
5
8
13
21
34
```

---

## Q23. Create a generator that generates numbers divisible by 5.

Generate values from 1 to 100 that are divisible by 5.

---

## Q24. Create a generator that generates prime numbers.

Generate prime numbers between 1 and 50.

---

## Q25. Create a generator that generates the reverse of a string.

Given:

```python
text = "PYTHON"
```

Generate:

```text
N
O
H
T
Y
P
```

---

## Q26. Create a generator that reads a list one element at a time.

Given:

```python
numbers = [10, 20, 30, 40, 50]
```

Generate each number separately.

---

## Q27. Create a generator for positive numbers.

Given:

```python
numbers = [-5, 10, -3, 20, 30, -7]
```

Generate only:

```text
10
20
30
```

---

## Q28. Create a generator for even numbers from a list.

Given:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
```

Generate:

```text
2
4
6
8
```

---

## Q29. Create a generator for words longer than 5 characters.

Given:

```python
words = [
    "Python",
    "AI",
    "Programming",
    "Code",
    "MachineLearning"
]
```

Generate only words longer than 5 characters.

---

## Q30. Create a generator that filters numbers greater than 50.

Given:

```python
numbers = [10, 60, 20, 80, 30, 100]
```

Expected output:

```text
60
80
100
```

---

# 🔵 LEVEL 4 — GENERATOR EXPRESSIONS

## Q31. Create a generator expression for squares from 1 to 10.

---

## Q32. Create a generator expression for even numbers from 1 to 20.

---

## Q33. Create a generator expression for numbers divisible by 3.

---

## Q34. Create a generator expression for cubes from 1 to 10.

---

## Q35. Convert the following list comprehension into a generator expression.

```python
numbers = [x * 2 for x in range(10)]
```

---

# 🟣 LEVEL 5 — CONCEPTUAL QUESTIONS

## Q36. What is the difference between `yield` and `return`?

Explain with examples.

---

## Q37. Why are generators memory efficient?

Explain in your own words.

---

## Q38. What is lazy evaluation?

Explain how generators use lazy evaluation.

---

## Q39. Why does a generator remember its state?

Explain the role of `yield`.

---

## Q40. What happens when a generator function is called?

Explain what object is returned.

---

# 🔴 LEVEL 6 — CHALLENGE QUESTIONS

## Q41. Create an infinite generator.

Generate:

```text
1
2
3
4
5
...
```

Use `while True`.

---

## Q42. Create an infinite even-number generator.

Generate:

```text
2
4
6
8
10
...
```

---

## Q43. Create an infinite Fibonacci generator.

Generate Fibonacci numbers continuously.

---

## Q44. Create a generator that generates numbers from 1 to 100 but skips multiples of 3.

---

## Q45. Create a generator that generates only prime numbers.

The generator should continue producing prime numbers.

---

## Q46. Create a generator that reads a large list in chunks.

For example, divide:

```python
numbers = list(range(1, 101))
```

into chunks of 10 values.

---

## Q47. Create a generator that processes a large file line by line.

The generator should return one line at a time instead of loading the entire file into memory.

---

## Q48. Create a generator that filters log messages.

Given a list of logs, generate only messages containing:

```text
ERROR
```

---

## Q49. Create a generator that calculates running totals.

Given:

```python
numbers = [10, 20, 30, 40]
```

Expected output:

```text
10
30
60
100
```

---

## Q50. Create a generator pipeline.

Create three generators:

```text
Input
  ↓
Filter
  ↓
Transform
  ↓
Output
```

Use them together to process numbers.

---

# 🏆 FINAL CHALLENGE

## Q51. Build a Number Processing Generator System

Create a Python program that:

1. Takes numbers from a list.
2. Generates only even numbers.
3. Squares those numbers.
4. Filters squares greater than 50.
5. Produces the final values using generators.

Example input:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
```

Expected process:

```text
Input
  ↓
Even Numbers
  ↓
Square
  ↓
Greater Than 50
  ↓
Final Generator
```

---

# 🎯 PRACTICE CHECKLIST

* [ ] Iterable
* [ ] Iterator
* [ ] `iter()`
* [ ] `next()`
* [ ] `StopIteration`
* [ ] Custom Iterator
* [ ] `__iter__()`
* [ ] `__next__()`
* [ ] Generator
* [ ] `yield`
* [ ] Generator Function
* [ ] Generator Expression
* [ ] `yield` vs `return`
* [ ] Lazy Evaluation
* [ ] Memory Efficiency
* [ ] Infinite Generator
* [ ] Generator Pipeline

---

# 🏆 DAY 17 PRACTICE GOAL

```text
50+ Practice Questions
        ↓
Basic Iterators
        ↓
Custom Iterators
        ↓
Generators
        ↓
Generator Expressions
        ↓
Lazy Evaluation
        ↓
Memory Efficiency
        ↓
Advanced Generator Problems
        ↓
Final Challenge 🚀
```

---

# 🔥 365 DAYS OF GROWTH

**Day 17 — Practice Completed 🚀**

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

