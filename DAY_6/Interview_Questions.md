# 🚀 DAY 06 — PYTHON TUPLES
# 🎤 INTERVIEW QUESTIONS & ANSWERS

## 365 Days of Growth

---

## 1. What is a Tuple in Python?

A Tuple is an ordered collection of elements in Python.

Example:

```python
numbers = (10, 20, 30)
```

---

## 2. What is the main difference between List and Tuple?

The main difference is:

```text
List  → Mutable
Tuple → Immutable
```

A List can be modified after creation, while a Tuple cannot normally be modified.

---

## 3. What does immutable mean?

Immutable means that the existing Tuple elements cannot be changed after the Tuple is created.

Example:

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This produces a `TypeError`.

---

## 4. How do you create a Tuple?

Using parentheses:

```python
numbers = (10, 20, 30)
```

---

## 5. How do you create an empty Tuple?

```python
numbers = ()
```

---

## 6. How do you create a single-element Tuple?

A comma is required:

```python
number = (10,)
```

Without the comma:

```python
number = (10)
```

This is an integer, not a Tuple.

---

## 7. Does a Tuple support indexing?

Yes.

Example:

```python
numbers = (10, 20, 30)

print(numbers[0])
```

Output:

```text
10
```

---

## 8. Does a Tuple support negative indexing?

Yes.

Example:

```python
numbers = (10, 20, 30)

print(numbers[-1])
```

Output:

```text
30
```

---

## 9. Does a Tuple support slicing?

Yes.

Example:

```python
numbers = (10, 20, 30, 40)

print(numbers[1:3])
```

Output:

```text
(20, 30)
```

---

## 10. Can a Tuple contain duplicate values?

Yes.

Example:

```python
numbers = (10, 20, 10, 30)
```

Duplicate values are allowed.

---

## 11. Can a Tuple contain different data types?

Yes.

Example:

```python
data = ("Amir", 20, 85.5, True)
```

---

## 12. Can a Tuple contain another Tuple?

Yes.

This is called a Nested Tuple.

Example:

```python
data = (
    ("Amir", 101),
    ("Rahul", 102)
)
```

---

## 13. How do you find the length of a Tuple?

Use `len()`.

```python
numbers = (10, 20, 30)

print(len(numbers))
```

---

## 14. What is Tuple Packing?

Tuple packing means storing multiple values together in a Tuple.

Example:

```python
student = "Amir", 101, 85
```

Python automatically creates a Tuple.

---

## 15. What is Tuple Unpacking?

Tuple unpacking means assigning Tuple elements to separate variables.

Example:

```python
student = ("Amir", 101, 85)

name, roll, marks = student
```

---

## 16. What happens if the number of variables doesn't match the Tuple elements during unpacking?

Python raises a `ValueError`.

Example:

```python
student = ("Amir", 101, 85)

name, roll = student
```

There are three values but only two variables.

---

## 17. Which methods are commonly available for Tuples?

Two commonly used Tuple methods are:

```python
count()
index()
```

---

## 18. What does `count()` do?

It counts how many times a particular element occurs.

Example:

```python
numbers = (10, 20, 10, 30)

print(numbers.count(10))
```

Output:

```text
2
```

---

## 19. What does `index()` do?

It returns the index of the first occurrence of an element.

Example:

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

Output:

```text
1
```

---

## 20. Can we use `append()` with a Tuple?

No.

Tuples are immutable and do not have an `append()` method.

---

## 21. Can we sort a Tuple directly using `sort()`?

No.

Tuple does not have the `sort()` method.

If required, convert it to a List first.

Example:

```python
numbers = (30, 10, 20)

numbers_list = list(numbers)

numbers_list.sort()

numbers = tuple(numbers_list)

print(numbers)
```

---

## 22. How do you convert a List into a Tuple?

Use `tuple()`.

```python
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
```

---

## 23. How do you convert a Tuple into a List?

Use `list()`.

```python
numbers = (10, 20, 30)

result = list(numbers)

print(result)
```

---

## 24. Can two Tuples be combined?

Yes.

Use the `+` operator.

```python
a = (1, 2)
b = (3, 4)

result = a + b

print(result)
```

---

## 25. Can a Tuple be repeated?

Yes.

Use the `*` operator.

```python
numbers = (1, 2)

print(numbers * 3)
```

Output:

```text
(1, 2, 1, 2, 1, 2)
```

---

# 🔥 IMPORTANT INTERVIEW QUESTIONS

## 26. Why would you use a Tuple instead of a List?

We use a Tuple when the data should remain fixed and should not normally be changed.

Example:

```python
coordinates = (28.61, 77.20)
```

---

## 27. Is a Tuple faster than a List?

In general, Tuples can have lower overhead than Lists because they are immutable. For fixed collections, this can make Tuples a suitable choice.

---

## 28. Are Tuples ordered?

Yes.

Tuple elements maintain their order.

Example:

```python
numbers = (10, 20, 30)
```

The order remains:

```text
10 → 20 → 30
```

---

## 29. Are Tuples mutable?

No.

Tuples are immutable.

---

## 30. Are Tuples hashable?

A Tuple can be hashable if all of its elements are hashable.

For example:

```python
data = (10, 20, 30)
```

can be used as a dictionary key.

But a Tuple containing a List generally cannot be hashed because the List is mutable.

---

## 31. Can a Tuple be used as a Dictionary key?

Yes, if all elements inside the Tuple are hashable.

Example:

```python
location = {
    (10, 20): "Point A"
}

print(location[(10, 20)])
```

---

## 32. What is a Nested Tuple?

A Tuple containing another Tuple is called a Nested Tuple.

Example:

```python
students = (
    ("Amir", 101),
    ("Rahul", 102)
)
```

---

## 33. How can you loop through a Tuple?

Using a `for` loop.

```python
numbers = (10, 20, 30)

for number in numbers:
    print(number)
```

---

## 34. How do you check whether an element exists in a Tuple?

Use the `in` operator.

```python
numbers = (10, 20, 30)

if 20 in numbers:
    print("Found")
```

---

## 35. Can a Tuple contain a List?

Yes.

Example:

```python
data = ([1, 2, 3], "Python")
```

The Tuple structure remains immutable, but the List inside it can be modified.

---

# 🧠 OUTPUT-BASED INTERVIEW QUESTIONS

## 36. What is the output?

```python
x = (10, 20, 30)

print(x[1])
```

**Answer:**

```text
20
```

---

## 37. What is the output?

```python
x = (10, 20, 30)

print(x[-1])
```

**Answer:**

```text
30
```

---

## 38. What is the output?

```python
x = (1, 2, 3)

print(x * 2)
```

**Answer:**

```text
(1, 2, 3, 1, 2, 3)
```

---

## 39. What is the output?

```python
x = (10, 20, 10, 30)

print(x.count(10))
```

**Answer:**

```text
2
```

---

## 40. What is the output?

```python
x = ("Python", "Java", "C++")

a, b, c = x

print(b)
```

**Answer:**

```text
Java
```

---

# 🎯 QUICK INTERVIEW REVISION

Remember these points:

```text
Tuple
  ↓
Ordered
  ↓
Immutable
  ↓
Supports Indexing
  ↓
Supports Slicing
  ↓
Allows Duplicates
  ↓
Allows Different Data Types
  ↓
Supports Packing & Unpacking
  ↓
count() + index()
```

---

# 💡 BEST INTERVIEW ANSWER

### Question:

**"Why would you use a Tuple instead of a List?"**

### Answer:

> "I would use a Tuple when I have a collection of values that should remain fixed and should not be modified during the program."

---

# 🏆 DAY 06 INTERVIEW TARGET

Practice answering these questions **without looking at the answers**.

Especially remember:

1. List vs Tuple
2. Mutable vs Immutable
3. Tuple Packing
4. Tuple Unpacking
5. Indexing
6. Slicing
7. `count()`
8. `index()`
9. Nested Tuple
10. Tuple vs List use cases

---

# 🚀 DAY 06 INTERVIEW GOAL

**Understand → Explain → Code → Answer Confidently**