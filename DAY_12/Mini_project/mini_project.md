# 🚀 Day 12 — Mini Project

# 🛡️ Safe Calculator Using Exception Handling

## 365 Days of Growth

---

# 📌 Project Name

**Safe Calculator**

---

# 🎯 Project Objective

The objective of this mini project is to create a calculator that can safely perform mathematical operations while handling invalid user input and runtime errors.

The calculator will handle:

- Addition
- Subtraction
- Multiplication
- Division
- Invalid input
- Division by zero
- Invalid menu choice

This project demonstrates the practical use of Python Exception Handling.

---

# 🧠 Concepts Used

This project uses:

- `try`
- `except`
- `else`
- `finally`
- `raise`
- Functions
- Loops
- Conditional Statements
- User Input
- Exception Handling

---

# 📂 Project Structure

```text
Day-12/
│
├── notes.md
├── practice.md
├── interview_questions.md
├── mcqs.md
├── reflection.md
├── README.md
│
└── mini_project/
    │
    ├── mini_project.md
    └── safe_calculator.py
```

---

# 💻 Complete Project Code

Create a file named:

```text
safe_calculator.py
```

Then paste the following code:

```python
# ============================================
# Day 12 Mini Project
# Safe Calculator
# Python Exception Handling
# ============================================


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        raise ZeroDivisionError(
            "Cannot divide by zero."
        )

    return a / b


while True:

    print("\n================================")
    print("       SAFE CALCULATOR")
    print("================================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:

        choice = int(
            input("Enter your choice: ")
        )

        if choice == 5:

            print("\nCalculator closed.")
            print("Thank you for using Safe Calculator!")
            break

        if choice not in [1, 2, 3, 4]:

            raise ValueError(
                "Invalid choice. Select 1 to 5."
            )

        num1 = float(
            input("Enter first number: ")
        )

        num2 = float(
            input("Enter second number: ")
        )

        if choice == 1:

            result = add(num1, num2)

        elif choice == 2:

            result = subtract(num1, num2)

        elif choice == 3:

            result = multiply(num1, num2)

        elif choice == 4:

            result = divide(num1, num2)

        else:

            raise ValueError(
                "Invalid operation."
            )

    except ValueError as e:

        print("\nInput Error:", e)

    except ZeroDivisionError as e:

        print("\nCalculation Error:", e)

    except Exception as e:

        print("\nUnexpected Error:", e)

    else:

        print("\n--------------------------------")
        print("Result:", result)
        print("--------------------------------")

    finally:

        print("\nOperation completed.")
```

---

# ▶️ How to Run

Open the terminal inside the `mini_project` folder.

Run:

```bash
python safe_calculator.py
```

---

# 🖥️ Sample Output

```text
================================
       SAFE CALCULATOR
================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice: 1
Enter first number: 20
Enter second number: 10

--------------------------------
Result: 30.0
--------------------------------

Operation completed.
```

---

# 🧪 Testing Division by Zero

Input:

```text
Enter your choice: 4
Enter first number: 20
Enter second number: 0
```

Output:

```text
Calculation Error: Cannot divide by zero.

Operation completed.
```

The program does not crash.

---

# 🧪 Testing Invalid Input

Input:

```text
Enter your choice: abc
```

Output:

```text
Input Error: invalid literal for int() with base 10: 'abc'

Operation completed.
```

The exception is handled using:

```python
except ValueError as e:
```

---

# 🧪 Testing Invalid Menu Choice

Input:

```text
Enter your choice: 10
```

Output:

```text
Input Error: Invalid choice. Select 1 to 5.

Operation completed.
```

---

# 🧠 How Exception Handling Works in This Project

## try

The risky calculator operations are placed inside `try`.

```python
try:
    choice = int(input("Enter your choice: "))
```

---

## except

Different errors are handled separately.

```python
except ValueError as e:
    print("Input Error:", e)
```

and:

```python
except ZeroDivisionError as e:
    print("Calculation Error:", e)
```

---

## else

The `else` block runs when no exception occurs.

```python
else:
    print("Result:", result)
```

---

## finally

The `finally` block runs after the operation.

```python
finally:
    print("Operation completed.")
```

---

## raise

The `raise` keyword is used to manually generate an exception.

```python
if choice not in [1, 2, 3, 4]:
    raise ValueError(
        "Invalid choice. Select 1 to 5."
    )
```

---

# 🔍 Project Flow

```text
Start
  ↓
Display Menu
  ↓
Take User Choice
  ↓
Validate Choice
  ↓
Take Two Numbers
  ↓
Perform Operation
  ↓
Exception?
  │
  ├── YES → Handle Error
  │
  └── NO  → Display Result
  ↓
finally
  ↓
Show Operation Completed
  ↓
Return to Menu
  ↓
Exit
```

---

# 🎓 What I Learned From This Project

By building this project, I learned how Exception Handling can be used in a real application.

I learned how to:

- Handle invalid input
- Handle division by zero
- Use multiple `except` blocks
- Use `else`
- Use `finally`
- Use `raise`
- Create reusable functions
- Build a menu-driven application
- Prevent a program from crashing

---

# 🚀 Possible Improvements

This project can be improved by adding:

- Percentage calculation
- Power calculation
- Square root
- Modulus
- History of calculations
- Clear screen option
- GUI using Tkinter
- Calculation history saved to a file

---

# 🏆 Project Completion Checklist

- [x] Created calculator
- [x] Added addition
- [x] Added subtraction
- [x] Added multiplication
- [x] Added division
- [x] Added input validation
- [x] Handled ValueError
- [x] Handled ZeroDivisionError
- [x] Used try
- [x] Used except
- [x] Used else
- [x] Used finally
- [x] Used raise
- [x] Tested the project

---

# 📸 GitHub Upload

Upload these files to your Day 12 folder:

```text
Day-12/
│
├── notes.md
├── practice.md
├── interview_questions.md
├── mcqs.md
├── reflection.md
├── README.md
│
└── mini_project/
    ├── mini_project.md
    └── safe_calculator.py
```

---

# 💡 Project Learning

> Exception Handling turns unexpected errors into manageable situations.

---

# 🏁 Day 12 Mini Project Complete

**Project:** Safe Calculator

**Topic:** Python Exception Handling

**Status:** Completed ✅

# DAY 12 / 365 🚀