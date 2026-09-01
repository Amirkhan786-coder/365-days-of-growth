#  Practice Questions
## Python Input & Type Conversion

---

# 🟢 LEVEL 1 — BASIC

### Q1.
What is the purpose of the `input()` function?

### Q2.
What data type does `input()` return by default?

### Q3.
Write a Python program to take the user's name as input and print it.

### Q4.
Write a program to take the user's age as input and display it.

### Q5.
What is type conversion?

### Q6.
Why is type conversion required when taking numerical input?

### Q7.
What does the `int()` function do?

### Q8.
What does the `float()` function do?

### Q9.
What does the `str()` function do?

### Q10.
What is the difference between `"20"` and `20`?

---

# 🟢 LEVEL 1 — SIMPLE PROGRAMS

### Q11.
Take two numbers from the user and print their addition.

### Q12.
Take two numbers and print their subtraction.

### Q13.
Take two numbers and print their multiplication.

### Q14.
Take two numbers and print their division.

### Q15.
Take the length and width of a rectangle and calculate its area.

### Q16.
Take the side of a square and calculate its area.

### Q17.
Take the radius of a circle and calculate its area.

### Q18.
Take the user's birth year and calculate their approximate age.

### Q19.
Take a product price and quantity and calculate the total price.

### Q20.
Take Celsius temperature and convert it into Fahrenheit.

---

# 🟡 LEVEL 2 — OUTPUT QUESTIONS

## Q21.

What will be the output?

```python
name = input("Enter name: ")
print(type(name))
````

If the user enters:

```text
Amir
```

---

## Q22.

What will be the output?

```python
x = input()
y = input()

print(x + y)
```

Input:

```text
10
20
```

---

## Q23.

What will be the output?

```python
x = int("50")

print(x + 10)
```

---

## Q24.

What will be the output?

```python
x = float("10.5")

print(x)
print(type(x))
```

---

## Q25.

What will be the output?

```python
x = str(100)

print(type(x))
```

---

# 🟡 LEVEL 2 — TYPE CONVERSION

### Q26.

Convert the string `"100"` into an integer.

### Q27.

Convert the string `"25.5"` into a float.

### Q28.

Convert the integer `500` into a string.

### Q29.

Convert the integer `50` into a float.

### Q30.

Convert the float `25.8` into an integer.

---

# 🟠 LEVEL 3 — INTERACTIVE PROGRAMS

### Q31.

Create a program that takes:

* Name
* Age
* College
* Branch

and displays the complete student profile.

### Q32.

Create a program that takes five subject marks and calculates:

* Total
* Average

### Q33.

Create a calculator that takes two numbers and displays:

* Addition
* Subtraction
* Multiplication
* Division

### Q34.

Create a program that takes product price and quantity and calculates the final bill.

### Q35.

Create a program that takes distance in kilometers and converts it into meters.

### Q36.

Create a program that takes hours and converts them into minutes.

### Q37.

Create a program that takes minutes and converts them into seconds.

### Q38.

Create a program that takes the user's age and displays their age after 5 years.

---

# 🔴 LEVEL 4 — CHALLENGE

### Q39.

Create a program that takes the birth year and calculates:

* Current age
* Age after 5 years
* Age after 10 years

### Q40.

Create a student result calculator that takes five subject marks and displays:

* Total Marks
* Average
* Percentage

Assume each subject is out of 100.

### Q41.

Create a bill calculator that takes:

* Product name
* Price
* Quantity

and displays the total amount.

### Q42.

Create a salary calculator that takes:

* Basic salary
* Bonus

and calculates the total salary.

### Q43.

Create a BMI calculator that takes:

* Weight in kilograms
* Height in meters

Use:

```text
BMI = weight / (height × height)
```

### Q44.

Create a currency-style calculator that takes an amount and converts it using a fixed conversion rate that you define in the program.

### Q45.

Create a time converter that takes total minutes and calculates:

* Hours
* Remaining minutes

---

# 🔥 LEVEL 5 — THINKING QUESTIONS

### Q46.

Why does this produce `1020` instead of `30`?

```python
a = input()
b = input()

print(a + b)
```

---

### Q47.

Why does this work?

```python
a = int(input())
b = int(input())

print(a + b)
```

---

### Q48.

What happens if we write:

```python
age = int(input())
```

and enter:

```text
abc
```

---

### Q49.

What is the difference between:

```python
int("10")
```

and:

```python
float("10")
```

---

### Q50.

Why is `str()` usually not required when storing normal user input?

---

# 🏆 DAY 004 FINAL CHALLENGE

Build a complete **Student Information & Result System**.

The program should take:

```text
Student Name
Age
College
Branch
Subject 1 Marks
Subject 2 Marks
Subject 3 Marks
Subject 4 Marks
Subject 5 Marks
```

Then display:

```text
========================================
       STUDENT RESULT SYSTEM
========================================

Name
Age
College
Branch

----------------------------------------
Subject Marks
----------------------------------------

Total Marks
Average
Percentage

========================================
```

### Requirements:

* Use `input()`
* Use `int()`
* Use `float()`
* Use variables
* Use arithmetic operators
* Use meaningful variable names
* Keep the output clean and readable

---

# ✅ DAY 004 PRACTICE TARGET

Minimum:

* 20 questions
* 10 Python programs
* 5 output questions
* 5 type-conversion exercises

Recommended:

* Complete all 50 questions
* Build the final challenge without copying
* Explain every line of your program yourself

---

# 🚀 Rule

Don't just copy the answers.

First:

```text
Understand
↓
Think
↓
Write
↓
Run
↓
Find Errors
↓
Fix
↓
Repeat
```

## 💡 Goal

Build problem-solving ability, not just syntax knowledge.

