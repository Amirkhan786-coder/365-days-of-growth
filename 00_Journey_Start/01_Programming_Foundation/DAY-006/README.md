

## 🎯 Today's Topic

### Python Conditional Statements

The main conditional statements in Python are:

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`

---

## 🧠 What I Learned Today

- What is a condition?
- How `if` works
- How `if-else` works
- How `elif` works
- Nested conditions
- Comparison operators
- Logical operators
- Python indentation
- Decision-making in programming

---

## 🔹 Basic Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
````

Output:

```text
You are eligible to vote
```

---

## 🔢 Comparison Operators

```text
==    Equal to
!=    Not equal to
>     Greater than
<     Less than
>=    Greater than or equal to
<=    Less than or equal to
```

Example:

```python
marks = 75

if marks >= 40:
    print("Pass")
```

---

## 🧠 Logical Operators

Python provides three important logical operators:

```text
and
or
not
```

Example:

```python
age = 25

if age >= 18 and age <= 60:
    print("Eligible")
```

---

## 🟢 if Statement

```python
if condition:
    statement
```

Example:

```python
number = 10

if number > 0:
    print("Positive")
```

---

## 🟡 if-else Statement

```python
if condition:
    statement
else:
    statement
```

Example:

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

---

## 🟠 if-elif-else

Used when there are multiple conditions.

```python
marks = 85

if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 70:
    print("B")

else:
    print("C")
```

Output:

```text
A
```

---

## 🔴 Nested if

An `if` statement inside another `if` statement is called a nested `if`.

```python
age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to vote")
```

---

## ⚠️ Important: `=` vs `==`

Assignment:

```python
age = 20
```

Comparison:

```python
age == 20
```

`=` stores a value.

`==` compares two values.

---

## ⚠️ Python Indentation

Python uses indentation to define blocks.

Correct:

```python
if age >= 18:
    print("Adult")
```

Incorrect:

```python
if age >= 18:
print("Adult")
```

Usually, Python uses **4 spaces** for indentation.

---

## 💻 Programs Practiced

1. Positive or Negative
2. Positive, Negative or Zero
3. Even or Odd
4. Pass or Fail
5. Grade Calculator
6. Voting Eligibility
7. Driving Eligibility
8. Largest of Two Numbers
9. Largest of Three Numbers
10. Smallest of Two Numbers
11. Age Category
12. Login System
13. ATM Withdrawal
14. Electricity Bill
15. Discount Calculator
16. BMI Category
17. Temperature Category
18. Leap Year Checker
19. Simple Calculator
20. Number Range Checker

---

## 🔥 Mini Project

### Student Result Management System

The program takes:

* Student Name
* Roll Number
* Marks of 5 subjects

And calculates:

* Total
* Percentage
* Grade
* Pass/Fail

### Grade System

```text
90+       → A+
80–89     → A
70–79     → B
60–69     → C
40–59     → D
Below 40  → Fail
```

The student should pass only when they pass in every subject.

---

## 🧠 Problem-Solving Approach

```text
Understand Problem
       ↓
Identify Input
       ↓
Identify Output
       ↓
Find Conditions
       ↓
Write Logic
       ↓
Write Code
       ↓
Test
       ↓
Debug
```

---

## 🔗 Connection With Future Topics

```text
Conditional Statements
        ↓
Loops
        ↓
Functions
        ↓
Data Structures
        ↓
DSA
        ↓
Algorithms
        ↓
Data Analysis
        ↓
Machine Learning
        ↓
AI/ML Projects
```

---

## 📝 Day 006 Reflection

### What I Learned

I learned how Python makes decisions using conditional statements.

### Most Important Concept

```text
if → elif → else
```

### What I Practiced

I practiced comparison operators, logical operators and decision-making programs.

### What I Need to Improve

I need more practice with nested conditions and solving problems independently.

---

## 🎯 Day 006 Checklist

* [x] Learn `if`
* [x] Learn `else`
* [x] Learn `elif`
* [x] Learn nested `if`
* [x] Learn comparison operators
* [x] Learn logical operators
* [x] Practice programs
* [x] Build mini project
* [ ] Revision
* [ ] GitHub Push

 