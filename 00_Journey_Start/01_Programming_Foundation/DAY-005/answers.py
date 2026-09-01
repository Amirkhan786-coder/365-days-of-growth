# ==========================================
# DAY 005 — PRACTICE ANSWERS
# PYTHON OPERATORS
# ==========================================


# ==========================================
# Q11 - Addition
# ==========================================

print("Q11:", 10 + 20)


# ==========================================
# Q12 - Subtraction
# ==========================================

print("Q12:", 50 - 25)


# ==========================================
# Q13 - Multiplication
# ==========================================

print("Q13:", 12 * 8)


# ==========================================
# Q14 - Division
# ==========================================

print("Q14:", 100 / 4)


# ==========================================
# Q15 - Modulus
# ==========================================

print("Q15:", 17 % 5)


# ==========================================
# Q16 - Floor Division
# ==========================================

print("Q16:", 20 // 3)


# ==========================================
# Q17 - Power
# ==========================================

print("Q17:", 2 ** 5)


# ==========================================
# Q18 - Addition of User Input
# ==========================================

print("\nQ18 - Addition")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)


# ==========================================
# Q19 - Difference
# ==========================================

print("\nQ19 - Difference")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Difference:", a - b)


# ==========================================
# Q20 - Product
# ==========================================

print("\nQ20 - Product")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Product:", a * b)


# ==========================================
# Q21 - Operator Precedence
# ==========================================

print("\nQ21:", 10 + 5 * 2)


# ==========================================
# Q22 - Parentheses
# ==========================================

print("Q22:", (10 + 5) * 2)


# ==========================================
# Q23 - Division
# ==========================================

print("Q23:", 10 / 2)


# ==========================================
# Q24 - Floor Division
# ==========================================

print("Q24:", 10 // 3)


# ==========================================
# Q25 - Modulus
# ==========================================

print("Q25:", 10 % 3)


# ==========================================
# Q26 - Exponentiation
# ==========================================

print("Q26:", 2 ** 4)


# ==========================================
# Q27 - +=
# ==========================================

x = 10
x += 5

print("Q27:", x)


# ==========================================
# Q28 - -=
# ==========================================

x = 20
x -= 8

print("Q28:", x)


# ==========================================
# Q29 - *=
# ==========================================

x = 5
x *= 4

print("Q29:", x)


# ==========================================
# Q30 - //=
# ==========================================

x = 20
x //= 3

print("Q30:", x)


# ==========================================
# Q31 - Greater Than
# ==========================================

print("\nQ31:", 10 > 5)


# ==========================================
# Q32 - Less Than
# ==========================================

print("Q32:", 10 < 5)


# ==========================================
# Q33 - Equal
# ==========================================

print("Q33:", 10 == 10)


# ==========================================
# Q34 - Not Equal
# ==========================================

print("Q34:", 10 != 5)


# ==========================================
# Q35 - Greater Than or Equal
# ==========================================

print("Q35:", 10 >= 10)


# ==========================================
# Q36 - Less Than or Equal
# ==========================================

print("Q36:", 5 <= 3)


# ==========================================
# Q37 - Check Equal
# ==========================================

print("\nQ37 - Equal Numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Are they equal?", a == b)


# ==========================================
# Q38 - Greater Number
# ==========================================

print("\nQ38 - Greater Number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("First number is greater:", a > b)
print("Second number is greater:", b > a)


# ==========================================
# Q39 - Age Check
# ==========================================

print("\nQ39 - Age Check")

age = int(input("Enter your age: "))

print("Age is 18 or above:", age >= 18)


# ==========================================
# Q40 - Passing Marks
# ==========================================

print("\nQ40 - Marks Check")

marks = float(input("Enter your marks: "))

print("Passed:", marks >= 40)


# ==========================================
# Q41 - +=
# ==========================================

x = 10
x += 5

print("\nQ41:", x)


# ==========================================
# Q42 - -=
# ==========================================

x = 50
x -= 20

print("Q42:", x)


# ==========================================
# Q43 - *=
# ==========================================

x = 10
x *= 5

print("Q43:", x)


# ==========================================
# Q44 - /=
# ==========================================

x = 100
x /= 4

print("Q44:", x)


# ==========================================
# Q45 - %=
# ==========================================

x = 17
x %= 5

print("Q45:", x)


# ==========================================
# Q46 - **=
# ==========================================

x = 2
x **= 5

print("Q46:", x)


# ==========================================
# Q47 - AND
# ==========================================

print("\nQ47:", True and True)


# ==========================================
# Q48 - AND
# ==========================================

print("Q48:", True and False)


# ==========================================
# Q49 - OR
# ==========================================

print("Q49:", True or False)


# ==========================================
# Q50 - OR
# ==========================================

print("Q50:", False or False)


# ==========================================
# Q51 - NOT
# ==========================================

print("Q51:", not True)


# ==========================================
# Q52 - Age Range
# ==========================================

print("\nQ52 - Age Range")

age = int(input("Enter age: "))

result = age >= 18 and age <= 60

print("Age is between 18 and 60:", result)


# ==========================================
# Q53 - Marks Range
# ==========================================

print("\nQ53 - Marks Range")

marks = float(input("Enter marks: "))

result = marks >= 40 and marks <= 100

print("Valid passing marks:", result)


# ==========================================
# Q54 - Number 10 or 20
# ==========================================

print("\nQ54 - Number Check")

number = int(input("Enter number: "))

result = number == 10 or number == 20

print("Number is 10 or 20:", result)


# ==========================================
# Q55 - Membership in String
# ==========================================

print("\nQ55 - Membership")

text = "Python is easy"

print("Python" in text)


# ==========================================
# Q56 - Java in String
# ==========================================

print("\nQ56")

print("Java" in "Python is easy")


# ==========================================
# Q57 - Character in Name
# ==========================================

print("\nQ57 - Character Check")

name = input("Enter your name: ")

print("'A' in name:", "A" in name)


# ==========================================
# Q58 - Python in List
# ==========================================

print("\nQ58 - Programming Languages")

languages = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript"
]

print("Python" in languages)


# ==========================================
# Q59 - JavaScript Not in List
# ==========================================

print("\nQ59")

print("JavaScript" not in languages)


# ==========================================
# Q60 - Identity
# ==========================================

print("\nQ60 - Identity Operator")

x = None

print(x is None)


# ==========================================
# Q61 - == vs is
# ==========================================

print("\nQ61 - == vs is")

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)
print("a is b:", a is b)


# ==========================================
# Q62 - is vs is not
# ==========================================

print("\nQ62")

x = None

print("x is None:", x is None)
print("x is not None:", x is not None)


# ==========================================
# Q63 - Bitwise AND
# ==========================================

print("\nQ63:", 5 & 3)


# ==========================================
# Q64 - Bitwise OR
# ==========================================

print("Q64:", 5 | 3)


# ==========================================
# Q65 - Bitwise XOR
# ==========================================

print("Q65:", 5 ^ 3)


# ==========================================
# Q66 - Bitwise NOT
# ==========================================

print("Q66:", ~5)


# ==========================================
# Q67 - Left Shift
# ==========================================

print("Q67:", 5 << 1)


# ==========================================
# Q68 - Right Shift
# ==========================================

print("Q68:", 5 >> 1)


# ==========================================
# Q69 - Binary of 5
# ==========================================

print("\nQ69:", bin(5))


# ==========================================
# Q70 - Binary of 10
# ==========================================

print("Q70:", bin(10))


# ==========================================
# Q71 - Precedence
# ==========================================

print("\nQ71:", 10 + 5 * 2)


# ==========================================
# Q72 - Parentheses
# ==========================================

print("Q72:", (10 + 5) * 2)


# ==========================================
# Q73
# ==========================================

print("Q73:", 20 - 5 * 2)


# ==========================================
# Q74
# ==========================================

print("Q74:", (20 - 5) * 2)


# ==========================================
# Q75
# ==========================================

print("Q75:", 10 + 20 / 5)


# ==========================================
# Q76
# ==========================================

print("Q76:", (10 + 20) / 5)


# ==========================================
# Q77
# ==========================================

print("Q77:", 2 + 3 * 4 ** 2)


# ==========================================
# Q78
# ==========================================

print("\nQ78")

result = (10 + 5) * 3.3333333333333335

print("Example with parentheses:", result)


# ==========================================
# Q79 - CALCULATOR
# ==========================================

print("\n========== Q79 - CALCULATOR ==========")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Remainder:", a % b)
else:
    print("Division: Cannot divide by zero.")
    print("Remainder: Cannot divide by zero.")


# ==========================================
# Q80 - EVEN OR ODD
# ==========================================

print("\n========== Q80 - EVEN OR ODD ==========")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ==========================================
# Q81 - DISCOUNT
# ==========================================

print("\n========== Q81 - DISCOUNT ==========")

price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount percentage: "))

discount = price * discount_percentage / 100
final_price = price - discount

print("Discount:", discount)
print("Final Price:", final_price)


# ==========================================
# Q82 - STUDENT RESULT
# ==========================================

print("\n========== Q82 - STUDENT RESULT ==========")

m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = total / 500 * 100

print("Total:", total)
print("Average:", average)
print("Percentage:", percentage, "%")


# ==========================================
# Q83 - SALARY CALCULATOR
# ==========================================

print("\n========== Q83 - SALARY ==========")

basic_salary = float(input("Basic Salary: "))
bonus = float(input("Bonus: "))
allowance = float(input("Allowance: "))

total_salary = basic_salary + bonus + allowance

print("Total Salary:", total_salary)


# ==========================================
# Q84 - TIME CONVERTER
# ==========================================

print("\n========== Q84 - TIME ==========")

minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours:", hours)
print("Remaining Minutes:", remaining_minutes)


# ==========================================
# Q85 - DISTANCE CONVERTER
# ==========================================

print("\n========== Q85 - DISTANCE ==========")

kilometers = float(input("Enter kilometers: "))

meters = kilometers * 1000
centimeters = meters * 100

print("Meters:", meters)
print("Centimeters:", centimeters)


# ==========================================
# Q86 - TEMPERATURE
# ==========================================

print("\n========== Q86 - TEMPERATURE ==========")

celsius = float(input("Enter Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)


# ==========================================
# Q87 - AVERAGE OF THREE NUMBERS
# ==========================================

print("\n========== Q87 ==========")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average:", average)


# ==========================================
# Q88 - SQUARE AND CUBE
# ==========================================

print("\n========== Q88 ==========")

number = float(input("Enter number: "))

print("Square:", number ** 2)
print("Cube:", number ** 3)


# ==========================================
# Q89 - FUTURE AGE
# ==========================================

print("\n========== Q89 ==========")

age = int(input("Enter current age: "))

print("Current Age:", age)
print("After 5 Years:", age + 5)
print("After 10 Years:", age + 10)
print("After 20 Years:", age + 20)


# ==========================================
# Q90 - PERCENTAGE
# ==========================================

print("\n========== Q90 ==========")

total_marks = float(input("Enter total marks: "))

percentage = total_marks / 500 * 100

print("Percentage:", percentage, "%")


# ==========================================
# Q91 - SHOPPING BILL
# ==========================================

print("\n========== Q91 ==========")

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

discount = subtotal * 10 / 100

final_amount = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Amount:", final_amount)


# ==========================================
# Q92 - AVERAGE CHECK
# ==========================================

print("\n========== Q92 ==========")

m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))

average = (m1 + m2 + m3) / 3

print("Average:", average)
print("Average >= 40:", average >= 40)


# ==========================================
# Q93 - NUMBER RANGE
# ==========================================

print("\n========== Q93 ==========")

number = float(input("Enter number: "))

print("Greater than 0:", number > 0)
print("Less than 100:", number < 100)


# ==========================================
# Q94 - AGE RANGE
# ==========================================

print("\n========== Q94 ==========")

age = int(input("Enter age: "))

result = age >= 18 and age < 60

print("Age is between 18 and 59:", result)


# ==========================================
# Q95 - THREE PRODUCT BILL
# ==========================================

print("\n========== Q95 ==========")

price1 = float(input("Product 1 price: "))
price2 = float(input("Product 2 price: "))
price3 = float(input("Product 3 price: "))

quantity = int(input("Quantity for each product: "))

total = (price1 + price2 + price3) * quantity

print("Total Bill:", total)


# ==========================================
# Q96 - PRECEDENCE EXPLANATION
# ==========================================

print("\n========== Q96 ==========")

print("10 + 5 * 2 =", 10 + 5 * 2)
print("(10 + 5) * 2 =", (10 + 5) * 2)

print("Multiplication happens before addition.")


# ==========================================
# Q97 - DIVISION
# ==========================================

print("\n========== Q97 ==========")

result = 10 / 2

print("Result:", result)
print("Type:", type(result))


# ==========================================
# Q98 - MODULUS
# ==========================================

print("\n========== Q98 ==========")

number = int(input("Enter number: "))

if number % 2 == 0:
    print("Remainder is 0 → Even")
else:
    print("Remainder is not 0 → Odd")


# ==========================================
# Q99 - == VS =
# ==========================================

print("\n========== Q99 ==========")

x = 10

print("x == 10:", x == 10)

print("""
=  → Assignment
== → Comparison
""")


# ==========================================
# Q100 - OPERATOR SUMMARY
# ==========================================

print("\n========== Q100 ==========")

print("Division        :", 10 / 3)
print("Floor Division :", 10 // 3)
print("Modulus        :", 10 % 3)
print("Power           :", 2 ** 3)



print("""
Operators Practiced:
✓ Arithmetic
✓ Assignment
✓ Comparison
✓ Logical
✓ Membership
✓ Identity
✓ Bitwise
✓ Operator Precedence
 
""")