# 🚀 DAY 03 - Python Loops

> "Automation begins with loops. Instead of repeating yourself, let the computer repeat the work."

---

# 📚 What is a Loop?

A loop is a programming structure that allows a block of code to run repeatedly until a condition becomes false.

Loops help us avoid writing the same code again and again.

---

# Why Do We Use Loops?

Without loops:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

With loops:

```python
for i in range(1, 6):
    print(i)
```

Less code.
More efficient.
Easy to understand.

---

# Types of Loops in Python

Python has two loops.

1. for Loop
2. while Loop

---

# 1. for Loop

A for loop is used when the number of iterations is known.

Syntax

```python
for variable in sequence:
    statements
```

Example

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# range() Function

The range() function generates numbers.

Syntax

```python
range(start, stop, step)
```

Examples

```python
range(5)
```

Output

```
0 1 2 3 4
```

---

```python
range(1,6)
```

Output

```
1 2 3 4 5
```

---

```python
range(2,11,2)
```

Output

```
2 4 6 8 10
```

---

# Printing Even Numbers

```python
for i in range(2,21,2):
    print(i)
```

---

# Printing Odd Numbers

```python
for i in range(1,20,2):
    print(i)
```

---

# Reverse Loop

```python
for i in range(10,0,-1):
    print(i)
```

---

# while Loop

A while loop executes until a condition becomes false.

Syntax

```python
while condition:
    statements
```

Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output

```
1
2
3
4
5
```

---

# Difference Between for and while

| for Loop | while Loop |
|-----------|------------|
| Fixed iterations | Unknown iterations |
| Easier syntax | Condition based |
| Mostly used with range() | Mostly used for user input |

---

# Infinite Loop

```python
while True:
    print("Hello")
```

Never stops until interrupted.

---

# break Statement

Stops the loop immediately.

Example

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

Output

```
0
1
2
3
4
```

---

# continue Statement

Skips the current iteration.

Example

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

Output

```
0
1
3
4
```

---

# pass Statement

Used as a placeholder.

```python
for i in range(5):
    pass
```

---

# Nested Loop

A loop inside another loop.

Example

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Output

```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

# Pattern Printing

Example

```python
for i in range(5):
    print("*" * (i + 1))
```

Output

```
*
**
***
****
*****
```

---

# Real-Life Uses of Loops

- ATM Machine
- Login System
- Password Validation
- Attendance System
- Billing Software
- E-commerce Cart
- Banking Applications
- Games
- AI Training
- Machine Learning Data Processing

---

# Common Mistakes

❌ Forgetting to update variable in while loop.

❌ Wrong indentation.

❌ Incorrect range() values.

❌ Infinite loop.

❌ Using break instead of continue.

---

# Interview Tips

✔ Know range()

✔ Difference between for and while

✔ break

✔ continue

✔ pass

✔ Nested loops

✔ Pattern Printing

✔ Infinite loop

---

# Quick Revision

✅ for Loop

✅ while Loop

✅ range()

✅ break

✅ continue

✅ pass

✅ Nested Loop

✅ Pattern Printing

---

# Learning Outcome

After completing Day 03, I can:

✔ Write for loops.

✔ Write while loops.

✔ Use range() effectively.

✔ Control loops using break and continue.

✔ Create simple patterns.

✔ Solve loop-based programming problems.

✔ Build loop-based mini projects.

---

# Quote of the Day

> "Don't fear repetition. Repetition is how mastery is built."