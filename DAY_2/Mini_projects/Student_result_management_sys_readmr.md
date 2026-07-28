# 🚀 DAY 2 MINI PROJECT

# Student Result Management System

---

# 📌 Project Level

Beginner

---

# 📚 Concepts Used

✅ Variables

✅ Input()

✅ Output()

✅ Arithmetic Operators

✅ Comparison Operators

✅ if

✅ elif

✅ else

✅ Percentage Calculation

---

# 🎯 Project Objective

Build a simple Student Result Management System.

The program should

• Take Student Details

• Take Subject Marks

• Calculate Total

• Calculate Percentage

• Assign Grade

• Display Pass/Fail

• Print Final Report Card

---

# 🌍 Real Life Use

Schools

Colleges

Coaching Institutes

Online Examination Systems

Learning Management Systems

---

# 📂 Folder Structure

Day-02

│

├── student_result.py

├── README.md

└── output.png (Optional Screenshot)

---

# 📝 Algorithm

Step 1

Take Student Name

↓

Step 2

Take Roll Number

↓

Step 3

Input Marks of 5 Subjects

↓

Step 4

Calculate Total

↓

Step 5

Calculate Percentage

↓

Step 6

Assign Grade

↓

Step 7

Check Pass or Fail

↓

Step 8

Display Report Card

---

# 🧠 Flow

Start

↓

Input Student Details

↓

Input Marks

↓

Calculate

↓

Check Grade

↓

Check Result

↓

Print Report

↓

End

---

# 💻 Complete Python Code

```python
print("=" * 45)
print(" STUDENT RESULT MANAGEMENT SYSTEM ")
print("=" * 45)

name = input("Enter Student Name : ")
roll = input("Enter Roll Number  : ")

print("\nEnter Marks (Out of 100)\n")

english = float(input("English : "))
math = float(input("Mathematics : "))
science = float(input("Science : "))
computer = float(input("Computer : "))
social = float(input("Social Science : "))

total = english + math + science + computer + social

percentage = total / 5

if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 33:
    grade = "D"

else:
    grade = "F"

if percentage >= 33:
    result = "PASS"

else:
    result = "FAIL"

print("\n")
print("=" * 45)
print("REPORT CARD")
print("=" * 45)

print("Student Name :", name)
print("Roll Number  :", roll)

print("------------------------------")

print("Total Marks  :", total, "/500")

print("Percentage   :", round(percentage,2), "%")

print("Grade        :", grade)

print("Result       :", result)

print("=" * 45)
```

---

# ▶ Sample Output

=============================================

STUDENT RESULT MANAGEMENT SYSTEM

=============================================

Enter Student Name : Amir

Enter Roll Number : 101

English : 89

Math : 95

Science : 91

Computer : 98

Social : 87

=============================================

REPORT CARD

=============================================

Student Name : Amir

Roll Number : 101

Total : 460 /500

Percentage : 92.00 %

Grade : A+

Result : PASS

=============================================

---

# 🚀 Future Improvements

You can improve this project by adding

✔ Subject-wise Grades

✔ Attendance

✔ Student ID

✔ Teacher Name

✔ School Name

✔ Rank Calculation

✔ Database

✔ File Handling

✔ CSV Export

✔ GUI using Tkinter

✔ Login System

---

# 🎯 Learning Outcome

After completing this project, you will understand

Variables

Input

Output

Arithmetic Operators

Comparison Operators

Decision Making

Program Structure

Formatting Output

---

# 📷 GitHub Screenshot

Take a screenshot after running the program.

Save it as

output.png

Upload it to GitHub.

---

# README.md

# 🎓 Student Result Management System

This project is built using Python.

## Features

- Student Details
- Marks Input
- Total Calculation
- Percentage
- Grade
- Pass/Fail
- Report Card

## Technologies Used

- Python 3

## Author

Amir Khan

365 Days of Growth

Day 02

---

# 📌 GitHub Commit

git add .

git commit -m "Day 2 Mini Project - Student Result Management System"

git push origin main

---

# ⭐ Mentor Challenge

Upgrade this project by adding

1.

Subject-wise Pass/Fail

2.

Overall Grade

3.

Topper Logic

4.

Percentage Bar

5.

Multiple Student Support

6.

Save Data in File

7.

Print Beautiful Report Card

If you complete all these improvements, your project will look much stronger in your GitHub portfolio.

---

# 🏆 Day 2 Achievement

✅ Learned Operators

✅ Learned Conditions

✅ Solved 15 Programs

✅ Built First Mini Project

✅ Improved Logic Building

🚀 Congratulations! Day 2 Completed Successfully.