# ============================================
# Project : Student Result Management System
# Day     : 02
# Author  : MD Amir Khan
# ============================================

print("=" * 60)
print("        STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 60)

# Student Details
Name = input("Enter Student Name : ")
Roll = input("Enter Roll Number  : ")

print("\nEnter Marks (Out of 100)\n")

# Input Marks
English = float(input("English          : "))
Maths = float(input("Mathematics      : "))
Science = float(input("Science          : "))
Computer = float(input("Computer         : "))
Social = float(input("Social Science   : "))

# Total
total = English + Maths + Science + Computer + Social

# Percentage
percentage = total / 5

# Grade Calculation
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

# Pass/Fail
if (English >= 33 and Maths >= 33 and Science >= 33 and
        Computer >= 33 and Social >= 33):
    result = "PASS"
else:
    result = "FAIL"

# Highest & Lowest Marks
highest = max(English, Maths, Science, Computer, Social)
lowest = min(English, Maths, Science, Computer, Social)

# Average Marks
average = total / 5

# Performance Message
if percentage >= 90:
    remark = "Outstanding Performance!"
elif percentage >= 80:
    remark = "Excellent Work!"
elif percentage >= 70:
    remark = "Very Good!"
elif percentage >= 60:
    remark = "Good Job!"
elif percentage >= 33:
    remark = "Keep Practicing!"
else:
    remark = "Needs Improvement."

# Subject Wise Result
print("\n")
print("=" * 60)
print("                 REPORT CARD")
print("=" * 60)

print(f"Student Name      : {Name}")
print(f"Roll Number       : {Roll}")

print("-" * 60)

print(f"English           : {English}")
print(f"Mathematics       : {Maths}")
print(f"Science           : {Science}")
print(f"Computer          : {Computer}")
print(f"Social Science    : {Social}")

print("-" * 60)

print(f"Total Marks       : {total}/500")
print(f"Average Marks     : {average:.2f}")
print(f"Percentage        : {percentage:.2f}%")
print(f"Grade             : {grade}")
print(f"Result            : {result}")

print("-" * 60)

print(f"Highest Marks     : {highest}")
print(f"Lowest Marks      : {lowest}")

print("-" * 60)

print("Teacher's Remark  :", remark)

print("=" * 60)
print("        THANK YOU! KEEP LEARNING 🚀")
print("=" * 60)