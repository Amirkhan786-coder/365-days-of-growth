
# 🚀 DAY 16 / 365 — MINI PROJECT
# Performance Monitor & Access Logger

> Python Decorators & Higher-Order Functions

---

## 📅 Day 16 / 365

This mini project is part of my **365 Days of Growth** journey.

Today I built a Python-based **Performance Monitor & Access Logger** using decorators.

The project demonstrates how multiple decorators can be combined to provide authentication, logging, and performance monitoring without changing the main function logic.

---

# 📌 Project Name

**Performance Monitor & Access Logger**

---

# 🎯 Project Objective

The main objective of this project is to understand the practical implementation of Python decorators.

This project demonstrates:

- First-Class Functions
- Higher-Order Functions
- Nested Functions
- Closures
- Decorators
- Wrapper Functions
- `*args`
- `**kwargs`
- `functools.wraps`
- Multiple Decorators
- Authentication
- Logging
- Performance Monitoring

---

# ✨ Features

## 🔐 1. Authentication

Only the username `admin` is allowed to access the dashboard.

If any other username is entered, access is denied.

Example:

```text
Enter username: admin

Authentication Successful
````

---

## 📝 2. Function Logging

The logger decorator displays the name of the function being executed.

Example:

```text
Function Called: dashboard
```

---

## ⏱️ 3. Performance Monitoring

The performance decorator measures how much time the function takes to execute.

Example:

```text
Execution Time: 0.045231 seconds
```

The exact execution time may be different on every computer.

---

## 🧮 4. Calculation

The dashboard function calculates the sum of numbers from `1` to `999999`.

Expected result:

```text
499999500000
```

---

## 🔄 5. Multiple Decorators

Three decorators are applied to the dashboard function:

```text
Authentication
       ↓
Logger
       ↓
Performance
       ↓
Dashboard
```

The function is written as:

```python
@authentication
@logger
@performance
def dashboard(username):
    ...
```

---

# 🧠 Concepts Used

## 1. First-Class Functions

Python treats functions as first-class objects.

A function can be:

* Stored in a variable
* Passed as an argument
* Returned from another function
* Stored inside a data structure

---

## 2. Higher-Order Functions

A Higher-Order Function is a function that accepts another function as an argument or returns another function.

Decorators are based on this concept.

---

## 3. Nested Functions

A function defined inside another function is called a nested function.

Example:

```python
def outer():

    def inner():
        print("Hello")

    inner()
```

---

## 4. Closures

A closure allows an inner function to remember values from its enclosing function.

Example:

```python
def outer(message):

    def inner():
        print(message)

    return inner
```

---

## 5. Decorators

A decorator adds additional functionality to an existing function without modifying its original code.

Example:

```python
def decorator(function):

    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper
```

---

## 6. Wrapper Functions

A wrapper function is an inner function used inside a decorator.

It allows additional code to execute before or after the original function.

---

## 7. `*args`

`*args` allows a function to accept multiple positional arguments.

Example:

```python
def show(*args):

    print(args)


show(10, 20, 30)
```

---

## 8. `**kwargs`

`**kwargs` allows a function to accept multiple keyword arguments.

Example:

```python
def show(**kwargs):

    print(kwargs)


show(name="Amir", age=19)
```

---

## 9. `functools.wraps`

`functools.wraps` preserves the metadata of the original function when using decorators.

Example:

```python
from functools import wraps
```

---

# 🔄 Project Workflow

```text
Start Program
      ↓
Enter Username
      ↓
Authentication Decorator
      ↓
Check Username
      ↓
Authentication Successful
      ↓
Logger Decorator
      ↓
Performance Decorator
      ↓
Dashboard Function
      ↓
Perform Calculation
      ↓
Calculate Execution Time
      ↓
Display Result
      ↓
Program Completed
```

---

# 🛠️ Technologies Used

```text
Python
Python Functions
Higher-Order Functions
Decorators
Nested Functions
Closures
Wrapper Functions
*args
**kwargs
functools
time module
```

---

# 📂 Project Structure

```text
Performance-Monitor-Access-Logger/
│
├── main.py
└── README.md
```

---

# ▶️ How to Run

## Step 1

Open the project folder in VS Code.

## Step 2

Open the terminal.

## Step 3

Run the following command:

```bash
python main.py
```

---

# 💻 Sample Output

```text
=======================================================
       PERFORMANCE MONITOR & ACCESS LOGGER
=======================================================

Enter username: admin

Authentication Successful
Function Called: dashboard

Welcome to the Dashboard, admin!

Execution Time: 0.045231 seconds

Calculation Result: 499999500000

Program completed successfully.

=======================================================
                    THANK YOU
=======================================================
```

> Note: Execution time can be different on different computers.

---

# ❌ Invalid Login Example

```text
=======================================================
       PERFORMANCE MONITOR & ACCESS LOGGER
=======================================================

Enter username: user

Authentication Failed
Access Denied!

Program stopped because authentication failed.

=======================================================
                    THANK YOU
=======================================================
```

---

# 💻 COMPLETE PROJECT CODE

## `main.py`

```python
# ============================================================
# 🚀 DAY 16 MINI PROJECT
# PERFORMANCE MONITOR & ACCESS LOGGER
# ============================================================
#
# Concepts Used:
#
# 1. First-Class Functions
# 2. Higher-Order Functions
# 3. Nested Functions
# 4. Closures
# 5. Decorators
# 6. Wrapper Functions
# 7. *args
# 8. **kwargs
# 9. functools.wraps
# 10. Multiple Decorators
# 11. Authentication
# 12. Logging
# 13. Performance Monitoring
#
# ============================================================

import time
from functools import wraps


# ============================================================
# 1. AUTHENTICATION DECORATOR
# ============================================================

def authentication(function):
    """
    Authentication decorator.

    Only the username 'admin'
    is allowed to access the dashboard.
    """

    @wraps(function)
    def wrapper(username, *args, **kwargs):

        # Check username
        if username != "admin":

            print("\n❌ Authentication Failed")
            print("❌ Access Denied!")

            return None

        # Authentication successful
        print("\n✅ Authentication Successful")

        # Execute original function
        return function(username, *args, **kwargs)

    return wrapper


# ============================================================
# 2. LOGGING DECORATOR
# ============================================================

def logger(function):
    """
    Logging decorator.

    Displays the name of the function
    being executed.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Display function name
        print("📝 Function Called:", function.__name__)

        # Execute original function
        return function(*args, **kwargs)

    return wrapper


# ============================================================
# 3. PERFORMANCE DECORATOR
# ============================================================

def performance(function):
    """
    Performance decorator.

    Measures the execution time
    of the original function.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Record start time
        start_time = time.time()

        # Execute original function
        result = function(*args, **kwargs)

        # Record end time
        end_time = time.time()

        # Calculate execution time
        execution_time = end_time - start_time

        print(
            f"⏱️ Execution Time: "
            f"{execution_time:.6f} seconds"
        )

        # Return result
        return result

    return wrapper


# ============================================================
# 4. DASHBOARD FUNCTION
# ============================================================

@authentication
@logger
@performance
def dashboard(username):
    """
    Dashboard function.

    Performs a calculation after
    successful authentication.
    """

    print(
        f"\n👋 Welcome to the Dashboard, {username}!"
    )

    # Variable for storing total
    total = 0

    # Calculate sum from 1 to 999999
    for number in range(1, 1000000):

        total += number

    # Return final result
    return total


# ============================================================
# 5. MAIN PROGRAM
# ============================================================

print("=" * 55)

print(
    "       PERFORMANCE MONITOR & ACCESS LOGGER"
)

print("=" * 55)


# ============================================================
# 6. USER INPUT
# ============================================================

username = input(
    "\nEnter username: "
)


# ============================================================
# 7. CALL DASHBOARD
# ============================================================

result = dashboard(username)


# ============================================================
# 8. DISPLAY RESULT
# ============================================================

if result is not None:

    print(
        "\n🧮 Calculation Result:",
        result
    )

    print(
        "\n✅ Program completed successfully."
    )

else:

    print(
        "\n⚠️ Program stopped because "
        "authentication failed."
    )


# ============================================================
# 9. END PROGRAM
# ============================================================

print("\n" + "=" * 55)

print(
    "                    THANK YOU"
)

print("=" * 55)
```

---

# 🌍 Real-World Applications

The concepts used in this project can be applied to:

* User Authentication
* API Authentication
* Logging Systems
* Performance Monitoring
* Input Validation
* Access Control
* Web Applications
* Backend Applications
* Security Systems
* Error Handling
* Monitoring Systems

---

# 📈 Future Improvements

This project can be improved by adding:

* Multiple users
* Password authentication
* File-based logging
* Login attempt tracking
* Date and time logging
* User roles
* Admin and normal users
* Database authentication
* SQLite database
* Login history
* GUI interface
* Web interface
* Better security

---

# 🎯 Learning Outcomes

After completing this project, I learned how to:

* [x] Create decorators
* [x] Use multiple decorators
* [x] Create wrapper functions
* [x] Use `*args`
* [x] Use `**kwargs`
* [x] Use `functools.wraps`
* [x] Perform authentication
* [x] Log function execution
* [x] Measure execution time
* [x] Build reusable Python functionality
* [x] Combine multiple decorators
* [x] Build a practical Python project

---

# 💡 Key Learning

Decorators allow us to add reusable functionality to existing functions without changing their core logic.

They make programs:

* Reusable
* Modular
* Maintainable
* Scalable
* Easier to understand

---

# 📊 Project Summary

| Feature                | Status      |
| ---------------------- | ----------- |
| Authentication         | ✅ Completed |
| Function Logging       | ✅ Completed |
| Performance Monitoring | ✅ Completed |
| Multiple Decorators    | ✅ Completed |
| Calculation            | ✅ Completed |
| Error Handling         | ✅ Completed |

---

# 🏆 Project Achievement

```text
Python Functions
       ↓
Higher-Order Functions
       ↓
Decorators
       ↓
Authentication
       ↓
Logging
       ↓
Performance Monitoring
       ↓
Multiple Decorators
       ↓
Real-World Application
       ↓
Mini Project Completed ✅
```

---

# 🔥 365 DAYS OF GROWTH

**Day 16 / 365**

```text
████░░░░░░░░░░░░░░░░  4.4%
```

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

# 🚀 DAY 16 — MINI PROJECT COMPLETED!


