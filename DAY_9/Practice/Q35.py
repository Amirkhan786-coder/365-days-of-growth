# Question: Create a function to calculate the grade of a student based on marks.

def calculate_grade(marks):

    if marks >= 90:
        return "Grade A"

    elif marks >= 80:
        return "Grade B"

    elif marks >= 70:
        return "Grade C"

    elif marks >= 60:
        return "Grade D"

    else:
        return "Fail"

print(calculate_grade(87))