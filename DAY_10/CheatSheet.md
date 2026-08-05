# 🚀 Day 10 - Python Modules & Packages Cheat Sheet

---

# 📌 Import a Module

```python
import math
```

---

# 📌 Import Multiple Modules

```python
import math
import random
import os
```

OR

```python
import math, random, os
```

---

# 📌 Module Alias

```python
import math as m

print(m.sqrt(25))
```

---

# 📌 Import Specific Function

```python
from math import sqrt

print(sqrt(81))
```

---

# 📌 Import Multiple Functions

```python
from math import sqrt, factorial
```

---

# 📌 Import Everything

```python
from math import *
```

---

# 📌 math Module

```python
import math

print(math.sqrt(64))
print(math.factorial(5))
print(math.pi)
print(math.ceil(2.3))
print(math.floor(2.9))
```

---

# 📌 random Module

```python
import random

print(random.randint(1,100))
print(random.choice(["A","B","C"]))
```

---

# 📌 datetime Module

```python
import datetime

print(datetime.datetime.now())
print(datetime.date.today())
```

---

# 📌 os Module

```python
import os

print(os.getcwd())
print(os.listdir())
```

---

# 📌 statistics Module

```python
import statistics

data = [10,20,30,40]

print(statistics.mean(data))
print(statistics.median(data))
```

---

# 📌 string Module

```python
import string

print(string.ascii_uppercase)
print(string.ascii_lowercase)
```

---

# 📌 calendar Module

```python
import calendar

print(calendar.month(2026,8))
```

---

# 📌 time Module

```python
import time

print(time.time())

time.sleep(2)
```

---

# 📌 sys Module

```python
import sys

print(sys.path)
```

---

# 📌 dir()

```python
import math

print(dir(math))
```

---

# 📌 User Defined Module

calculator.py

```python
def add(a,b):
    return a+b
```

main.py

```python
import calculator

print(calculator.add(10,20))
```

---

# 📌 Package Structure

```
MyPackage/

│── __init__.py
│── add.py
│── sub.py
```

---

# 📌 __name__

```python
if __name__ == "__main__":
    print("Running Directly")
```

---

# 🎯 Remember

✅ Modules = Reusable Code

✅ Package = Collection of Modules

✅ import = Use Module

✅ as = Alias

✅ from = Import Specific Function

✅ __name__ = Current Module Name

✅ __main__ = Direct Execution