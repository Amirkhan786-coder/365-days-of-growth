# 📚 Day 12 - Python Exception Handling

# PART 1 — Exception Handling Basics

---

# 1. What is Exception Handling?

Exception Handling is a mechanism in Python used to handle unexpected problems that occur while a program is running.

Normally, when an exception occurs, Python stops the program and displays an error message.

Exception Handling allows us to handle these problems properly without suddenly stopping the program.

### Example Without Exception Handling

```python
number = 10
result = number / 0

print(result)
```

Output:

```text
ZeroDivisionError: division by zero
```

### Example With Exception Handling

```python
try:
    number = 10
    result = number / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

---

# 2. Why Do We Need Exception Handling?

Exception Handling is useful because it:

- Prevents unexpected program termination
- Handles invalid input
- Provides meaningful error messages
- Makes programs more reliable
- Improves user experience
- Handles file errors
- Handles database errors
- Handles API errors
- Helps with input validation
- Makes applications safer and more robust

---

# 3. Error vs Exception

## Error

An error is a problem in a program.

Some errors can prevent the program from running.

Examples:

- SyntaxError
- IndentationError

Example:

```python
if True
    print("Hello")
```

This produces a `SyntaxError`.

---

## Exception

An exception is an event that occurs during program execution and interrupts the normal flow of the program.

Examples:

- ValueError
- TypeError
- ZeroDivisionError
- IndexError
- KeyError
- FileNotFoundError

Example:

```python
number = int("Hello")
```

This produces:

```text
ValueError
```

---

# 4. Basic Exception Handling

Python mainly provides four important keywords:

- `try`
- `except`
- `else`
- `finally`

Basic structure:

```python
try:
    # risky code

except:
    # error handling
```

---

# 5. try Block

The `try` block contains code that may generate an exception.

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input.")
```

The risky code should be placed inside the `try` block.

---

# 6. except Block

The `except` block handles an exception.

Example:

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

---

# 7. Basic try-except Syntax

```python
try:
    risky_code()

except ExceptionType:
    handle_error()
```

Example:

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number.")
```

---

# 8. ValueError

`ValueError` occurs when a function receives a value of the correct type but an inappropriate value.

Example:

```python
number = int("Hello")
```

Output:

```text
ValueError
```

Handling:

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number.")
```

---

# 9. TypeError

`TypeError` occurs when an operation is performed on incompatible data types.

Example:

```python
result = "10" + 5
```

Handling:

```python
try:
    result = "10" + 5

except TypeError:
    print("Incompatible data types.")
```

---

# 10. ZeroDivisionError

`ZeroDivisionError` occurs when we try to divide a number by zero.

Example:

```python
result = 10 / 0
```

Handling:

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 11. IndexError

`IndexError` occurs when we access an index that does not exist.

Example:

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Handling:

```python
try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Index is out of range.")
```

---

# 12. KeyError

`KeyError` occurs when a dictionary key does not exist.

Example:

```python
student = {
    "name": "Amir",
    "age": 20
}

print(student["course"])
```

Handling:

```python
try:
    print(student["course"])

except KeyError:
    print("Key does not exist.")
```

A safer alternative:

```python
print(student.get("course"))
```

---

# 13. NameError

`NameError` occurs when a variable or name has not been defined.

Example:

```python
print(age)
```

Handling:

```python
try:
    print(age)

except NameError:
    print("Variable is not defined.")
```

---

# 14. FileNotFoundError

`FileNotFoundError` occurs when Python tries to open a file that does not exist.

Example:

```python
file = open("unknown.txt", "r")
```

Handling:

```python
try:
    file = open("unknown.txt", "r")

except FileNotFoundError:
    print("File does not exist.")
```

---

# 15. AttributeError

`AttributeError` occurs when an object does not have the requested attribute or method.

Example:

```python
number = 10

number.append(5)
```

Handling:

```python
try:
    number = 10
    number.append(5)

except AttributeError:
    print("This object does not support this operation.")
```

---

# 16. ImportError

`ImportError` occurs when Python cannot import something.

Example:

```python
try:
    from math import unknown_function

except ImportError:
    print("Import failed.")
```

---

# 17. ModuleNotFoundError

`ModuleNotFoundError` occurs when Python cannot find the requested module.

Example:

```python
try:
    import unknown_module

except ModuleNotFoundError:
    print("Module not found.")
```

---

# 18. PermissionError

`PermissionError` occurs when the program does not have the required permission to access a resource.

Example:

```python
try:
    file = open("protected.txt", "r")

except PermissionError:
    print("Permission denied.")
```

---

# 19. Common Built-in Exceptions

| Exception | Meaning |
|---|---|
| ValueError | Invalid value |
| TypeError | Incompatible data types |
| ZeroDivisionError | Division by zero |
| IndexError | Invalid index |
| KeyError | Dictionary key does not exist |
| NameError | Name is not defined |
| FileNotFoundError | File does not exist |
| AttributeError | Attribute or method does not exist |
| ImportError | Import problem |
| ModuleNotFoundError | Module cannot be found |
| PermissionError | Permission problem |

---

# 20. Multiple except Blocks

We can use multiple `except` blocks to handle different exceptions.

Example:

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 21. Handling Multiple Exceptions Together

If multiple exceptions require the same handling, they can be grouped.

Example:

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Invalid operation.")
```

---

# END OF PART 1


# PART 2 — Advanced Exception Handling

---

# 22. else Block

The `else` block executes only when no exception occurs in the `try` block.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)
```

### Important

- `try` → risky code
- `except` → handles exception
- `else` → runs when no exception occurs

---

# 23. finally Block

The `finally` block always executes.

It runs whether an exception occurs or not.

Example:

```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Error")

finally:
    print("Program completed.")
```

Output:

```text
5.0
Program completed.
```

---

# 24. Complete try-except-else-finally

Syntax:

```python
try:
    # risky code

except ExceptionType:
    # handle exception

else:
    # runs when no exception occurs

finally:
    # always runs
```

Example:

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Calculation completed.")
```

---

# 25. Exception Object

We can store exception information using `as`.

Example:

```python
try:
    result = 10 / 0

except ZeroDivisionError as e:
    print("Error:", e)
```

Output:

```text
Error: division by zero
```

Here:

```python
as e
```

stores the exception object inside the variable `e`.

We can print `e` to see the error message.

---

# 26. General Exception

`Exception` is the base class for many common application-level exceptions.

Example:

```python
try:
    number = int(input("Enter number: "))

except Exception as e:
    print("Error:", e)
```

This can catch many common exceptions.

However, when we know the exact exception, it is usually better to catch the specific exception.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Please enter a valid number.")
```

---

# 27. Specific Exception vs General Exception

## Specific Exception

```python
try:
    number = int(input())

except ValueError:
    print("Invalid number.")
```

This is preferred when we know which exception we expect.

---

## General Exception

```python
try:
    number = int(input())

except Exception as e:
    print("Error:", e)
```

This is useful when we need broader error handling.

### Best Practice

Prefer specific exceptions whenever possible.

---

# 28. Bare except

Python allows:

```python
try:
    risky_code()

except:
    print("Error")
```

But bare `except` is generally discouraged.

Why?

Because it can catch exceptions too broadly and make debugging difficult.

Instead of:

```python
except:
    print("Error")
```

Prefer:

```python
except ValueError:
    print("Invalid value.")
```

or:

```python
except Exception as e:
    print("Error:", e)
```

---

# 29. raise Keyword

The `raise` keyword is used to manually generate an exception.

Example:

```python
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above.")
```

Output:

```text
ValueError: Age must be 18 or above.
```

---

# 30. Why Use raise?

The `raise` keyword is useful for:

- Input validation
- Data validation
- Business rules
- Application-specific errors
- Creating custom error conditions

Example:

```python
marks = 150

if marks > 100:
    raise ValueError("Marks cannot be greater than 100.")
```

---

# 31. Custom Exceptions

Python allows us to create our own exceptions.

A custom exception is created using a class that inherits from `Exception`.

Syntax:

```python
class MyError(Exception):
    pass
```

Example:

```python
class AgeError(Exception):
    pass
```

---

# 32. Using Custom Exception

Example:

```python
class AgeError(Exception):
    pass


try:
    age = int(input("Enter age: "))

    if age < 18:
        raise AgeError("You must be 18 or above.")

    print("Eligible")

except AgeError as e:
    print("Error:", e)
```

If the user enters:

```text
15
```

Output:

```text
Error: You must be 18 or above.
```

---

# 33. Custom Banking Exception

We can create custom exceptions for real-world applications.

Example:

```python
class InsufficientBalanceError(Exception):
    pass


balance = 5000
amount = 7000

try:

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")

    print("Transaction successful.")

except InsufficientBalanceError as e:

    print("Error:", e)
```

Output:

```text
Error: Insufficient balance.
```

---

# 34. Nested try-except

A `try-except` block can be placed inside another `try-except` block.

Example:

```python
try:

    number = int(input("Enter number: "))

    try:

        print(100 / number)

    except ZeroDivisionError:

        print("Cannot divide by zero.")

except ValueError:

    print("Invalid input.")
```

Here:

- Outer `try` handles input conversion.
- Inner `try` handles division.
- Different exceptions can be handled separately.

---

# 35. Exception Handling with Functions

Exception Handling can be used inside functions.

Example:

```python
def divide(a, b):

    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero"


print(divide(10, 2))
print(divide(10, 0))
```

Output:

```text
5.0
Cannot divide by zero
```

---

# 36. Exception Handling with User Input

User input can be invalid.

For example, `int()` cannot convert normal text into an integer.

Example:

```python
try:

    age = int(input("Enter your age: "))

    print("Your age is:", age)

except ValueError:

    print("Please enter a valid number.")
```

If the user enters:

```text
abc
```

Output:

```text
Please enter a valid number.
```

---

# 37. Exception Handling with Loops

Exception Handling can be used inside loops to repeatedly request valid input.

Example:

```python
while True:

    try:

        number = int(input("Enter a number: "))

        print("You entered:", number)

        break

    except ValueError:

        print("Invalid input. Try again.")
```

The loop continues until valid input is entered.

---

# 38. Exception Handling with Lists

Example:

```python
numbers = [10, 20, 30]

try:

    index = int(input("Enter index: "))

    print(numbers[index])

except ValueError:

    print("Please enter a valid index.")

except IndexError:

    print("Index is out of range.")
```

Possible errors:

- `ValueError` → invalid index input
- `IndexError` → index does not exist

---

# 39. Exception Handling with Dictionaries

Example:

```python
student = {
    "name": "Amir",
    "age": 20,
    "course": "CSE"
}

try:

    key = input("Enter key: ")

    print(student[key])

except KeyError:

    print("Key does not exist.")
```

Example:

If the user enters:

```text
city
```

Output:

```text
Key does not exist.
```

---

# 40. Exception Handling with Files

File operations can generate exceptions.

Example:

```python
try:

    with open("student.txt", "r") as file:

        content = file.read()

        print(content)

except FileNotFoundError:

    print("File Not Found!")
```

If the file does not exist, the program will not crash.

Instead:

```text
File Not Found!
```

will be displayed.

---

# 41. Exception Handling with File Writing

Example:

```python
try:

    with open("student.txt", "w") as file:

        file.write("Amir Khan")

except PermissionError:

    print("Permission denied.")

except OSError:

    print("File operation failed.")
```

Here:

- `PermissionError` handles permission problems.
- `OSError` handles other operating-system-related file errors.

---

# 42. Exception Handling with Type Conversion

Type conversion can produce `ValueError`.

Example:

```python
try:

    number = float(input("Enter a number: "))

except ValueError:

    print("Please enter a valid number.")

else:

    print("Number:", number)
```

Example input:

```text
25.5
```

Output:

```text
Number: 25.5
```

Invalid input:

```text
hello
```

Output:

```text
Please enter a valid number.
```

---

# 43. Exception Handling with JSON

JSON files are commonly used in Python applications.

Example:

```python
import json

try:

    with open("data.json", "r") as file:

        data = json.load(file)

except FileNotFoundError:

    print("JSON file not found.")

except json.JSONDecodeError:

    print("Invalid JSON data.")
```

Possible exceptions:

- `FileNotFoundError`
- `JSONDecodeError`

---

# 44. Exception Handling with APIs

API calls can fail due to:

- Network problems
- Timeout
- Invalid response
- Authentication failure
- Server errors

Basic structure:

```python
try:

    # API request

    print("API request successful.")

except Exception as e:

    print("API request failed:", e)
```

In real projects, it is better to catch the specific exceptions provided by the API/library being used.

---

# 45. Exception Hierarchy

Python exceptions follow an inheritance hierarchy.

Simplified structure:

```text
BaseException
│
└── Exception
    │
    ├── ValueError
    ├── TypeError
    ├── IndexError
    ├── KeyError
    ├── NameError
    ├── FileNotFoundError
    ├── AttributeError
    ├── ImportError
    └── ZeroDivisionError
```

Most application-level exceptions inherit from:

```python
Exception
```

---

# 46. Exception Propagation

If an exception is not handled inside a function, it can move to the calling function.

Example:

```python
def divide():

    return 10 / 0


try:

    divide()

except ZeroDivisionError:

    print("Cannot divide by zero.")
```

The exception is generated inside:

```python
divide()
```

but handled outside the function.

This movement of an exception is called **Exception Propagation**.

---

# 47. Re-raising an Exception

Sometimes we catch an exception but want to send it to a higher level.

We can use `raise`.

Example:

```python
try:

    number = int("Hello")

except ValueError:

    print("Logging the error.")

    raise
```

Here:

1. The exception is caught.
2. A message is printed.
3. `raise` sends the same exception again.

---

# 48. Exception Chaining

Python allows one exception to be raised because of another exception.

Example:

```python
try:

    number = int("Hello")

except ValueError as e:

    raise RuntimeError("Unable to process input") from e
```

Here:

- `ValueError` is the original exception.
- `RuntimeError` is the new exception.
- `from e` connects the new exception to the original exception.

This is called **Exception Chaining**.

---

# 49. finally and return

The `finally` block executes even when a function returns.

Example:

```python
def test():

    try:
        return "Try"

    finally:
        print("Finally executed")


print(test())
```

Output:

```text
Finally executed
Try
```

The `finally` block runs before the function actually returns.

---

# 50. Exception Handling with Resource Cleanup

`finally` is useful for cleanup.

Example:

```python
file = None

try:

    file = open("data.txt", "r")

    print(file.read())

except FileNotFoundError:

    print("File not found.")

finally:

    if file is not None:
        file.close()
```

The file is closed during cleanup.

However, for files, using `with open()` is usually cleaner and safer.

---

# 51. with Statement and Exception Handling

Best practice for files:

```python
try:

    with open("data.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("File not found.")
```

The `with` statement automatically manages the file resource.

It automatically closes the file after the block finishes.

---

# END OF PART 2

# PART 3 — Best Practices, Applications & Revision

---

# 52. Best Practices

Good Exception Handling makes a program reliable, readable, and easier to debug.

---

## 1. Catch Specific Exceptions

Prefer:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")
```

Instead of unnecessarily using:

```python
try:
    number = int(input("Enter number: "))

except:
    print("Error.")
```

Specific exceptions make the program easier to understand and debug.

---

## 2. Keep try Blocks Small

Only place code that may generate an exception inside the `try` block.

Good:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")
```

Avoid putting the entire program inside one large `try` block.

---

## 3. Use Meaningful Error Messages

Good:

```python
except ValueError:
    print("Please enter a valid age.")
```

Better than:

```python
except ValueError:
    print("Error")
```

A meaningful message helps the user understand the problem.

---

## 4. Do Not Hide Errors

Avoid:

```python
try:
    risky_code()

except:
    pass
```

This silently ignores the error.

It can make debugging very difficult.

---

## 5. Use finally for Cleanup

Use `finally` when some operation must happen whether an exception occurs or not.

Example:

```python
try:
    print("Opening resource.")

except Exception:
    print("Error.")

finally:
    print("Closing resource.")
```

---

## 6. Use with for Files

For file handling, prefer:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

instead of manually opening and closing the file.

---

## 7. Validate User Input

Always consider that users may enter:

- Wrong data type
- Empty input
- Negative values
- Invalid values
- Unexpected characters

Example:

```python
try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
    print("Error:", e)
```

---

## 8. Use Custom Exceptions When Appropriate

Custom exceptions are useful when an application has its own specific rules.

Example:

```python
class InsufficientBalanceError(Exception):
    pass
```

---

# 53. Common Mistakes

---

## Mistake 1: Using Bare except Unnecessarily

Bad:

```python
try:
    number = int(input())

except:
    print("Error")
```

Better:

```python
try:
    number = int(input())

except ValueError:
    print("Invalid number.")
```

---

## Mistake 2: Using an Extremely Large try Block

Avoid:

```python
try:

    # hundreds of lines of code

except:
    print("Error")
```

Instead, keep the `try` block focused on the code that may fail.

---

## Mistake 3: Ignoring Useful Exception Information

Bad:

```python
except Exception:
    print("Something went wrong.")
```

Better:

```python
except Exception as e:
    print("Error:", e)
```

When appropriate, logging can also be used in real applications.

---

## Mistake 4: Silently Passing Errors

Bad:

```python
except:
    pass
```

This hides the problem.

---

## Mistake 5: Using Exception Handling for Normal Conditions

Do not use exceptions when a simple condition can handle the situation.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

There is no need for exception handling here.

---

# 54. Exception Handling vs if-else

`if-else` is used to check expected conditions.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Exception Handling is used to handle unexpected or exceptional situations.

Example:

```python
try:

    age = int(input("Enter age: "))

except ValueError:

    print("Invalid input.")
```

### Difference

| if-else | Exception Handling |
|---|---|
| Checks conditions | Handles exceptions |
| Used for normal program logic | Used for exceptional situations |
| Uses conditions | Uses try-except |
| Predictable situations | Unexpected problems |

---

# 55. Real-Life Applications

Exception Handling is used in almost every real-world software application.

---

## Banking Applications

Exception Handling can handle:

- Invalid transactions
- Insufficient balance
- Invalid amount
- Transaction failures
- Connection failures

Example:

```python
class InsufficientBalanceError(Exception):
    pass
```

---

## Login Systems

Exception Handling can handle:

- Invalid input
- Authentication errors
- Invalid credentials
- Database connection problems

---

## File Management

Exception Handling can handle:

- Missing files
- Invalid paths
- Permission problems
- File reading errors
- File writing errors

---

## APIs

Exception Handling can handle:

- Connection failures
- Invalid responses
- Timeouts
- Authentication errors
- Server errors

---

## Databases

Exception Handling can handle:

- Connection failures
- Invalid queries
- Missing records
- Duplicate records
- Database server errors

---

## AI/ML Applications

Exception Handling can handle:

- Invalid input
- Missing dataset
- Model loading errors
- Data validation errors
- File errors
- API errors
- Invalid model parameters

---

# 56. Interview Quick Revision

Remember the basic flow:

```text
try
  ↓
Contains risky code
  ↓
Exception occurs?
  ↓
YES ───────────────→ except
                       ↓
                  Handle error

NO
 ↓
else
 ↓
Successful execution

finally
 ↓
Always executes
```

---

## Important Keywords

### try

Contains code that may generate an exception.

```python
try:
    risky_code()
```

---

### except

Handles the exception.

```python
except ValueError:
    print("Invalid value.")
```

---

### else

Runs when no exception occurs.

```python
else:
    print("Success")
```

---

### finally

Always executes.

```python
finally:
    print("Cleanup")
```

---

### raise

Manually raises an exception.

```python
raise ValueError("Invalid value")
```

---

# 57. Important Syntax Cheat Sheet

## Basic try-except

```python
try:
    code

except ValueError:
    print("Error")
```

---

## Multiple Exceptions

```python
try:
    code

except ValueError:
    print("Value Error")

except TypeError:
    print("Type Error")
```

---

## Grouped Exceptions

```python
try:
    code

except (ValueError, TypeError):
    print("Error")
```

---

## try-except-else

```python
try:
    code

except ValueError:
    print("Error")

else:
    print("Success")
```

---

## try-except-finally

```python
try:
    code

except ValueError:
    print("Error")

finally:
    print("Cleanup")
```

---

## Complete Structure

```python
try:
    code

except ValueError:
    handle_error

else:
    success

finally:
    cleanup
```

---

## Exception Object

```python
try:
    code

except Exception as e:
    print(e)
```

---

## raise

```python
raise ValueError("Invalid value")
```

---

## Custom Exception

```python
class MyError(Exception):
    pass
```

---

## Custom Exception with raise

```python
class AgeError(Exception):
    pass


age = 15

if age < 18:
    raise AgeError("Age must be 18 or above.")
```

---

# 58. Safe Calculator Example

This mini project combines multiple Exception Handling concepts.

It uses:

- Functions
- try
- except
- raise
- ValueError
- ZeroDivisionError
- finally
- User input validation

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


while True:

    print("\n===== SAFE CALCULATOR =====")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 5:

            print("Calculator closed.")
            break

        if choice not in [1, 2, 3, 4]:

            raise ValueError("Invalid choice.")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:

            print("Result:", add(num1, num2))

        elif choice == 2:

            print("Result:", subtract(num1, num2))

        elif choice == 3:

            print("Result:", multiply(num1, num2))

        elif choice == 4:

            print("Result:", divide(num1, num2))

    except ValueError as e:

        print("Input Error:", e)

    except ZeroDivisionError as e:

        print("Calculation Error:", e)

    except Exception as e:

        print("Unexpected Error:", e)

    finally:

        print("Thank you for using Safe Calculator.")
```

---

## Safe Calculator — Concepts Used

```text
User Input
    ↓
Validate Choice
    ↓
Validate Numbers
    ↓
Perform Operation
    ↓
Exception?
    ↓
YES → Handle Error
    ↓
finally
    ↓
Continue / Exit
```

---

# END OF PART 3


# PART 4 — Practice, Checklist & Key Takeaways

---

# 59. Practice Questions

## Beginner Questions

### 1. What is an exception?

An exception is an unexpected event that occurs during program execution and interrupts the normal flow of the program.

---

### 2. What is Exception Handling?

Exception Handling is a mechanism used to handle runtime problems without unnecessarily terminating the program.

---

### 3. Why do we need Exception Handling?

We need Exception Handling to:

- Prevent program crashes
- Handle invalid input
- Display meaningful error messages
- Make programs reliable
- Handle file errors
- Handle API and database errors

---

### 4. What is the purpose of `try`?

The `try` block contains code that may generate an exception.

---

### 5. What is the purpose of `except`?

The `except` block handles an exception generated inside the `try` block.

---

### 6. What is ValueError?

`ValueError` occurs when a function receives a value of the correct type but an inappropriate value.

Example:

```python
int("hello")
```

---

### 7. What is TypeError?

`TypeError` occurs when an operation is performed on incompatible data types.

Example:

```python
"10" + 5
```

---

### 8. What is ZeroDivisionError?

`ZeroDivisionError` occurs when a number is divided by zero.

Example:

```python
10 / 0
```

---

### 9. What is IndexError?

`IndexError` occurs when we try to access an index that does not exist.

Example:

```python
numbers = [10, 20, 30]

print(numbers[5])
```

---

### 10. What is KeyError?

`KeyError` occurs when a requested dictionary key does not exist.

Example:

```python
student = {"name": "Amir"}

print(student["age"])
```

---

### 11. What is NameError?

`NameError` occurs when we use a variable or name that has not been defined.

Example:

```python
print(age)
```

---

### 12. What is FileNotFoundError?

`FileNotFoundError` occurs when Python tries to access a file that does not exist.

Example:

```python
open("unknown.txt", "r")
```

---

# Intermediate Questions

### 13. Explain try-except.

`try-except` is used to handle exceptions.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")
```

---

### 14. Explain try-except-else.

The `else` block executes only when no exception occurs.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Valid number:", number)
```

---

### 15. Explain try-except-finally.

`finally` always executes whether an exception occurs or not.

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

### 16. What is the purpose of finally?

`finally` is mainly used for cleanup operations.

Examples:

- Closing files
- Releasing resources
- Closing connections
- Cleaning temporary resources

---

### 17. Can we have multiple except blocks?

Yes.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

### 18. How can multiple exceptions be handled together?

Multiple exceptions can be placed inside a tuple.

Example:

```python
try:
    code()

except (ValueError, TypeError):
    print("Invalid operation.")
```

---

### 19. What is an exception object?

An exception object contains information about the exception.

Example:

```python
try:
    result = 10 / 0

except ZeroDivisionError as e:
    print(e)
```

---

### 20. What does `as e` mean?

`as e` stores the exception object in the variable `e`.

Example:

```python
except ValueError as e:
    print(e)
```

---

### 21. What is the `raise` keyword?

`raise` is used to manually generate an exception.

Example:

```python
raise ValueError("Invalid value")
```

---

### 22. What is a custom exception?

A custom exception is an exception created by the programmer for a specific application requirement.

Example:

```python
class AgeError(Exception):
    pass
```

---

### 23. What is Exception Propagation?

Exception Propagation is the process where an unhandled exception moves from one function to its calling function.

Example:

```python
def test():
    return 10 / 0


try:
    test()

except ZeroDivisionError:
    print("Error handled")
```

---

### 24. What is Exception Chaining?

Exception Chaining occurs when one exception is raised because of another exception.

Example:

```python
try:
    number = int("Hello")

except ValueError as e:
    raise RuntimeError("Input processing failed") from e
```

---

### 25. What is Exception Re-raising?

Re-raising means catching an exception and then raising the same exception again using `raise`.

Example:

```python
try:
    number = int("Hello")

except ValueError:
    print("Error logged")
    raise
```

---

### 26. Why should bare `except` usually be avoided?

Bare `except` can catch exceptions too broadly.

It can:

- Hide programming errors
- Make debugging difficult
- Make unexpected problems harder to identify

Prefer specific exceptions.

---

# Coding Practice Questions

### 27. Division by Zero

Write a program that handles division by zero.

Expected concept:

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

### 28. Invalid Integer Input

Write a program that handles invalid integer input.

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid integer.")
```

---

### 29. Invalid List Index

Write a program that handles an invalid list index.

```python
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index out of range.")
```

---

### 30. Missing Dictionary Key

Write a program that handles a missing dictionary key.

```python
student = {
    "name": "Amir",
    "age": 20
}

try:
    print(student["city"])

except KeyError:
    print("Key does not exist.")
```

---

### 31. Missing File

Write a program that handles a missing file.

```python
try:

    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")
```

---

### 32. Create Custom AgeError

```python
class AgeError(Exception):
    pass


age = int(input("Enter age: "))

if age < 18:
    raise AgeError("Age must be 18 or above.")
```

---

### 33. Create Custom InsufficientBalanceError

```python
class InsufficientBalanceError(Exception):
    pass


balance = 5000
withdraw = 7000

try:

    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance.")

except InsufficientBalanceError as e:

    print(e)
```

---

### 34. Create a Calculator Using Exception Handling

Create a calculator that supports:

- Addition
- Subtraction
- Multiplication
- Division

Handle:

- Invalid choice
- Invalid numbers
- Division by zero

---

### 35. Repeatedly Ask for a Valid Number

Write a program that keeps asking the user for a number until valid input is provided.

Example:

```python
while True:

    try:

        number = int(input("Enter number: "))

        print("Valid number:", number)

        break

    except ValueError:

        print("Invalid input. Try again.")
```

---

### 36. Use try-except-else-finally

Create a program that demonstrates all four blocks:

```python
try:
    # risky code

except:
    # error

else:
    # success

finally:
    # always execute
```

---

### 37. Use Multiple Exceptions

Create a program that handles:

- ValueError
- ZeroDivisionError
- IndexError

using separate `except` blocks.

---

### 38. Use Nested try-except

Create a program where one `try-except` block is inside another.

---

### 39. Handle File Errors

Create a program that:

1. Opens a file.
2. Reads the file.
3. Handles FileNotFoundError.
4. Handles PermissionError.

---

### 40. Use raise

Create a program that validates marks.

Rules:

- Marks must be between 0 and 100.
- If marks are less than 0 or greater than 100, raise `ValueError`.

Example:

```python
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    raise ValueError("Marks must be between 0 and 100.")

print("Valid marks:", marks)
```

---

# 60. Day 12 Checklist

## Theory

- [ ] Understand Exception Handling
- [ ] Understand Error vs Exception
- [ ] Learn `try`
- [ ] Learn `except`
- [ ] Learn `else`
- [ ] Learn `finally`
- [ ] Learn multiple exceptions
- [ ] Learn exception objects
- [ ] Learn built-in exceptions
- [ ] Learn `raise`
- [ ] Learn custom exceptions
- [ ] Learn nested try-except
- [ ] Learn exception propagation
- [ ] Learn exception chaining
- [ ] Learn exception re-raising

---

## Practical

- [ ] Handle user input
- [ ] Handle ValueError
- [ ] Handle TypeError
- [ ] Handle ZeroDivisionError
- [ ] Handle IndexError
- [ ] Handle KeyError
- [ ] Handle FileNotFoundError
- [ ] Handle file errors
- [ ] Handle functions
- [ ] Handle loops
- [ ] Handle JSON errors
- [ ] Understand API error handling

---

## Coding

- [ ] Solve beginner questions
- [ ] Solve intermediate questions
- [ ] Practice multiple exceptions
- [ ] Practice custom exceptions
- [ ] Practice `raise`
- [ ] Practice nested exceptions
- [ ] Build Safe Calculator

---

# 61. Key Takeaways

- `try` contains risky code.
- `except` handles exceptions.
- `else` runs when no exception occurs.
- `finally` always runs.
- `raise` manually generates an exception.
- Specific exceptions are generally preferred.
- Custom exceptions can be created using classes.
- Exception objects provide useful error information.
- Exception Handling improves program reliability.
- User input should be validated.
- File operations should handle possible errors.
- `with` is recommended for file handling.
- Errors should not be silently hidden.
- Exception Handling is widely used in real-world software.

---

# ⭐ Important Exceptions to Remember

```text
ValueError
    ↓
Invalid value

TypeError
    ↓
Wrong/incompatible data type

ZeroDivisionError
    ↓
Division by zero

IndexError
    ↓
Invalid list/sequence index

KeyError
    ↓
Missing dictionary key

NameError
    ↓
Undefined variable/name

FileNotFoundError
    ↓
File does not exist

AttributeError
    ↓
Object does not have requested attribute/method

ImportError
    ↓
Import problem

ModuleNotFoundError
    ↓
Module cannot be found

PermissionError
    ↓
Permission problem
```

---

# ⭐ Exception Handling Flow

```text
             START
               |
               ↓
          try block
               |
        ┌──────┴──────┐
        ↓             ↓
   No Exception    Exception
        |             |
        ↓             ↓
      else          except
        |             |
        └──────┬──────┘
               ↓
           finally
               |
               ↓
              END
```

---

# ⭐ Exception Handling Cheat Sheet

```python
# Basic

try:
    code()

except ValueError:
    print("Invalid value.")
```

```python
# Multiple exceptions

try:
    code()

except ValueError:
    print("Value error.")

except TypeError:
    print("Type error.")
```

```python
# Grouped exceptions

try:
    code()

except (ValueError, TypeError):
    print("Invalid operation.")
```

```python
# else

try:
    code()

except ValueError:
    print("Error.")

else:
    print("Success.")
```

```python
# finally

try:
    code()

except ValueError:
    print("Error.")

finally:
    print("Cleanup.")
```

```python
# Exception object

try:
    code()

except Exception as e:
    print("Error:", e)
```

```python
# raise

raise ValueError("Invalid value")
```

```python
# Custom exception

class MyError(Exception):
    pass
```

---

# 🚀 DAY 12 — 365 DAYS OF GROWTH

## Topic

Python Exception Handling

---

## Main Concepts

- Exception Handling
- Error vs Exception
- try
- except
- else
- finally
- Multiple Exceptions
- Built-in Exceptions
- Exception Objects
- raise
- Custom Exceptions
- Nested try-except
- Exception Propagation
- Exception Chaining
- Exception Re-raising
- File Exception Handling
- JSON Exception Handling
- User Input Validation
- Best Practices

---

## Mini Project

### Safe Calculator

The Safe Calculator demonstrates:

- Functions
- User Input
- try
- except
- ValueError
- ZeroDivisionError
- raise
- finally
- Input Validation

---

## Learning Outcome

After completing Day 12, you should be able to:

- Understand Python exceptions
- Identify common exceptions
- Handle runtime errors
- Use try-except
- Use else and finally
- Raise exceptions manually
- Create custom exceptions
- Handle user input errors
- Handle file errors
- Handle errors in functions and loops
- Build more reliable Python programs

---

# 🎯 DAY 12 COMPLETION CHECK

```text
Theory              ✅
Exception Basics    ✅
Built-in Errors     ✅
try-except          ✅
else                ✅
finally             ✅
raise               ✅
Custom Exception   ✅
Nested Exception   ✅
Exception Flow     ✅
Best Practices     ✅
Practice Questions  ✅
Mini Project        ✅
```

---

# 💡 FINAL REVISION

Remember this simple rule:

```text
try
    ↓
Run risky code

except
    ↓
Handle the error

else
    ↓
Run if everything is successful

finally
    ↓
Always execute

raise
    ↓
Create an exception manually
```

---

# 🔥 DAY 12 COMPLETE

## Python Exception Handling

### Keep Learning
### Keep Practicing
### Keep Building
### Keep Growing

# DAY 12 / 365 ✅