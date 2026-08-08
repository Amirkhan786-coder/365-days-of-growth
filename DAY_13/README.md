# 🚀 Day 13 / 365 — Python Modules & Packages

> **365 Days of Growth — Python to AI Engineer Journey**

---

## 📅 Day 13

### 📚 Topic

**Python Modules & Packages**

---

## 🎯 Today's Goal

Today I learned how to organize Python code using:

- Modules
- Packages
- Built-in Modules
- Custom Modules
- `import`
- `from ... import`
- Module Aliases
- `__name__`
- `__main__`
- pip
- `requirements.txt`
- Virtual Environments

---

# 📖 Topics Covered

## 1. Python Module

A module is a Python file containing reusable code.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

---

## 2. Importing a Module

```python
import math

print(math.sqrt(25))
```

---

## 3. Import Specific Functions

```python
from math import sqrt

print(sqrt(36))
```

---

## 4. Module Alias

```python
import math as m

print(m.sqrt(49))
```

---

## 5. Built-in Modules

Practiced:

```text
math
random
datetime
os
sys
json
```

---

## 6. Custom Modules

Created my own Python modules and imported them into another Python file.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

```python
# main.py

import calculator

print(calculator.add(10, 5))
```

---

## 7. Python Packages

Learned how packages organize multiple related modules.

Example:

```text
student/
│
├── __init__.py
├── details.py
└── marks.py
```

---

## 8. `__name__`

Learned that Python provides the special variable:

```python
__name__
```

When a file is executed directly:

```python
__name__ == "__main__"
```

---

## 9. `if __name__ == "__main__"`

Example:

```python
def main():
    print("Program Started")


if __name__ == "__main__":
    main()
```

---

## 10. pip

`pip` is Python's package installer.

Example:

```bash
pip install numpy
```

---

## 11. requirements.txt

Used to store project dependencies.

Example:

```text
numpy
pandas
requests
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 12. Virtual Environment

Created to isolate project dependencies.

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 💻 Practice

Completed **35 practice questions** covering:

- Modules
- Imports
- Built-in modules
- Custom modules
- Packages
- `__name__`
- `__main__`
- pip
- `requirements.txt`
- Virtual environments

---

# 📝 MCQs

Completed:

**35 MCQs**

Topics included:

- Module
- Package
- Import
- Standard library
- External packages
- pip
- `__name__`
- `__main__`
- `sys.path`

---

# 💼 Interview Preparation

Completed:

**35 Interview Questions**

Important interview concepts:

```text
Module vs Package
import vs from import
Built-in vs External packages
__name__
__main__
pip
requirements.txt
sys.path
Virtual Environment
Circular Import
ModuleNotFoundError
ImportError
```

---

# 🚀 Mini Project

## Student Information System

Built a basic project using modules and packages.

### Concept Used

```text
Python Modules
       ↓
Python Packages
       ↓
Code Organization
       ↓
Code Reusability
```

---

# 📂 Day 13 Structure

```text
Day13/
│
├── notes.md
├── practice.md
├── mcqs.md
├── interview_questions.md
├── reflection.md
├── README.md
│
└── mini_project/
    ├── main.py
    ├── student.py
    └── marks.py
```

---

# 🧠 Key Learnings

Today I learned that professional Python projects should not put everything into one file.

Instead:

```text
Large Project
     ↓
Packages
     ↓
Modules
     ↓
Functions / Classes
     ↓
Reusable Code
```

This makes projects:

- Easier to understand
- Easier to debug
- Easier to test
- Easier to maintain
- Easier to scale

---

# 🏆 Day 13 Achievement

| Task | Status |
|---|---|
| Notes | ✅ |
| Practice | ✅ |
| MCQs | ✅ |
| Interview Questions | ✅ |
| Mini Project | ✅ |
| Reflection | ✅ |
| README | ✅ |

---

# 📊 Progress

```text
Day 01 → █
Day 02 → ██
Day 03 → ███
...
Day 13 → █████████████
```

### Progress: **13 / 365 Days**

---

# 💡 Today's Lesson

> **Write code once, organize it properly, and reuse it whenever possible.**

---

# 🎯 Tomorrow's Goal

Continue the Python journey with the next topic and keep improving:

```text
Learning
   ↓
Practice
   ↓
Projects
   ↓
GitHub
   ↓
Consistency
```

---

# 🚀 365 DAYS OF GROWTH

**Day 13 Completed ✅**

**Python → AI Engineer Journey**

**Keep Learning. Keep Building. Keep Growing.**