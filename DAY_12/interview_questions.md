# 💼 Day 12 — Python Exception Handling Interview Questions

# 365 Days of Growth

## Topic: Python Exception Handling

---

# Q1. What is an Exception?

An exception is an unexpected event that occurs during program execution and interrupts the normal flow of a program.

Example:

```python
print(10 / 0)
```

This produces a `ZeroDivisionError`.

---

# Q2. What is Exception Handling?

Exception Handling is a mechanism used to handle runtime problems so that the program can respond properly instead of terminating unexpectedly.

Python mainly uses:

```text
try
except
else
finally
```

---

# Q3. What is the difference between an Error and an Exception?

An error is a problem in a program.

An exception is a runtime problem that can often be handled using Exception Handling.

Examples:

```text
SyntaxError
    ↓
Syntax problem

ValueError
    ↓
Invalid value during execution

ZeroDivisionError
    ↓
Division by zero
```

---

# Q4. Why is Exception Handling important?

Exception Handling is important because it:

- Prevents unexpected program termination
- Handles invalid user input
- Makes programs more reliable
- Helps with debugging
- Handles file errors
- Handles database/API errors
- Provides meaningful error messages

---

# Q5. What is the purpose of try?

The `try` block contains code that may generate an exception.

Example:

```python
try:
    result = 10 / 0
```

---

# Q6. What is the purpose of except?

The `except` block handles an exception generated inside the `try` block.

Example:

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# Q7. What is finally?

The `finally` block executes whether an exception occurs or not.

Example:

```python
try:
    print("Hello")

except:
    print("Error")

finally:
    print("Program completed.")
```

---

# Q8. What is else in Exception Handling?

The `else` block executes only when no exception occurs in the `try` block.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Valid number:", number)
```

---

# Q9. Can try be used without except?

Yes.

`try` can be used with `finally`.

Example:

```python
try:
    print("Hello")

finally:
    print("Completed.")
```

---

# Q10. Can we use multiple except blocks?

Yes.

Different exceptions can be handled using different `except` blocks.

Example:

```python
try:
    number = int(input("Enter number: "))

    result = 100 / number

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# Q11. What is ValueError?

`ValueError` occurs when a function receives a value of the correct type but an inappropriate value.

Example:

```python
number = int("hello")
```

---

# Q12. What is TypeError?

`TypeError` occurs when an operation is performed on incompatible data types.

Example:

```python
result = "10" + 5
```

---

# Q13. What is ZeroDivisionError?

`ZeroDivisionError` occurs when a number is divided by zero.

Example:

```python
result = 10 / 0
```

---

# Q14. What is IndexError?

`IndexError` occurs when we try to access an index that does not exist.

Example:

```python
numbers = [10, 20, 30]

print(numbers[5])
```

---

# Q15. What is KeyError?

`KeyError` occurs when we try to access a dictionary key that does not exist.

Example:

```python
student = {
    "name": "Amir"
}

print(student["age"])
```

---

# Q16. What is NameError?

`NameError` occurs when Python cannot find a variable or name.

Example:

```python
print(age)
```

If `age` was never defined, Python raises `NameError`.

---

# Q17. What is FileNotFoundError?

`FileNotFoundError` occurs when Python tries to open a file that does not exist.

Example:

```python
with open("unknown.txt", "r") as file:
    print(file.read())
```

---

# Q18. What is an Exception Object?

An exception object contains information about an exception.

We can store it using `as`.

Example:

```python
try:
    result = 10 / 0

except ZeroDivisionError as e:
    print(e)
```

---

# Q19. What does `as e` mean?

`as e` stores the exception object in the variable `e`.

Example:

```python
except ValueError as e:
    print(e)
```

This allows us to access the error message.

---

# Q20. What is the raise keyword?

The `raise` keyword is used to manually generate an exception.

Example:

```python
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above.")
```

---

# Q21. What is a Custom Exception?

A Custom Exception is an exception created by the programmer for a specific requirement.

Example:

```python
class AgeError(Exception):
    pass
```

Using it:

```python
raise AgeError("Invalid age.")
```

---

# Q22. Why create Custom Exceptions?

Custom Exceptions are useful when built-in exceptions do not clearly describe a specific application problem.

Examples:

- InsufficientBalanceError
- InvalidAgeError
- InvalidMarksError
- WeakPasswordError

---

# Q23. What is Exception Propagation?

Exception Propagation occurs when an exception is not handled inside a function and moves to the calling code.

Example:

```python
def divide():
    return 10 / 0


try:
    divide()

except ZeroDivisionError:
    print("Exception handled.")
```

---

# Q24. What is Exception Chaining?

Exception Chaining occurs when one exception causes another exception.

Python uses:

```python
raise ... from e
```

Example:

```python
try:
    number = int("Hello")

except ValueError as e:
    raise RuntimeError("Input processing failed.") from e
```

---

# Q25. What is Exception Re-raising?

Exception Re-raising means catching an exception and then raising it again using `raise`.

Example:

```python
try:
    number = int("Hello")

except ValueError:
    print("Error occurred.")
    raise
```

---

# Q26. What is the difference between raise and re-raise?

### raise

Used to manually create an exception.

```python
raise ValueError("Invalid value.")
```

### Re-raise

Used inside an `except` block to raise the current exception again.

```python
except ValueError:
    raise
```

---

# Q27. What is a bare except?

A bare except catches almost any exception.

Example:

```python
try:
    code()

except:
    print("Error")
```

It is generally better to use specific exceptions.

Example:

```python
except ValueError:
    print("Invalid value.")
```

---

# Q28. Why should we avoid bare except?

Bare `except` can:

- Hide programming errors
- Make debugging difficult
- Catch unexpected exceptions
- Make error handling less precise

Specific exceptions are usually better.

---

# Q29. Can multiple exceptions be handled in one except block?

Yes.

Example:

```python
try:
    code()

except (ValueError, TypeError):
    print("Invalid operation.")
```

This handles both `ValueError` and `TypeError`.

---

# Q30. What is the purpose of finally in file handling?

`finally` can be used for cleanup operations such as closing resources.

However, for files, Python generally recommends using `with`.

Example:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

The file is automatically managed after the block.

---

# Q31. What happens if an exception is not handled?

If an exception is not handled, Python stops the normal execution of the program and displays a traceback.

Example:

```python
result = 10 / 0
```

Python will raise:

```text
ZeroDivisionError
```

---

# Q32. Can we nest try-except blocks?

Yes.

Example:

```python
try:

    number = int(input("Enter number: "))

    try:

        result = 100 / number

        print(result)

    except ZeroDivisionError:

        print("Cannot divide by zero.")

except ValueError:

    print("Invalid input.")
```

---

# Q33. What is Exception Handling best practice?

Important practices include:

- Catch specific exceptions
- Keep try blocks small
- Give meaningful error messages
- Avoid unnecessary bare `except`
- Don't silently ignore errors
- Use `with` for file handling
- Validate user input
- Use custom exceptions when appropriate

---

# Q34. What is the difference between try-except and if-else?

`if-else` is used for normal condition checking.

`try-except` is used for handling exceptions.

Example:

```python
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

Exception handling:

```python
try:
    age = int(input("Enter age: "))

except ValueError:
    print("Invalid age.")
```

---

# Q35. What is the most important concept to remember in Exception Handling?

Remember the basic flow:

```text
try
  ↓
Risky Code
  ↓
Exception?
  ↓
YES → except
  ↓
NO → else
  ↓
finally
  ↓
Program continues
```

The main goal of Exception Handling is to make programs safer, more reliable, and easier to debug.

---

# ⭐ Quick Interview Revision

```text
try       → Risky code
except    → Handle exception
else      → Runs when no exception occurs
finally   → Always executes
raise     → Manually raises exception
as e      → Stores exception object
```

---

# 🔥 Important Built-in Exceptions

```text
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
NameError
FileNotFoundError
AttributeError
ImportError
ModuleNotFoundError
PermissionError
```

---

# 🎯 Interview Preparation Checklist

- [ ] Exception
- [ ] Exception Handling
- [ ] Error vs Exception
- [ ] try
- [ ] except
- [ ] else
- [ ] finally
- [ ] Multiple except
- [ ] Built-in Exceptions
- [ ] Exception Object
- [ ] raise
- [ ] Custom Exception
- [ ] Exception Propagation
- [ ] Exception Chaining
- [ ] Re-raising
- [ ] Nested try-except
- [ ] Best Practices

---

# 🏆 DAY 12 INTERVIEW PREPARATION COMPLETE

## Python Exception Handling

**Learn → Practice → Prepare → Build → Grow**

# DAY 12 / 365 ✅