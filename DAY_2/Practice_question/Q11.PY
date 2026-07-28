# Program: BMI Calculator

weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI = {bmi:.2f}")