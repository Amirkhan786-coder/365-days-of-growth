# 🚀 365 Days of Growth
# 📖 Day 7 - Python Sets (Part A)
**Author:** Md Amir Khan

**Day:** 007/365

---

# 📌 Chapter 1 - Introduction to Sets

## What is a Set?

A Set is a built-in data structure in Python that stores multiple values in a single variable.

Unlike Lists and Tuples, Sets do not allow duplicate values and do not maintain the order of elements.

A Set is mainly used when we need unique values and fast searching.

Python represents Sets using curly braces {}.

Example

```python
fruits = {"Apple", "Banana", "Mango"}

print(fruits)
```

Output

```
{'Apple', 'Banana', 'Mango'}
```

---

# Definition

A Set is

- Unordered
- Mutable
- Unindexed
- Does not allow duplicate values

---

# Why do we use Sets?

Suppose a school stores student roll numbers.

Example

```
101
102
103
101
102
104
```

Here,

101 and 102 appear multiple times.

Instead of storing duplicates,

Python Set automatically removes them.

Example

```python
roll_numbers = {101,102,103,101,102,104}

print(roll_numbers)
```

Output

```
{101,102,103,104}
```

Duplicates are automatically removed.

---

# Real World Applications of Sets

Sets are widely used in software development.

---

## 1. Student Registration System

Remove duplicate student IDs.

Example

```
101

102

103

101

102
```

Stored Set

```
101

102

103
```

---

## 2. Attendance System

Store unique student attendance.

Duplicate attendance is automatically ignored.

---

## 3. Email Database

Prevent duplicate email addresses.

Example

```
amir@gmail.com

rahul@gmail.com

amir@gmail.com
```

Stored

```
amir@gmail.com

rahul@gmail.com
```

---

## 4. Contact Management

Unique phone numbers.

---

## 5. Inventory Management

Unique Product IDs.

---

## 6. Online Gaming

Unique Player IDs.

---

## 7. Social Media

Unique Followers

Unique Usernames

---

## 8. Search Engines

Unique Keywords

---

## 9. Banking

Unique Account Numbers

Transaction IDs

---

## 10. Artificial Intelligence

Removing duplicate training data.

Filtering duplicate predictions.

---

# Characteristics of Sets

Python Sets have several important properties.

---

## 1. Unordered

Sets do not store data in order.

Example

```python
numbers = {10,20,30,40}

print(numbers)
```

Output may appear in any order.

```
{20,10,40,30}
```

---

## 2. Unique Elements

Duplicate values are not allowed.

Example

```python
numbers = {10,20,30,20,10}

print(numbers)
```

Output

```
{10,20,30}
```

---

## 3. Mutable

We can

Add Elements

Remove Elements

Update Elements

Example

```python
fruits = {"Apple","Banana"}

fruits.add("Mango")
```

---

## 4. Unindexed

Unlike Lists,

Sets do not support indexing.

Wrong

```python
numbers = {10,20,30}

print(numbers[0])
```

This produces an error.

---

## 5. Can Store Multiple Data Types

Example

```python
data = {

10,

3.14,

"Python",

True

}
```

---

## 6. Fast Searching

Sets use Hashing internally.

Searching in Sets is much faster than Lists.

That's why Sets are widely used in

Databases

Search Engines

AI

Machine Learning

Cyber Security

---

# Advantages of Sets

✔ Removes Duplicate Values Automatically

✔ Fast Searching

✔ Mathematical Operations

✔ Easy to Use

✔ Efficient Memory Usage

✔ High Performance

---

# Disadvantages of Sets

❌ No Indexing

❌ No Slicing

❌ Elements are Unordered

❌ Cannot Store Mutable Objects like Lists

Example

Wrong

```python
numbers = {

[1,2,3]

}
```

This produces an error because Lists are mutable.

---

# Comparison

| Feature | List | Tuple | Set |
|----------|------|-------|-----|
| Ordered | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ |
| Duplicate Allowed | ✅ | ✅ | ❌ |
| Indexing | ✅ | ✅ | ❌ |
| Slicing | ✅ | ✅ | ❌ |
| Speed | Medium | Fast | Very Fast |

---

# Summary

A Set is one of the most useful Python data structures when working with unique values.

It automatically removes duplicates, provides very fast searching, and supports powerful mathematical operations.

Sets are widely used in Data Science, Artificial Intelligence, Machine Learning, Cyber Security, Databases, and Software Development.

---

# Key Points to Remember

✅ Set uses `{}` brackets.

✅ Duplicate values are automatically removed.

✅ Sets are unordered.

✅ Sets are mutable.

✅ Sets do not support indexing.

✅ Sets do not support slicing.

✅ Searching in Sets is very fast.

✅ Sets are ideal for storing unique values.

# 📌 Chapter 2 - Creating Sets

A Set can be created in multiple ways in Python.

The most common method is using curly braces `{}`.

---

## Method 1 - Using Curly Braces

Syntax

```python
set_name = {value1, value2, value3}
```

Example

```python
fruits = {"Apple", "Banana", "Mango"}

print(fruits)
```

Output

```
{'Apple', 'Banana', 'Mango'}
```

---

## Method 2 - Using set() Constructor

Python provides a built-in function called `set()`.

Syntax

```python
set_name = set(iterable)
```

Example

```python
numbers = set([10, 20, 30, 40])

print(numbers)
```

Output

```
{10, 20, 30, 40}
```

---

## Method 3 - Creating Set from List

A List can easily be converted into a Set.

Example

```python
numbers = [10, 20, 30, 20, 10]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output

```
{10, 20, 30}
```

Notice that duplicate values are automatically removed.

---

## Method 4 - Creating Set from Tuple

Example

```python
numbers = (1, 2, 3, 2, 1)

new_set = set(numbers)

print(new_set)
```

Output

```
{1, 2, 3}
```

---

## Method 5 - Creating Set from String

Each character becomes a unique element.

Example

```python
text = "python"

letters = set(text)

print(letters)
```

Possible Output

```
{'p', 'y', 't', 'h', 'o', 'n'}
```

---

# Empty Set

Many beginners make mistakes here.

Wrong

```python
data = {}

print(type(data))
```

Output

```
<class 'dict'>
```

`{}` creates an empty Dictionary, NOT a Set.

---

## Correct Way

```python
data = set()

print(type(data))
```

Output

```
<class 'set'>
```

Always use `set()` to create an empty Set.

---

# Data Types Allowed in Sets

A Set can store immutable data types.

Examples

- Integer
- Float
- String
- Boolean
- Tuple

Example

```python
data = {

10,

20.5,

"Python",

True,

(1,2)

}

print(data)
```

Output

```
{10, 20.5, 'Python', True, (1,2)}
```

---

# Data Types NOT Allowed

Mutable objects cannot be stored inside a Set.

Examples

❌ List

❌ Dictionary

❌ Another Set

Wrong Example

```python
data = {

[1,2,3]

}
```

Output

```
TypeError:
unhashable type: 'list'
```

---

# Why Lists Cannot Be Stored?

Lists are mutable.

Python Sets use Hashing.

Only immutable objects can be hashed.

Therefore,

Lists cannot become Set elements.

---

# Duplicate Values

One of the biggest advantages of Sets is automatic duplicate removal.

Example

```python
numbers = {

10,

20,

20,

30,

30,

40

}

print(numbers)
```

Output

```
{10,20,30,40}
```

Duplicates are removed automatically.

---

# Can Sets Store Mixed Data Types?

Yes.

Example

```python
data = {

10,

3.14,

"Python",

False,

(1,2)

}

print(data)
```

Output

```
{10,3.14,'Python',False,(1,2)}
```

---

# Mutable vs Immutable

A Set itself is Mutable.

Its elements must be Immutable.

Example

```python
fruits = {

"Apple",

"Banana"

}

fruits.add("Mango")

print(fruits)
```

Output

```
{'Apple','Banana','Mango'}
```

The Set changed.

Therefore,

Sets are Mutable.

---

# Hashing

Internally,

Python stores Set elements using Hash Tables.

Benefits

✔ Fast Searching

✔ Fast Insertion

✔ Fast Deletion

Average Time Complexity

Searching

O(1)

Insertion

O(1)

Deletion

O(1)

This makes Sets much faster than Lists.

---

# Memory Representation

Example

```python
numbers = {

10,

20,

30

}
```

Python stores these values using hashing instead of indexes.

That's why

Indexing is not possible.

---

# Common Beginner Mistakes

❌ Creating Empty Set using {}

Correct

```python
set()
```

---

❌ Expecting Ordered Output

Wrong

```python
numbers = {

1,

2,

3

}
```

Output order may change.

---

❌ Using Indexing

Wrong

```python
numbers[0]
```

Sets do not support indexing.

---

❌ Adding List inside Set

Wrong

```python
data = {

[1,2]

}
```

Produces TypeError.

---

# Interview Tips

Remember these points.

✔ Empty Set = set()

✔ {} creates Dictionary

✔ Duplicate values removed automatically

✔ Mutable Collection

✔ Unordered Collection

✔ No Indexing

✔ No Slicing

✔ Fast Searching using Hashing

---

# Chapter Summary

In this chapter, we learned how to create Sets using different methods. We also learned about empty Sets, duplicate removal, supported data types, hashing, mutable behavior, and common mistakes.

Understanding these concepts is important before learning Set methods and operations.

# 📌 Chapter 3 - Set Methods

Python provides several built-in methods to perform different operations on Sets.

These methods make adding, removing, updating, and managing Set elements easy and efficient.

---

# 1. add()

## Definition

The `add()` method is used to add **one single element** to a Set.

If the element already exists, nothing changes.

---

## Syntax

```python
set_name.add(element)
```

---

## Example 1

```python
fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)
```

Output

```
{'Apple', 'Banana', 'Mango'}
```

---

## Example 2

```python
numbers = {10,20,30}

numbers.add(40)

print(numbers)
```

Output

```
{10,20,30,40}
```

---

## Duplicate Example

```python
numbers = {10,20,30}

numbers.add(20)

print(numbers)
```

Output

```
{10,20,30}
```

Duplicate value is ignored.

---

## Real-Life Example

Student Registration System

```python
students = {"Amir","Rahul"}

students.add("Aman")

print(students)
```

---

# 2. update()

## Definition

The `update()` method adds multiple elements to a Set.

It accepts

- List
- Tuple
- Set
- String

---

## Syntax

```python
set_name.update(iterable)
```

---

## Example 1

```python
numbers = {10,20}

numbers.update([30,40,50])

print(numbers)
```

Output

```
{10,20,30,40,50}
```

---

## Example 2

```python
fruits = {"Apple"}

fruits.update(("Banana","Mango"))

print(fruits)
```

---

## Example 3

```python
letters = {"A"}

letters.update("BCD")

print(letters)
```

Output

```
{'A','B','C','D'}
```

---

## Difference

add()

Adds only one element.

update()

Adds multiple elements.

---

# 3. remove()

## Definition

The `remove()` method removes an element from a Set.

If the element is not found,

Python gives an error.

---

## Syntax

```python
set_name.remove(element)
```

---

## Example

```python
numbers = {10,20,30}

numbers.remove(20)

print(numbers)
```

Output

```
{10,30}
```

---

## Error Example

```python
numbers = {10,20}

numbers.remove(100)
```

Output

```
KeyError
```

---

# 4. discard()

## Definition

discard() removes an element.

If the element does not exist,

No error occurs.

---

## Syntax

```python
set_name.discard(element)
```

---

## Example

```python
numbers = {10,20,30}

numbers.discard(20)

print(numbers)
```

Output

```
{10,30}
```

---

## Missing Element Example

```python
numbers = {10,20}

numbers.discard(100)

print(numbers)
```

Output

```
{10,20}
```

No error.

---

# Difference

| remove() | discard() |
|-----------|-----------|
| Error if element missing | No Error |
| Less Safe | Safer |

---

# 5. pop()

## Definition

The pop() method removes and returns a random element.

Since Sets are unordered,

we cannot predict which element will be removed.

---

## Syntax

```python
set_name.pop()
```

---

## Example

```python
numbers = {10,20,30}

removed = numbers.pop()

print(removed)

print(numbers)
```

Possible Output

```
10

{20,30}
```

Another run may remove another value.

---

# 6. clear()

## Definition

clear() removes all elements.

The Set becomes empty.

---

## Syntax

```python
set_name.clear()
```

---

## Example

```python
numbers = {10,20,30}

numbers.clear()

print(numbers)
```

Output

```
set()
```

---

# 7. copy()

## Definition

Creates a copy of a Set.

---

## Syntax

```python
new_set = old_set.copy()
```

---

## Example

```python
numbers = {10,20,30}

copy_set = numbers.copy()

print(copy_set)
```

Output

```
{10,20,30}
```

---

# Method Comparison

| Method | Purpose |
|----------|---------|
| add() | Add one element |
| update() | Add multiple elements |
| remove() | Remove element (Error if missing) |
| discard() | Remove element (No Error) |
| pop() | Remove random element |
| clear() | Remove all elements |
| copy() | Create duplicate Set |

---

# Real-World Example

```python
students = {"Amir","Rahul"}

students.add("Aman")

students.update(["Ali","Rohan"])

students.remove("Rahul")

print(students)
```

Possible Output

```
{'Amir','Ali','Rohan','Aman'}
```

---

# Common Beginner Mistakes

❌ Using update() with single integer

Wrong

```python
numbers.update(10)
```

Correct

```python
numbers.add(10)
```

---

❌ Using remove() without checking

Wrong

```python
numbers.remove(100)
```

Use discard() if unsure.

---

❌ Expecting pop() to remove last element

Sets have no order.

---

# Interview Tips

Remember

✔ add() → One Element

✔ update() → Multiple Elements

✔ remove() → Error if Missing

✔ discard() → No Error

✔ pop() → Random Element

✔ clear() → Empty Set

✔ copy() → Duplicate Set

---

# Chapter Summary

In this chapter, we learned all important Set methods used in Python. These methods help us add, update, remove, copy, and manage Set elements efficiently. Understanding these methods is essential before moving to Set Operations.

# 📌 Chapter 4 - Set Operations

One of the biggest advantages of Python Sets is their powerful mathematical operations.

These operations are based on Set Theory (Mathematics).

They are widely used in:

- Data Science
- Artificial Intelligence
- Machine Learning
- Databases
- Cyber Security

---

# 1. union()

## Definition

The `union()` method combines all unique elements from two or more Sets.

Duplicate values appear only once.

---

## Syntax

```python
set1.union(set2)
```

or

```python
set1 | set2
```

---

## Example 1

```python
A = {1,2,3}

B = {3,4,5}

print(A.union(B))
```

Output

```
{1,2,3,4,5}
```

---

## Example 2

```python
A = {"Apple","Banana"}

B = {"Banana","Mango"}

print(A | B)
```

Output

```
{'Apple','Banana','Mango'}
```

---

## Real Life Example

Student List

Class A

```
Amir

Rahul

Aman
```

Class B

```
Aman

Rohan

Ali
```

Union gives

```
Amir

Rahul

Aman

Rohan

Ali
```

---

# 2. intersection()

## Definition

Returns only the common elements present in both Sets.

---

## Syntax

```python
set1.intersection(set2)
```

or

```python
set1 & set2
```

---

## Example

```python
A = {1,2,3,4}

B = {3,4,5,6}

print(A.intersection(B))
```

Output

```
{3,4}
```

---

## Example 2

```python
A = {"Python","Java","C"}

B = {"Java","C++","Python"}

print(A & B)
```

Output

```
{'Python','Java'}
```

---

## Real Life Example

Students enrolled in

Python Course

AND

Java Course

Intersection gives students studying both.

---

# 3. difference()

## Definition

Returns elements present in the first Set but not in the second Set.

---

## Syntax

```python
set1.difference(set2)
```

or

```python
set1 - set2
```

---

## Example

```python
A = {1,2,3,4}

B = {3,4,5}

print(A.difference(B))
```

Output

```
{1,2}
```

---

## Reverse Example

```python
print(B.difference(A))
```

Output

```
{5}
```

Difference depends on order.

---

## Real Life Example

Students who attended

Python Class

but did not attend

Java Class.

---

# 4. symmetric_difference()

## Definition

Returns elements that are present in either Set,

but NOT in both.

---

## Syntax

```python
set1.symmetric_difference(set2)
```

or

```python
set1 ^ set2
```

---

## Example

```python
A = {1,2,3}

B = {3,4,5}

print(A.symmetric_difference(B))
```

Output

```
{1,2,4,5}
```

Notice

3 is removed because it exists in both Sets.

---

## Real Life Example

Students who enrolled in

Python

OR

Java

but NOT both.

---

# 5. issubset()

## Definition

Checks whether every element of one Set exists inside another Set.

Returns

True

or

False

---

## Syntax

```python
set1.issubset(set2)
```

---

## Example

```python
A = {1,2}

B = {1,2,3,4}

print(A.issubset(B))
```

Output

```
True
```

---

## Example 2

```python
A = {1,5}

B = {1,2,3,4}

print(A.issubset(B))
```

Output

```
False
```

---

# 6. issuperset()

## Definition

Checks whether one Set contains all elements of another Set.

---

## Syntax

```python
set1.issuperset(set2)
```

---

## Example

```python
A = {1,2,3,4}

B = {1,2}

print(A.issuperset(B))
```

Output

```
True
```

---

# 7. isdisjoint()

## Definition

Returns True if two Sets have no common elements.

---

## Syntax

```python
set1.isdisjoint(set2)
```

---

## Example

```python
A = {1,2}

B = {3,4}

print(A.isdisjoint(B))
```

Output

```
True
```

---

## Example 2

```python
A = {1,2,3}

B = {3,4,5}

print(A.isdisjoint(B))
```

Output

```
False
```

---

# Comparison of Set Operations

| Method | Meaning |
|---------|---------|
| union() | Combines all unique elements |
| intersection() | Common elements |
| difference() | Elements in first Set only |
| symmetric_difference() | Elements not common |
| issubset() | Checks subset |
| issuperset() | Checks superset |
| isdisjoint() | Checks no common elements |

---

# Time Complexity

| Operation | Average Complexity |
|------------|-------------------|
| union() | O(n+m) |
| intersection() | O(min(n,m)) |
| difference() | O(n) |
| symmetric_difference() | O(n+m) |
| issubset() | O(n) |
| issuperset() | O(n) |
| isdisjoint() | O(min(n,m)) |

---

# Real-World Applications

## Artificial Intelligence

Finding common features between datasets.

---

## Data Science

Removing duplicate records.

---

## Cyber Security

Comparing blacklisted IP addresses.

---

## Database

Finding common customers.

---

## Machine Learning

Comparing training and testing datasets.

---

## College Management

Students studying multiple subjects.

---

# Common Beginner Mistakes

❌ Confusing Difference with Symmetric Difference.

Difference

```
A-B
```

Only removes elements from A.

---

Symmetric Difference

Returns elements that are not common in both Sets.

---

❌ Forgetting that order does not matter.

Sets are unordered.

---

# Interview Tips

Remember these shortcuts.

```
Union → |

Intersection → &

Difference → -

Symmetric Difference → ^
```

---

# Chapter Summary

Set Operations make Python Sets one of the most powerful data structures.

Using these operations, we can efficiently compare datasets, remove duplicates, find common values, and perform mathematical operations.

These concepts are frequently used in interviews, competitive programming, and real-world software development.

# 📌 Chapter 5 - Frozen Set (frozenset)

## What is a Frozen Set?

A Frozen Set is an immutable version of a Set.

This means that once a Frozen Set is created, its elements cannot be changed.

Unlike normal Sets, you cannot:

- Add elements
- Remove elements
- Update elements

Frozen Sets are useful when data should remain constant throughout the program.

---

## Syntax

```python
frozenset_name = frozenset(iterable)
```

---

## Example 1

```python
numbers = frozenset({10,20,30})

print(numbers)
```

Output

```
frozenset({10,20,30})
```

---

## Example 2

```python
fruits = frozenset(["Apple","Banana","Mango"])

print(fruits)
```

Output

```
frozenset({'Apple','Banana','Mango'})
```

---

## Trying to Add Elements

```python
numbers = frozenset({10,20,30})

numbers.add(40)
```

Output

```
AttributeError:
'frozenset' object has no attribute 'add'
```

---

## Trying to Remove Elements

```python
numbers = frozenset({10,20,30})

numbers.remove(20)
```

Output

```
AttributeError
```

---

# Difference Between Set and Frozen Set

| Feature | Set | Frozen Set |
|----------|-----|------------|
| Mutable | ✅ Yes | ❌ No |
| Add Elements | ✅ | ❌ |
| Remove Elements | ✅ | ❌ |
| Update Elements | ✅ | ❌ |
| Duplicate Values | ❌ | ❌ |
| Ordered | ❌ | ❌ |

---

# Advantages of Sets

Python Sets provide many advantages.

---

## 1. Automatically Removes Duplicate Values

Example

```python
numbers = {1,2,2,3,3}

print(numbers)
```

Output

```
{1,2,3}
```

---

## 2. Fast Searching

Searching inside a Set is much faster than searching inside a List because Sets use Hash Tables.

---

## 3. Faster Insertion

Adding new elements takes very little time.

---

## 4. Faster Deletion

Removing elements is also efficient.

---

## 5. Mathematical Operations

Supports

- Union
- Intersection
- Difference
- Symmetric Difference

---

## 6. Memory Efficient

Stores only unique values.

---

## 7. Simple Syntax

Easy to create and use.

---

# Disadvantages of Sets

---

## 1. No Indexing

Wrong

```python
numbers[0]
```

Produces an error.

---

## 2. No Slicing

Wrong

```python
numbers[1:3]
```

Sets do not support slicing.

---

## 3. Unordered Collection

Output order may change every time.

---

## 4. Cannot Store Mutable Objects

Wrong

```python
data = {

[1,2]

}
```

Produces TypeError.

---

# Real-Life Applications of Sets

---

## 1. Student Registration System

Remove duplicate student IDs.

---

## 2. Attendance Management

Store only unique student attendance.

---

## 3. Email Management

Remove duplicate email addresses.

---

## 4. Contact Management

Unique mobile numbers.

---

## 5. Banking

Unique Account Numbers

Unique Transaction IDs

---

## 6. Library Management

Unique Book IDs.

---

## 7. Hospital Management

Unique Patient IDs.

---

## 8. Social Media

Unique Followers

Unique Usernames

---

## 9. Artificial Intelligence

Removing duplicate data.

---

## 10. Machine Learning

Cleaning datasets before training models.

---

## 11. Data Science

Removing duplicate records.

---

## 12. Cyber Security

Comparing malicious IP addresses.

---

# Common Errors

---

## Error 1

Creating Empty Set

Wrong

```python
data = {}
```

Correct

```python
data = set()
```

---

## Error 2

Using Indexing

Wrong

```python
numbers[0]
```

---

## Error 3

Adding List inside Set

Wrong

```python
data = {

[1,2]

}
```

---

## Error 4

Using remove() without checking

Use discard() if the element may not exist.

---

## Error 5

Expecting Ordered Output

Sets are unordered.

---

# Best Practices

✔ Use meaningful variable names.

✔ Use Sets whenever duplicate values should be removed.

✔ Use discard() instead of remove() when unsure.

✔ Use Frozen Sets for constant data.

✔ Use Set Operations instead of loops whenever possible.

✔ Keep Sets small and relevant for better performance.

---

# Interview Tips

Remember these points.

✔ Set is Mutable.

✔ Frozen Set is Immutable.

✔ Duplicate values are automatically removed.

✔ Sets use Hashing.

✔ Searching is O(1) on average.

✔ Sets are Unordered.

✔ No Indexing.

✔ No Slicing.

✔ Mathematical Operations supported.

---

# Quick Revision

✔ Set uses {}

✔ Empty Set uses set()

✔ Duplicate values are removed automatically

✔ Unordered Collection

✔ Mutable

✔ Fast Searching

✔ Fast Insertion

✔ Fast Deletion

✔ Supports Mathematical Operations

✔ Frozen Set is Immutable

---

# Chapter Summary

Python Sets are one of the most powerful data structures used for storing unique values efficiently.

They automatically remove duplicates, provide very fast searching through hashing, and support powerful mathematical operations like union, intersection, difference, and symmetric difference.

Sets are widely used in Artificial Intelligence, Machine Learning, Data Science, Cyber Security, Database Systems, Banking, Inventory Management, and Software Development.

Understanding Sets is essential for writing efficient Python programs and solving real-world problems.

---

# 🎯 Day 7 Summary

After completing Day 7, you can now:

✅ Create Sets

✅ Create Empty Sets

✅ Understand Set Characteristics

✅ Add Elements

✅ Update Elements

✅ Remove Elements

✅ Copy Sets

✅ Clear Sets

✅ Perform Set Operations

✅ Use Frozen Sets

✅ Apply Sets in Real-Life Projects

---

# 🚀 What's Next?

Tomorrow (Day 8)

📖 Dictionaries

- Creating Dictionaries
- Dictionary Methods
- Nested Dictionaries
- Dictionary Comprehension
- Student Contact Book Project
