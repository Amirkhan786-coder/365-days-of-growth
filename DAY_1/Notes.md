# 🚀 365 Days of Growth
# 📖 Day 1 - Python Fundamentals

**Author:** Md Amir Khan  
**Day:** 001/365  
**Date:** 26 July 2026

---

# 📌 Chapter 1 - Introduction to Python

## What is Python?

Python is a **high-level, interpreted, object-oriented, and general-purpose programming language** created by **Guido van Rossum** in **1991**.

Python is one of the world's most popular programming languages because it is simple, readable, and powerful. It is used by beginners as well as professionals to build software, websites, artificial intelligence systems, machine learning models, automation scripts, games, and much more.

Unlike many other programming languages, Python focuses on code readability, allowing developers to write fewer lines of code while solving complex problems.

---

# 🌍 Real-World Applications of Python

Python is used in almost every major technology field.

## 1️⃣ Artificial Intelligence (AI)

Python is widely used to build intelligent systems.

### Examples

- ChatGPT
- Recommendation Systems
- Voice Assistants
- Face Recognition

### Popular Libraries

- TensorFlow
- PyTorch
- Scikit-Learn

---

## 2️⃣ Machine Learning

Machine Learning helps computers learn from data.

### Examples

- House Price Prediction
- Spam Detection
- Stock Market Prediction

### Popular Libraries

- NumPy
- Pandas
- Scikit-Learn

---

## 3️⃣ Data Science

Python is one of the most popular languages for Data Science.

### Uses

- Data Cleaning
- Data Analysis
- Data Visualization

### Popular Libraries

- Pandas
- NumPy
- Matplotlib

---

## 4️⃣ Web Development

Python can build websites and APIs using

- Flask
- Django
- FastAPI

### Real World Examples

- Instagram Backend
- Spotify Services

---

## 5️⃣ Automation

Python automates repetitive tasks.

### Examples

- Sending Emails
- Renaming Files
- Excel Automation
- File Management

---

## 6️⃣ Cyber Security

Python is used in

- Ethical Hacking
- Network Automation
- Penetration Testing
- Security Tools

---

## 7️⃣ Internet of Things (IoT)

Python works with

- Raspberry Pi
- ESP32
- Arduino (using MicroPython)

### Examples

- Smart Home Automation
- Weather Monitoring
- Home Security Systems

---

# 📌 Chapter 2 - Features of Python

Python became popular because of its amazing features.

## ✅ Easy to Learn

Python syntax is very simple.

```python
print("Hello World")
```

Even beginners can understand this code.

---

## ✅ Easy to Read

Python avoids unnecessary symbols.

```python
age = 19
```

Python code looks almost like English.

---

## ✅ Interpreted Language

Python executes code **line by line**.

### Advantages

- Easy Debugging
- Faster Testing
- Immediate Output

---

## ✅ Platform Independent

Python programs run on

- Windows
- Linux
- macOS

without changing the source code.

---

## ✅ Open Source

Python is completely free to download and use.

---

## ✅ Huge Community Support

Millions of developers use Python.

Whenever you face an error, chances are someone has already solved it.

---

## ✅ Large Library Collection

| Library | Purpose |
|----------|----------|
| NumPy | Numerical Computing |
| Pandas | Data Analysis |
| Matplotlib | Data Visualization |
| OpenCV | Computer Vision |
| Flask | Web Development |
| Streamlit | Data Apps |
| TensorFlow | Deep Learning |

---

# 📌 Chapter 3 - Installing Python

## Steps

1. Download Python from

https://python.org

2. Install Python.

3. Tick

✅ Add Python to PATH

4. Open Terminal.

5. Run

```bash
python --version
```

### Output

```
Python 3.x.x
```

---

# 📌 Chapter 4 - Your First Python Program

```python
print("Hello World")
```

### Output

```
Hello World
```

## Explanation

`print()` is a built-in function used to display output on the screen.

Example

```python
print("Welcome")
print("Python")
print("Day 1")
```

Output

```
Welcome
Python
Day 1
```

---

# 📌 Chapter 5 - Variables

## What is a Variable?

A variable is a named memory location used to store data.

Think of it as a labeled container.

Example

```
Name  → Amir
Age   → 19
CGPA  → 8.60
```

Python Code

```python
name = "Amir"
age = 19
cgpa = 8.60
```

---

## Why Do We Use Variables?

Variables help us

- Store Data
- Update Data
- Reuse Data
- Make programs dynamic

Without variables, programming becomes difficult.

---

## Variable Naming Rules

### ✅ Correct

```python
student_name
age
cgpa
mobileNumber
```

### ❌ Wrong

```python
1name
student-name
class
```

---

## Variable Naming Tips

✔ Use meaningful names

❌ x

✔ student_name

✔ total_marks

✔ average_salary

---

# 📌 Chapter 6 - Data Types

Everything stored in Python has a data type.

---

## Integer (int)

Stores whole numbers.

```python
age = 19
```

---

## Float

Stores decimal numbers.

```python
cgpa = 8.45
```

---

## String (str)

Stores text.

```python
college = "Shobhit University"
```

---

## Boolean (bool)

Stores only

```python
True
False
```

Example

```python
passed = True
```

---

## Checking Data Type

```python
print(type(age))
print(type(college))
```

Output

```
<class 'int'>
<class 'str'>
```

---

# 📌 Chapter 7 - Input Function

Python accepts user input using

```python
input()
```

Example

```python
name = input("Enter Name : ")
print(name)
```

Output

```
Enter Name : Amir
Amir
```

---

## Multiple Inputs

```python
name = input()

age = input()

college = input()
```

---

# 📌 Chapter 8 - Type Casting

Input always returns **String**.

Example

```python
age = input()
```

If user enters

```
19
```

Python stores

```
"19"
```

---

## Integer Conversion

```python
age = int(input())
```

---

## Float Conversion

```python
salary = float(input())
```

---

## String Conversion

```python
name = str(input())
```

---

# 📌 Chapter 9 - Operators

Operators perform operations on values.

---

## Arithmetic Operators

| Operator | Meaning |
|----------|---------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulus |
| // | Floor Division |
| ** | Power |

Example

```python
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
```

Output

```
13
7
30
3.333
1
3
1000
```

---

## Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than Equal |
| <= | Less Than Equal |

Example

```python
a = 10
b = 20

print(a > b)
print(a < b)
```

Output

```
False
True
```

---

## Logical Operators

| Operator | Meaning |
|----------|---------|
| and | Both conditions True |
| or | Any one condition True |
| not | Reverse Result |

Example

```python
age = 20

print(age > 18 and age < 30)
```

Output

```
True
```

---

## Assignment Operators

| Operator | Meaning |
|----------|---------|
| = | Assign |
| += | Add and Assign |
| -= | Subtract and Assign |
| *= | Multiply and Assign |
| /= | Divide and Assign |

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

# 📌 Chapter 10 - Comments

Comments improve code readability.

## Single Line Comment

```python
# This is a comment
```

---

## Multi-Line Comment

```python
"""
Python Day 1
Learning Notes
"""
```

---

# 📌 Common Beginner Mistakes

- Forgetting quotation marks.
- Using reserved keywords.
- Wrong indentation.
- Wrong variable names.
- Forgetting type conversion.
- Confusing `=` with `==`.

---

# 🎯 Key Takeaways

After completing Day 1, you should be able to

- Explain what Python is.
- Write your first Python program.
- Create variables.
- Understand Python data types.
- Take user input.
- Perform type casting.
- Use arithmetic, comparison, logical and assignment operators.
- Write comments in Python.

---

# 📚 Day 1 Summary

## Topics Covered

- Introduction to Python
- Features of Python
- Installing Python
- First Python Program
- Variables
- Data Types
- Input Function
- Type Casting
- Operators
- Comments

## Status

✅ Theory Completed

## Next Topic

**Day 2 - Strings, Conditional Statements and Loops**

---

# 🏆 Quote of the Day

> **"Consistency beats talent when talent doesn't stay consistent."**

**Day 001 Completed Successfully ✅**