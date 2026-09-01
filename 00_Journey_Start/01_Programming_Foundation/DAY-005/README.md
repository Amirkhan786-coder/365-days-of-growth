
#  Python Operators

Welcome to Day 005 of my 365 Days of Growth journey! 

Today, I learned about Python Operators.

Operators are special symbols or keywords used to perform operations on values and variables.

## 🎯 Topics Covered

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Membership Operators
- Identity Operators
- Bitwise Operators
- Operator Precedence
- Practical Programming Problems

## 🧠 What is an Operator?

An operator is a symbol or keyword that performs an operation.

Example:

```python
a = 10
b = 5

print(a + b)
````

Here:

* `+` is the operator
* `a` and `b` are operands

Output:

```text
15
```

## 🔢 Types of Operators

### 1. Arithmetic Operators

Used for mathematical calculations.

```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
%    Modulus
//   Floor Division
**   Exponentiation
```

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
```

### 2. Assignment Operators

Used to assign and update values.

```text
= 
+=
-=
*=
/=
%=
```

Example:

```python
x = 10

x += 5

print(x)
```

Output:

```text
15
```

### 3. Comparison Operators

Used to compare two values.

```text
==
!=
>
<
>=
<=
```

The result is always:

```text
True
```

or:

```text
False
```

Example:

```python
a = 10
b = 5

print(a > b)
```

Output:

```text
True
```

### 4. Logical Operators

Python provides:

```text
and
or
not
```

Example:

```python
age = 20

print(age >= 18 and age <= 60)
```

### 5. Membership Operators

Used to check whether a value exists inside a sequence.

```text
in
not in
```

Example:

```python
name = "Amir"

print("A" in name)
```

### 6. Identity Operators

Used to check whether two variables refer to the same object.

```text
is
is not
```

Example:

```python
a = None

print(a is None)
```

### 7. Bitwise Operators

Used to perform operations at the binary level.

```text
&
|
^
~
<<
>>
```

These will become more important when studying computer fundamentals and advanced programming.

## 🧮 Operator Precedence

When multiple operators are used in an expression, Python follows a specific order.

Example:

```python
result = 10 + 5 * 2
```

Multiplication is performed first.

So:

```text
10 + 5 * 2
= 10 + 10
= 20
```

Use parentheses when you want to clearly control the order:

```python
result = (10 + 5) * 2
```

Output:

```text
30
```

## 🛠️ Practical Applications

Operators are used in:

* Calculators
* Banking systems
* Student result systems
* Billing systems
* Age calculators
* Games
* Data structures
* Algorithms
* Machine Learning calculations
* Data preprocessing

## 📁 Files

* README.md
* notes.md
* operators.py
* practice_questions.md
* answers.py
* mini_project.py

## 🎯 Day 005 Goal

By the end of today, I should be able to:

* Understand different operators
* Perform mathematical calculations
* Compare values
* Combine conditions
* Update variables
* Solve basic programming problems
* Understand operator precedence

## 🚀 Journey Progress

* ✅ Day 001 — Journey Foundation
* ✅ Day 002 — Programming Foundations & Problem Solving
* ✅ Day 003 — Python Variables & Data Types
* ✅ Day 004 — Python Input & Type Conversion
* 🚀 Day 005 — Python Operators

## 💡 Final Thought

> Strong programming starts with understanding how small operations work.

Learn → Practice → Solve → Build → Improve
