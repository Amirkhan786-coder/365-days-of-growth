# Program: Grade Calculator

percentage = float(input("Enter Percentage: "))

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 33:
    print("Grade: D")
else:
    print("Fail")