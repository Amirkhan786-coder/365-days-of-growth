# 🚀 Day 12 — Python Exception Handling

## 365 Days of Growth

> Learning Python one day at a time and building my skills through consistent practice.

---

## 📅 Day 12

### 📚 Today's Topic

**Python Exception Handling**

Today I learned how to identify, handle, and manage errors and exceptions in Python programs.

---

# 🧠 Topics Covered

- What is an Exception?
- Exception Handling
- `try`
- `except`
- `else`
- `finally`
- `raise`
- Custom Exceptions
- Exception Object
- Multiple Exceptions
- Nested `try-except`
- Exception Propagation
- Exception Chaining
- Exception Re-raising
- Built-in Exceptions
- File Exception Handling
- Best Practices

---

# 🔥 Important Exceptions

```text
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
NameError
FileNotFoundError
PermissionError
AttributeError
ImportError
ModuleNotFoundError
```

---

# 💻 Basic Example

```python
try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Operation successful.")

finally:
    print("Program completed.")
```

---

# 🛠️ Custom Exception Example

```python
class AgeError(Exception):
    pass


try:

    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above.")

    print("You are eligible.")

except ValueError:

    print("Please enter a valid age.")

except AgeError as e:

    print("Error:", e)
```

---

# 🧪 Practice

I completed **35 Exception Handling practice questions**.

Practice included:

- ValueError handling
- TypeError handling
- ZeroDivisionError handling
- IndexError handling
- KeyError handling
- FileNotFoundError handling
- Multiple exceptions
- Nested exceptions
- Custom exceptions
- Exception propagation
- Exception chaining
- File handling
- Calculator
- Student Management System
- Student Result System

---

# 📝 Interview Preparation

Completed **35 Python Exception Handling Interview Questions**.

Important concepts:

```text
try       → Risky code

except    → Handles exception

else      → Runs when no exception occurs

finally   → Executes after try/except

raise     → Manually raises exception

as e      → Stores exception object
```

---

# 🎯 MCQs

Completed:

**35 MCQs**

Topics covered:

- Exception Handling
- Built-in Exceptions
- `try-except`
- `else`
- `finally`
- `raise`
- Custom Exceptions
- Exception Propagation
- Exception Chaining

---

# 💡 What I Learned

Today I learned that errors are a normal part of programming.

Instead of allowing a program to crash, Exception Handling allows us to:

- Detect problems
- Handle problems
- Show meaningful messages
- Continue program execution when appropriate
- Build reliable applications

---

# 🌍 Real-World Applications

Exception Handling is commonly used in:

- Banking Systems
- Login Systems
- Student Management Systems
- Hospital Management Systems
- File Management Systems
- E-commerce Applications
- APIs
- AI Applications
- Database Applications

---

# 📂 Day 12 Files

```text
Day-12/
│
├── notes.md
├── practice.md
├── interview_questions.md
├── mcqs.md
├── reflection.md
├── README.md
│
└── mini_project/
    └── ...
```

---

# 🏆 Day 12 Achievement

```text
Topic              : Python Exception Handling
Practice Questions : 35
MCQs               : 35
Interview Questions: 35
Reflection         : Completed
Notes              : Completed
GitHub README      : Completed
```

---

# 📈 Learning Progress

```text
Day 01  █████░░░░░
Day 02  █████░░░░░
Day 03  █████░░░░░
Day 04  █████░░░░░
Day 05  █████░░░░░
Day 06  █████░░░░░
Day 07  █████░░░░░
Day 08  █████░░░░░
Day 09  █████░░░░░
Day 10  █████░░░░░
Day 11  █████░░░░░
Day 12  ██████░░░░
```

---

# 🔥 My Learning Rule

```text
Learn
  ↓
Practice
  ↓
Make Mistakes
  ↓
Debug
  ↓
Improve
  ↓
Build
  ↓
Repeat
```

---

# 💭 Reflection

Exception Handling showed me that programming is not only about writing code that works.

It is also about preparing the program for unexpected situations.

I learned how to understand errors instead of being afraid of them.

Every error gives me an opportunity to improve my code.

---

# 🎯 Tomorrow's Goal

Tomorrow I will:

- Learn the next Python topic
- Practice coding problems
- Complete interview questions
- Solve MCQs
- Build a mini project
- Update GitHub
- Continue my 365 Days of Growth journey

---

# 🚀 365 Days of Growth

### Day 12 / 365 ✅

**Python Exception Handling**

**Learn → Practice → Debug → Build → Grow**

---

## ⭐ Consistency > Motivation

I don't need to be perfect every day.

I just need to keep moving forward.

# DAY 12 COMPLETE 🚀