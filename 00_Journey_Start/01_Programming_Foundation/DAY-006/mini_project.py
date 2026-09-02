# ============================================================
#  DAY 006 / 365
#  PYTHON CONDITIONAL STATEMENTS
#  MINI PROJECT — STUDENT RESULT MANAGEMENT SYSTEM
# ============================================================


print("=" * 50)
print("          STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 50)


# ------------------------------------------------------------
# 1. Student Information
# ------------------------------------------------------------

name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")


# ------------------------------------------------------------
# 2. Subject Marks
# ------------------------------------------------------------

english = float(input("Enter English Marks: "))
maths = float(input("Enter Maths Marks: "))
physics = float(input("Enter Physics Marks: "))
chemistry = float(input("Enter Chemistry Marks: "))
computer = float(input("Enter Computer Marks: "))


# ------------------------------------------------------------
# 3. Calculate Total
# ------------------------------------------------------------

total = english + maths + physics + chemistry + computer


# ------------------------------------------------------------
# 4. Calculate Percentage
# ------------------------------------------------------------

percentage = total / 5


# ------------------------------------------------------------
# 5. Check Pass / Fail
# ------------------------------------------------------------

if (
    english >= 40
    and maths >= 40
    and physics >= 40
    and chemistry >= 40
    and computer >= 40
):
    result = "PASS"
else:
    result = "FAIL"


# ------------------------------------------------------------
# 6. Calculate Grade
# ------------------------------------------------------------

if result == "FAIL":
    grade = "F"

elif percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

else:
    grade = "D"


# ------------------------------------------------------------
# 7. Display Result
# ------------------------------------------------------------

print()
print("=" * 50)
print("              STUDENT RESULT")
print("=" * 50)

print("Name        :", name)
print("Roll Number :", roll_number)

print("-" * 50)

print("English     :", english)
print("Maths       :", maths)
print("Physics     :", physics)
print("Chemistry   :", chemistry)
print("Computer    :", computer)

print("-" * 50)

print("Total       :", total)
print("Percentage  :", percentage, "%")
print("Grade       :", grade)
print("Result      :", result)

print("=" * 50)


# ------------------------------------------------------------
# 8. Performance Message
# ------------------------------------------------------------

if result == "FAIL":
    print("Keep practicing and improve your weak subjects.")

elif grade == "A+":
    print("Excellent performance! 🔥")

elif grade == "A":
    print("Great performance! 👏")

elif grade == "B":
    print("Good performance! Keep improving.")

elif grade == "C":
    print("You can do better. Keep practicing.")

else:
    print("Keep working hard and improve your fundamentals.")


print("=" * 50)
print("        🚀 DAY 006 MINI PROJECT COMPLETED")
print("=" * 50)


# ============================================================
# 🧠 CONCEPTS USED
#
# ✓ Variables
# ✓ input()
# ✓ int() / float()
# ✓ Arithmetic operators
# ✓ Comparison operators
# ✓ Logical operator: and
# ✓ if
# ✓ elif
# ✓ else
# ✓ Nested decision-making
# ✓ String formatting basics
#
# ============================================================