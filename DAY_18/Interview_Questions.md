
# 🚀 DAY 18 / 365 — PYTHON EXCEPTION HANDLING
# 🎯 INTERVIEW QUESTIONS & ANSWERS

> Continuing my 365 Days of Growth journey 🚀

---

## 1. What is an Exception in Python?

An exception is an error that occurs during the execution of a program and interrupts the normal flow of the program.

Example:

```python
number = 10 / 0
````

This produces a `ZeroDivisionError`.

---

## 2. What is Exception Handling?

Exception handling is a mechanism used to handle runtime errors without crashing the entire program.

Python mainly uses:

```text
try
except
else
finally
```

---

## 3. What is the purpose of `try`?

The `try` block contains code that may produce an exception.

Example:

```python
try:
    number = int(input("Enter number: "))
```

---

## 4. What is the purpose of `except`?

The `except` block handles an exception raised inside the `try` block.

Example:

```python
try:
    number = int("Python")

except ValueError:
    print("Invalid number")
```

---

## 5. What is `else` in exception handling?

The `else` block executes only when no exception occurs inside the `try` block.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

else:
    print("Valid number:", number)
```

---

## 6. What is `finally`?

The `finally` block always executes whether an exception occurs or not.

Example:

```python
try:
    print("Program running")

except Exception:
    print("Error")

finally:
    print("Program completed")
```

---

## 7. Can we use multiple `except` blocks?

Yes.

Example:

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 8. What is `ValueError`?

`ValueError` occurs when a function receives a value of the correct type but an inappropriate value.

Example:

```python
number = int("Python")
```

---

## 9. What is `TypeError`?

`TypeError` occurs when an operation is performed on an inappropriate data type.

Example:

```python
result = 10 + "Python"
```

---

## 10. What is `ZeroDivisionError`?

`ZeroDivisionError` occurs when a number is divided by zero.

Example:

```python
result = 10 / 0
```

---

## 11. What is `IndexError`?

`IndexError` occurs when we try to access an index that does not exist.

Example:

```python
numbers = [10, 20, 30]

print(numbers[10])
```

---

## 12. What is `KeyError`?

`KeyError` occurs when we try to access a dictionary key that does not exist.

Example:

```python
student = {
    "name": "Aman"
}

print(student["age"])
```

---

## 13. What is `FileNotFoundError`?

`FileNotFoundError` occurs when Python tries to open a file that does not exist.

Example:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

---

## 14. What is `raise`?

The `raise` keyword is used to manually generate an exception.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## 15. Can we create our own exceptions?

Yes.

Custom exceptions can be created by inheriting from the `Exception` class.

Example:

```python
class InvalidAgeError(Exception):
    pass
```

---

## 16. What is a custom exception?

A custom exception is a user-defined exception created for a specific application requirement.

Example:

```python
class InsufficientBalanceError(Exception):
    pass
```

---

## 17. What is `Exception`?

`Exception` is the base class for most built-in exceptions in Python.

Example:

```python
try:
    number = 10 / 0

except Exception as e:
    print(e)
```

---

## 18. What does `as e` mean?

`as e` stores the exception object in a variable.

Example:

```python
try:
    number = int("Python")

except ValueError as e:
    print(e)
```

Here, `e` contains the error message.

---

## 19. What happens if an exception is not handled?

If an exception is not handled, Python terminates the program and displays a traceback.

Example:

```python
number = 10 / 0
```

The program stops with:

```text
ZeroDivisionError
```

---

## 20. Can `try` have multiple `except` blocks?

Yes.

Example:

```python
try:
    value = int(input("Enter number: "))

except ValueError:
    print("Invalid value")

except TypeError:
    print("Invalid type")
```

---

## 21. Can we use `else` with `try` and `except`?

Yes.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

else:
    print("Number:", number)
```

---

## 22. Can we use `finally` without `except`?

Yes.

Example:

```python
try:
    print("Hello")

finally:
    print("Always executed")
```

---

## 23. Why is `finally` useful?

`finally` is useful for cleanup operations such as:

* Closing files
* Closing database connections
* Releasing resources
* Cleaning temporary data

Example:

```python
file = None

try:
    file = open("data.txt", "r")

finally:
    if file:
        file.close()
```

---

## 24. What is the difference between an error and an exception?

An error is a general problem in a program.

An exception is an event that occurs during program execution and can often be handled using exception-handling mechanisms.

---

## 25. What is the difference between syntax error and exception?

A syntax error occurs when Python cannot understand the program syntax.

Example:

```python
if True
    print("Hello")
```

An exception occurs during program execution.

Example:

```python
print(10 / 0)
```

---

## 26. Can we catch multiple exceptions in one `except`?

Yes.

Example:

```python
try:
    number = int(input("Enter number: "))

except (ValueError, TypeError):
    print("Invalid input")
```

---

## 27. What is exception propagation?

Exception propagation means an exception moves up through the calling functions until it is handled.

Example:

```python
def function1():
    return 10 / 0


def function2():
    function1()


try:
    function2()

except ZeroDivisionError:
    print("Exception handled")
```

---

## 28. Should we use a broad `except Exception` everywhere?

No.

It is usually better to catch specific exceptions when possible.

Better:

```python
except ValueError:
    print("Invalid input")
```

Instead of:

```python
except Exception:
    print("Something went wrong")
```

Specific exceptions make programs easier to debug and maintain.

---

## 29. What is the difference between `raise` and `except`?

`raise` is used to create or re-raise an exception.

`except` is used to handle an exception.

Example:

```python
try:

    age = -1

    if age < 0:
        raise ValueError("Invalid age")

except ValueError as e:

    print(e)
```

---

## 30. What is the role of exception handling in real-world applications?

Exception handling helps applications remain stable when unexpected situations occur.

It is commonly used in:

* Web applications
* APIs
* Banking systems
* Authentication systems
* File processing
* Database applications
* Data processing
* Automation
* Machine Learning applications

---

# 🔥 QUICK INTERVIEW REVISION

```text
try
↓
Contains risky code

except
↓
Handles exceptions

else
↓
Runs when no exception occurs

finally
↓
Always executes

raise
↓
Manually raises an exception

Exception
↓
Base exception class

Custom Exception
↓
User-defined exception
```

---

# 🧠 IMPORTANT EXCEPTIONS

```text
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
PermissionError
OSError
```

---

# 🏆 DAY 18 INTERVIEW PREPARATION COMPLETE

```text
30 Interview Questions
        ↓
Exception Handling
        ↓
try / except
        ↓
else / finally
        ↓
raise
        ↓
Custom Exceptions
        ↓
Real-World Applications
        ↓
Interview Ready 🚀
```

---

# 🔥 365 DAYS OF GROWTH

**Day 18 / 365**

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

**18 / 365 — Keep Growing 🚀**

