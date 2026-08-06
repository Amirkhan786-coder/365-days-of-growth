# 📚 Day 11 - Notes (Python File Handling)

# What is File Handling?

File Handling is the process of **creating, reading, writing, updating, appending, and deleting files** using Python.

Instead of storing data temporarily in variables, File Handling allows us to store data permanently inside files.

### Examples

- Student Records
- Employee Details
- Login Credentials
- Chat Messages
- Bank Transactions

All these applications use File Handling.

---

# Why Do We Need File Handling?

Without File Handling:

- Data is lost after the program ends.
- No permanent storage.
- Cannot reuse data.

With File Handling:

- Permanent Storage
- Easy Data Management
- Data Sharing
- Real-world Applications

---

# Advantages of File Handling

- Permanent Data Storage
- Easy Data Retrieval
- Data Backup
- Data Sharing
- Large Data Storage
- Used in Real Projects

---

# Types of Files

There are mainly two types of files.

## 1. Text File (.txt)

Stores readable text.

Example

```
Amir Khan
Python
AI Engineer
```

---

## 2. Binary File (.bin)

Stores images, videos, PDFs, audio, etc.

Examples

- Image
- PDF
- MP3
- MP4

---

# Opening a File

Python uses the **open()** function.

### Syntax

```python
file = open("filename.txt", "mode")
```

### Example

```python
file = open("data.txt", "r")
```

---

# Syntax of open()

```python
open(file_name, mode)
```

### Example

```python
f = open("student.txt", "r")
```

Where

- `file_name` → Name of the file
- `mode` → Operation to perform

---

# File Modes

Python provides different modes to open files.

## Read Mode (r)

Reads the file only.

```python
file = open("data.txt", "r")
```

If the file doesn't exist:

```
FileNotFoundError
```

---

## Write Mode (w)

Creates a new file.

If the file already exists, old data is deleted.

```python
file = open("data.txt", "w")
```

---

## Append Mode (a)

Adds data at the end of the file.

Existing data remains safe.

```python
file = open("data.txt", "a")
```

---

## Create Mode (x)

Creates a new file only.

If the file already exists:

```
FileExistsError
```

```python
file = open("data.txt", "x")
```

---

## Read + Write (r+)

Reads and writes data.

```python
file = open("data.txt", "r+")
```

---

## Write + Read (w+)

Writes and then reads.

```python
file = open("data.txt", "w+")
```

---

## Append + Read (a+)

Appends data and reads the file.

```python
file = open("data.txt", "a+")
```

---

# Summary of File Modes

| Mode | Purpose |
|------|---------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| r+ | Read + Write |
| w+ | Write + Read |
| a+ | Append + Read |

---

# Closing a File

Always close files after use.

### Syntax

```python
file.close()
```

### Example

```python
file = open("data.txt", "r")

file.close()
```

---

# Why Close Files?

- Saves Memory
- Prevents Data Corruption
- Releases System Resources
- Improves Performance

---

# Real-Life Uses of File Handling

- Student Management System
- Banking System
- Hospital Management System
- Library Management System
- Employee Management System
- Login System
- Attendance System
- AI Dataset Storage

---

# Key Points

- `open()` is used to open a file.
- `close()` is used to close a file.
- `r` = Read
- `w` = Write
- `a` = Append
- `x` = Create
- `r+` = Read + Write
- `w+` = Write + Read
- `a+` = Append + Read
- File Handling stores data permanently.


# 📚 Day 11 - Notes (Part 2)

# Reading Files

Python provides three methods to read data from a file.

- read()
- readline()
- readlines()

---

# 1. read()

The `read()` method reads the entire content of the file.

### Syntax

```python
file.read()
```

### Example

```python
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# 2. readline()

The `readline()` method reads only one line at a time.

### Example

```python
file = open("data.txt", "r")

print(file.readline())
print(file.readline())

file.close()
```

---

# 3. readlines()

The `readlines()` method reads all lines and stores them in a list.

### Example

```python
file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

Output

```python
['Python\n', 'AI\n', 'Machine Learning\n']
```

---

# Writing into a File

The `write()` method writes data into a file.

### Syntax

```python
file.write(data)
```

### Example

```python
file = open("student.txt", "w")

file.write("Amir Khan")

file.close()
```

---

# Writing Multiple Lines

```python
file = open("student.txt", "w")

file.write("Python\n")
file.write("AI\n")
file.write("Machine Learning\n")

file.close()
```

---

# writelines()

The `writelines()` method writes multiple lines from a list.

### Example

```python
file = open("student.txt", "w")

data = [
    "Python\n",
    "AI\n",
    "Machine Learning\n"
]

file.writelines(data)

file.close()
```

---

# Appending Data

Append means adding data at the end of an existing file.

### Example

```python
file = open("student.txt", "a")

file.write("\nData Science")

file.close()
```

---

# Using with Statement

The `with` statement automatically closes the file after use.

### Syntax

```python
with open("file.txt", "mode") as file:
    # File operations
```

### Example

```python
with open("student.txt", "r") as file:

    print(file.read())
```

Advantages

- No need to call `close()`
- Cleaner code
- Safer programming
- Automatic resource management

---

# File Pointer

A file pointer indicates the current position inside a file.

Python provides two functions:

- tell()
- seek()

---

# tell()

Returns the current cursor position.

### Example

```python
file = open("student.txt", "r")

print(file.tell())

file.read(5)

print(file.tell())

file.close()
```

---

# seek()

Moves the cursor to a specific position.

### Example

```python
file = open("student.txt", "r")

file.seek(0)

print(file.read())

file.close()
```

---

# Exception Handling with Files

Sometimes a file does not exist.

Instead of crashing the program, we use `try` and `except`.

### Example

```python
try:

    file = open("student.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File Not Found!")
```

---

# Working with CSV Files

CSV stands for **Comma Separated Values**.

Example

```
Name,Age,City
Amir,20,Meerut
Rahul,21,Delhi
```

### Reading CSV

```python
import csv

with open("student.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

# Writing CSV

```python
import csv

with open("student.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Amir", 20, "Meerut"])
```

---

# Best Practices

- Always use `with open()`
- Close files properly
- Handle exceptions
- Use meaningful file names
- Keep backup of important files
- Validate file paths
- Avoid unnecessary file opening

---

# Real-Life Applications

- Attendance System
- Student Management System
- Hospital Management
- Banking Software
- Inventory Management
- Billing Software
- AI Dataset Storage
- Chat Applications
- Log Files
- Report Generation

---

# Key Points

- `read()` → Reads entire file
- `readline()` → Reads one line
- `readlines()` → Reads all lines into a list
- `write()` → Writes data
- `writelines()` → Writes multiple lines
- `append()` → Adds data at the end
- `with` → Automatically closes the file
- `tell()` → Current cursor position
- `seek()` → Moves cursor
- `try-except` → Handles file errors
- `csv` → Read and write CSV files