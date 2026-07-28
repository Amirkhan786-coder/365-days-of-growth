# Mini Project: Student Result Management System

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = float(input("English: "))
m2 = float(input("Math: "))
m3 = float(input("Science: "))
m4 = float(input("Computer: "))
m5 = float(input("Social Science: "))

total = m1 + m2 + m3 + m4 + m5
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

status = "Pass" if percentage >= 33 else "Fail"

print("\n===== STUDENT REPORT =====")
print(f"Name       : {name}")
print(f"Roll No.   : {roll}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Result     : {status}")