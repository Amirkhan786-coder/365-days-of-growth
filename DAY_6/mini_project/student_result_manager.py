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

# Subjects stored in Tuple
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
            mark = float(input(f"Enter marks in {subject}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

# Convert List into Tuple
marks = tuple(marks)

# Calculations
total = sum(marks)
average = total / len(marks)
percentage = average
highest = max(marks)
lowest = min(marks)

# Grade and Result
grade = calculate_grade(percentage)
result = calculate_result(marks)

# Student Record stored in Tuple
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
print("-" * 45)

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