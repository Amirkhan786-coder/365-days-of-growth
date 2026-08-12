
# 🚀 DAY 18 / 365 — PYTHON EXCEPTION HANDLING

> Continuing my 365 Days of Growth journey 🚀

---

## 📅 Day 18

Today I learned **Python Exception Handling** and built a practical mini project based on error handling and file validation.

I learned how to handle runtime errors using `try`, `except`, `else`, and `finally`, and how to create custom exceptions using `raise`.

---

# 📚 Topics Covered

- Exception Handling
- `try`
- `except`
- `else`
- `finally`
- `raise`
- Custom Exceptions
- `ValueError`
- `TypeError`
- `ZeroDivisionError`
- `IndexError`
- `KeyError`
- `FileNotFoundError`
- `PermissionError`
- `OSError`
- File Handling
- Input Validation
- Exception Propagation
- Multiple Exceptions

---

# 🧠 Key Concepts

## 1. Exception Handling

Exception handling allows a Python program to handle runtime errors without immediately crashing.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")
````

---

## 2. `try`

The `try` block contains code that may generate an exception.

```python
try:
    result = 10 / 2
```

---

## 3. `except`

The `except` block handles an exception.

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 4. `else`

The `else` block executes when no exception occurs.

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Valid number:", number)
```

---

## 5. `finally`

The `finally` block executes whether an exception occurs or not.

```python
try:
    print("Program running.")

finally:
    print("Program completed.")
```

---

## 6. `raise`

The `raise` keyword is used to manually generate an exception.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

## 7. Custom Exception

Python allows us to create our own exceptions.

```python
class InvalidNumberError(Exception):
    pass
```

---

# ⚠️ Important Python Exceptions

| Exception           | Meaning                     |
| ------------------- | --------------------------- |
| `ValueError`        | Invalid value               |
| `TypeError`         | Invalid data type           |
| `ZeroDivisionError` | Division by zero            |
| `IndexError`        | Invalid list index          |
| `KeyError`          | Missing dictionary key      |
| `FileNotFoundError` | File does not exist         |
| `PermissionError`   | Permission denied           |
| `OSError`           | Operating system/file error |

---

# 🧪 Practice Completed

Today I practiced:

* ✅ 30 Exception Handling Questions
* ✅ 30 Separate Python Codes
* ✅ `try` and `except`
* ✅ `else` and `finally`
* ✅ `raise`
* ✅ Custom Exceptions
* ✅ File Handling
* ✅ Input Validation
* ✅ Multiple Exception Handling

---

# 🛠️ Mini Project

## 🛡️ Smart Error Handler & File Validator

The mini project demonstrates practical use of Python Exception Handling.

---

# 🎯 Project Objective

The project is designed to safely handle:

* Invalid user input
* Division by zero
* Invalid numbers
* Missing files
* File permission errors
* File system errors
* Custom validation errors

---

# ✨ Project Features

## 🔢 1. Safe Division

The program performs division while safely handling:

```text
ValueError
ZeroDivisionError
```

---

## 🔍 2. Number Validation

The program validates user-entered numbers.

Negative numbers are handled using a custom exception.

---

## 📁 3. File Validator

The program allows the user to enter a filename and safely read the file.

It handles:

```text
FileNotFoundError
PermissionError
OSError
```

---

## 🧠 4. Custom Exception

The project uses:

```python
class InvalidNumberError(Exception):
    pass
```

This is used to handle invalid number conditions.

---

## 🔄 5. Menu-Based Interface

The project provides a simple menu:

```text
=======================================================
       SMART ERROR HANDLER & FILE VALIDATOR
=======================================================

1. Safe Division
2. Validate Number
3. Read File
4. Exit
```

---

# 📂 Project Structure

```text
Day18/
│
├── README.md
│
├── notes.md
│
├── practice_questions.md
│
├── practice_codes/
│   ├── q1_safe_integer_input.py
│   ├── q2_division_by_zero.py
│   ├── q3_safe_division.py
│   ├── q4_list_index.py
│   ├── q5_dictionary_key.py
│   ├── q6_string_to_integer.py
│   ├── q7_invalid_integer.py
│   ├── q8_type_error.py
│   ├── q9_file_not_found.py
│   ├── q10_finally.py
│   ├── q11_positive_number.py
│   ├── q12_age_validator.py
│   ├── q13_voting_eligibility.py
│   ├── q14_multiple_exceptions.py
│   ├── q15_safe_list_access.py
│   ├── q16_safe_dictionary.py
│   ├── q17_file_reading.py
│   ├── q18_file_writing.py
│   ├── q19_multiple_exception_blocks.py
│   ├── q20_exception_as_e.py
│   ├── q21_calculator.py
│   ├── q22_student_marks.py
│   ├── q23_password_validator.py
│   ├── q24_atm_withdrawal.py
│   ├── q25_temperature_converter.py
│   ├── q26_number_guessing.py
│   ├── q27_menu_program.py
│   ├── q28_safe_file_manager.py
│   ├── q29_user_registration.py
│   └── q30_login_system.py
│
├── interview_questions.md
│
├── mcqs.md
│
└── mini_project/
    ├── main.py
    └── project.md
```

---

# ▶️ How to Run the Mini Project

## Step 1

Open the `mini_project` folder in VS Code.

## Step 2

Open the terminal.

## Step 3

Run:

```bash
python main.py
```

---

# 💻 Sample Output

```text
=======================================================
       SMART ERROR HANDLER & FILE VALIDATOR
=======================================================

1. Safe Division
2. Validate Number
3. Read File
4. Exit

Enter your choice: 1

========== SAFE DIVISION ==========

Enter first number: 100
Enter second number: 5

Division successful.
Result: 20.0

Division operation completed.
```

---

# ❌ Division by Zero Example

```text
Enter your choice: 1

Enter first number: 100
Enter second number: 0

Error: Cannot divide by zero.

Division operation completed.
```

---

# ❌ Invalid Number Example

```text
Enter your choice: 2

Enter a number: abc

Error: Invalid number.

Number validation completed.
```

---

# 📁 File Not Found Example

```text
Enter your choice: 3

Enter filename: unknown.txt

Error: File not found.

File operation completed.
```

---

# 🧠 Exception Handling Flow

```text
User Input
    ↓
try
    ↓
Operation
    ↓
Exception?
   ↙     ↘
 YES      NO
  ↓        ↓
except    else
  ↓        ↓
Handle   Continue
 Error
    ↓
finally
    ↓
Program Continues
```

---

# 🌍 Real-World Applications

Exception handling is useful in:

* Web Applications
* Backend Development
* APIs
* Banking Systems
* Authentication Systems
* File Management
* Database Applications
* Data Processing
* Automation
* Machine Learning Applications
* Cloud Applications

---

# 📈 Future Improvements

The project can be improved by adding:

* Multiple file operations
* File creation
* File writing
* File deletion
* Error logging
* Login system
* Database integration
* GUI interface
* Web interface
* User authentication
* Advanced validation
* Error history

---

# 🎯 Learning Outcomes

After completing Day 18, I learned how to:

* Handle runtime exceptions
* Use `try`
* Use `except`
* Use `else`
* Use `finally`
* Use `raise`
* Create custom exceptions
* Handle file errors
* Validate user input
* Handle multiple exceptions
* Build safer Python applications

---

# 🏆 Day 18 Achievement

```text
Python Exception Handling
          ↓
try / except
          ↓
else / finally
          ↓
raise
          ↓
Custom Exceptions
          ↓
File Handling
          ↓
Input Validation
          ↓
30 Practice Codes
          ↓
30 MCQs
          ↓
30 Interview Questions
          ↓
Mini Project
          ↓
DAY 18 COMPLETED ✅
```

---

# 📊 Day 18 Progress

| Activity            | Status         |
| ------------------- | -------------- |
| Notes               | ✅ Completed    |
| Practice Questions  | ✅ Completed    |
| Practice Codes      | ✅ 30 Completed |
| MCQs                | ✅ 30 Completed |
| Interview Questions | ✅ 30 Completed |
| Mini Project        | ✅ Completed    |
| README              | ✅ Completed    |

---

# 🔥 365 DAYS OF GROWTH

**Day 18 / 365**

```text
██████████░░░░░░░░░░  4.93%
```

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

---

# 🚀 DAY 18 COMPLETED

## 🛡️ Smart Error Handler & File Validator

**18 / 365 — Keep Growing 🚀**

