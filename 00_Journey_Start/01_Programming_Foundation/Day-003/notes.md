
# 📚 Python Variables & Data Types

## 1. What is Python?

Python is a high-level and easy-to-read programming language.

It is widely used in:

- Web Development
- Automation
- Data Analysis
- Artificial Intelligence
- Machine Learning
- Deep Learning

Python is popular because its syntax is simple and readable.

---

# 2. What is a Variable?

A variable is a name used to store data.

Example:

```python
name = "Amir Khan"

Here:

name is the variable name.
= is the assignment operator.
"Amir Khan" is the value.

Another example:

age = 20

Variables allow us to store and reuse information.

3. Why Do We Use Variables?

Example without variables:

print("Amir Khan")
print("Amir Khan")
print("Amir Khan")

Using a variable:

name = "Amir Khan"

print(name)
print(name)
print(name)

Variables make programs easier to manage and update.

4. Variable Naming Rules
Valid Variable Names
name = "Amir"
student_age = 20
marks1 = 90
_my_variable = "Python"
Invalid Variable Names
1name
student age
my-variable
Rules
A variable cannot start with a number.
Spaces are not allowed.
Hyphens are not allowed.
Underscores are allowed.
Python keywords should not be used as variable names.
Variable names are case-sensitive.
5. Data Types

Different types of values have different data types.

String — str

Used for text.

name = "Amir Khan"
Integer — int

Used for whole numbers.

age = 20
marks = 95
Float — float

Used for decimal numbers.

height = 5.8
percentage = 89.5
Boolean — bool

Boolean has two values:

True
False

Example:

is_student = True
is_logged_in = False
6. The type() Function

The type() function is used to check the data type of a value or variable.

Example:

age = 20

print(type(age))

Output:

<class 'int'>

Examples:

print(type("Hello"))
print(type(100))
print(type(5.5))
print(type(True))
🧠 Quick Summary
"Hello" → str
100 → int
5.5 → float
True → bool
Key Lesson

Variables store data.

Data types tell Python what kind of data is being stored.