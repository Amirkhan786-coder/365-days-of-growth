# ============================================================
#  DAY 006 / 365
#  PYTHON CONDITIONAL STATEMENTS
# ============================================================
#
# Topics:
# - if
# - if-else
# - if-elif-else
# - nested if
# - comparison operators
# - logical operators
#
# ============================================================


# ------------------------------------------------------------
# Q1. Positive or Negative
# ------------------------------------------------------------

number = int(input("Q1 - Enter a number: "))

if number >= 0:
    print("Positive")
else:
    print("Negative")


# ------------------------------------------------------------
# Q2. Positive, Negative or Zero
# ------------------------------------------------------------

number = int(input("\nQ2 - Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ------------------------------------------------------------
# Q3. Even or Odd
# ------------------------------------------------------------

number = int(input("\nQ3 - Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ------------------------------------------------------------
# Q4. Pass or Fail
# ------------------------------------------------------------

marks = float(input("\nQ4 - Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# ------------------------------------------------------------
# Q5. Voting Eligibility
# ------------------------------------------------------------

age = int(input("\nQ5 - Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# ------------------------------------------------------------
# Q6. Greater of Two Numbers
# ------------------------------------------------------------

a = int(input("\nQ6 - Enter first number: "))
b = int(input("Q6 - Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")


# ------------------------------------------------------------
# Q7. Smallest of Two Numbers
# ------------------------------------------------------------

a = int(input("\nQ7 - Enter first number: "))
b = int(input("Q7 - Enter second number: "))

if a < b:
    print(a, "is smaller")
elif b < a:
    print(b, "is smaller")
else:
    print("Both numbers are equal")


# ------------------------------------------------------------
# Q8. Divisible by 5
# ------------------------------------------------------------

number = int(input("\nQ8 - Enter a number: "))

if number % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")


# ------------------------------------------------------------
# Q9. Largest of Three Numbers
# ------------------------------------------------------------

a = int(input("\nQ9 - Enter first number: "))
b = int(input("Q9 - Enter second number: "))
c = int(input("Q9 - Enter third number: "))

if a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")


# ------------------------------------------------------------
# Q10. Smallest of Three Numbers
# ------------------------------------------------------------

a = int(input("\nQ10 - Enter first number: "))
b = int(input("Q10 - Enter second number: "))
c = int(input("Q10 - Enter third number: "))

if a <= b and a <= c:
    print(a, "is smallest")
elif b <= a and b <= c:
    print(b, "is smallest")
else:
    print(c, "is smallest")


# ------------------------------------------------------------
# Q11. Grade Calculator
# ------------------------------------------------------------

marks = float(input("\nQ11 - Enter marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")


# ------------------------------------------------------------
# Q12. Age Category
# ------------------------------------------------------------

age = int(input("\nQ12 - Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")


# ------------------------------------------------------------
# Q13. Vowel or Consonant
# ------------------------------------------------------------

character = input("\nQ13 - Enter a character: ").lower()

if character in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# ------------------------------------------------------------
# Q14. Leap Year
# ------------------------------------------------------------

year = int(input("\nQ14 - Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# ------------------------------------------------------------
# Q15. Number Range
# ------------------------------------------------------------

number = int(input("\nQ15 - Enter a number: "))

if number <= 10:
    print("Small")
elif number <= 50:
    print("Medium")
elif number <= 100:
    print("Large")
else:
    print("Very Large")


# ------------------------------------------------------------
# Q16. Temperature Category
# ------------------------------------------------------------

temperature = float(input("\nQ16 - Enter temperature: "))

if temperature < 10:
    print("Very Cold")
elif temperature < 20:
    print("Cold")
elif temperature < 30:
    print("Normal")
elif temperature < 40:
    print("Hot")
else:
    print("Very Hot")


# ------------------------------------------------------------
# Q17. Simple Calculator
# ------------------------------------------------------------

a = float(input("\nQ17 - Enter first number: "))
b = float(input("Q17 - Enter second number: "))
operator = input("Q17 - Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)

elif operator == "-":
    print("Result:", a - b)

elif operator == "*":
    print("Result:", a * b)

elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")


# ------------------------------------------------------------
# Q18. Discount Calculator
# ------------------------------------------------------------

price = float(input("\nQ18 - Enter shopping amount: "))

if price >= 5000:
    discount = price * 0.20
elif price >= 3000:
    discount = price * 0.10
else:
    discount = 0

final_price = price - discount

print("Discount:", discount)
print("Final Price:", final_price)


# ------------------------------------------------------------
# Q19. Login System
# ------------------------------------------------------------

username = input("\nQ19 - Enter username: ")
password = input("Q19 - Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")


# ------------------------------------------------------------
# Q20. Positive Even / Odd Classification
# ------------------------------------------------------------

number = int(input("\nQ20 - Enter a number: "))

if number == 0:
    print("Zero")

elif number > 0 and number % 2 == 0:
    print("Positive Even")

elif number > 0 and number % 2 != 0:
    print("Positive Odd")

elif number < 0 and number % 2 == 0:
    print("Negative Even")

else:
    print("Negative Odd")


