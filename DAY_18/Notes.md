
# 🚀 DAY 18 / 365 — PYTHON EXCEPTION HANDLING

> Continuing my 365 Days of Growth journey 🚀

---

## 📅 Day 18

Today I learned about **Exception Handling in Python**.

Exception handling helps programs handle unexpected situations without suddenly crashing.

I learned how to detect errors, handle exceptions, create custom exceptions, and write safer and more reliable Python programs.

---

# 📚 TODAY'S TOPICS

1. Errors vs Exceptions
2. Syntax Errors
3. Runtime Errors
4. Exceptions
5. `try`
6. `except`
7. `else`
8. `finally`
9. Multiple `except` Blocks
10. Exception as `e`
11. Common Built-in Exceptions
12. `ValueError`
13. `TypeError`
14. `ZeroDivisionError`
15. `IndexError`
16. `KeyError`
17. `FileNotFoundError`
18. `raise`
19. Custom Exceptions
20. Exception Handling Best Practices
21. Real-World Applications

---

# 🧠 1. ERRORS VS EXCEPTIONS

Errors are problems that occur while writing or executing a program.

Python programs can encounter different types of errors.

The major categories are:

```text
Syntax Errors
Runtime Errors
Exceptions
````

Understanding errors helps us write better and more reliable programs.

---

# 📝 2. SYNTAX ERRORS

A SyntaxError occurs when Python code does not follow the correct syntax.

### Example

```python
if True
    print("Hello")
```

The above code is incorrect because the `if` statement is missing a colon.

### Correct Code

```python
if True:
    print("Hello")
```

---

# ⚡ 3. RUNTIME ERRORS

Runtime errors occur while the program is executing.

Example:

```python
number = 10

result = number / 0
```

The program starts running but produces a `ZeroDivisionError`.

Runtime errors are commonly handled using exception handling.

---

# 🚨 4. EXCEPTIONS

An exception is an event that interrupts the normal execution of a program.

Example:

```python
number = int("Python")
```

This produces:

```text
ValueError
```

We can handle exceptions using:

```python
try
except
```

---

# 🛡️ 5. TRY

The `try` block contains code that may produce an exception.

### Example

```python
try:

    number = int(input("Enter a number: "))

    print(number)

except ValueError:

    print("Please enter a valid number.")
```

---

# 🛡️ 6. EXCEPT

The `except` block handles an exception.

### Example

```python
try:

    result = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero.")
```

### Output

```text
Cannot divide by zero.
```

---

# ✅ 7. ELSE

The `else` block runs only when no exception occurs.

### Example

```python
try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid input.")

else:

    print("You entered:", number)
```

---

# 🔚 8. FINALLY

The `finally` block runs whether an exception occurs or not.

### Example

```python
try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid input.")

finally:

    print("Program finished.")
```

---

# 🔄 9. MULTIPLE EXCEPT BLOCKS

We can handle different exceptions separately.

### Example

```python
try:

    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:

    print("Please enter a valid number.")

except ZeroDivisionError:

    print("Cannot divide by zero.")
```

This allows us to provide different messages for different errors.

---

# 🧩 10. EXCEPTION AS `e`

We can store the exception object using `as`.

### Example

```python
try:

    number = int("Python")

except ValueError as e:

    print("Error:", e)
```

The variable `e` contains information about the exception.

---

# 🧨 11. COMMON BUILT-IN EXCEPTIONS

Python provides many built-in exceptions.

Important exceptions include:

```text
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
NameError
AttributeError
ImportError
OSError
```

---

# 🔢 12. VALUEERROR

`ValueError` occurs when a function receives a value of the correct type but an inappropriate value.

### Example

```python
number = int("abc")
```

### Handling ValueError

```python
try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid number.")
```

---

# 🔤 13. TYPEERROR

`TypeError` occurs when an operation is performed on an inappropriate data type.

### Example

```python
number = 10

text = "Python"

result = number + text
```

### Handling TypeError

```python
try:

    result = 10 + "Python"

except TypeError:

    print("Cannot add integer and string.")
```

---

# ➗ 14. ZERODIVISIONERROR

`ZeroDivisionError` occurs when a number is divided by zero.

### Example

```python
try:

    result = 10 / 0

except ZeroDivisionError:

    print("Division by zero is not allowed.")
```

---

# 📋 15. INDEXERROR

`IndexError` occurs when we try to access an index that does not exist.

### Example

```python
numbers = [10, 20, 30]

try:

    print(numbers[5])

except IndexError:

    print("Index does not exist.")
```

---

# 🔑 16. KEYERROR

`KeyError` occurs when we try to access a dictionary key that does not exist.

### Example

```python
student = {
    "name": "Aman",
    "age": 20
}

try:

    print(student["course"])

except KeyError:

    print("Key does not exist.")
```

---

# 📁 17. FILENOTFOUNDERROR

`FileNotFoundError` occurs when Python cannot find the requested file.

### Example

```python
try:

    file = open("data.txt")

except FileNotFoundError:

    print("File not found.")
```

---

# 🚨 18. RAISE

The `raise` statement allows us to manually generate an exception.

### Example

```python
age = 15

if age < 18:

    raise ValueError("Age must be 18 or above.")
```

---

# 🧱 19. CUSTOM EXCEPTIONS

We can create our own exception classes.

### Example

```python
class AgeError(Exception):

    pass
```

We can then use the custom exception:

```python
age = 15

if age < 18:

    raise AgeError("Age must be 18 or above.")
```

Custom exceptions make large programs easier to understand and maintain.

---

# 🔥 20. COMPLETE TRY-EXCEPT-ELSE-FINALLY

The complete structure can look like this:

```python
try:

    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:

    print("Invalid input.")

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Result:", result)

finally:

    print("Program execution completed.")
```

---

# 🔄 EXCEPTION HANDLING FLOW

```text
Program Starts
      ↓
    try
      ↓
Code Executes
      ↓
 ┌────┴─────┐
 ↓          ↓
No Error   Error
 ↓          ↓
else      except
 └────┬─────┘
      ↓
   finally
      ↓
Program Ends
```

---

# 🧪 21. PRACTICAL EXAMPLES

## Example 1 — Safe Division

```python
try:

    first = int(input("Enter first number: "))

    second = int(input("Enter second number: "))

    result = first / second

    print("Result:", result)

except ValueError:

    print("Please enter numbers only.")

except ZeroDivisionError:

    print("Cannot divide by zero.")
```

---

## Example 2 — Safe List Access

```python
numbers = [10, 20, 30]

try:

    index = int(input("Enter index: "))

    print(numbers[index])

except ValueError:

    print("Enter a valid integer.")

except IndexError:

    print("Index is outside the list.")
```

---

## Example 3 — Safe Dictionary Access

```python
student = {
    "name": "Aman",
    "age": 20
}

try:

    key = input("Enter key: ")

    print(student[key])

except KeyError:

    print("Key not found.")
```

---

# 🧠 EXCEPTION HANDLING BEST PRACTICES

Good exception handling should:

* Handle specific exceptions
* Avoid unnecessary broad `except`
* Provide meaningful error messages
* Keep error handling simple
* Use `finally` when cleanup is required
* Validate user input
* Use custom exceptions when necessary
* Avoid hiding important errors
* Keep normal program logic separate from error handling

---

# 🌍 REAL-WORLD APPLICATIONS

Exception handling is commonly used in:

```text
User Input Validation
File Processing
Database Applications
API Requests
Web Applications
Payment Systems
Authentication Systems
Data Processing
Network Applications
Backend Applications
```

---

# 💻 PRACTICE TASKS

Today I will practice:

```text
1. Safe Division
2. User Input Validation
3. Multiple Exceptions
4. List Index Handling
5. Dictionary Key Handling
6. File Handling Exceptions
7. Custom Exceptions
8. raise
9. try-except-else-finally
10. Error Handling in Real Applications
```

---

# 🎯 KEY TAKEAWAYS

```text
try
 ↓
Code that may cause an exception

except
 ↓
Handles the exception

else
 ↓
Runs when no exception occurs

finally
 ↓
Runs whether an exception occurs or not

raise
 ↓
Manually creates an exception
```

---

# 🏆 DAY 18 GOAL

By the end of Day 18, I should be able to:

* Understand errors and exceptions
* Use `try`
* Use `except`
* Use `else`
* Use `finally`
* Handle multiple exceptions
* Understand common built-in exceptions
* Use exception messages
* Use `raise`
* Create custom exceptions
* Build safer Python programs

---

# 💡 KEY LEARNING

> Exception handling makes Python programs more reliable by allowing unexpected situations to be handled gracefully instead of crashing the entire program.

---

# 📈 365 DAYS OF GROWTH

**Day 18 / 365**

```text
█████░░░░░░░░░░░░░░░  4.9%
```

---

# 🔥 MY COMMITMENT

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

**18 / 365 — Keep Growing 🚀**


