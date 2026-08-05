# 📘 Day 10 - Python Modules & Packages

---

# What is a Module?

A Module is a Python file (.py) that contains functions, variables, classes, or executable code which can be reused in other Python programs.

Instead of writing the same code repeatedly, we place it inside a module and import it whenever needed.

Example:

math.py
calculator.py
random.py

---

# Why Do We Use Modules?

Modules help us to:

✔ Reuse Code

✔ Organize Programs

✔ Reduce Code Duplication

✔ Improve Readability

✔ Easy Maintenance

✔ Faster Development

---

# Types of Modules

Python has two types of modules.

1. Built-in Modules

Already available in Python.

Examples

- math
- random
- datetime
- os
- statistics
- time

---

2. User Defined Modules

Modules created by the programmer.

Example

calculator.py

student.py

marks.py

---

# Import Statement

The import keyword is used to use a module.

Syntax

import module_name

Example

import math

print(math.sqrt(25))

Output

5.0

---

# Import Multiple Modules

Example

import math
import random
import os

---

# Import Multiple Modules in One Line

Example

import math, random, os

---

# Aliasing Modules

We can give a short name to a module using the as keyword.

Syntax

import module as alias

Example

import math as m

print(m.sqrt(49))

Output

7.0

---

# from...import Statement

Instead of importing the whole module, we can import only required functions.

Example

from math import sqrt

print(sqrt(81))

Output

9.0

---

# Import Multiple Functions

Example

from math import sqrt, factorial

print(sqrt(64))

print(factorial(5))

---

# Import Everything

Example

from math import *

print(sqrt(100))

print(pow(2,5))

Note:
Using * is not recommended in professional coding because it can create naming conflicts.

---

# Creating Your Own Module

Create a file

calculator.py

Example

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

Save the file.

Now create another file.

main.py

Example

import calculator

print(calculator.add(10,20))

print(calculator.sub(20,10))

---

# User Defined Module

A module created by the programmer is called a User Defined Module.

Example

student.py

employee.py

calculator.py

---

# Module Search Path

When Python imports a module, it searches in the following order.

1. Current Folder

↓

2. Installed Python Libraries

↓

3. System Path

Python stores these paths in

sys.path

Example

import sys

print(sys.path)

---

# Built-in Modules

Python provides many ready-made modules.

Some commonly used modules are:

math

random

datetime

os

statistics

time

calendar

string

---

# math Module

Used for mathematical operations.

Common Functions

sqrt()

pow()

factorial()

ceil()

floor()

fabs()

pi

e

Example

import math

print(math.sqrt(64))

print(math.factorial(5))

print(math.pi)

---

# random Module

Used for generating random values.

Functions

randint()

choice()

shuffle()

random()

uniform()

Example

import random

print(random.randint(1,100))

---

# datetime Module

Used for working with dates and time.

Example

import datetime

today = datetime.datetime.now()

print(today)

Useful Methods

now()

today()

date()

time()

strftime()

---

# os Module

Used to interact with the Operating System.

Functions

getcwd()

mkdir()

listdir()

rename()

remove()

system()

Example

import os

print(os.getcwd())

---

# dir() Function

Used to display all available functions inside a module.

Example

import math

print(dir(math))

---

# Packages

A Package is a collection of multiple modules.

Example

MyPackage/

│

├── add.py

├── sub.py

└── __init__.py

Import

from MyPackage import add

---

# __name__ Variable

Every Python file has a special variable named

__name__

When the file runs directly,

__name__ == "__main__"

When imported,

__name__ becomes the module name.

Example

if __name__ == "__main__":
    print("Program Running Directly")

---

# Advantages of Modules

✔ Code Reusability

✔ Easy Debugging

✔ Easy Maintenance

✔ Better Organization

✔ Faster Development

✔ Modular Programming

✔ Less Code Duplication

---

# Disadvantages

❌ Too many modules may make projects difficult to manage.

❌ Circular imports can cause errors.

---

# Best Practices

✔ Use meaningful module names.

✔ Keep one purpose per module.

✔ Avoid "from module import *"

✔ Organize related modules into packages.

✔ Write reusable functions.

✔ Add comments and documentation.

---

# Real-Life Uses

Modules are used in

✔ Web Development

✔ AI & Machine Learning

✔ Data Science

✔ Automation

✔ Cyber Security

✔ Game Development

✔ Desktop Applications

✔ APIs

✔ Banking Software

✔ Hospital Management Systems

---

# Summary

A Module is a reusable Python file that helps organize code.

Python provides many built-in modules, and developers can also create their own modules.

Using modules makes programs cleaner, reusable, maintainable, and suitable for large real-world projects.