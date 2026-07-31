# 🚀 365 Days of Growth
# 📖 Day 005 - Python Lists (Part A)

**Author:** Md Amir Khan  
**Day:** 005/365

---

# 📌 Chapter 1 - Introduction to Python Lists

## What is a List?

A List is one of the most powerful built-in data structures in Python.

A List is used to store multiple values in a single variable.

Unlike variables that store only one value, Lists can store many values together.

Lists are:

- Ordered
- Mutable (can be changed)
- Allow duplicate values
- Can store different data types

Example

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

# Why Do We Need Lists?

Imagine storing marks of 100 students.

Without List

```python
mark1 = 90
mark2 = 85
mark3 = 78
...
```

Very difficult.

Using List

```python
marks = [90,85,78]
```

Easy to manage.

---

# Real Life Examples

Python Lists are used in

- Student Marks
- Shopping Cart
- Mobile Contacts
- Product Lists
- Attendance System
- Online Food Orders
- Employee Records

---

# Characteristics of Lists

✔ Ordered

Elements maintain order.

Example

```python
colors = ["Red","Green","Blue"]
```

Output

```
Red
Green
Blue
```

---

✔ Mutable

We can modify elements.

Example

```python
colors[1] = "Yellow"
```

Output

```
['Red', 'Yellow', 'Blue']
```

---

✔ Duplicate Allowed

```python
numbers = [10,20,20,30]
```

Output

```
[10,20,20,30]
```

---

✔ Different Data Types

```python
data = ["Amir",19,8.7,True]
```

Python allows storing multiple data types.

---

# Creating Lists

Method 1

```python
fruits = ["Apple","Banana","Orange"]
```

Method 2

```python
numbers = list((1,2,3,4))
```

---

# Empty List

```python
students = []
```

or

```python
students = list()
```

---

# Length of List

Use

```python
len()
```

Example

```python
fruits = ["Apple","Banana","Mango"]

print(len(fruits))
```

Output

```
3
```

---

# Accessing List Elements

Every element has an Index.

Example

```python
fruits = ["Apple","Banana","Orange"]
```

| Element | Index |
|---------|------|
| Apple | 0 |
| Banana | 1 |
| Orange | 2 |

Example

```python
print(fruits[0])
```

Output

```
Apple
```

---

# Negative Indexing

Python also supports negative indexing.

| Element | Index |
|---------|------|
| Apple | -3 |
| Banana | -2 |
| Orange | -1 |

Example

```python
print(fruits[-1])
```

Output

```
Orange
```

---

# List Slicing

Syntax

```python
list[start:end]
```

Example

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

Output

```
[20,30,40]
```

---

# Skipping Elements

Syntax

```python
list[start:end:step]
```

Example

```python
numbers = [10,20,30,40,50,60]

print(numbers[0:6:2])
```

Output

```
[10,30,50]
```

---

# Updating List

Lists are mutable.

Example

```python
fruits = ["Apple","Banana","Orange"]

fruits[1] = "Mango"

print(fruits)
```

Output

```
['Apple','Mango','Orange']
```

---

# Adding Elements

## append()

Adds one element at the end.

Example

```python
fruits = ["Apple","Banana"]

fruits.append("Orange")
```

Output

```
['Apple','Banana','Orange']
```

---

## insert()

Adds element at a specific index.

Example

```python
fruits.insert(1,"Mango")
```

Output

```
['Apple','Mango','Banana']
```

---

## extend()

Adds multiple elements.

Example

```python
fruits.extend(["Kiwi","Grapes"])
```

Output

```
['Apple','Banana','Kiwi','Grapes']
```

---

# Removing Elements

## remove()

Removes by value.

Example

```python
fruits.remove("Apple")
```

---

## pop()

Removes by index.

```python
fruits.pop(2)
```

---

## clear()

Deletes all elements.

```python
fruits.clear()
```

Output

```
[]
```

---

## del Keyword

Delete whole list.

```python
del fruits
```

---

# Sorting List

Ascending

```python
numbers.sort()
```

Descending

```python
numbers.sort(reverse=True)
```

---

# Reversing List

```python
numbers.reverse()
```

---

# Copying Lists

```python
copy_list = numbers.copy()
```

---

# count()

Counts occurrences.

Example

```python
marks = [10,20,20,30]

print(marks.count(20))
```

Output

```
2
```

---

# index()

Returns first index.

Example

```python
marks.index(30)
```

Output

```
3
```

---

# Nested Lists

Lists inside another list.

Example

```python
students = [
    ["Amir",90],
    ["Rahul",85],
    ["Aman",88]
]
```

---

# List Comprehension

A shorter way to create lists.

Example

```python
numbers = [x for x in range(1,11)]
```

Output

```
[1,2,3,4,5,6,7,8,9,10]
```

Even Numbers

```python
even = [x for x in range(1,21) if x%2==0]
```

---

# Common Beginner Mistakes

❌ Using ()

Instead of

[]

---

❌ Index Out of Range

```python
marks[10]
```

when list has only 5 elements.

---

❌ Confusing append() and extend()

append()

Adds single item.

extend()

Adds multiple items.

---

❌ Forgetting Lists are Mutable

Lists can be modified anytime.

---

# Best Practices

✔ Use meaningful names

```python
student_marks
```

instead of

```python
a
```

---

✔ Keep related data together.

---

✔ Use List methods instead of manual operations.

---

✔ Avoid unnecessary duplicate values.

---

# Interview Tips

Remember these points

- List is Mutable.
- Tuple is Immutable.
- Lists use [] brackets.
- Supports Indexing.
- Supports Slicing.
- Allows Duplicate Values.
- Stores Multiple Data Types.
- List Comprehension is faster and cleaner.
- append() adds one item.
- extend() adds multiple items.

---

# Summary

Today you learned

✔ Introduction to Lists

✔ Creating Lists

✔ Indexing

✔ Negative Indexing

✔ Slicing

✔ Updating Lists

✔ append()

✔ insert()

✔ extend()

✔ remove()

✔ pop()

✔ clear()

✔ del

✔ sort()

✔ reverse()

✔ copy()

✔ count()

✔ index()

✔ Nested Lists

✔ List Comprehension

✔ Best Practices

✔ Interview Tips

🎯 Congratulations!

You have completed the theory of Python Lists.