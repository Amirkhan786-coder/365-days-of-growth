# 🛠 Day 10 - Common Errors and Fixes

---

## Error 1

### ModuleNotFoundError

```python
import calculator
```

### Reason

The module file does not exist or is in another folder.

### Fix

Place `calculator.py` in the same directory as `main.py`.

---

## Error 2

### ImportError

```python
from math import square
```

### Reason

The function does not exist.

### Fix

```python
from math import sqrt
```

---

## Error 3

### NameError

```python
sqrt(25)
```

### Reason

The function was used without importing it.

### Fix

```python
from math import sqrt

print(sqrt(25))
```

---

## Error 4

### AttributeError

```python
import math

print(math.square(5))
```

### Reason

The `math` module has no `square()` function.

### Fix

```python
print(5 ** 2)
```

or

```python
print(math.pow(5,2))
```

---

## Error 5

### ModuleNotFoundError

```python
import randoms
```

### Reason

Incorrect module name.

### Fix

```python
import random
```

---

## Error 6

### FileNotFoundError

```python
os.chdir("D:/Python")
```

### Reason

Folder does not exist.

### Fix

Use a valid folder path.

---

## Error 7

### Forgetting Alias

```python
import math as m

print(math.sqrt(25))
```

### Reason

Imported with alias but used original name.

### Fix

```python
import math as m

print(m.sqrt(25))
```

---

## Error 8

### Circular Import

### Reason

Two modules import each other.

Example

```
A.py → imports B.py

B.py → imports A.py
```

### Fix

Restructure the project or move shared code into a separate module.

---

## 🎯 Best Practices

- Use meaningful module names.
- Keep one purpose per module.
- Avoid `from module import *`.
- Use aliases only when needed.
- Organize related modules into packages.
- Write reusable code.
- Add comments and documentation.