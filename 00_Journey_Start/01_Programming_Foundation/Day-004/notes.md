
#  Python Input & Type Conversion

## 1. What is input()?

The `input()` function is used to take information from the user while the program is running.

Syntax:

```python
input("Message")
````

Example:

```python
name = input("Enter your name: ")

print("Hello", name)
```

If the user enters:

Amir

Output:

Hello Amir

---

## 2. Taking Multiple Inputs

We can take multiple values from the user and store them in different variables.

```python
name = input("Enter your name: ")
college = input("Enter your college name: ")
branch = input("Enter your branch: ")

print("Name:", name)
print("College:", college)
print("Branch:", branch)
```

---

## 3. Important: input() Returns a String

The `input()` function always returns a string by default.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

20

The output will be:

```text
<class 'str'>
```

Python treats the entered value as:

```text
"20"
```

not:

```text
20
```

---

## 4. Why Does This Matter?

Consider this program:

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)
```

If the user enters:

10

20

The output will be:

1020

This happens because both values are strings.

Python performs:

```text
"10" + "20"
```

which gives:

```text
"1020"
```

This is called string concatenation.

---

## 5. Type Conversion

Type conversion means changing one data type into another data type.

Common type conversion functions are:

```text
int()
float()
str()
```

---

## 6. int()

The `int()` function converts a value into an integer.

Example:

```python
number = int("50")

print(number)
print(type(number))
```

Output:

```text
50
<class 'int'>
```

We commonly use `int()` with user input:

```python
age = int(input("Enter your age: "))
```

Now the age can be used in mathematical calculations.

Example:

```python
age = int(input("Enter your age: "))

future_age = age + 5

print("Your age after 5 years:", future_age)
```

---

## 7. float()

The `float()` function converts a value into a decimal number.

Example:

```python
height = float("5.8")

print(height)
print(type(height))
```

Output:

```text
5.8
<class 'float'>
```

Using user input:

```python
height = float(input("Enter your height: "))
```

`float()` is useful for:

* Height
* Weight
* Price
* Percentage
* Temperature
* Measurements

---

## 8. str()

The `str()` function converts a value into a string.

Example:

```python
number = 100

text = str(number)

print(text)
print(type(text))
```

Output:

```text
100
<class 'str'>
```

---

## 9. Input with Type Conversion

We can directly convert user input.

### Integer

```python
age = int(input("Enter your age: "))
```

### Float

```python
height = float(input("Enter your height: "))
```

### String

```python
name = str(input("Enter your name: "))
```

The `str()` conversion is usually unnecessary here because `input()` already returns a string.

---

## 10. Input → Process → Output

Many basic programs follow this structure:

```text
INPUT
  ↓
PROCESS
  ↓
OUTPUT
```

Example:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

print("Addition:", result)
```

Here:

Input:

```text
num1
num2
```

Process:

```text
num1 + num2
```

Output:

```text
result
```

---

## 11. Difference Between String, Integer and Float

String:

```python
"20"
```

Integer:

```python
20
```

Float:

```python
20.0
```

All three represent different data types.

We can check them using:

```python
print(type("20"))
print(type(20))
print(type(20.0))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
```

---

## 12. Real-Life Example

Suppose we want to calculate the total price of products.

We need:

* Product price
* Quantity
* Total cost

Program:

```python
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total Cost:", total)
```

Here:

```text
price → float
quantity → int
total → multiplication result
```

---

## 13. Age Calculator Example

```python
birth_year = int(input("Enter your birth year: "))

current_year = 2026

age = current_year - birth_year

print("Your approximate age is:", age)
```

The important part is:

```python
birth_year = int(input("Enter your birth year: "))
```

Without `int()`, subtraction would not work correctly because input would be a string.

---

## 14. Celsius to Fahrenheit

Formula:

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

Python program:

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
```

---

## 15. Common Error — ValueError

Consider:

```python
age = int(input("Enter your age: "))
```

If the user enters:

```text
abc
```

Python cannot convert `"abc"` into an integer.

Therefore, Python can produce:

```text
ValueError
```

This happens because the entered value is not a valid integer.

---

## 16. Important Rules to Remember

### Rule 1

`input()` returns a string.

### Rule 2

Use `int()` for whole numbers.

### Rule 3

Use `float()` for decimal numbers.

### Rule 4

Use `str()` when a value needs to be converted into text.

### Rule 5

Always think about the data type before performing an operation.

---

## 🧠 Quick Revision

```text
input()
    ↓
Takes user input
    ↓
Returns str
```

```text
int()
    ↓
Integer
```

```text
float()
    ↓
Decimal number
```

```text
str()
    ↓
String
```

---

## 🚀 Key Takeaway

User input is the starting point of many real-world programs.

A basic program often works like this:

```text
User Input
     ↓
Type Conversion
     ↓
Processing
     ↓
Output
```

Understanding this flow is an important step toward building larger Python applications.

---

## 💡 Day 004 Learning Goal

I am focusing on understanding the concept instead of just memorizing syntax.

Learn → Understand → Practice → Build → Improve

