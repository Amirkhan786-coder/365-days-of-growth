print("=" * 50)
print("     STUDENT MARKS ANALYZER")
print("=" * 50)

student_name = input("Enter Student Name : ")

marks = []

subjects = ["HISTORY", "CHEMISTRY", "PHYSICS", "MATHS", "ENGLISH"]

for subject in subjects:
    mark = int(input(f"Enter Marks in {subject} : "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
percentage = (total / 500) * 100

highest = max(marks)
lowest = min(marks)

passed_subjects = 0
failed_subjects = 0

for mark in marks:
    if mark >= 33:
        passed_subjects += 1
    else:
        failed_subjects += 1

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 33:
    grade = "E"
else:
    grade = "F"

if failed_subjects == 0:
    result = "PASS"
else:
    result = "FAIL"

print("\n" + "=" * 50)
print("         STUDENT RESULT")
print("=" * 50)

print(f"Student Name      : {student_name}")
print(f"Marks             : {marks}")
print(f"Total Marks       : {total}")
print(f"Average Marks     : {average:.2f}")
print(f"Percentage        : {percentage:.2f}%")
print(f"Highest Marks     : {highest}")
print(f"Lowest Marks      : {lowest}")
print(f"Passed Subjects   : {passed_subjects}")
print(f"Failed Subjects   : {failed_subjects}")
print(f"Grade             : {grade}")
print(f"Final Result      : {result}")

print("=" * 50)
print("Day 05 / 365 Days Of Growth")
print("=" * 50)