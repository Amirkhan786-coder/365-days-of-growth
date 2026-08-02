# 🎯 Day 007 - Interview Questions
# Topic: Python Sets

**Total Questions:** 25

---

# Q1. What is a Set in Python?

### Answer

A Set is a built-in data structure used to store multiple unique values in a single variable.

Features:

- Unordered
- Mutable
- Unindexed
- No Duplicate Values

Example

```python
numbers = {10,20,30}
```

---

# Q2. What are the characteristics of a Set?

### Answer

- Unordered
- Mutable
- Unique Elements
- No Indexing
- No Slicing
- Fast Searching

---

# Q3. How do you create a Set?

### Answer

Using curly braces.

```python
fruits = {"Apple","Banana","Mango"}
```

Or

```python
numbers = set([10,20,30])
```

---

# Q4. How do you create an Empty Set?

### Answer

```python
data = set()
```

Do NOT use

```python
{}
```

because it creates a Dictionary.

---

# Q5. Can Sets contain duplicate values?

### Answer

No.

Duplicate values are automatically removed.

Example

```python
numbers = {10,20,20,30}

print(numbers)
```

Output

```
{10,20,30}
```

---

# Q6. Are Sets Ordered?

### Answer

No.

Python Sets are unordered.

The output order may change every time.

---

# Q7. Can we access Set elements using Index?

### Answer

No.

Sets do not support indexing.

Example

```python
numbers[0]
```

Produces

```
TypeError
```

---

# Q8. Difference between List and Set?

### Answer

| List | Set |
|------|------|
| Ordered | Unordered |
| Allows Duplicates | No Duplicates |
| Indexed | Not Indexed |
| Supports Slicing | No Slicing |

---

# Q9. Difference between Set and Tuple?

### Answer

| Tuple | Set |
|--------|-----|
| Ordered | Unordered |
| Immutable | Mutable |
| Duplicate Allowed | Duplicate Not Allowed |
| Indexed | No Index |

---

# Q10. What is add()?

### Answer

Adds one element.

```python
A = {10,20}

A.add(30)
```

---

# Q11. What is update()?

### Answer

Adds multiple elements.

```python
A = {1,2}

A.update([3,4,5])
```

---

# Q12. Difference between remove() and discard()?

### Answer

remove()

- Gives error if element does not exist.

discard()

- Does not give error.

---

# Q13. What does pop() do?

### Answer

Removes a random element from the Set.

```python
A.pop()
```

---

# Q14. What does clear() do?

### Answer

Removes all elements.

```python
A.clear()
```

---

# Q15. What does copy() do?

### Answer

Creates a duplicate Set.

```python
B = A.copy()
```

---

# Q16. What is Union?

### Answer

Combines all unique elements.

```python
A.union(B)
```

or

```python
A | B
```

---

# Q17. What is Intersection?

### Answer

Returns common elements.

```python
A.intersection(B)
```

or

```python
A & B
```

---

# Q18. What is Difference?

### Answer

Returns elements present in the first Set only.

```python
A - B
```

---

# Q19. What is Symmetric Difference?

### Answer

Returns elements present in either Set but not both.

```python
A ^ B
```

---

# Q20. What is frozenset()?

### Answer

A Frozen Set is an immutable version of a Set.

Once created, it cannot be modified.

Example

```python
A = frozenset({1,2,3})
```

---

# Q21. What is the Time Complexity of Searching in a Set?

### Answer

Average Time Complexity

```
O(1)
```

because Sets use Hash Tables.

---

# Q22. Can Sets store Lists?

### Answer

No.

Lists are mutable.

Sets only store immutable objects.

---

# Q23. Can Sets store Tuples?

### Answer

Yes.

Because Tuples are immutable.

Example

```python
A = {(1,2),(3,4)}
```

---

# Q24. Where are Sets used in Real Life?

### Answer

- Artificial Intelligence
- Machine Learning
- Data Science
- Banking
- Hospital Management
- Student Management
- Inventory System
- Cyber Security
- Email Management

---

# Q25. Why are Sets faster than Lists?

### Answer

Because Sets use Hash Tables internally.

Searching, Insertion, and Deletion take approximately

```
O(1)
```

which is much faster than Lists.

---

# 🎯 Most Asked Interview Questions

⭐ What is Set?

⭐ Difference between List and Set?

⭐ Difference between remove() and discard()?

⭐ Difference between add() and update()?

⭐ What is frozenset()?

⭐ Explain Union and Intersection.

⭐ Why are Sets faster than Lists?

⭐ Can Sets contain duplicate values?

⭐ Can Sets store Lists?

⭐ How do you create an Empty Set?

---

# 💡 Quick Revision

✅ Set → {}

✅ Empty Set → set()

✅ Duplicate → Removed Automatically

✅ Mutable

✅ Unordered

✅ No Indexing

✅ No Slicing

✅ Fast Searching (O(1))

✅ Supports Mathematical Operations

✅ Frozen Set → Immutable

---

# 🎉 Day 7 Interview Preparation Completed

✔ 25 Interview Questions

✔ Detailed Answers

✔ Fresher Interview Ready

✔ Placement Ready

✔ GitHub Ready