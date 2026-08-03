# 🚀 365 Days of Growth

# 📖 Day 8 - Python Dictionaries

**Author:** Md Amir Khan

**Day:** 008/365

**Date:** ____________

---

# 📌 Chapter 1 - Introduction to Dictionary

## What is a Dictionary?

A Dictionary is a built-in Python data structure that stores data in the form of **Key : Value** pairs.

Each key must be unique, while values can be duplicated.

Dictionary is one of the most powerful data structures in Python because it allows fast searching and organized data storage.

Example

```python
student = {
    "name": "Amir",
    "age": 19,
    "college": "Shobhit University"
}
```

Output

```
{
'name':'Amir',
'age':19,
'college':'Shobhit University'
}
```

---

# 📌 Chapter 2 - Features of Dictionary

Python Dictionaries have several important features.

## 1. Mutable

Values can be modified.

Example

```python
student["age"] = 20
```

---

## 2. Key-Value Pair

Every item contains

```
Key : Value
```

Example

```
"name" : "Amir"
```

---

## 3. Ordered

Python 3.7+

Dictionary maintains insertion order.

---

## 4. No Duplicate Keys

Wrong

```python
student = {
"name":"Amir",
"name":"Rahul"
}
```

Output

```
Rahul
```

Only last value remains.

---

## 5. Duplicate Values Allowed

```python
{
"A":100,
"B":100
}
```

Valid.

---

# 📌 Chapter 3 - Creating Dictionary

Method 1

```python
student = {
"name":"Amir",
"age":19,
"cgpa":8.5
}
```

---

Method 2

Using dict()

```python
student = dict(
name="Amir",
age=19
)
```

---

Empty Dictionary

```python
student = {}
```

or

```python
student = dict()
```

---

# 📌 Chapter 4 - Accessing Values

Using Key

```python
student = {
"name":"Amir",
"age":19
}

print(student["name"])
```

Output

```
Amir
```

---

Using get()

```python
print(student.get("age"))
```

Output

```
19
```

---

# 📌 Chapter 5 - Adding Items

```python
student["branch"]="CSE"
```

Output

```
{
'name':'Amir',
'age':19,
'branch':'CSE'
}
```

---

# 📌 Chapter 6 - Updating Values

```python
student["age"]=20
```

Output

```
20
```

---

# 📌 Chapter 7 - Removing Items

Using pop()

```python
student.pop("age")
```

---

Using popitem()

```python
student.popitem()
```

Removes last item.

---

Using del

```python
del student["name"]
```

---

Using clear()

```python
student.clear()
```

Dictionary becomes empty.

---

# 📌 Chapter 8 - Dictionary Methods

## keys()

Returns all keys.

```python
student.keys()
```

---

## values()

Returns all values.

```python
student.values()
```

---

## items()

Returns key-value pairs.

```python
student.items()
```

---

## get()

Safely returns value.

```python
student.get("name")
```

---

## update()

Updates dictionary.

```python
student.update({
"city":"Delhi"
})
```

---

## copy()

Creates copy.

```python
student2 = student.copy()
```

---

## pop()

Removes specific key.

```python
student.pop("age")
```

---

## popitem()

Removes last key.

```python
student.popitem()
```

---

## clear()

Deletes everything.

```python
student.clear()
```

---

# 📌 Chapter 9 - Looping Through Dictionary

Keys

```python
for i in student:
    print(i)
```

---

Values

```python
for i in student.values():
    print(i)
```

---

Items

```python
for key,value in student.items():
    print(key,value)
```

---

# 📌 Chapter 10 - Nested Dictionary

Example

```python
students = {

101:{
"name":"Amir",
"age":19
},

102:{
"name":"Rahul",
"age":20
}

}
```

Access

```python
print(students[101]["name"])
```

Output

```
Amir
```

---

# 📌 Chapter 11 - Dictionary Comprehension

Syntax

```python
square = {
x:x*x
for x in range(1,6)
}
```

Output

```
{
1:1,
2:4,
3:9,
4:16,
5:25
}
```

---

# 📌 Chapter 12 - Membership Operators

Using in

```python
student = {
"name":"Amir"
}

print("name" in student)
```

Output

```
True
```

---

Using not in

```python
print("age" not in student)
```

Output

```
True
```

---

# 📌 Chapter 13 - Length of Dictionary

```python
len(student)
```

Returns total key-value pairs.

---

# 📌 Chapter 14 - Real Life Applications

Python Dictionaries are widely used in

✅ Student Management System

✅ Banking System

✅ Hospital Management

✅ Contact Book

✅ Inventory Management

✅ Employee Database

✅ AI Applications

✅ Machine Learning

✅ APIs

---

# 📌 Common Beginner Mistakes

❌ Using duplicate keys

❌ Forgetting quotes around string keys

❌ Using list as key

❌ Accessing missing key

❌ Confusing keys() with values()

❌ Forgetting dictionary is mutable

❌ Using [] instead of get() for unknown keys

---

# 📌 Summary

Today we learned

✔ Dictionary Basics

✔ Creating Dictionary

✔ Accessing Values

✔ Updating Values

✔ Removing Values

✔ Dictionary Methods

✔ Looping

✔ Nested Dictionary

✔ Dictionary Comprehension

✔ Membership Operators

✔ Real-Life Applications

---

# 🎯 Tomorrow's Goal

📖 Python Functions

✔ User Defined Functions

✔ Parameters

✔ Arguments

✔ Return Statement

✔ Lambda Functions

✔ Recursion