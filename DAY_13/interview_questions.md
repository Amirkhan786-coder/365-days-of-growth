# 💼 Day 13 — Python Modules & Packages
# Interview Questions with Answers

# 365 Days of Growth

---

## Q1. What is a module in Python?

### Answer:

A module is a Python file containing reusable code such as functions, variables, classes, and statements.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

---

## Q2. Why are modules used in Python?

### Answer:

Modules are used to:

- Reuse code
- Organize large programs
- Avoid duplicate code
- Improve readability
- Make maintenance easier
- Divide a large project into smaller components

---

## Q3. What is the difference between a module and a package?

### Answer:

A **module** is generally a single Python file.

Example:

```text
calculator.py
```

A **package** is a directory containing related Python modules.

Example:

```text
calculator/
├── __init__.py
├── basic.py
└── advanced.py
```

---

## Q4. How do you import a module in Python?

### Answer:

Use the `import` keyword.

```python
import math

print(math.sqrt(25))
```

---

## Q5. What is the difference between `import module` and `from module import function`?

### Answer:

With:

```python
import math
```

we access functions using the module name:

```python
math.sqrt(25)
```

With:

```python
from math import sqrt
```

we can directly use:

```python
sqrt(25)
```

---

## Q6. What is module aliasing?

### Answer:

Module aliasing means giving an imported module another name using `as`.

Example:

```python
import math as m

print(m.sqrt(25))
```

Here `m` is an alias for `math`.

---

## Q7. What is the purpose of `from ... import`?

### Answer:

It allows us to import specific functions, classes, or variables from a module.

Example:

```python
from math import sqrt

print(sqrt(36))
```

---

## Q8. Can we import multiple functions from a module?

### Answer:

Yes.

Example:

```python
from math import sqrt, factorial

print(sqrt(25))
print(factorial(5))
```

---

## Q9. What is a built-in or standard library module?

### Answer:

A standard library module is a module provided with Python.

Examples:

```text
math
random
datetime
os
sys
json
csv
```

These normally do not require separate installation.

---

## Q10. What is the `math` module?

### Answer:

The `math` module provides mathematical functions and constants.

Example:

```python
import math

print(math.sqrt(25))
print(math.pi)
```

---

## Q11. What is the `random` module?

### Answer:

The `random` module is used for generating pseudo-random values and making random selections.

Example:

```python
import random

print(random.randint(1, 10))
```

---

## Q12. What is the `datetime` module?

### Answer:

The `datetime` module is used for working with dates and times.

Example:

```python
import datetime

print(datetime.datetime.now())
```

---

## Q13. What is the `os` module?

### Answer:

The `os` module provides functions for interacting with the operating system.

Examples:

```python
import os

print(os.getcwd())
print(os.listdir())
```

---

## Q14. What is the `sys` module?

### Answer:

The `sys` module provides access to Python interpreter and system-specific functionality.

Example:

```python
import sys

print(sys.version)
```

---

## Q15. What is `sys.path`?

### Answer:

`sys.path` is a list containing locations where Python searches for modules.

Example:

```python
import sys

print(sys.path)
```

---

## Q16. What is `__name__` in Python?

### Answer:

`__name__` is a special built-in variable that identifies the current module.

When a file is executed directly:

```python
__name__ == "__main__"
```

When imported, it normally contains the module's name.

---

## Q17. Why do we use `if __name__ == "__main__":`?

### Answer:

It is used to ensure that certain code runs only when the file is executed directly.

Example:

```python
def main():
    print("Program started")


if __name__ == "__main__":
    main()
```

This prevents the `main()` call from running automatically when the module is imported.

---

## Q18. What is a custom module?

### Answer:

A custom module is a Python module created by the programmer.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

It can then be imported:

```python
import calculator
```

---

## Q19. How do you create your own module?

### Answer:

Create a `.py` file and put reusable code inside it.

Example:

```python
# greetings.py

def greet(name):
    print("Hello,", name)
```

Then:

```python
import greetings

greetings.greet("Amir")
```

---

## Q20. What is `__init__.py`?

### Answer:

`__init__.py` is commonly used inside Python packages.

Example:

```text
student/
├── __init__.py
├── details.py
└── marks.py
```

It can contain package initialization code or be empty.

---

## Q21. What is pip?

### Answer:

`pip` is Python's package installer.

It is used to install, upgrade, and uninstall Python packages.

Example:

```bash
pip install requests
```

---

## Q22. How do you install a Python package?

### Answer:

Use:

```bash
pip install package_name
```

Example:

```bash
pip install numpy
```

---

## Q23. How do you uninstall a Python package?

### Answer:

Use:

```bash
pip uninstall package_name
```

Example:

```bash
pip uninstall numpy
```

---

## Q24. How do you see installed packages?

### Answer:

Use:

```bash
pip list
```

It displays packages installed in the current Python environment.

---

## Q25. What is `requirements.txt`?

### Answer:

`requirements.txt` is a file containing the dependencies required by a Python project.

Example:

```text
numpy
pandas
requests
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## Q26. What is the difference between standard and external packages?

### Answer:

### Standard Library

Comes with Python.

Examples:

```text
math
random
os
sys
datetime
```

### External Packages

Usually installed separately.

Examples:

```text
numpy
pandas
requests
flask
```

---

## Q27. What is a wildcard import?

### Answer:

A wildcard import imports all names from a module.

Example:

```python
from math import *
```

However, it is generally discouraged because it can make code harder to understand and may cause name conflicts.

Prefer:

```python
import math
```

or:

```python
from math import sqrt
```

---

## Q28. Can a module contain classes and variables?

### Answer:

Yes.

A module can contain:

- Functions
- Classes
- Variables
- Constants
- Statements

Example:

```python
# student.py

name = "Amir"


class Student:
    pass


def greet():
    print("Hello")
```

---

## Q29. What is module reusability?

### Answer:

Module reusability means writing code once in a module and using it in multiple programs.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

This function can be imported into many programs.

---

## Q30. What is a circular import?

### Answer:

A circular import occurs when two modules directly or indirectly import each other.

Example:

```text
module_a
   ↓
module_b
   ↓
module_a
```

Circular imports can cause errors or complicated dependencies and should generally be avoided through better project design.

---

## Q31. What is a virtual environment?

### Answer:

A virtual environment is an isolated Python environment for a project.

It helps keep project dependencies separate.

Create one using:

```bash
python -m venv venv
```

On Windows PowerShell, activate it with:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Q32. Why are virtual environments useful?

### Answer:

Virtual environments help:

- Avoid package conflicts
- Separate project dependencies
- Maintain different package versions
- Keep projects organized
- Make projects easier to reproduce

---

## Q33. What happens if Python cannot find an imported module?

### Answer:

Python generally raises:

```text
ModuleNotFoundError
```

Example:

```python
import unknown_module
```

This can happen if the module is not installed or cannot be found in the module search path.

---

## Q34. What is the difference between `ModuleNotFoundError` and `ImportError`?

### Answer:

`ModuleNotFoundError` is raised when Python cannot find the requested module.

Example:

```python
import unknown_module
```

`ImportError` can occur when a module exists but the requested item cannot be imported.

Example:

```python
from math import unknown_function
```

---

## Q35. Why are modules and packages important in real-world projects?

### Answer:

Modules and packages help developers build large applications in an organized way.

They provide:

- Code reusability
- Better organization
- Easier debugging
- Easier testing
- Better collaboration
- Easier maintenance
- Scalability

Example project:

```text
AI_Project/
│
├── main.py
├── model.py
├── database.py
├── utils.py
├── config.py
│
└── services/
    ├── __init__.py
    ├── api.py
    └── authentication.py
```

This structure is much easier to maintain than putting the entire application into one huge file.

---

# 🔥 QUICK INTERVIEW REVISION

```text
Module
→ A Python file containing reusable code.

Package
→ A directory containing related modules.

import
→ Imports a module.

from ... import
→ Imports specific items.

as
→ Creates an alias.

math
→ Mathematical operations.

random
→ Random values and selections.

datetime
→ Date and time operations.

os
→ Operating system interaction.

sys
→ Python/system information.

__name__
→ Special module variable.

__main__
→ Indicates direct execution.

pip
→ Python package installer.

requirements.txt
→ Stores project dependencies.

sys.path
→ Module search locations.

Virtual Environment
→ Isolated Python environment.
```

# 🏆 DAY 13 INTERVIEW PREPARATION COMPLETE

**Total Questions:** 35

**Topic:** Python Modules & Packages

**Status:** ✅ Completed

# 🚀 DAY 13 / 365