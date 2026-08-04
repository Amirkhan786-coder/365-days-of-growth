# 🚀 DAY 09 – Python Functions

# 📌 What is a Function?

A Function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we can write it once inside a function and call it whenever needed.

Functions make programs:

- Reusable
- Organized
- Easy to Read
- Easy to Debug
- Easy to Maintain

---

# 📌 Why Do We Use Functions?

Suppose you want to print a welcome message 20 times.

Without Function:

print("Welcome")
print("Welcome")
print("Welcome")
...
(repeat many times)

This creates repetitive code.

With Function:

```python
def welcome():
    print("Welcome")

welcome()
welcome()
welcome()
```

Now the same code is reused multiple times.

---

# 📌 Advantages of Functions

✔ Code Reusability

✔ Less Repetition

✔ Easy Maintenance

✔ Better Readability

✔ Faster Development

✔ Easier Debugging

✔ Modular Programming

---

# 📌 Syntax of Function

```python
def function_name():
    # code
```

Example

```python
def hello():
    print("Hello World")
```

---

# 📌 Calling a Function

A function does nothing until it is called.

Example

```python
def hello():
    print("Hello Python")

hello()
```

Output

```
Hello Python
```

---

# 📌 Function Execution Flow

Program Starts

↓

Function Defined

↓

Function Called

↓

Function Executes

↓

Program Continues

---

# 📌 Function Naming Rules

✔ Can contain letters

✔ Can contain numbers

✔ Can contain underscore (_)

✔ Cannot start with number

✔ Cannot contain spaces

✔ Should use meaningful names

Good

```python
calculate_marks()

student_details()

find_average()
```

Bad

```python
abc()

xyz()

test1()
```

---

# 📌 Types of Functions

Python has two main types.

## 1. Built-in Functions

Already available in Python.

Examples

```python
print()

len()

type()

input()

max()

min()

sum()

range()
```

---

## 2. User Defined Functions

Functions created by programmers.

Example

```python
def greet():
    print("Good Morning")
```

---

# 📌 Real-Life Examples

ATM

Withdraw()

Deposit()

CheckBalance()

Restaurant

TakeOrder()

PrepareFood()

GenerateBill()

School

AddStudent()

CalculateMarks()

GenerateResult()

Hospital

BookAppointment()

GeneratePrescription()

---

# 📌 Flow Diagram

Input

↓

Function

↓

Processing

↓

Output

---

# 📌 Interview Question

Q. What is a Function?

Answer:

A Function is a reusable block of code that performs a specific task. It improves readability, reduces repetition, and makes programs modular.

---

# 📌 Summary

✔ Function = Reusable Code

✔ Improves Readability

✔ Reduces Duplicate Code

✔ Makes Projects Modular

✔ Easy to Maintain

✔ Easy to Debug

✔ Used in Every Large Software Project


# 📌 Parameters and Arguments

Functions become more useful when we pass data to them.

The values received by a function are called **Parameters**, and the values passed while calling the function are called **Arguments**.

---

# 📌 Parameter

A Parameter is a variable written inside the function definition.

Syntax

```python
def function_name(parameter):
    # code
```

Example

```python
def greet(name):
    print("Hello", name)
```

Here,

name → Parameter

---

# 📌 Argument

An Argument is the actual value passed while calling a function.

Example

```python
def greet(name):
    print("Hello", name)

greet("Amir")
```

Output

```
Hello Amir
```

Here,

"Amir" → Argument

---

# 📌 Parameter vs Argument

| Parameter | Argument |
|------------|----------|
| Defined in Function | Passed during Function Call |
| Placeholder | Actual Value |
| Variable | Data |

Example

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Parameters

a

b

Arguments

10

20

---

# 📌 Positional Arguments

Arguments are assigned according to their position.

Example

```python
def student(name, age):
    print(name)
    print(age)

student("Amir", 19)
```

Output

```
Amir
19
```

---

# 📌 Keyword Arguments

Arguments are passed using parameter names.

Example

```python
def student(name, age):
    print(name)
    print(age)

student(age=19, name="Amir")
```

Output

```
Amir
19
```

The order does not matter.

---

# 📌 Default Arguments

A parameter can have a default value.

Example

```python
def country(name, nation="India"):
    print(name)
    print(nation)

country("Amir")
```

Output

```
Amir
India
```

If another value is passed

```python
country("Amir", "USA")
```

Output

```
Amir
USA
```

---

# 📌 Variable Length Arguments (*args)

Sometimes we don't know how many arguments will be passed.

Syntax

```python
def function(*args):
```

Example

```python
def numbers(*num):
    print(num)

numbers(10, 20, 30, 40)
```

Output

```
(10, 20, 30, 40)
```

---

# 📌 Looping Through *args

Example

```python
def total(*marks):
    for i in marks:
        print(i)

total(80, 90, 85)
```

Output

```
80
90
85
```

---

# 📌 Keyword Variable Arguments (**kwargs)

Used when passing multiple keyword arguments.

Example

```python
def student(**data):
    print(data)

student(Name="Amir", Age=19, City="Meerut")
```

Output

```
{'Name': 'Amir', 'Age': 19, 'City': 'Meerut'}
```

---

# 📌 Accessing kwargs

```python
def student(**data):
    print(data["Name"])

student(Name="Amir", Age=19)
```

Output

```
Amir
```

---

# 📌 Mixing Different Arguments

Example

```python
def info(name, age=18, *marks, **details):
    print(name)
    print(age)
    print(marks)
    print(details)

info("Amir", 19, 80, 90, City="Meerut")
```

Output

```
Amir
19
(80, 90)
{'City': 'Meerut'}
```

---

# 📌 Rules

✔ Positional Arguments first

✔ Default Arguments after Positional

✔ *args before **kwargs

✔ **kwargs should be last

---

# 📌 Real-Life Example

Online Shopping

```python
def order(name, product, quantity=1):
    print(name)
    print(product)
    print(quantity)

order("Amir", "Laptop")
```

Output

```
Amir
Laptop
1
```

---

# 🎤 Interview Questions

Q. What is the difference between Parameter and Argument?

Answer:

A Parameter is a variable defined in the function declaration, while an Argument is the actual value passed when calling the function.

---

Q. Difference between *args and **kwargs?

Answer:

*args accepts multiple positional arguments.

**kwargs accepts multiple keyword arguments.

---

# 📌 Summary

✔ Parameters receive values

✔ Arguments send values

✔ Positional Arguments

✔ Keyword Arguments

✔ Default Arguments

✔ Variable Length Arguments

✔ *args

✔ **kwargs

# 📌 Return Statement

A **return statement** is used to send a value back from a function to the place where it was called.

Instead of printing the result inside the function, we return it so it can be used later.

---

# 📌 Syntax

```python
def function_name():
    return value
```

---

# 📌 Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output

```
30
```

---

# 📌 Difference Between print() and return

## print()

- Displays output on the screen.
- Cannot be reused later.

Example

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

## return

- Sends the value back.
- Can be stored in a variable.
- Can be used in another calculation.

Example

```python
def add(a, b):
    return a + b

total = add(10, 20)

print(total * 2)
```

Output

```
60
```

---

# 📌 Returning Multiple Values

Python allows returning multiple values.

Example

```python
def calculate(a, b):
    return a+b, a-b, a*b

sum, sub, mul = calculate(20,10)

print(sum)
print(sub)
print(mul)
```

Output

```
30
10
200
```

---

# 📌 Local Variable

A Local Variable is created inside a function.

It can only be used inside that function.

Example

```python
def demo():
    x = 10
    print(x)

demo()
```

---

# 📌 Global Variable

A Global Variable is created outside the function.

It can be accessed from anywhere in the program.

Example

```python
name = "Amir"

def student():
    print(name)

student()
```

---

# 📌 Global Keyword

The **global** keyword allows you to modify a global variable inside a function.

Example

```python
count = 0

def increase():
    global count
    count += 1

increase()

print(count)
```

Output

```
1
```

---

# 📌 Variable Scope

Python has two main scopes.

## Local Scope

Variable exists only inside a function.

## Global Scope

Variable exists throughout the program.

---

# 📌 Recursive Function

A Recursive Function is a function that calls itself.

Example

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n-1)

countdown(5)
```

Output

```
5
4
3
2
1
```

---

# 📌 Factorial Using Recursion

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))
```

Output

```
120
```

---

# 📌 Lambda Function

A Lambda Function is an anonymous function written in one line.

Syntax

```python
lambda arguments : expression
```

---

# 📌 Example

```python
square = lambda x: x*x

print(square(5))
```

Output

```
25
```

---

# 📌 Lambda with Multiple Arguments

```python
add = lambda a, b: a+b

print(add(10,20))
```

Output

```
30
```

---

# 📌 Docstrings

A Docstring is used to describe what a function does.

Example

```python
def greet():

    """
    This function prints a welcome message.
    """

    print("Welcome")

greet()
```

---

# 📌 Built-in Functions

Python provides many ready-made functions.

Examples

```python
print()

len()

type()

input()

max()

min()

sum()

range()

abs()

round()

sorted()
```

---

# 📌 Real-Life Example

Bank

```python
def withdraw(balance, amount):

    if amount <= balance:
        return balance - amount

    return balance

print(withdraw(5000, 1500))
```

Output

```
3500
```

---

# 📌 Best Practices

✔ Use meaningful function names

✔ Keep functions short

✔ Avoid duplicate code

✔ Use return instead of print when needed

✔ Add docstrings

✔ Keep one task per function

---

# 🎤 Interview Questions

Q. What is the difference between Local and Global Variables?

Answer:

Local Variables exist only inside a function, while Global Variables can be accessed throughout the program.

---

Q. Why is return better than print()?

Answer:

Because return sends data back to the caller, allowing it to be reused in other operations.

---

Q. What is a Lambda Function?

Answer:

A Lambda Function is a small anonymous function written in a single line using the lambda keyword.

---

Q. What is Recursion?

Answer:

Recursion is a technique in which a function calls itself until a base condition is met.

---

# 📌 Summary

✔ Return Statement

✔ Local Variables

✔ Global Variables

✔ Variable Scope

✔ Global Keyword

✔ Recursive Functions

✔ Lambda Functions

✔ Docstrings

✔ Built-in Functions

✔ Best Practices

