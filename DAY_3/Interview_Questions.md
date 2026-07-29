# 🚀 DAY 03 – Python Loops Interview Questions

## 📚 Topic
Python Loops (for, while, break, continue, pass)

---

# 1. What is a loop in Python?

**Answer:**
A loop is a programming structure used to execute a block of code repeatedly until a condition becomes false or a sequence is exhausted.

---

# 2. How many types of loops are available in Python?

**Answer:**

There are two main loops:

- for loop
- while loop

---

# 3. What is a for loop?

**Answer:**
A for loop is used to iterate over a sequence or perform a task a fixed number of times.

Example:

```python
for i in range(5):
    print(i)
```

---

# 4. What is a while loop?

**Answer:**
A while loop executes repeatedly as long as its condition remains True.

Example:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# 5. What is the difference between for and while loops?

**Answer:**

| for Loop | while Loop |
|-----------|------------|
| Used for fixed iterations | Used when iterations are unknown |
| Easier to write | Condition-based |
| Mostly used with range() | Mostly used with user input |

---

# 6. What is the range() function?

**Answer:**
The range() function generates a sequence of numbers.

Example:

```python
range(1, 6)
```

Output:

```
1 2 3 4 5
```

---

# 7. What are the parameters of range()?

**Answer:**

```python
range(start, stop, step)
```

Example:

```python
range(2, 11, 2)
```

Output:

```
2 4 6 8 10
```

---

# 8. What is an infinite loop?

**Answer:**
An infinite loop never stops because its condition is always True.

Example:

```python
while True:
    print("Hello")
```

---

# 9. What is the break statement?

**Answer:**
The break statement immediately terminates the loop.

Example:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

# 10. What is the continue statement?

**Answer:**
The continue statement skips the current iteration and moves to the next iteration.

Example:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# 11. What is the pass statement?

**Answer:**
The pass statement is a placeholder that does nothing.

Example:

```python
for i in range(5):
    pass
```

---

# 12. What is a nested loop?

**Answer:**
A nested loop is a loop inside another loop.

---

# 13. Why are nested loops used?

**Answer:**
Nested loops are mainly used for:

- Pattern printing
- Matrix operations
- Table generation

---

# 14. Can we use break inside a while loop?

**Answer:**
Yes.

---

# 15. Can we use continue inside a for loop?

**Answer:**
Yes.

---

# 16. What happens if we forget to update the variable in a while loop?

**Answer:**
It may create an infinite loop.

---

# 17. Which loop is best for traversing a list?

**Answer:**
The for loop.

---

# 18. Which loop is used when the number of iterations is unknown?

**Answer:**
The while loop.

---

# 19. What is loop iteration?

**Answer:**
One execution of the loop body is called an iteration.

---

# 20. Can we use else with loops?

**Answer:**
Yes.

Example:

```python
for i in range(3):
    print(i)
else:
    print("Loop Finished")
```

---

# 21. What is loop control?

**Answer:**
Loop control statements change the normal flow of a loop.

Examples:

- break
- continue
- pass

---

# 22. What is the time complexity of a simple loop?

**Answer:**
Generally **O(n)**.

---

# 23. What is the time complexity of nested loops?

**Answer:**
Generally **O(n²)**.

---

# 24. What are common mistakes while using loops?

**Answer:**

- Infinite loops
- Wrong indentation
- Incorrect range()
- Forgetting to update variables

---

# 25. Can a loop exist without a condition?

**Answer:**
A `for` loop iterates over a sequence, while a `while` loop always requires a condition.

---

# 26. Which loop is more readable?

**Answer:**
Usually the for loop.

---

# 27. Give some real-life applications of loops.

**Answer:**

- ATM Machine
- Login System
- Games
- Billing Software
- Attendance System
- AI Model Training
- Data Processing

---

# 28. What is pattern printing?

**Answer:**
Pattern printing is the process of generating shapes using loops.

Example:

```
*
**
***
****
*****
```

---

# 29. What are loop variables?

**Answer:**
Loop variables change automatically during each iteration.

Example:

```python
for i in range(5):
    print(i)
```

Here, **i** is the loop variable.

---

# 30. Why are loops important?

**Answer:**
Loops reduce code repetition, improve efficiency, automate repetitive tasks, and make programs easier to maintain.

---

# 🎯 Interview Tips

✅ Understand the difference between `for` and `while`.

✅ Learn `range()` thoroughly.

✅ Practice `break`, `continue`, and `pass`.

✅ Be comfortable with nested loops.

✅ Practice pattern-printing questions.

✅ Solve real-world loop problems.

---

# 🌟 Key Takeaway

> "Loops help programmers write less code and accomplish more work."