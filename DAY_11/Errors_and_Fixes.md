# 📄 Day 11 - Errors_and_Fixes.md

# 🛠 Common Errors and Fixes

---

## Error 1

### FileNotFoundError

```python
open("abc.txt","r")
```

### Reason

File does not exist.

### Fix

- Check file name.
- Check file path.
- Create the file first.

---

## Error 2

### FileExistsError

```python
open("data.txt","x")
```

### Reason

The file already exists.

### Fix

Use another filename or use `w` mode.

---

## Error 3

### UnsupportedOperation

```python
file = open("data.txt","r")

file.write("Python")
```

### Reason

Cannot write in read mode.

### Fix

Use `w`, `a`, or `r+` mode.

---

## Error 4

### PermissionError

### Reason

The file is opened by another program or you don't have permission.

### Fix

Close the file in other applications or run with proper permissions.

---

## Error 5

### Forgetting close()

```python
file = open("data.txt","r")
```

### Reason

Resources remain allocated.

### Fix

```python
file.close()
```

or

```python
with open("data.txt","r") as file:
    print(file.read())
```

---

## Error 6

### Incorrect File Path

```python
open("student.txt","r")
```

### Reason

Python cannot locate the file.

### Fix

Use the correct absolute or relative path.

---

## Error 7

### Forgetting seek()

```python
file = open("data.txt","w+")

file.write("Python")

print(file.read())
```

### Reason

The file pointer is at the end.

### Fix

```python
file.seek(0)

print(file.read())
```

---

## Error 8

### CSV Blank Lines (Windows)

### Reason

Extra blank lines appear while writing CSV files.

### Fix

```python
with open("students.csv","w",newline="") as file:
```

Always use `newline=""`.

---

## Error 9

### UnicodeDecodeError

### Reason

Wrong file encoding.

### Fix

```python
with open("data.txt","r",encoding="utf-8") as file:
    print(file.read())
```

---

## Error 10

### NameError

```python
print(file.read())
```

### Reason

The file variable was never created.

### Fix

```python
file = open("data.txt","r")

print(file.read())

file.close()
```

---

# ✅ Best Practices

- Always use `with open()`
- Handle exceptions using `try-except`
- Close files properly
- Use meaningful filenames
- Keep backups of important files
- Validate file paths
- Use UTF-8 encoding when needed
- Use `newline=""` for CSV files