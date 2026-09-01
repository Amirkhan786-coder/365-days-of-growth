
#  Python Input & Type Conversion

Welcome to Day 004 of my 365 Days of Growth journey! 🐍💻

Today, I learned how to make Python programs interactive by taking input directly from the user.

## 🎯 Topics Covered

- input() function
- Taking user input
- Understanding input data types
- Type Conversion
- int()
- float()
- str()
- Building interactive programs

## 🧠 What I Learned

The input() function is used to take information from the user.

Example:

```python
name = input("Enter your name: ")
print("Hello", name)
````

One important concept is that input() returns data as a string by default.

Example:

```python
age = input("Enter your age: ")
print(type(age))
```

Even if the user enters 20, Python stores it as a string.

To perform calculations, we can convert the input:

```python
age = int(input("Enter your age: "))
```

## 🔄 Type Conversion

Python provides different functions to convert data types.

| Function | Purpose                     |
| -------- | --------------------------- |
| int()    | Converts a value to integer |
| float()  | Converts a value to float   |
| str()    | Converts a value to string  |

Example:

```python
age = int("20")
height = float("5.8")
number = str(100)
```

## 📁 Files

* README.md
* notes.md
* input_basics.py
* type_conversion.py
* interactive_programs.py
* practice_questions.md
* answers.py
* mini_project.py

## 🛠️ Mini Project

### Student Result Calculator

The project takes:

* Student name
* Student age
* College name
* Branch
* Marks of five subjects

and calculates:

* Total marks
* Average marks

## 🔥 Key Takeaway

> input() takes information from the user, but Python stores that input as a string by default.

When calculations are required, type conversion becomes important.

## 🚀 Journey Progress

* ✅ Day 001 — Journey Foundation
* ✅ Day 002 — Programming Foundations & Problem Solving
* ✅ Day 003 — Python Variables & Data Types
* 🚀 Day 004 — Python Input & Type Conversion

## 💡 Final Thought

> Learn the basics deeply. Advanced programming is built on strong foundations.
