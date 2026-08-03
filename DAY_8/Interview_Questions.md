# 🎤 Day 8 - Interview Questions (Python Dictionaries)

## 1. What is a Dictionary in Python?

**Answer:**
A Dictionary is a built-in data structure that stores data as **key-value pairs**. Keys are unique, while values can be duplicated.

---

## 2. Why do we use Dictionaries?

**Answer:**
Dictionaries are used to store and retrieve data efficiently using keys instead of indexes.

---

## 3. What are the main features of a Dictionary?

**Answer:**
- Mutable
- Ordered (Python 3.7+)
- Key-Value Pair
- Unique Keys
- Duplicate Values Allowed
- Fast Searching

---

## 4. How do you create a Dictionary?

**Answer:**

```python
student = {
    "Name": "Amir",
    "Age": 19
}
```

---

## 5. How do you access a value in a Dictionary?

**Answer:**

Using key

```python
print(student["Name"])
```

or

```python
print(student.get("Name"))
```

---

## 6. What is the difference between [] and get()?

**Answer:**

- `[]` gives a KeyError if the key is not found.
- `get()` returns `None` (or a default value) instead of an error.

---

## 7. How do you add a new item to a Dictionary?

**Answer:**

```python
student["Branch"] = "CSE"
```

---

## 8. How do you update an existing value?

**Answer:**

```python
student["Age"] = 20
```

---

## 9. How do you delete a key from a Dictionary?

**Answer:**

```python
del student["Age"]
```

or

```python
student.pop("Age")
```

---

## 10. What is the use of pop()?

**Answer:**
`pop()` removes a specific key and returns its value.

---

## 11. What is the use of popitem()?

**Answer:**
`popitem()` removes and returns the last inserted key-value pair.

---

## 12. What is the use of clear()?

**Answer:**
It removes all key-value pairs from the dictionary.

---

## 13. What is the use of keys()?

**Answer:**
It returns all keys of the dictionary.

Example:

```python
student.keys()
```

---

## 14. What is the use of values()?

**Answer:**
It returns all values stored in the dictionary.

---

## 15. What is the use of items()?

**Answer:**
It returns all key-value pairs as tuple objects.

Example:

```python
student.items()
```

---

## 16. What is the use of update()?

**Answer:**
It updates an existing dictionary or merges another dictionary.

---

## 17. What is Dictionary Comprehension?

**Answer:**
Dictionary Comprehension is a concise way to create dictionaries using loops.

Example:

```python
square = {x: x*x for x in range(1,6)}
```

---

## 18. What is a Nested Dictionary?

**Answer:**
A Dictionary inside another Dictionary is called a Nested Dictionary.

---

## 19. Can Dictionary keys be duplicated?

**Answer:**
No.
Dictionary keys must always be unique.

---

## 20. Can Dictionary values be duplicated?

**Answer:**
Yes.
Values can be duplicated.

---

## 21. Which data types can be used as Dictionary keys?

**Answer:**

- String
- Integer
- Float
- Tuple

(Any immutable data type)

---

## 22. Which data type cannot be used as a Dictionary key?

**Answer:**
Mutable data types like **List**, **Set**, and **Dictionary** cannot be used as keys.

---

## 23. How do you check if a key exists?

**Answer:**

```python
"Name" in student
```

---

## 24. What are some real-life applications of Dictionaries?

**Answer:**

- Student Management System
- Banking System
- Contact Book
- Inventory Management
- Employee Records
- APIs
- Machine Learning
- JSON Data Handling

---

## 25. Why are Dictionaries faster than Lists for searching?

**Answer:**
Because Dictionaries use **Hash Tables**, which provide very fast key-based lookup compared to searching elements one by one in a List.

---

# 🎯 Interview Tip

Always prefer `get()` instead of `[]` when the key may not exist because it avoids `KeyError`.

Example:

```python
student.get("Phone")
```

instead of

```python
student["Phone"]
```