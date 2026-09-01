# Day 004 - Interactive Python Programs


# ==========================================
# Program 1: Addition of Two Numbers
# ==========================================

print("----- ADDITION -----")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

print("Addition:", result)


# ==========================================
# Program 2: Subtraction of Two Numbers
# ==========================================

print("\n----- SUBTRACTION -----")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 - num2

print("Subtraction:", result)


# ==========================================
# Program 3: Multiplication
# ==========================================

print("\n----- MULTIPLICATION -----")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 * num2

print("Multiplication:", result)


# ==========================================
# Program 4: Division
# ==========================================

print("\n----- DIVISION -----")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 / num2

print("Division:", result)


# ==========================================
# Program 5: Rectangle Area
# ==========================================

print("\n----- RECTANGLE AREA -----")

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of Rectangle:", area)


# ==========================================
# Program 6: Square Area
# ==========================================

print("\n----- SQUARE AREA -----")

side = float(input("Enter side: "))

area = side * side

print("Area of Square:", area)


# ==========================================
# Program 7: Circle Area
# ==========================================

print("\n----- CIRCLE AREA -----")

radius = float(input("Enter radius: "))

area = 3.14159 * radius * radius

print("Area of Circle:", area)


# ==========================================
# Program 8: Simple Age Calculator
# ==========================================

print("\n----- AGE CALCULATOR -----")

birth_year = int(input("Enter your birth year: "))

current_year = 2026

age = current_year - birth_year

print("Your approximate age is:", age)


# ==========================================
# Program 9: Age After 5 Years
# ==========================================

print("\n----- FUTURE AGE -----")

name = input("Enter your name: ")
age = int(input("Enter your current age: "))

future_age = age + 5

print(name, "will be", future_age, "years old after 5 years.")


# ==========================================
# Program 10: Total Marks
# ==========================================

print("\n----- TOTAL MARKS -----")

mark1 = float(input("Enter Subject 1 marks: "))
mark2 = float(input("Enter Subject 2 marks: "))
mark3 = float(input("Enter Subject 3 marks: "))

total = mark1 + mark2 + mark3

print("Total Marks:", total)


# ==========================================
# Program 11: Average Marks
# ==========================================

print("\n----- AVERAGE MARKS -----")

mark1 = float(input("Enter Subject 1 marks: "))
mark2 = float(input("Enter Subject 2 marks: "))
mark3 = float(input("Enter Subject 3 marks: "))

average = (mark1 + mark2 + mark3) / 3

print("Average Marks:", average)


# ==========================================
# Program 12: Product Price Calculator
# ==========================================

print("\n----- PRODUCT PRICE -----")

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_price = price * quantity

print("Total Price:", total_price)


# ==========================================
# Program 13: Celsius to Fahrenheit
# ==========================================

print("\n----- TEMPERATURE CONVERTER -----")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# ==========================================
# Program 14: Kilometers to Meters
# ==========================================

print("\n----- DISTANCE CONVERTER -----")

kilometers = float(input("Enter distance in kilometers: "))

meters = kilometers * 1000

print("Distance in meters:", meters)


# ==========================================
# Program 15: Hours to Minutes
# ==========================================

print("\n----- TIME CONVERTER -----")

hours = float(input("Enter hours: "))

minutes = hours * 60

print("Time in minutes:", minutes)


# ==========================================
# Program 16: Minutes to Seconds
# ==========================================

print("\n----- SECONDS CONVERTER -----")

minutes = float(input("Enter minutes: "))

seconds = minutes * 60

print("Time in seconds:", seconds)


# ==========================================
# Program 17: Simple Calculator
# ==========================================

print("\n----- SIMPLE CALCULATOR -----")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)


# ==========================================
# Program 18: Student Profile
# ==========================================

print("\n----- STUDENT PROFILE -----")

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_branch = input("Enter branch: ")
student_college = input("Enter college: ")

print("\n========== PROFILE ==========")

print("Name:", student_name)
print("Age:", student_age)
print("Branch:", student_branch)
print("College:", student_college)

print("=============================")