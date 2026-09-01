# Day 004 - Python Type Conversion


# ==========================================
# 1. String to Integer
# ==========================================

number_string = "100"

number_integer = int(number_string)

print("Original Value:", number_string)
print("Converted Value:", number_integer)
print("Data Type:", type(number_integer))


# ==========================================
# 2. String to Float
# ==========================================

decimal_string = "25.5"

decimal_number = float(decimal_string)

print("\nOriginal Value:", decimal_string)
print("Converted Value:", decimal_number)
print("Data Type:", type(decimal_number))


# ==========================================
# 3. Integer to String
# ==========================================

number = 500

number_text = str(number)

print("\nOriginal Value:", number)
print("Converted Value:", number_text)
print("Data Type:", type(number_text))


# ==========================================
# 4. Float to Integer
# ==========================================

price = 99.99

integer_price = int(price)

print("\nOriginal Float:", price)
print("Converted Integer:", integer_price)
print("Data Type:", type(integer_price))


# ==========================================
# 5. Integer to Float
# ==========================================

marks = 95

float_marks = float(marks)

print("\nOriginal Integer:", marks)
print("Converted Float:", float_marks)
print("Data Type:", type(float_marks))


# ==========================================
# 6. Taking Integer Input
# ==========================================

age = int(input("\nEnter your age: "))

print("Your age is:", age)
print("Data Type:", type(age))


# ==========================================
# 7. Taking Float Input
# ==========================================

height = float(input("Enter your height in feet: "))

print("Your height is:", height)
print("Data Type:", type(height))


# ==========================================
# 8. Two Number Addition
# ==========================================

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

print("Addition:", result)


# ==========================================
# 9. Price Calculation
# ==========================================

product_price = float(input("\nEnter product price: "))
quantity = int(input("Enter quantity: "))

total_price = product_price * quantity

print("Total Price:", total_price)


# ==========================================
# 10. Checking Different Data Types
# ==========================================

print("\n========== DATA TYPES ==========")

a = "Amir"
b = 20
c = 5.8

print(a, "->", type(a))
print(b, "->", type(b))
print(c, "->", type(c))

print("================================")