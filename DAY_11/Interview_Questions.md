# 🎤 Day 11 – Python File Handling Interview Questions & Answers

---

## 1. What is File Handling in Python?

**Answer:**

File Handling is the process of creating, opening, reading, writing, appending, updating, and deleting files using Python. It allows data to be stored permanently.

---

## 2. Why is File Handling important?

**Answer:**

File Handling is important because it:

- Stores data permanently
- Retrieves saved data
- Manages large amounts of information
- Is used in real-world applications like banking, hospitals, and student management systems

---

## 3. What is the syntax of the `open()` function?

**Answer:**

```python
file = open("filename.txt", "mode")
```

Example:

```python
file = open("student.txt", "r")
```

---

## 4. What are the different file modes in Python?

**Answer:**

| Mode | Description |
|------|-------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create New File |
| r+ | Read and Write |
| w+ | Write and Read |
| a+ | Append and Read |

---

## 5. What is the difference between `r` and `w` mode?

**Answer:**

- **r (Read):** Opens an existing file for reading. If the file does not exist, it raises `FileNotFoundError`.
- **w (Write):** Creates a new file or overwrites the existing file.

---

## 6. What is the difference between `w` and `a` mode?

**Answer:**

- **w:** Deletes old content before writing new data.
- **a:** Adds new data at the end without deleting existing content.

---

## 7. What does the `read()` method do?

**Answer:**

The `read()` method reads the entire content of a file.

Example:

```python
file = open("data.txt", "r")
print(file.read())
file.close()
```

---

## 8. What is the difference between `read()`, `readline()`, and `readlines()`?

**Answer:**

- `read()` → Reads the complete file.
- `readline()` → Reads one line at a time.
- `readlines()` → Reads all lines and returns them as a list.

---

## 9. What is the purpose of the `write()` method?

**Answer:**

The `write()` method writes data into a file.

Example:

```python
file = open("data.txt", "w")
file.write("Hello Python")
file.close()
```

---

## 10. What is `writelines()`?

**Answer:**

`writelines()` is used to write multiple lines from a list into a file.

Example:

```python
lines = ["Python\n", "AI\n", "ML\n"]

file = open("data.txt", "w")
file.writelines(lines)
file.close()
```

---

## 11. Why should we close a file?

**Answer:**

Closing a file:

- Saves data properly
- Frees system resources
- Prevents data corruption
- Improves program performance

---

## 12. What is the `with` statement?

**Answer:**

The `with` statement automatically closes the file after completing file operations.

Example:

```python
with open("data.txt", "r") as file:
    print(file.read())
```

---

## 13. Why is `with open()` better than `open()`?

**Answer:**

Advantages:

- Automatically closes the file
- Cleaner code
- Prevents resource leaks
- Safer programming

---

## 14. What is `tell()`?

**Answer:**

`tell()` returns the current position of the file pointer.

Example:

```python
file = open("data.txt", "r")
print(file.tell())
file.close()
```

---

## 15. What is `seek()`?

**Answer:**

`seek()` moves the file pointer to a specific position.

Example:

```python
file = open("data.txt", "r")
file.seek(0)
print(file.read())
file.close()
```

---

## 16. What is `FileNotFoundError`?

**Answer:**

`FileNotFoundError` occurs when Python tries to open a file that does not exist.

Example:

```python
open("abc.txt", "r")
```

---

## 17. How do you handle file-related exceptions?

**Answer:**

Use `try-except`.

Example:

```python
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File Not Found!")
```

---

## 18. What is a CSV file?

**Answer:**

CSV (Comma Separated Values) is a file format used to store tabular data.

Example:

```
Name,Age,City
Amir,20,Meerut
Rahul,21,Delhi
```

---

## 19. Which module is used to work with CSV files?

**Answer:**

The `csv` module.

Example:

```python
import csv
```

---

## 20. How do you write data into a CSV file?

**Answer:**

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Amir", 20])
```

---

## 21. How do you read data from a CSV file?

**Answer:**

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

## 22. Which module is used for file operations like rename and delete?

**Answer:**

The `os` module.

Example:

```python
import os
```

---

## 23. How do you check whether a file exists?

**Answer:**

```python
import os

if os.path.exists("data.txt"):
    print("File Exists")
else:
    print("File Does Not Exist")
```

---

## 24. What are the real-world applications of File Handling?

**Answer:**

- Student Management System
- Banking System
- Hospital Management System
- Library Management
- Inventory Management
- Attendance System
- Log Files
- Report Generation
- AI Dataset Storage

---

## 25. What are the best practices for File Handling?

**Answer:**

- Always use `with open()`
- Close files properly
- Handle exceptions using `try-except`
- Use meaningful file names
- Validate file paths
- Keep backups of important files
- Avoid unnecessary file operations
- Organize files properly

---

# 💡 Interview Tip

In interviews, remember these key points:

- `read()` → Reads the entire file
- `readline()` → Reads one line
- `readlines()` → Reads all lines as a list
- `write()` → Writes data
- `writelines()` → Writes multiple lines
- `with open()` → Automatically closes the file
- `tell()` → Current file pointer position
- `seek()` → Moves the file pointer
- `try-except` → Handles file-related errors
- `csv` module → Used for CSV file operations