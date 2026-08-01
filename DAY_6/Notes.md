# 🚀 DAY 06 — PYTHON TUPLES

## 365 Days of Growth

---

# 📚 1. What is a Tuple?

A Tuple is an ordered collection of elements in Python.

Tuples are similar to Lists, but the main difference is:

> **Tuples are immutable.**

This means once a Tuple is created, its elements cannot be changed.

Example:

```python
numbers = (10, 20, 30, 40)

print(numbers)
```

Output:

```text
(10, 20, 30, 40)
```

---

# 🔹 2. Creating a Tuple

Tuples are generally created using parentheses `()`.

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits)
```

Output:

```text
('Apple', 'Banana', 'Mango')
```

---

# 🔹 3. Empty Tuple

An empty Tuple can be created using:

```python
my_tuple = ()

print(my_tuple)
```

Output:

```text
()
```

---

# 🔹 4. Single Element Tuple

A single-element Tuple requires a comma.

Correct:

```python
number = (10,)

print(number)
```

Incorrect:

```python
number = (10)
```

The second example is simply an integer, not a Tuple.

Check:

```python
number = (10,)

print(type(number))
```

Output:

```text
<class 'tuple'>
```

---

# 🔹 5. Tuple Without Parentheses

Python also allows tuple creation without parentheses.

```python
numbers = 10, 20, 30

print(numbers)
```

Output:

```text
(10, 20, 30)
```

This is called **Tuple Packing**.

---

# 🔹 6. Tuple Indexing

Tuple indexing works like List indexing.

Python indexing starts from `0`.

```python
numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

Index positions:

```text
10 → 0
20 → 1
30 → 2
40 → 3
```

---

# 🔹 7. Negative Indexing

Negative indexing starts from the end.

```python
numbers = (10, 20, 30, 40)

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

Position:

```text
10 → -4
20 → -3
30 → -2
40 → -1
```

---

# 🔹 8. Tuple Slicing

Tuple slicing is used to extract a portion of a Tuple.

Syntax:

```python
tuple[start:stop]
```

Example:

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

---

# 🔹 9. Tuple Slicing with Step

Syntax:

```python
tuple[start:stop:step]
```

Example:

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[::2])
```

Output:

```text
(10, 30, 50)
```

---

# 🔹 10. Reverse a Tuple

We can use slicing to reverse a Tuple.

```python
numbers = (10, 20, 30, 40)

print(numbers[::-1])
```

Output:

```text
(40, 30, 20, 10)
```

---

# 🔹 11. Tuple is Immutable

This is one of the most important properties of Tuples.

Example:

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This will produce:

```text
TypeError
```

because Tuple elements cannot be modified.

---

# 🔹 12. Accessing Tuple Elements

We can access elements using indexes.

```python
student = ("Amir", 20, "AIML")

print(student[0])
print(student[1])
print(student[2])
```

Output:

```text
Amir
20
AIML
```

---

# 🔹 13. Tuple Length

Use the `len()` function.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

Output:

```text
4
```

---

# 🔹 14. Checking an Element

Use the `in` operator.

```python
fruits = ("Apple", "Banana", "Mango")

print("Apple" in fruits)
```

Output:

```text
True
```

Example:

```python
print("Orange" in fruits)
```

Output:

```text
False
```

---

# 🔹 15. Tuple Looping

We can use a `for` loop to access every element.

```python
fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Mango
```

---

# 🔹 16. Tuple Packing

Tuple packing means putting multiple values into a Tuple.

```python
student = "Amir", 101, 85

print(student)
```

Output:

```text
('Amir', 101, 85)
```

---

# 🔹 17. Tuple Unpacking

Tuple unpacking means assigning Tuple elements to separate variables.

```python
student = ("Amir", 101, 85)

name, roll, marks = student

print(name)
print(roll)
print(marks)
```

Output:

```text
Amir
101
85
```

---

# 🔹 18. Extended Tuple Unpacking

The `*` operator can be used during unpacking.

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
10
[20, 30, 40]
50
```

---

# 🔹 19. Tuple count()

`count()` returns how many times a value appears.

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

Output:

```text
3
```

---

# 🔹 20. Tuple index()

`index()` returns the position of the first occurrence.

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits.index("Mango"))
```

Output:

```text
2
```

---

# 🔹 21. Nested Tuple

A Tuple can contain another Tuple.

Example:

```python
data = (
    ("Amir", 101),
    ("Rahul", 102)
)

print(data)
```

---

# 🔹 22. Accessing Nested Tuple

```python
data = (
    ("Amir", 101),
    ("Rahul", 102)
)

print(data[0][0])
print(data[1][1])
```

Output:

```text
Amir
102
```

---

# 🔹 23. Tuple with Different Data Types

A Tuple can contain different types of data.

```python
data = ("Amir", 20, 85.5, True)

print(data)
```

---

# 🔹 24. Duplicate Values in Tuple

Tuples can contain duplicate values.

```python
numbers = (10, 20, 10, 30, 20)

print(numbers)
```

Output:

```text
(10, 20, 10, 30, 20)
```

---

# 🔹 25. Tuple Concatenation

Two Tuples can be joined using `+`.

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)
```

Output:

```text
(1, 2, 3, 4, 5, 6)
```

---

# 🔹 26. Tuple Repetition

The `*` operator can repeat a Tuple.

```python
numbers = (1, 2)

print(numbers * 3)
```

Output:

```text
(1, 2, 1, 2, 1, 2)
```

---

# 🔹 27. Convert List into Tuple

Use the `tuple()` function.

```python
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
```

Output:

```text
(10, 20, 30)
```

---

# 🔹 28. Convert Tuple into List

Use the `list()` function.

```python
numbers = (10, 20, 30)

result = list(numbers)

print(result)
```

Output:

```text
[10, 20, 30]
```

---

# 🔹 29. Tuple vs List

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[]` | `()` |
| Mutable | Yes | No |
| Ordered | Yes | Yes |
| Duplicates | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| Methods | Many | Few |
| Data Change | Allowed | Not allowed |

---

# 🔹 30. Why Use Tuples?

Tuples are useful when data should not be changed accidentally.

Example:

```python
coordinates = (28.61, 77.20)
```

Coordinates can be represented as a Tuple because they are naturally grouped together.

---

# 🔹 31. Tuple in Real-World Programming

Tuples can represent fixed groups of related information.

Example:

```python
student = ("Amir", 101, "AIML")
```

Here:

```text
Name     → Amir
Roll No  → 101
Course   → AIML
```

---

# 🔹 32. Tuple in AI/ML

Tuples are useful for storing fixed information such as:

```python
image_size = (224, 224, 3)
```

This can represent:

```text
Height = 224
Width  = 224
Channels = 3
```

Another example:

```python
coordinates = (10.5, 20.8)
```

---

# 🔹 33. Tuple Methods

Tuples have two commonly used methods:

### count()

```python
numbers.count(10)
```

### index()

```python
numbers.index(10)
```

---

# 🔹 34. Built-in Functions with Tuples

Some useful Python functions:

```python
len()
max()
min()
sum()
```

Example:

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

Output:

```text
4
40
10
100
```

---

# 🔹 35. Important Point

A Tuple itself is immutable, but it can contain mutable objects.

Example:

```python
data = ([1, 2, 3], "Python")

data[0].append(4)

print(data)
```

Output:

```text
([1, 2, 3, 4], 'Python')
```

The Tuple structure cannot be changed, but the List inside it can be modified.

---

# 🧠 Important Rules to Remember

```text
1. Tuple is ordered.
2. Tuple is immutable.
3. Indexing starts from 0.
4. Negative indexing starts from -1.
5. Tuple supports slicing.
6. Duplicate values are allowed.
7. Different data types can be stored.
8. A single-element Tuple needs a comma.
9. Tuple supports packing and unpacking.
10. Tuple has count() and index() methods.
```

---

# 🎯 Quick Revision

### List:

```python
numbers = [10, 20, 30]
```

Can be changed:

```python
numbers[0] = 100
```

### Tuple:

```python
numbers = (10, 20, 30)
```

Cannot be changed:

```python
numbers[0] = 100
```

This produces:

```text
TypeError
```

---

# 🔥 Day 06 Key Takeaway

> **Lists are mutable, while Tuples are immutable.**

Understanding this difference is one of the most important concepts of Python data structures.

---

# 🚀 Day 06 Learning Formula

```text
LEARN
   ↓
UNDERSTAND
   ↓
PRACTICE
   ↓
BUILD
   ↓
DOCUMENT
   ↓
PUSH TO GITHUB
```

**Python Tuples — Day 06 Complete Notes ✅**