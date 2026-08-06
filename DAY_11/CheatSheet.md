# 📄 Day 11 - CheatSheet.md

# 📚 Python File Handling Cheat Sheet

---

# Open a File

```python
file = open("data.txt", "r")
```

---

# Close a File

```python
file.close()
```

---

# Read Entire File

```python
file = open("data.txt", "r")

print(file.read())

file.close()
```

---

# Read One Line

```python
file = open("data.txt", "r")

print(file.readline())

file.close()
```

---

# Read All Lines

```python
file = open("data.txt", "r")

print(file.readlines())

file.close()
```

---

# Write to File

```python
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

---

# Append Data

```python
file = open("data.txt", "a")

file.write("\nAI Engineer")

file.close()
```

---

# Create New File

```python
file = open("newfile.txt", "x")

file.close()
```

---

# Read & Write

```python
file = open("data.txt", "r+")

print(file.read())

file.write("Python")

file.close()
```

---

# Write & Read

```python
file = open("data.txt", "w+")

file.write("Python")

file.seek(0)

print(file.read())

file.close()
```

---

# Append & Read

```python
file = open("data.txt", "a+")

file.write("\nMachine Learning")

file.seek(0)

print(file.read())

file.close()
```

---

# with Statement

```python
with open("data.txt","r") as file:

    print(file.read())
```

---

# tell()

```python
file = open("data.txt","r")

print(file.tell())

file.close()
```

---

# seek()

```python
file = open("data.txt","r")

file.seek(0)

print(file.read())

file.close()
```

---

# Exception Handling

```python
try:

    file = open("data.txt","r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File Not Found")
```

---

# CSV Write

```python
import csv

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name","Age"])

    writer.writerow(["Amir",20])
```

---

# CSV Read

```python
import csv

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)
```

---

# File Modes

| Mode | Meaning |
|------|---------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| r+ | Read + Write |
| w+ | Write + Read |
| a+ | Append + Read |

---

# Important Methods

- open()
- close()
- read()
- readline()
- readlines()
- write()
- writelines()
- seek()
- tell()

---

# CSV Module

```python
import csv
```

---

# OS Module

```python
import os
```

Useful Functions

```python
os.rename()

os.remove()

os.path.exists()

os.path.getsize()
```

---

# Best Practices

✔ Always use `with open()`

✔ Close files properly

✔ Handle exceptions

✔ Use meaningful filenames

✔ Backup important files

✔ Validate file paths