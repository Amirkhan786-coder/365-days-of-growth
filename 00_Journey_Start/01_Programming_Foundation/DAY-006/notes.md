
# PYTHON CONDITIONAL STATEMENTS

## Complete Notes

Conditional statements allow a program to **make decisions** based on conditions.

For example:

- If marks are 40 or more → Pass
- If age is 18 or more → Eligible
- If number is divisible by 2 → Even
- Otherwise → Odd

---

# 1. 🧠 What is a Condition?

A condition is an expression whose result is either:

```text
True
False
````

Example:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

Another example:

```python
age = 15

print(age >= 18)
```

Output:

```text
False
```

Conditions are commonly created using comparison operators.

---

# 2. 🔢 Comparison Operators

| Operator | Meaning                  | Example    |
| -------- | ------------------------ | ---------- |
| `==`     | Equal to                 | `5 == 5`   |
| `!=`     | Not equal to             | `5 != 3`   |
| `>`      | Greater than             | `10 > 5`   |
| `<`      | Less than                | `3 < 8`    |
| `>=`     | Greater than or equal to | `10 >= 10` |
| `<=`     | Less than or equal to    | `5 <= 10`  |

Example:

```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

Output:

```text
False
True
True
False
True
True
```

---

# 3. 🟢 `if` Statement

The `if` statement executes a block of code when a condition is `True`.

Syntax:

```python
if condition:
    statement
```

Example:

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Output:

```text
You are an adult
```

If the condition is `False`, the code inside the `if` block will not execute.

Example:

```python
age = 15

if age >= 18:
    print("You are an adult")
```

There will be no output.

---

# 4. 📌 Colon `:`

A colon is required after the condition.

Correct:

```python
if age >= 18:
    print("Adult")
```

Incorrect:

```python
if age >= 18
    print("Adult")
```

The colon tells Python that the block of code is starting.

---

# 5. 📏 Python Indentation

Python uses indentation to define blocks of code.

Correct:

```python
age = 20

if age >= 18:
    print("Adult")
```

Incorrect:

```python
age = 20

if age >= 18:
print("Adult")
```

Usually, Python uses **4 spaces** for indentation.

Example:

```python
if True:
    print("Hello")
    print("Python")
```

Both statements belong to the `if` block.

---

# 6. 🟡 `if-else` Statement

Sometimes we need two possible outcomes.

If the condition is `True`, execute the `if` block.

Otherwise, execute the `else` block.

Syntax:

```python
if condition:
    statement
else:
    statement
```

Example:

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Not Positive")
```

Output:

```text
Positive
```

---

# 7. 🔢 Even or Odd

The modulus operator `%` can be used to check whether a number is even or odd.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

Logic:

```text
number % 2 == 0
        ↓
      EVEN

Otherwise
        ↓
       ODD
```

---

# 8. 🟠 `if-elif-else`

When we have multiple conditions, we use:

```text
if
elif
else
```

Syntax:

```python
if condition1:
    statement

elif condition2:
    statement

else:
    statement
```

Example:

```python
marks = 85

if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 70:
    print("B")

else:
    print("C")
```

Output:

```text
A
```

Python checks the conditions from top to bottom.

As soon as one condition becomes `True`, that block executes and the remaining conditions are skipped.

---

# 9. 📊 Grade Calculator

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Fail")
```

Example:

```text
Enter marks: 85
Grade A
```

---

# 10. 🔴 Nested `if`

An `if` statement inside another `if` statement is called a **nested if**.

Example:

```python
age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to vote")
```

The program first checks:

```text
age >= 18
```

If that is true, it checks:

```text
citizen
```

Then it prints:

```text
Eligible to vote
```

---

# 11. 🔵 Logical Operators

Python has three important logical operators:

```text
and
or
not
```

They are used to combine multiple conditions.

---

# 12. `and` Operator

`and` returns `True` only when **all conditions are True**.

Example:

```python
age = 25

if age >= 18 and age <= 60:
    print("Eligible")
```

Both conditions must be true.

Truth table:

```text
True  AND True  → True
True  AND False → False
False AND True  → False
False AND False → False
```

---

# 13. `or` Operator

`or` returns `True` when at least one condition is `True`.

Example:

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

Output:

```text
Weekend
```

Truth table:

```text
True  OR True  → True
True  OR False → True
False OR True  → True
False OR False → False
```

---

# 14. `not` Operator

The `not` operator reverses a Boolean result.

Example:

```python
is_raining = False

if not is_raining:
    print("You don't need an umbrella")
```

Logic:

```text
not True  → False
not False → True
```

---

# 15. ⚠️ `=` vs `==`

This is one of the most common beginner mistakes.

### Assignment

```python
age = 20
```

This stores `20` in the variable `age`.

### Comparison

```python
age == 20
```

This checks whether `age` is equal to `20`.

Remember:

```text
=   → Assignment
==  → Comparison
```

---

# 16. ⌨️ Taking Input

Conditional statements are commonly used with user input.

Example:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

Example output:

```text
Enter your age: 19
Eligible to vote
```

---

# 17. 🔢 Positive, Negative or Zero

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

Logic:

```text
number > 0
    ↓
Positive

number < 0
    ↓
Negative

otherwise
    ↓
Zero
```

---

# 18. 🎂 Age Category

```python
age = int(input("Enter age: "))

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")
```

---

# 19. 🏆 Largest of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is larger")

elif b > a:
    print("B is larger")

else:
    print("Both are equal")
```

---

# 20. 🏆 Largest of Three Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("A is largest")

elif b >= a and b >= c:
    print("B is largest")

else:
    print("C is largest")
```

---

# 21. 🔐 Simple Login System

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
```

This is only a beginner programming example.

Real applications should use proper authentication and secure password handling.

---

# 22. 🏧 Simple ATM Logic

```python
balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")

elif amount <= balance:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)

else:
    print("Insufficient balance")
```

This example combines:

* Input
* Variables
* Comparison operators
* `if`
* `elif`
* `else`
* Arithmetic operators

---

# 23. 💰 Discount Calculator

```python
price = float(input("Enter price: "))

if price >= 5000:
    discount = price * 0.20

elif price >= 3000:
    discount = price * 0.10

else:
    discount = 0

final_price = price - discount

print("Discount:", discount)
print("Final Price:", final_price)
```

---

# 24. ⚡ Electricity Bill Logic

Example:

```python
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = units * 7

else:
    bill = units * 10

print("Electricity Bill:", bill)
```

The rates above are only for programming practice.

---

# 25. 📅 Leap Year Checker

```python
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("Not a Leap Year")

elif year % 4 == 0:
    print("Leap Year")

else:
    print("Not a Leap Year")
```

The important programming concept here is combining multiple conditions.

---

# 26. 🧮 Simple Calculator

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(a + b)

elif operator == "-":
    print(a - b)

elif operator == "*":
    print(a * b)

elif operator == "/":

    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")
```

This example demonstrates a **nested condition**.

---

# 27. 🌡️ Temperature Category

```python
temperature = float(input("Enter temperature: "))

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
```

---

# 28. 📚 Pass or Fail

```python
marks = float(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

# 29. 🧠 Condition Ordering

The order of conditions is extremely important.

Consider:

```python
marks = 95

if marks >= 40:
    print("Pass")

elif marks >= 90:
    print("A+")
```

Output:

```text
Pass
```

Why?

Because:

```text
95 >= 40
```

is already `True`.

Python therefore executes the first block and does not check the `elif`.

Correct approach:

```python
if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 70:
    print("B")

elif marks >= 40:
    print("Pass")

else:
    print("Fail")
```

### Important Rule

When checking ranges, carefully arrange conditions from the appropriate higher/specific range toward the lower range.

---

# 30. 🔄 Conditional Statement Flow

## `if`

```text
       Condition
           ↓
      ┌────┴────┐
    True      False
      ↓          ↓
   Execute      Skip
```

## `if-else`

```text
       Condition
           ↓
      ┌────┴────┐
    True      False
      ↓          ↓
     IF         ELSE
      ↓          ↓
      └────┬─────┘
           ↓
        Continue
```

## `if-elif-else`

```text
      Condition 1
           ↓
       True?
      /     \
    Yes      No
    ↓         ↓
 Execute   Condition 2
              ↓
           True?
          /     \
        Yes      No
        ↓         ↓
     Execute     ELSE
```

---

# 31. ❌ Common Mistakes

## Mistake 1: Using `=` instead of `==`

Wrong:

```python
if age = 18:
    print("18")
```

Correct:

```python
if age == 18:
    print("18")
```

---

## Mistake 2: Forgetting `:`

Wrong:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 3: Incorrect Indentation

Wrong:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 4: Wrong Condition Order

Wrong ordering can produce unexpected results.

Always think about:

```text
Which condition should be checked first?
```

---

## Mistake 5: Forgetting Input Conversion

`input()` normally returns a string.

For numbers, use:

```python
age = int(input("Enter age: "))
```

or:

```python
price = float(input("Enter price: "))
```

---

# 32. 🌍 Real-World Applications

Conditional statements are used everywhere.

### Banking

```text
If balance >= withdrawal
→ Allow withdrawal
```

### E-Commerce

```text
If order amount >= minimum amount
→ Free delivery
```

### Education

```text
If marks >= passing marks
→ Pass
```

### Authentication

```text
If username and password are correct
→ Login
```

### Games

```text
If health <= 0
→ Game Over
```

### Applications

```text
If user is logged in
→ Show dashboard
```

---

# 33. 🤖 Connection With AI/ML

Conditional logic is also important in AI/ML.

For example:

```python
probability = 0.85

if probability >= 0.80:
    print("High confidence prediction")
else:
    print("Low confidence prediction")
```

Later, AI/ML concepts will involve:

* Classification
* Thresholds
* Predictions
* Decision boundaries
* Model evaluation
* Confidence scores

Strong conditional logic will help in understanding these concepts.

---

# 34. 🧠 Problem-Solving Framework

Whenever you get a conditional programming question, follow this process:

```text
Understand Problem
        ↓
Identify Input
        ↓
Identify Output
        ↓
Find Conditions
        ↓
Write Logic
        ↓
Write Code
        ↓
Test
        ↓
Debug
```

Example:

### Problem

Check whether a person is eligible to vote.

### Input

```text
Age
```

### Condition

```text
Age >= 18
```

### Output

```text
Eligible
OR
Not Eligible
```

### Code

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

---

# 35. 🧪 Test Multiple Cases

Never test a program with only one input.

For example:

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

Test:

```text
Input: 20
Expected: Eligible

Input: 18
Expected: Eligible

Input: 17
Expected: Not Eligible

Input: 0
Expected: Not Eligible
```

Testing multiple cases helps identify logical errors.

---

# 36. 🔥 Beginner → Intermediate Logic

### Beginner

```python
if number > 0:
    print("Positive")
```

### Intermediate

```python
if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

### More Advanced

```python
if number > 0 and number % 2 == 0:
    print("Positive Even")

elif number > 0 and number % 2 != 0:
    print("Positive Odd")

elif number < 0 and number % 2 == 0:
    print("Negative Even")

elif number < 0 and number % 2 != 0:
    print("Negative Odd")

else:
    print("Zero")
```

This shows how multiple conditions can be combined.

---

# 37. 🎯 Important Concepts to Remember

```text
if
↓
Checks a condition

else
↓
Runs when the previous condition is False

elif
↓
Checks another condition

nested if
↓
An if statement inside another if

and
↓
All conditions should be True

or
↓
At least one condition should be True

not
↓
Reverses True and False
```

---

# 38. 🧠 Quick Revision

### What is `if`?

Used to execute code when a condition is true.

### What is `else`?

Used when the `if` condition is false.

### What is `elif`?

Used to check additional conditions.

### What is nested `if`?

An `if` inside another `if`.

### What does `==` do?

It compares two values.

### What does `=` do?

It assigns a value.

### What does `and` do?

All conditions must be true.

### What does `or` do?

At least one condition must be true.

### What does `not` do?

It reverses a Boolean result.

---

# 39. 🚀 Connection With Future Topics

Conditional statements are a foundation for:

```text
Conditional Statements
        ↓
Loops
        ↓
Functions
        ↓
Lists / Tuples / Dictionaries
        ↓
Problem Solving
        ↓
DSA
        ↓
Algorithms
        ↓
Data Analysis
        ↓
Machine Learning
        ↓
Artificial Intelligence
```

---

# 40. 🏆 Day 006 Summary

Today I learned:

* Conditions
* Boolean values
* `if`
* `if-else`
* `if-elif-else`
* Nested `if`
* Comparison operators
* Logical operators
* User input with conditions
* Python indentation
* Condition ordering
* Common mistakes
* Real-world applications
* Problem-solving techniques

---

# 🔥 Day 006 Key Takeaway

Don't just memorize syntax.

Ask yourself:

> "What decision does my program need to make?"

Then convert that decision into a condition.

```text
THINK
  ↓
LOGIC
  ↓
CODE
  ↓
TEST
  ↓
DEBUG
  ↓
IMPROVE

