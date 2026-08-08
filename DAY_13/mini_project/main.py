# ============================================
# Day 13 - Mini Project
# Student Information System
# File: main.py
# ============================================

from student import get_student_details
from marks import get_marks, calculate_result


print("=" * 45)
print("       STUDENT INFORMATION SYSTEM")
print("=" * 45)

# Student Details
name, age, course = get_student_details()

print("\nEnter Student Marks")
print("-" * 30)

# Marks
python, java, maths = get_marks()

# Calculate Result
total, percentage, result = calculate_result(
    python,
    java,
    maths
)

# Display Result
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