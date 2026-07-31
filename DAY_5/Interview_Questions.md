# 🎤 Day 005 - Python Lists
# Interview Questions & Answers

---

## Q1. What is a List in Python?

### Answer

A List is a built-in data structure in Python used to store multiple values in a single variable.

Lists are:

- Ordered
- Mutable
- Allow duplicate values
- Can store multiple data types

Example

```python
numbers = [10,20,30]
```

---

## Q2. Why do we use Lists?

### Answer

Lists are used to

- Store multiple values
- Reduce code repetition
- Manage related data
- Perform operations easily

Example

Student Marks

Shopping Cart

Employee Records

---

## Q3. What are the characteristics of a List?

### Answer

✔ Ordered

✔ Mutable

✔ Indexed

✔ Duplicate values allowed

✔ Multiple Data Types

---

## Q4. What is the difference between List and Tuple?

### Answer

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| [] | () |
| Slower | Faster |
| Can Modify | Cannot Modify |

---

## Q5. What is Indexing?

### Answer

Every element has a position called Index.

Example

```python
fruits = ["Apple","Banana","Mango"]

print(fruits[0])
```

Output

```
Apple
```

---

## Q6. What is Negative Indexing?

### Answer

Negative indexing starts from the last element.

Example

```python
fruits[-1]
```

returns

```
Mango
```

---

## Q7. What is Slicing?

### Answer

Slicing extracts a portion of a list.

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

## Q8. Explain append().

### Answer

append() adds one element at the end.

Example

```python
numbers.append(50)
```

---

## Q9. Explain extend().

### Answer

extend() adds multiple elements.

Example

```python
numbers.extend([60,70])
```

---

## Q10. Difference between append() and extend()?

### Answer

append()

Adds one element.

extend()

Adds multiple elements.

Example

```python
a.append(5)
```

vs

```python
a.extend([5,6])
```

---

## Q11. Explain insert().

### Answer

insert() inserts an element at a specified position.

Example

```python
numbers.insert(2,100)
```

---

## Q12. Explain remove().

### Answer

remove() deletes an element by value.

Example

```python
numbers.remove(20)
```

---

## Q13. Explain pop().

### Answer

pop() removes an element by index.

If no index is given,

it removes the last element.

Example

```python
numbers.pop()
```

---

## Q14. Explain clear().

### Answer

clear() removes all elements.

Example

```python
numbers.clear()
```

Output

```
[]
```

---

## Q15. What is List Comprehension?

### Answer

List Comprehension is a shorter and faster way to create lists.

Example

```python
numbers = [x for x in range(10)]
```

---

## Q16. Which functions are commonly used with Lists?

### Answer

- len()
- max()
- min()
- sum()
- sorted()

---

## Q17. How do you copy a List?

### Answer

Using copy()

Example

```python
copy = numbers.copy()
```

---

## Q18. Can Lists store different data types?

### Answer

Yes.

Example

```python
data = ["Amir",19,8.6,True]
```

---

## Q19. What are Nested Lists?

### Answer

A List inside another List is called Nested List.

Example

```python
students = [
    ["Amir",90],
    ["Rahul",85]
]
```

---

## Q20. What are some real-world applications of Lists?

### Answer

Lists are used in

- Shopping Cart
- Student Management System
- Employee Records
- Contact Book
- Banking Applications
- Attendance System
- Inventory Management
- E-commerce Websites

---

# 🎯 Interview Tips

✔ Remember:

- List is Mutable.
- Uses [] brackets.
- Supports Indexing & Slicing.
- Allows Duplicates.
- Stores Multiple Data Types.
- append() → One Item
- extend() → Multiple Items
- remove() → By Value
- pop() → By Index
- List Comprehension makes code shorter and cleaner.