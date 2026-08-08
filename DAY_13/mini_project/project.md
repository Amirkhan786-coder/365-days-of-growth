# 🚀 Day 13 Mini Project
# Student Information System

## 📌 Project Name

**Student Information System**

---

## 🎯 Project Objective

The objective of this project is to create a simple Student Information System using Python Modules.

This project demonstrates how a large Python program can be divided into multiple smaller and reusable files.

---

# 🧠 Concepts Used

This project uses:

- Python Modules
- `import`
- `from ... import`
- Functions
- Variables
- User Input
- Conditional Statements
- Arithmetic Operations
- Return Statements
- Code Reusability
- Project Organization

---

# 📂 Project Structure

```text
Day13/
│
├── notes.md
├── practice.md
├── mcqs.md
├── interview_questions.md
├── reflection.md
├── README.md
├── project.md
│
└── mini_project/
    │
    ├── main.py
    ├── student.py
    └── marks.py
```

---

# 📄 File 1 — student.py

This file handles student information.

```python
def get_student_details():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")

    return name, age, course
```

---

# 📄 File 2 — marks.py

This file handles student marks and result calculation.

```python
def get_marks():
    python = float(input("Enter Python marks: "))
    java = float(input("Enter Java marks: "))
    maths = float(input("Enter Maths marks: "))

    return python, java, maths


def calculate_result(python, java, maths):

    total = python + java + maths
    percentage = total / 3

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return total, percentage, result
```

---

# 📄 File 3 — main.py

This is the main file that imports and uses the other modules.

```python
from student import get_student_details
from marks import get_marks, calculate_result


print("=" * 45)
print("       STUDENT INFORMATION SYSTEM")
print("=" * 45)

name, age, course = get_student_details()

print("\nEnter Student Marks")
print("-" * 30)

python, java, maths = get_marks()

total, percentage, result = calculate_result(
    python,
    java,
    maths
)

print("\n" + "=" * 45)
print("          STUDENT REPORT")
print("=" * 45)

print("Name       :", name)
print("Age        :", age)
print("Course     :", course)

print("-" * 45)

print("Python     :", python)
print("Java       :", java)
print("Maths      :", maths)

print("-" * 45)

print("Total      :", total)
print("Percentage :", round(percentage, 2), "%")
print("Result     :", result)

print("=" * 45)
print("       THANK YOU FOR USING THE SYSTEM")
print("=" * 45)
```

---

# ▶️ How to Run

Open the terminal inside the `mini_project` folder.

Run:

```bash
python main.py
```

---

# 💻 Example Input

```text
Enter student name: Amir
Enter student age: 20
Enter course: B.Tech CSE

Enter Student Marks
------------------------------
Enter Python marks: 85
Enter Java marks: 80
Enter Maths marks: 90
```

---

# 🖥️ Example Output

```text
=============================================
          STUDENT REPORT
=============================================
Name       : Amir
Age        : 20
Course     : B.Tech CSE
---------------------------------------------
Python     : 85.0
Java       : 80.0
Maths      : 90.0
---------------------------------------------
Total      : 255.0
Percentage : 85.0 %
Result     : PASS
=============================================
```

---

# 🔍 How the Project Works

The project is divided into three files.

```text
student.py
     ↓
Collects student information
     ↓
marks.py
     ↓
Collects marks and calculates result
     ↓
main.py
     ↓
Displays final student report
```

---

# 📚 Module Concept

The important concept demonstrated by this project is **code modularity**.

Instead of writing everything inside `main.py`, different responsibilities are divided into different modules.

```text
student.py
→ Student information

marks.py
→ Marks and result

main.py
→ Main program
```

---

# ✅ Features

- Accepts student name
- Accepts student age
- Accepts course
- Accepts subject marks
- Calculates total marks
- Calculates percentage
- Determines PASS/FAIL
- Displays student report
- Uses custom Python modules

---

# 🔮 Future Improvements

This project can be improved by adding:

- Multiple students
- More subjects
- Grade calculation
- Student ID
- File storage
- CSV database
- Search student
- Update student
- Delete student
- Login system
- GUI
- Database connectivity

---

# 🧠 What I Learned From This Project

Through this project I learned how to:

- Create custom modules
- Import custom modules
- Use functions across different files
- Return multiple values
- Organize project files
- Separate responsibilities
- Build a modular Python application

---

# 🏆 Project Status

```text
Project Created       ✅
Modules Created       ✅
Functions Used        ✅
Module Import         ✅
Result Calculation    ✅
Testing               ✅
Documentation         ✅
```

---

# 📊 Day 13 Progress

```text
Notes                  ✅
Practice Questions     ✅
MCQs                   ✅
Interview Questions    ✅
Reflection             ✅
README                 ✅
Mini Project           ✅
Project Documentation  ✅
```

---

# 🚀 Day 13 Complete

**Topic:** Python Modules & Packages

**Mini Project:** Student Information System

**Progress:** 13 / 365

> Learn → Practice → Build → Document → Repeat