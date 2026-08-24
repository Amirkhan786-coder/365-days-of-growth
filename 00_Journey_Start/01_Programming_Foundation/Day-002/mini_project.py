# Day 002 Mini Project
# Student Result Calculator

print("=" * 40)
print("STUDENT RESULT CALCULATOR")
print("=" * 40)

name = input("Enter student name: ")

math_marks = float(input("Enter Mathematics marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

total = math_marks + science_marks + english_marks

average = total / 3

print("\n" + "=" * 40)
print("RESULT")
print("=" * 40)

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)