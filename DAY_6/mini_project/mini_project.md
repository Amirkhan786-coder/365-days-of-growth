# 🚀 DAY 06 — MINI PROJECT

# 🎓 STUDENT RESULT MANAGER

## 365 Days of Growth

---

## 📌 Project Overview

Student Result Manager ek simple Python-based mini project hai jo student ki basic information aur marks ko manage karta hai.

Is project me hum **Python Tuples** ka practical use karenge.

Program student ke:

- Name
- Roll Number
- Subjects
- Marks
- Total Marks
- Average
- Percentage
- Grade
- Pass/Fail Result

ko calculate aur display karega.

---

# 🎯 Project Objective

Is project ka main objective hai:

```text
Python Tuples
      ↓
Tuple Indexing
      ↓
Tuple Unpacking
      ↓
Loops
      ↓
Conditional Statements
      ↓
Functions
      ↓
Result Calculation
```

In concepts ko ek real-world project me apply karna.

---

# 🧠 Concepts Used

- Python Tuples
- Tuple Indexing
- Tuple Unpacking
- Nested Tuples
- `len()`
- `sum()`
- `max()`
- `min()`
- `input()`
- `if-elif-else`
- `for` loop
- Functions
- String Formatting
- Basic Calculations

---

# 📂 Project Structure

```text
07_Mini_Project/
│
├── student_result_manager.py
└── README.md
```

---

# 💻 MAIN CODE

File:

`student_result_manager.py`

```python
# ==========================================
# STUDENT RESULT MANAGER
# Day 06 - Python Tuples
# 365 Days of Growth
# ==========================================


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    elif percentage >= 40:
        return "E"

    else:
        return "F"


def calculate_result(marks):

    for mark in marks:

        if mark < 33:
            return "FAIL"

    return "PASS"


print("=" * 45)
print("       STUDENT RESULT MANAGER")
print("=" * 45)


# Student Information

name = input("Enter Student Name: ")

roll_number = input("Enter Roll Number: ")

course = input("Enter Course: ")


# Subjects

subjects = (
    "Python",
    "Mathematics",
    "English",
    "Computer",
    "Data Science"
)


# Taking Marks

marks = []

for subject in subjects:

    while True:

        try:

            mark = float(
                input(f"Enter marks in {subject}: ")
            )

            if 0 <= mark <= 100:

                marks.append(mark)

                break

            else:

                print("Enter marks between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")


# Convert List into Tuple

marks = tuple(marks)


# Calculate Result

total = sum(marks)

average = total / len(marks)

percentage = average

highest = max(marks)

lowest = min(marks)

grade = calculate_grade(percentage)

result = calculate_result(marks)


# Student Record Tuple

student = (
    name,
    roll_number,
    course,
    subjects,
    marks
)


# Display Result

print()
print("=" * 45)
print("             STUDENT RESULT")
print("=" * 45)

print("Name       :", student[0])
print("Roll No.   :", student[1])
print("Course     :", student[2])

print("-" * 45)

print("Subject-wise Marks:")

for subject, mark in zip(student[3], student[4]):

    print(f"{subject:<15}: {mark:g}")


print("-" * 45)

print("Total Marks:", total)
print("Average    :", average)
print("Percentage :", percentage)
print("Highest    :", highest)
print("Lowest     :", lowest)
print("Grade      :", grade)
print("Result     :", result)

print("=" * 45)

print("       THANK YOU FOR USING")
print("       STUDENT RESULT MANAGER")
print("=" * 45)
```

---

# 🖥️ SAMPLE OUTPUT

```text
=============================================
       STUDENT RESULT MANAGER
=============================================

Enter Student Name: Amir
Enter Roll Number: 101
Enter Course: AIML

Enter marks in Python: 85
Enter marks in Mathematics: 90
Enter marks in English: 78
Enter marks in Computer: 92
Enter marks in Data Science: 88


=============================================
             STUDENT RESULT
=============================================

Name       : Amir
Roll No.   : 101
Course     : AIML

---------------------------------------------
Subject-wise Marks:

Python         : 85
Mathematics    : 90
English        : 78
Computer       : 92
Data Science   : 88

---------------------------------------------

Total Marks: 433
Average    : 86.6
Percentage : 86.6
Highest    : 92
Lowest     : 78
Grade      : A
Result     : PASS

=============================================
       THANK YOU FOR USING
       STUDENT RESULT MANAGER
=============================================
```

---

# 🔍 HOW THE PROJECT WORKS

## Step 1 — Student Information

User se:

```text
Name
Roll Number
Course
```

input liya jata hai.

---

## Step 2 — Subjects

Subjects ko Tuple me store kiya gaya:

```python
subjects = (
    "Python",
    "Mathematics",
    "English",
    "Computer",
    "Data Science"
)
```

---

## Step 3 — Marks Input

`for` loop se har subject ke marks liye jaate hain.

```python
for subject in subjects:
```

---

## Step 4 — Marks Validation

Program check karta hai ki marks:

```text
0 ≤ marks ≤ 100
```

ke beech hain.

---

## Step 5 — List to Tuple

Input ke time marks temporarily List me store hote hain.

Uske baad:

```python
marks = tuple(marks)
```

se List ko Tuple me convert kar diya jata hai.

---

## Step 6 — Calculation

Total:

```python
total = sum(marks)
```

Average:

```python
average = total / len(marks)
```

Highest:

```python
highest = max(marks)
```

Lowest:

```python
lowest = min(marks)
```

---

## Step 7 — Grade

Percentage ke according grade calculate hota hai.

```text
90+  → A+
80+  → A
70+  → B
60+  → C
50+  → D
40+  → E
<40  → F
```

---

## Step 8 — Pass/Fail

Agar kisi bhi subject me marks `33` se kam hain:

```text
FAIL
```

Otherwise:

```text
PASS
```

---

# 🧠 IMPORTANT TUPLE CONCEPT

Student record ko Tuple me store kiya gaya:

```python
student = (
    name,
    roll_number,
    course,
    subjects,
    marks
)
```

Isse hum Tuple indexing ka use kar sakte hain:

```python
student[0]
```

→ Name

```python
student[1]
```

→ Roll Number

```python
student[2]
```

→ Course

```python
student[3]
```

→ Subjects

```python
student[4]
```

→ Marks

---

# 🔥 PROJECT CHALLENGES

Project complete hone ke baad ye features khud add karo:

### Challenge 1

Student ka percentage calculate karo.

### Challenge 2

Student ka pass/fail status show karo.

### Challenge 3

Highest marks wala subject find karo.

### Challenge 4

Lowest marks wala subject find karo.

### Challenge 5

A+ se F tak complete grading system improve karo.

### Challenge 6

Multiple students ka record store karo.

Example:

```python
students = (
    ("Amir", 101, 86),
    ("Rahul", 102, 91),
    ("Aman", 103, 78)
)
```

### Challenge 7

Class topper find karo.

### Challenge 8

Result ko formatted table ki tarah display karo.

---

# 🎯 LEARNING OUTCOME

Project complete karne ke baad mujhe:

- Tuples samajh aayenge
- Tuple indexing aayegi
- Tuple unpacking aayegi
- Nested Tuples samajh aayenge
- Loops ka practical use aayega
- Conditions ka use aayega
- Functions ka use samajh aayega
- Basic result calculation aayega
- Real-world Python project banana aayega

---

# 🏆 PROJECT STATUS

```text
Project Idea       ✅
Tuple Concept      ✅
Input System       ✅
Marks Calculation  ✅
Grade System       ✅
Pass/Fail          ✅
Result Display     ✅
Validation         ✅
Mini Project       ✅
```

---

# 🚀 DAY 06 MINI PROJECT

## STUDENT RESULT MANAGER

**Technology:**

```text
Python
```

**Main Concept:**

```text
Tuples
```

**Project Type:**

```text
Console-Based Python Application
```

**Status:**

```text
COMPLETED ✅
```

---

# 💡 FINAL MESSAGE

> Don't just learn Python. Use Python to solve problems.

**Day 06 — Learn → Practice → Build → Push → Grow 🚀**