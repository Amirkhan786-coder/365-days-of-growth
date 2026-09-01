# ==========================================
# DAY 005 — PYTHON OPERATORS
# ==========================================


# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================

print("\n========== ARITHMETIC OPERATORS ==========")

a = 10
b = 3

print("a =", a)
print("b =", b)

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Modulus        :", a % b)
print("Floor Division :", a // b)
print("Power          :", a ** b)


# ==========================================
# 2. ASSIGNMENT OPERATORS
# ==========================================

print("\n========== ASSIGNMENT OPERATORS ==========")

x = 10

print("Initial x:", x)

x += 5
print("After x += 5:", x)

x -= 3
print("After x -= 3:", x)

x *= 2
print("After x *= 2:", x)

x /= 4
print("After x /= 4:", x)

x //= 2
print("After x //= 2:", x)

x %= 3
print("After x %= 3:", x)

x **= 2
print("After x **= 2:", x)


# ==========================================
# 3. COMPARISON OPERATORS
# ==========================================

print("\n========== COMPARISON OPERATORS ==========")

a = 10
b = 5

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)


# ==========================================
# 4. LOGICAL OPERATORS
# ==========================================

print("\n========== LOGICAL OPERATORS ==========")

age = 20

print("Age:", age)

print("age >= 18 and age <= 60:",
      age >= 18 and age <= 60)

print("age < 18 or age > 60:",
      age < 18 or age > 60)

print("not(age >= 18):",
      not(age >= 18))


# ==========================================
# 5. MEMBERSHIP OPERATORS
# ==========================================

print("\n========== MEMBERSHIP OPERATORS ==========")

name = "Amir Khan"

print("Name:", name)

print("'A' in name:",
      "A" in name)

print("'z' in name:",
      "z" in name)

print("'A' not in name:",
      "A" not in name)

print("'z' not in name:",
      "z" not in name)


# ==========================================
# 6. MEMBERSHIP WITH LIST
# ==========================================

print("\n========== MEMBERSHIP WITH LIST ==========")

languages = ["Python", "Java", "C", "C++"]

print("Languages:", languages)

print("'Python' in languages:",
      "Python" in languages)

print("'JavaScript' in languages:",
      "JavaScript" in languages)


# ==========================================
# 7. IDENTITY OPERATORS
# ==========================================

print("\n========== IDENTITY OPERATORS ==========")

a = None

print("a is None:", a is None)
print("a is not None:", a is not None)


# ==========================================
# 8. == VS is
# ==========================================

print("\n========== == VS is ==========")

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)


# ==========================================
# 9. BITWISE OPERATORS
# ==========================================

print("\n========== BITWISE OPERATORS ==========")

a = 5
b = 3

print("a =", a)
print("b =", b)

print("a & b  :", a & b)
print("a | b  :", a | b)
print("a ^ b  :", a ^ b)
print("~a     :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)


# ==========================================
# 10. EVEN OR ODD
# ==========================================

print("\n========== EVEN OR ODD ==========")

number = int(input("Enter a number: "))

remainder = number % 2

print("Remainder:", remainder)

if remainder == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")


# ==========================================
# 11. LARGER NUMBER
# ==========================================

print("\n========== LARGER NUMBER ==========")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("First number:", num1)
print("Second number:", num2)

print("Is first number greater?",
      num1 > num2)

print("Is second number greater?",
      num2 > num1)

print("Are both equal?",
      num1 == num2)


# ==========================================
# 12. OPERATOR PRECEDENCE
# ==========================================

print("\n========== OPERATOR PRECEDENCE ==========")

result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print("10 + 5 * 2 =", result1)
print("(10 + 5) * 2 =", result2)


# ==========================================
# 13. REAL-WORLD CALCULATOR
# ==========================================

print("\n========== CALCULATOR ==========")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("\nResults:")

print("Addition       :", number1 + number2)
print("Subtraction    :", number1 - number2)
print("Multiplication :", number1 * number2)

if number2 != 0:
    print("Division       :", number1 / number2)
    print("Floor Division :", number1 // number2)
    print("Remainder      :", number1 % number2)
else:
    print("Division       : Cannot divide by zero.")
    print("Floor Division : Cannot divide by zero.")
    print("Remainder      : Cannot divide by zero.")


# ==========================================
# 14. STUDENT MARKS COMPARISON
# ==========================================

print("\n========== STUDENT MARKS ==========")

marks1 = float(input("Enter Subject 1 marks: "))
marks2 = float(input("Enter Subject 2 marks: "))
marks3 = float(input("Enter Subject 3 marks: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\nTotal Marks:", total)
print("Average:", average)

print("Passed minimum average:",
      average >= 40)


# ==========================================
# 15. DISCOUNT CALCULATION
# ==========================================

print("\n========== DISCOUNT CALCULATOR ==========")

price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Original Price:", price)
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)


# ==========================================
# 16. SIMPLE BMI CALCULATION
# ==========================================

print("\n========== BMI CALCULATOR ==========")

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("BMI:", bmi)


# ==========================================
# 17. MULTIPLE OPERATORS
# ==========================================

print("\n========== MULTIPLE OPERATORS ==========")

a = 20
b = 5
c = 2

result = a + b * c

print("Expression: a + b * c")
print("Result:", result)

result = (a + b) * c

print("Expression: (a + b) * c")
print("Result:", result)


# ==========================================
# FINAL MESSAGE
# ==========================================

print("\n" + "=" * 50)
print("       DAY 005 OPERATORS COMPLETED 🚀")
print("=" * 50)

print("""
Topics Practiced:
✓ Arithmetic Operators
✓ Assignment Operators
✓ Comparison Operators
✓ Logical Operators
✓ Membership Operators
✓ Identity Operators
✓ Bitwise Operators
✓ Operator Precedence
✓ Real-World Calculations
""")

