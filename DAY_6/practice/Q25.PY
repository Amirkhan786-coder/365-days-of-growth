# students grades

marks = (85, 90, 78, 92, 88)

percentage = sum(marks) / len(marks)

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
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("Percentage:", percentage)
print("Grade:", grade)