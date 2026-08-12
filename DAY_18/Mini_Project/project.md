
# 🚀 DAY 18 / 365 — MINI PROJECT
# 🛡️ SMART ERROR HANDLER & FILE VALIDATOR

> Continuing my 365 Days of Growth journey 🚀

---

## 📅 Day 18

Today I built a Python mini project to practice **Exception Handling**.

The project demonstrates how Python programs can safely handle invalid input, file errors, division errors, and custom exceptions without crashing.

---

# 🎯 Project Objective

The main objective of this project is to build a simple **Smart Error Handler & File Validator** that can:

- Validate user input
- Perform safe division
- Read files safely
- Handle missing files
- Validate numbers
- Handle multiple exceptions
- Use custom exceptions
- Display meaningful error messages

---

# ✨ Features

## 🔢 1. Safe Number Input

The program asks the user to enter a number.

If the user enters invalid data, the program handles the `ValueError`.

---

## ➗ 2. Safe Division

The program performs division between two numbers.

If the second number is zero, the program catches `ZeroDivisionError`.

---

## 📁 3. File Validation

The user can enter a filename.

The program checks whether the file exists before reading it.

If the file does not exist, `FileNotFoundError` is handled.

---

## 📝 4. File Reading

If the file exists, the program reads and displays its content.

---

## 🔐 5. Custom Exception

The project contains a custom exception called:

```text
InvalidNumberError
````

This exception is raised when an invalid number is entered.

---

## 🧠 6. Multiple Exception Handling

The project handles different exceptions separately.

Examples:

```text
ValueError
ZeroDivisionError
FileNotFoundError
PermissionError
OSError
InvalidNumberError
```

---

## 🔄 7. Finally Block

The project uses `finally` to display a completion message regardless of whether an error occurs.

---

# 🧠 Concepts Used

```text
try
except
else
finally
raise
Custom Exceptions
ValueError
TypeError
ZeroDivisionError
FileNotFoundError
PermissionError
OSError
File Handling
Input Validation
```

---

# 🛠️ Technologies Used

```text
Python
Exception Handling
File Handling
Custom Exceptions
```

---

# 📂 Project Structure

```text
Day18-Mini-Project/
│
├── main.py
└── project.md
```

---

# ▶️ How to Run

## Step 1

Open the project folder in VS Code.

## Step 2

Open the terminal.

## Step 3

Run:

```bash
python main.py
```

---

# 💻 Main Program

The complete program is available in:

```text
main.py
```

The program provides a menu-based interface.

---

# 📋 Program Menu

```text
==================================================
       SMART ERROR HANDLER & FILE VALIDATOR
==================================================

1. Safe Division
2. Validate Number
3. Read File
4. Exit

Enter your choice:
```

---

# 🧪 Feature 1 — Safe Division

Example:

```text
Enter your choice: 1

Enter first number: 100
Enter second number: 5

Result: 20.0
```

If zero is entered:

```text
Enter first number: 100
Enter second number: 0

Error: Cannot divide by zero.
```

---

# 🧪 Feature 2 — Number Validation

Example:

```text
Enter your choice: 2

Enter number: 50

Valid number: 50
```

Invalid input:

```text
Enter your choice: 2

Enter number: abc

Error: Please enter a valid number.
```

---

# 🧪 Feature 3 — File Validation

Example:

```text
Enter your choice: 3

Enter filename: data.txt

File found successfully.

File Content:
Python is easy to learn.
```

If the file does not exist:

```text
Enter filename: unknown.txt

Error: File not found.
```

---

# 🧪 Feature 4 — Exit

```text
Enter your choice: 4

Thank you for using Smart Error Handler!
```

---

# 🧠 Exception Handling Flow

```text
User Input
     ↓
Try Block
     ↓
Operation
     ↓
Exception?
   ↙     ↘
 YES      NO
 ↓         ↓
Except    Else
 ↓         ↓
Handle   Continue
Error
     ↓
 Finally
     ↓
 Program Continues
```

---

# 🌍 Real-World Applications

Exception handling is widely used in:

* Web applications
* Backend systems
* APIs
* Banking applications
* Authentication systems
* File management systems
* Database applications
* Data processing
* Automation
* Machine Learning applications
* Cloud applications

---

# 📈 Future Improvements

This project can be improved by adding:

* Multiple file operations
* File creation
* File deletion
* File writing
* Logging system
* Error log file
* User authentication
* Database integration
* GUI interface
* Web interface
* Password validation
* Advanced input validation

---

# 🎯 Learning Outcomes

After completing this project, I learned how to:

* Handle runtime errors
* Use `try`
* Use `except`
* Use `else`
* Use `finally`
* Use `raise`
* Create custom exceptions
* Handle file errors
* Validate user input
* Prevent program crashes
* Write safer Python programs

---

# 🏆 Project Achievement

```text
Exception Handling
        ↓
Input Validation
        ↓
Safe Division
        ↓
File Validation
        ↓
Custom Exceptions
        ↓
Multiple Exception Handling
        ↓
Real-World Application
        ↓
Mini Project Completed ✅
```

---

# 💡 Key Learning

Exception handling makes Python programs more reliable and user-friendly.

Instead of allowing a program to crash when something unexpected happens, we can catch the problem and provide a meaningful message to the user.

---

# 📊 Project Status

| Feature             | Status      |
| ------------------- | ----------- |
| Safe Input          | ✅ Completed |
| Safe Division       | ✅ Completed |
| File Validation     | ✅ Completed |
| File Reading        | ✅ Completed |
| Custom Exception    | ✅ Completed |
| Multiple Exceptions | ✅ Completed |
| Finally Block       | ✅ Completed |
| Error Handling      | ✅ Completed |

---

# 🔥 365 DAYS OF GROWTH

**Day 18 / 365**

```text
Learn
  ↓
Practice
  ↓
Code
  ↓
Build
  ↓
Improve
```

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

**18 / 365 — Keep Growing 🚀**

---

# ✅ MINI PROJECT COMPLETED

```text
🛡️ SMART ERROR HANDLER
        +
📁 FILE VALIDATOR
        +
⚠️ EXCEPTION HANDLING
        =
🚀 DAY 18 PROJECT
