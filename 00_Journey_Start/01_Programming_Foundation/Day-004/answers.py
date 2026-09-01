# Day 004 - Practice Answers
# Python Input & Type Conversion


# ==========================================
# Q3 - Take User Name
# ==========================================

name = input("Enter your name: ")

print("Your name is:", name)


# ==========================================
# Q4 - Take User Age
# ==========================================

age = int(input("Enter your age: "))

print("Your age is:", age)


# ==========================================
# Q11 - Addition
# ==========================================

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)


# ==========================================
# Q12 - Subtraction
# ==========================================

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Subtraction:", num1 - num2)


# ==========================================
# Q13 - Multiplication
# ==========================================

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Multiplication:", num1 * num2)


# ==========================================
# Q14 - Division
# ==========================================

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("Division:", num1 / num2)


# ==========================================
# Q15 - Rectangle Area
# ==========================================

length = float(input("\nEnter rectangle length: "))
width = float(input("Enter rectangle width: "))

area = length * width

print("Rectangle Area:", area)


# ==========================================
# Q16 - Square Area
# ==========================================

side = float(input("\nEnter square side: "))

area = side * side

print("Square Area:", area)


# ==========================================
# Q17 - Circle Area
# ==========================================

radius = float(input("\nEnter circle radius: "))

area = 3.14159 * radius * radius

print("Circle Area:", area)


# ==========================================
# Q18 - Age Calculator
# ==========================================

birth_year = int(input("\nEnter your birth year: "))

current_year = 2026

age = current_year - birth_year

print("Your approximate age:", age)


# ==========================================
# Q19 - Product Price
# ==========================================

price = float(input("\nEnter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total Price:", total)


# ==========================================
# Q20 - Celsius to Fahrenheit
# ==========================================

celsius = float(input("\nEnter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# ==========================================
# Q26 - String to Integer
# ==========================================

value = "100"

converted_value = int(value)

print("\nConverted Integer:", converted_value)
print("Data Type:", type(converted_value))


# ==========================================
# Q27 - String to Float
# ==========================================

value = "25.5"

converted_value = float(value)

print("\nConverted Float:", converted_value)
print("Data Type:", type(converted_value))


# ==========================================
# Q28 - Integer to String
# ==========================================

value = 500

converted_value = str(value)

print("\nConverted String:", converted_value)
print("Data Type:", type(converted_value))


# ==========================================
# Q29 - Integer to Float
# ==========================================

value = 50

converted_value = float(value)

print("\nConverted Float:", converted_value)
print("Data Type:", type(converted_value))


# ==========================================
# Q30 - Float to Integer
# ==========================================

value = 25.8

converted_value = int(value)

print("\nConverted Integer:", converted_value)
print("Data Type:", type(converted_value))


# ==========================================
# Q31 - Student Profile
# ==========================================

print("\n========== STUDENT PROFILE ==========")

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
college = input("Enter college name: ")
branch = input("Enter branch: ")

print("\nName:", student_name)
print("Age:", student_age)
print("College:", college)
print("Branch:", branch)


# ==========================================
# Q32 - Five Subject Result
# ==========================================

print("\n========== STUDENT RESULT ==========")

m1 = float(input("Enter Subject 1 marks: "))
m2 = float(input("Enter Subject 2 marks: "))
m3 = float(input("Enter Subject 3 marks: "))
m4 = float(input("Enter Subject 4 marks: "))
m5 = float(input("Enter Subject 5 marks: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("Total Marks:", total)
print("Average:", average)


# ==========================================
# Q33 - Calculator
# ==========================================

print("\n========== CALCULATOR ==========")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# ==========================================
# Q34 - Bill Calculator
# ==========================================

print("\n========== BILL CALCULATOR ==========")

product = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\nProduct:", product)
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)


# ==========================================
# Q35 - Kilometers to Meters
# ==========================================

kilometers = float(input("\nEnter distance in kilometers: "))

meters = kilometers * 1000

print("Distance in meters:", meters)


# ==========================================
# Q36 - Hours to Minutes
# ==========================================

hours = float(input("\nEnter hours: "))

minutes = hours * 60

print("Minutes:", minutes)


# ==========================================
# Q37 - Minutes to Seconds
# ==========================================

minutes = float(input("\nEnter minutes: "))

seconds = minutes * 60

print("Seconds:", seconds)


# ==========================================
# Q38 - Age After 5 Years
# ==========================================

age = int(input("\nEnter your current age: "))

future_age = age + 5

print("Your age after 5 years:", future_age)


# ==========================================
# Q39 - Future Age Calculator
# ==========================================

birth_year = int(input("\nEnter your birth year: "))

current_year = 2026

age = current_year - birth_year
age_after_5 = age + 5
age_after_10 = age + 10

print("Current Age:", age)
print("Age After 5 Years:", age_after_5)
print("Age After 10 Years:", age_after_10)


# ==========================================
# Q40 - Student Percentage
# ==========================================

print("\n========== PERCENTAGE CALCULATOR ==========")

s1 = float(input("Enter Subject 1 marks: "))
s2 = float(input("Enter Subject 2 marks: "))
s3 = float(input("Enter Subject 3 marks: "))
s4 = float(input("Enter Subject 4 marks: "))
s5 = float(input("Enter Subject 5 marks: "))

total = s1 + s2 + s3 + s4 + s5
average = total / 5
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage, "%")


# ==========================================
# Q41 - Product Bill
# ==========================================

print("\n========== PRODUCT BILL ==========")

product_name = input("Enter product name: ")
product_price = float(input("Enter price: "))
product_quantity = int(input("Enter quantity: "))

final_amount = product_price * product_quantity

print("\nProduct:", product_name)
print("Price:", product_price)
print("Quantity:", product_quantity)
print("Final Amount:", final_amount)


# ==========================================
# Q42 - Salary Calculator
# ==========================================

print("\n========== SALARY CALCULATOR ==========")

basic_salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))

total_salary = basic_salary + bonus

print("Basic Salary:", basic_salary)
print("Bonus:", bonus)
print("Total Salary:", total_salary)


# ==========================================
# Q43 - BMI Calculator
# ==========================================

print("\n========== BMI CALCULATOR ==========")

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("Your BMI:", bmi)


# ==========================================
# Q45 - Minutes to Hours
# ==========================================

print("\n========== TIME CONVERTER ==========")

total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print("Hours:", hours)
print("Remaining Minutes:", remaining_minutes)


# ==========================================
# Q46 - Understanding String Concatenation
# ==========================================

a = input("\nEnter first value: ")
b = input("Enter second value: ")

print("Without conversion:", a + b)

a = int(a)
b = int(b)

print("After conversion:", a + b)


# ==========================================
# Q47 - Integer Input
# ==========================================

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)


# ==========================================
# Q48 - Invalid Integer Input
# ==========================================

print("\nIf we run:")
print('age = int(input())')
print('and enter "abc", Python raises ValueError.')


# ==========================================
# Q49 - int() vs float()
# ==========================================

integer_value = int("10")
float_value = float("10")

print("\nInteger Value:", integer_value)
print("Integer Type:", type(integer_value))

print("Float Value:", float_value)
print("Float Type:", type(float_value))


# ==========================================
# Q50 - Why str() is Usually Not Needed
# ==========================================

name = input("\nEnter your name: ")

print("Name:", name)
print("Type:", type(name))

# input() already returns a string,
# so str() is normally unnecessary here.


