# 📚 Day 13 — Python Modules & Packages

# 365 Days of Growth

---

# 1. What is a Module?

A **module** is a Python file containing code such as:

- Functions
- Variables
- Classes
- Statements

A module usually has the `.py` extension.

Example:

```text
math_utils.py
```

A module helps us organize code and reuse it in different programs.

---

# 2. Why Do We Use Modules?

Modules are useful because they help us:

- Reuse code
- Organize large programs
- Reduce duplicate code
- Make programs easier to maintain
- Improve readability
- Separate different functionalities

Instead of writing everything in one file, we can divide our program into multiple modules.

---

# 3. Creating a Module

Create a file:

```text
calculator.py
```

Add:

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

Now `calculator.py` is a module.

---

# 4. Importing a Module

We can import our module using `import`.

Example:

```python
import calculator
```

Then use its functions:

```python
print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
```

Output:

```text
15
5
```

---

# 5. import Statement

The `import` statement is used to import a complete module.

Syntax:

```python
import module_name
```

Example:

```python
import math
```

---

# 6. from ... import

We can import specific functions or variables from a module.

Syntax:

```python
from module_name import function_name
```

Example:

```python
from math import sqrt

print(sqrt(25))
```

Output:

```text
5.0
```

---

# 7. Import Multiple Items

We can import multiple functions from a module.

```python
from math import sqrt, factorial

print(sqrt(25))
print(factorial(5))
```

---

# 8. import as

We can give an imported module a shorter name using `as`.

Example:

```python
import math as m

print(m.sqrt(25))
```

Output:

```text
5.0
```

Another example:

```python
import datetime as dt

print(dt.datetime.now())
```

---

# 9. Built-in Modules

Python provides many modules that are already available.

Examples:

```text
math
random
datetime
os
sys
statistics
json
csv
time
re
```

These are called **standard library modules**.

---

# 10. math Module

The `math` module provides mathematical functions.

Import:

```python
import math
```

---

## Important math Functions

### sqrt()

Returns square root.

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

### pow()

Calculates power.

```python
import math

print(math.pow(2, 3))
```

Output:

```text
8.0
```

---

### factorial()

Calculates factorial.

```python
import math

print(math.factorial(5))
```

Output:

```text
120
```

---

### ceil()

Rounds a number upward.

```python
import math

print(math.ceil(4.2))
```

Output:

```text
5
```

---

### floor()

Rounds a number downward.

```python
import math

print(math.floor(4.8))
```

Output:

```text
4
```

---

### pi

Python provides the value of π.

```python
import math

print(math.pi)
```

---

# 11. random Module

The `random` module is used to generate random values.

Import:

```python
import random
```

---

## randint()

Generates a random integer between two values.

```python
import random

number = random.randint(1, 10)

print(number)
```

---

## randrange()

Generates a random number from a specified range.

```python
import random

number = random.randrange(1, 10)

print(number)
```

---

## choice()

Selects a random item from a sequence.

```python
import random

names = ["Amir", "Rahul", "Aman", "Ravi"]

print(random.choice(names))
```

---

## shuffle()

Randomly rearranges items in a list.

```python
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)
```

---

# 12. datetime Module

The `datetime` module is used to work with dates and times.

Example:

```python
import datetime

current_time = datetime.datetime.now()

print(current_time)
```

---

## Current Date

```python
import datetime

today = datetime.date.today()

print(today)
```

---

# 13. os Module

The `os` module allows Python to interact with the operating system.

Import:

```python
import os
```

---

## Current Working Directory

```python
import os

print(os.getcwd())
```

`getcwd()` returns the current working directory.

---

## List Files and Folders

```python
import os

print(os.listdir())
```

---

## Create a Folder

```python
import os

os.mkdir("new_folder")
```

---

# 14. sys Module

The `sys` module provides access to Python's system-specific functionality.

Example:

```python
import sys

print(sys.version)
```

This displays the Python version.

---

# 15. json Module

The `json` module is used to work with JSON data.

JSON means:

**JavaScript Object Notation**

Example JSON:

```json
{
    "name": "Amir",
    "age": 20
}
```

---

## Convert Python Dictionary to JSON

```python
import json

student = {
    "name": "Amir",
    "age": 20
}

data = json.dumps(student)

print(data)
```

---

## Convert JSON to Python Object

```python
import json

data = '{"name": "Amir", "age": 20}'

student = json.loads(data)

print(student["name"])
```

---

# 16. Creating Your Own Module

Create:

```text
my_module.py
```

Code:

```python
def greet(name):
    return f"Hello, {name}"


def square(number):
    return number * number
```

Create another file:

```text
main.py
```

Code:

```python
import my_module

print(my_module.greet("Amir"))
print(my_module.square(5))
```

Output:

```text
Hello, Amir
25
```

---

# 17. Using from with Custom Module

Instead of importing the complete module:

```python
from my_module import greet

print(greet("Amir"))
```

---

# 18. Using import as with Custom Module

```python
import my_module as mm

print(mm.greet("Amir"))
```

---

# 19. What is a Package?

A **package** is a directory containing related Python modules.

A package helps organize large Python projects.

Example:

```text
student_project/
│
├── main.py
│
└── student/
    ├── __init__.py
    ├── details.py
    └── marks.py
```

Here:

```text
student
```

is a package.

---

# 20. __init__.py

The `__init__.py` file is commonly used inside a Python package.

Example:

```text
student/
│
├── __init__.py
├── details.py
└── marks.py
```

It can be empty or contain package initialization code.

Modern Python also supports namespace packages without requiring `__init__.py` in every case, but using it is still common for regular packages.

---

# 21. Importing From a Package

Suppose:

```text
student/
│
├── __init__.py
├── details.py
└── marks.py
```

We can write:

```python
from student import details
```

Then:

```python
details.show_student()
```

---

# 22. __name__

Every Python module has a special built-in variable called:

```python
__name__
```

When a file is executed directly, its value is:

```text
__main__
```

When the file is imported, its value is usually the module's name.

---

# 23. __name__ == "__main__"

This is commonly used to make sure some code runs only when the file is executed directly.

Example:

```python
def greet():
    print("Hello Python")


if __name__ == "__main__":
    greet()
```

If the file is run directly:

```text
Hello Python
```

If the file is imported into another module, the code inside the `if` block does not run automatically.

---

# 24. Why Use __main__?

It helps us:

- Separate reusable code from test code
- Prevent unwanted execution during import
- Make modules reusable
- Organize programs properly

---

# 25. Module Search Path

When Python imports a module, it searches specific locations.

We can view the search path using:

```python
import sys

print(sys.path)
```

`sys.path` contains directories where Python looks for modules.

---

# 26. External Packages

Python also has packages developed by other programmers.

Examples:

```text
requests
numpy
pandas
matplotlib
flask
django
```

These are not all part of Python's standard library.

They usually need to be installed separately.

---

# 27. What is pip?

`pip` is Python's package installer.

It is used to install and manage Python packages.

Example:

```bash
pip install requests
```

---

# 28. Installing a Package

Example:

```bash
pip install numpy
```

After installation:

```python
import numpy

print(numpy.__version__)
```

---

# 29. Updating a Package

```bash
pip install --upgrade requests
```

---

# 30. Uninstalling a Package

```bash
pip uninstall requests
```

---

# 31. Checking Installed Packages

```bash
pip list
```

This displays installed Python packages.

---

# 32. requirements.txt

A `requirements.txt` file stores project dependencies.

Example:

```text
requests
numpy
pandas
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

This is useful when sharing a project with others.

---

# 33. Module vs Package

| Module | Package |
|---|---|
| Usually a `.py` file | Usually a directory |
| Contains code | Contains related modules |
| Smaller unit | Larger organizational unit |
| Example: `math_utils.py` | Example: `student/` |

---

# 34. Standard Library vs External Package

## Standard Library

Comes with Python.

Examples:

```text
math
random
datetime
os
sys
json
```

Usually no separate installation is required.

---

## External Package

Usually installed separately.

Examples:

```text
numpy
pandas
requests
flask
django
```

Installation:

```bash
pip install package_name
```

---

# 35. Module Aliasing

Aliasing means giving a module another name.

Example:

```python
import datetime as dt

print(dt.datetime.now())
```

Here:

```text
datetime → dt
```

---

# 36. Importing Specific Functions

Instead of:

```python
import math

print(math.sqrt(25))
```

We can use:

```python
from math import sqrt

print(sqrt(25))
```

---

# 37. Import Everything

It is possible to write:

```python
from math import *
```

However, this is generally discouraged because it can make code harder to understand and can cause name conflicts.

Prefer:

```python
import math
```

or:

```python
from math import sqrt
```

---

# 38. Module Reusability

One of the biggest advantages of modules is reusability.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

This function can be reused in many programs.

---

# 39. Code Organization

Without modules:

```text
main.py
→ Everything in one file
```

With modules:

```text
project/
│
├── main.py
├── calculator.py
├── database.py
├── utilities.py
└── authentication.py
```

This makes the project easier to maintain.

---

# 40. Practical Example

Suppose we are building a Student Management System.

Instead of putting everything in one file:

```text
student_system.py
```

we can organize it:

```text
student_system/
│
├── main.py
├── student.py
├── file_handler.py
├── utils.py
│
└── data/
    └── students.json
```

Each module has a specific responsibility.

---

# 41. Module Responsibilities

### main.py

Controls the main program.

### student.py

Contains student-related classes and functions.

### file_handler.py

Handles file operations.

### utils.py

Contains reusable utility functions.

---

# 42. Benefits of Good Module Structure

Good module structure provides:

- Better readability
- Easy debugging
- Code reuse
- Easy testing
- Better collaboration
- Easier maintenance
- Scalability

---

# 43. Common Import Errors

## ModuleNotFoundError

Occurs when Python cannot find the requested module.

Example:

```python
import unknown_module
```

---

## ImportError

Can occur when an imported name cannot be found in a module.

Example:

```python
from math import unknown_function
```

---

# 44. Circular Import

A circular import occurs when two modules depend on each other.

Example:

```text
module_a → imports module_b

module_b → imports module_a
```

Circular imports can create errors and should generally be avoided through better project organization.

---

# 45. Best Practices

### 1. Use meaningful module names

Good:

```text
calculator.py
database.py
student.py
```

Avoid unclear names such as:

```text
abc.py
xyz.py
test123.py
```

for production code.

---

### 2. Keep modules focused

A module should generally have a clear responsibility.

---

### 3. Avoid unnecessary imports

Only import what your program needs.

---

### 4. Avoid wildcard imports

Avoid:

```python
from module import *
```

Prefer:

```python
from module import function
```

---

### 5. Use virtual environments

For projects with external packages, use a virtual environment.

Example:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 46. Virtual Environment

A virtual environment creates an isolated Python environment for a project.

Benefits:

- Avoid package conflicts
- Keep project dependencies separate
- Easier project management
- Reproducible environments

---

# 47. Complete Import Example

```python
import math
import random
import datetime
import os
import sys

print(math.sqrt(16))

print(random.randint(1, 10))

print(datetime.date.today())

print(os.getcwd())

print(sys.version)
```

---

# 48. Important Syntax Revision

## Import Module

```python
import module
```

## Import Specific Function

```python
from module import function
```

## Import Multiple Functions

```python
from module import function1, function2
```

## Alias

```python
import module as alias
```

## Package Import

```python
from package import module
```

---

# 49. Real-World Applications

Modules and packages are used in:

- Web Development
- Artificial Intelligence
- Machine Learning
- Data Science
- Automation
- Game Development
- Backend Development
- Desktop Applications
- API Development
- Database Applications

---

# 50. Key Takeaways

```text
Module
→ A Python file containing reusable code.

Package
→ A collection of related Python modules.

import
→ Imports a module.

from ... import
→ Imports specific items.

as
→ Creates an alias.

pip
→ Installs Python packages.

__name__
→ Special variable containing module identity.

__main__
→ Indicates direct execution of a Python file.

sys.path
→ Shows Python's module search locations.
```

---

# 🔥 Quick Revision

```text
Module
   ↓
Reusable Python File
   ↓
import
   ↓
Use Functions / Classes / Variables
```

```text
Package
   ↓
Collection of Related Modules
   ↓
Better Project Organization
```

```text
pip
   ↓
Install External Packages
   ↓
Use Them in Projects
```

---

# 🎯 Day 13 Learning Goal

By the end of this topic, I should be able to:

- Create a Python module
- Import a module
- Import specific functions
- Create module aliases
- Use built-in modules
- Create packages
- Understand `__init__.py`
- Understand `__name__`
- Use `__main__`
- Install packages using pip
- Use `requirements.txt`
- Organize a Python project into multiple files

---

# 🏆 DAY 13 COMPLETE — NOTES

## Topic:

**Python Modules & Packages**

## Main Concepts:

```text
Modules
Imports
Built-in Modules
Custom Modules
Packages
__init__.py
__name__
__main__
pip
External Packages
Virtual Environments
Project Structure
```

# 🚀 365 DAYS OF GROWTH

## DAY 13 / 365