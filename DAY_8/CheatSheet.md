# 🚀 Day 8 - Python Dictionary Cheat Sheet

## 📌 Create Dictionary

```python
student = {
    "Name": "Amir",
    "Age": 19
}
```

---

## 📌 Empty Dictionary

```python
student = {}
```

OR

```python
student = dict()
```

---

## 📌 Access Value

```python
print(student["Name"])
```

```python
print(student.get("Name"))
```

---

## 📌 Add Item

```python
student["City"] = "Meerut"
```

---

## 📌 Update Item

```python
student["Age"] = 20
```

---

## 📌 Delete Item

```python
del student["Age"]
```

---

## 📌 Remove Using pop()

```python
student.pop("Age")
```

---

## 📌 Remove Last Item

```python
student.popitem()
```

---

## 📌 Clear Dictionary

```python
student.clear()
```

---

## 📌 Copy Dictionary

```python
new_student = student.copy()
```

---

## 📌 Dictionary Methods

```python
student.keys()
student.values()
student.items()
student.get("Name")
student.update({"City":"Delhi"})
student.pop("Age")
student.popitem()
student.clear()
student.copy()
```

---

## 📌 Loop Through Keys

```python
for key in student:
    print(key)
```

---

## 📌 Loop Through Values

```python
for value in student.values():
    print(value)
```

---

## 📌 Loop Through Items

```python
for key, value in student.items():
    print(key, value)
```

---

## 📌 Check Key Exists

```python
print("Name" in student)
```

---

## 📌 Check Key Doesn't Exist

```python
print("Phone" not in student)
```

---

## 📌 Length

```python
print(len(student))
```

---

## 📌 Nested Dictionary

```python
students = {
    101: {
        "Name": "Amir",
        "Age": 19
    }
}
```

---

## 📌 Dictionary Comprehension

```python
square = {
    x: x*x
    for x in range(1,6)
}
```

---

## 📌 Merge Dictionaries

```python
a = {"A":1}
b = {"B":2}

a.update(b)
```

---

## 📌 Create Dictionary Using zip()

```python
keys = ["Name","Age"]

values = ["Amir",19]

student = dict(zip(keys,values))
```

---

# 🎯 Remember

✅ Keys → Unique

✅ Values → Can Repeat

✅ Mutable

✅ Ordered (Python 3.7+)

✅ Fast Searching
