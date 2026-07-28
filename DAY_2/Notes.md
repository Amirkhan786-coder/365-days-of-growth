# 🚀 DAY 2 / 365

# Python Operators & Conditional Statements

---

# 📅 Date

Day 2

---

# 🎯 Learning Objective

By the end of today, I will be able to:

✅ Understand Python Operators

✅ Perform Mathematical Operations

✅ Compare Values

✅ Write Logical Conditions

✅ Use if Statement

✅ Use if-else Statement

✅ Use if-elif-else Statement

✅ Build Simple Decision-Making Programs

---

# 📖 Introduction

Programming is all about solving problems.

A computer cannot think on its own.

We give instructions to the computer.

Sometimes the computer needs to make decisions.

Example:

If marks are greater than or equal to 33,
the student passes.

Otherwise,
the student fails.

This decision-making process is called Conditional Programming.

---

# What are Operators?

Operators are special symbols used to perform operations on values and variables.

Example

```python
a = 20
b = 10

print(a + b)
```

Output

```
30
```

Here

+

is an Operator.

---

# Types of Operators

Python has several types of operators.

1. Arithmetic Operators

2. Assignment Operators

3. Comparison Operators

4. Logical Operators

5. Identity Operators

6. Membership Operators

---

# 1. Arithmetic Operators

These operators perform mathematical calculations.

| Operator | Meaning | Example |
|----------|---------|----------|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| % | Modulus | 10 % 3 |
| // | Floor Division | 10 // 3 |
| ** | Exponent | 2 ** 3 |

---

## Example

```python
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
```

---

# 2. Assignment Operators

These operators assign values.

Example

```python
x = 10
```

Now x stores 10.

Other assignment operators:

+=

-=

*=

/=

%=

Example

```python
x = 10

x += 5

print(x)
```

Output

```
15
```

---

# 3. Comparison Operators

These compare two values.

Result is always

True

or

False

Operators

==

!=

>

<

>=

<=

Example

```python
a = 15
b = 20

print(a > b)
```

Output

```
False
```

---

# 4. Logical Operators

Logical operators combine multiple conditions.

Three logical operators:

and

or

not

Example

```python
age = 20

print(age >= 18 and age <= 60)
```

Output

```
True
```

---

# 5. Identity Operators

Identity operators check whether two variables refer to the same object.

Operators

is

is not

Example

```python
a = 10
b = 10

print(a is b)
```

Output

```
True
```

---

# 6. Membership Operators

These check whether a value exists inside a sequence.

Operators

in

not in

Example

```python
name = "Amir"

print("A" in name)
```

Output

```
True
```

---

# Type Casting

Sometimes we need to convert one data type into another.

This process is called Type Casting.

Functions

int()

float()

str()

bool()

Example

```python
num = "25"

print(int(num) + 5)
```

Output

```
30
```

---

# Conditional Statements

Conditional statements help the computer make decisions.

---

# if Statement

Syntax

```python
if condition:
    statement
```

Example

```python
age = 20

if age >= 18:
    print("Eligible for Voting")
```

---

# if else Statement

Syntax

```python
if condition:
    statement
else:
    statement
```

Example

```python
marks = 28

if marks >= 33:
    print("Pass")
else:
    print("Fail")
```

---

# if elif else Statement

Used when multiple conditions exist.

Example

```python
marks = 85

if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 70:
    print("B")

else:
    print("Needs Improvement")
```

---

# Nested if

One if statement inside another.

Example

```python
age = 20

citizen = True

if age >= 18:
    if citizen:
        print("Eligible")
```

---

# Real Life Examples

ATM Machine

If Balance > Withdrawal Amount

Cash Withdrawn

Else

Transaction Failed

------------------------------------

Google Login

If Password Correct

Login Success

Else

Access Denied

------------------------------------

E-commerce Website

If Coupon Available

Discount Applied

Else

Original Price

---

# Common Errors

❌ Missing Colon

Wrong

```python
if age > 18
```

Correct

```python
if age > 18:
```

---

❌ Wrong Indentation

Wrong

```python
if age > 18:
print(age)
```

Correct

```python
if age > 18:
    print(age)
```

---

❌ Comparing String with Integer

Wrong

```python
age = input()

if age > 18:
```

Correct

```python
age = int(input())

if age > 18:
```

---

# Best Practices

✔ Use meaningful variable names

✔ Maintain indentation

✔ Keep conditions simple

✔ Use comments

✔ Write readable code

✔ Test every program

---

# Interview Tips

Remember these points.

Difference between = and ==

Difference between if and if-else

Difference between / and //

Difference between is and ==

Difference between int() and float()

Meaning of Boolean

Meaning of True and False

---

# Revision Summary

Today I learned

✔ Operators

✔ Arithmetic Operators

✔ Assignment Operators

✔ Comparison Operators

✔ Logical Operators

✔ Membership Operators

✔ Identity Operators

✔ Type Casting

✔ if Statement

✔ if else Statement

✔ if elif else Statement

✔ Nested if

---

# Quick Revision Questions

1. What is an operator?

2. Name different types of operators.

3. Difference between == and = ?

4. What is Type Casting?

5. Difference between if and if else?

6. What is Nested if?

7. What is Logical Operator?

8. Difference between and & or?

9. What is Membership Operator?

10. What is Identity Operator?

---

# End of Notes

"Strong fundamentals build strong programmers."

🚀 Day 2 Theory Completed Successfully.