
# 🚀 DAY 18 / 365 — PYTHON EXCEPTION HANDLING
# 🧠 MCQs — 30 QUESTIONS

> Continuing my 365 Days of Growth journey 🚀

---

## Q1. What is an exception in Python?

A. A variable  
B. A runtime error  
C. A loop  
D. A function  

**Answer:** B. A runtime error

---

## Q2. Which keyword is used to handle exceptions?

A. error  
B. catch  
C. except  
D. handle  

**Answer:** C. except

---

## Q3. Which keyword contains code that may generate an exception?

A. try  
B. except  
C. finally  
D. raise  

**Answer:** A. try

---

## Q4. Which block executes when no exception occurs?

A. catch  
B. else  
C. error  
D. raise  

**Answer:** B. else

---

## Q5. Which block normally executes whether an exception occurs or not?

A. try  
B. except  
C. else  
D. finally  

**Answer:** D. finally

---

## Q6. Which exception occurs when dividing a number by zero?

A. ValueError  
B. TypeError  
C. ZeroDivisionError  
D. ArithmeticError  

**Answer:** C. ZeroDivisionError

---

## Q7. Which exception occurs when converting `"Python"` to an integer?

A. TypeError  
B. ValueError  
C. KeyError  
D. IndexError  

**Answer:** B. ValueError

---

## Q8. Which exception occurs when accessing an invalid list index?

A. IndexError  
B. KeyError  
C. ValueError  
D. TypeError  

**Answer:** A. IndexError

---

## Q9. Which exception occurs when accessing a missing dictionary key?

A. IndexError  
B. ValueError  
C. KeyError  
D. NameError  

**Answer:** C. KeyError

---

## Q10. Which exception occurs when a file does not exist?

A. FileError  
B. FileNotFoundError  
C. IOError  
D. OpenError  

**Answer:** B. FileNotFoundError

---

## Q11. Which keyword is used to manually raise an exception?

A. throw  
B. error  
C. raise  
D. exception  

**Answer:** C. raise

---

## Q12. Which class is commonly used as the base class for custom exceptions?

A. Error  
B. Exception  
C. Base  
D. Runtime  

**Answer:** B. Exception

---

## Q13. What does `as e` do in an except block?

A. Creates a loop  
B. Stores the exception object  
C. Stops the program  
D. Creates a function  

**Answer:** B. Stores the exception object

---

## Q14. Which of the following is valid?

A.

```python
try:
    print("Hello")
except:
    print("Error")
````

B.

```python
try:
    print("Hello")
catch:
    print("Error")
```

C.

```python
try:
    print("Hello")
handle:
    print("Error")
```

D.

```python
try:
    print("Hello")
error:
    print("Error")
```

**Answer:** A

---

## Q15. What happens if an exception is not handled?

A. Program automatically fixes it
B. Program continues normally
C. Program may terminate with a traceback
D. Python ignores it

**Answer:** C. Program may terminate with a traceback

---

## Q16. Which exception occurs in this code?

```python
print(10 / 0)
```

A. ValueError
B. TypeError
C. ZeroDivisionError
D. IndexError

**Answer:** C. ZeroDivisionError

---

## Q17. Which exception occurs here?

```python
number = int("hello")
```

A. TypeError
B. ValueError
C. KeyError
D. IndexError

**Answer:** B. ValueError

---

## Q18. Which exception occurs here?

```python
numbers = [10, 20, 30]
print(numbers[5])
```

A. KeyError
B. ValueError
C. IndexError
D. TypeError

**Answer:** C. IndexError

---

## Q19. Which exception occurs here?

```python
student = {"name": "Aman"}
print(student["age"])
```

A. KeyError
B. IndexError
C. ValueError
D. TypeError

**Answer:** A. KeyError

---

## Q20. Which exception occurs here?

```python
result = 10 + "20"
```

A. ValueError
B. TypeError
C. KeyError
D. ZeroDivisionError

**Answer:** B. TypeError

---

## Q21. Can Python have multiple `except` blocks?

A. Yes
B. No
C. Only two
D. Only three

**Answer:** A. Yes

---

## Q22. Can we use `try` with `finally` without `except`?

A. Yes
B. No
C. Only in Python 2
D. Only with custom exceptions

**Answer:** A. Yes

---

## Q23. What is the purpose of `finally`?

A. Handle only ValueError
B. Run cleanup code
C. Create exceptions
D. Stop loops

**Answer:** B. Run cleanup code

---

## Q24. Which is the correct custom exception?

A.

```python
class MyError(Exception):
    pass
```

B.

```python
exception MyError:
    pass
```

C.

```python
class MyError(Error):
    pass
```

D.

```python
create MyError(Exception)
```

**Answer:** A

---

## Q25. What will this code do?

```python
try:
    number = 10
except:
    print("Error")
else:
    print("Success")
```

A. Prints Error
B. Prints Success
C. Prints nothing
D. Gives syntax error

**Answer:** B. Prints Success

---

## Q26. What will this code print?

```python
try:
    print("A")
finally:
    print("B")
```

A. A
B. B
C. A then B
D. Error

**Answer:** C. A then B

---

## Q27. Which statement is best for specific exception handling?

A.

```python
except:
```

B.

```python
except Exception:
```

C.

```python
except ValueError:
```

D.

```python
except Error:
```

**Answer:** C. `except ValueError:`

---

## Q28. What is exception propagation?

A. Creating a new variable
B. Moving an exception up through function calls until handled
C. Deleting an exception
D. Converting an exception into a string

**Answer:** B. Moving an exception up through function calls until handled

---

## Q29. Which combination represents the main Python exception-handling keywords?

A. if, else, loop
B. try, except, else, finally
C. for, while, break
D. class, object, method

**Answer:** B. try, except, else, finally

---

## Q30. Why is exception handling important?

A. It makes code longer
B. It prevents many runtime problems from crashing the program
C. It removes all errors automatically
D. It replaces functions

**Answer:** B. It prevents many runtime problems from crashing the program

---

# 🧠 QUICK REVISION

```text
try
 ↓
Risky Code
 ↓
Exception?
 ↓
YES → except → Handle Error
 ↓
NO → else → Continue Normally
 ↓
finally → Cleanup / Always Execute
```

---

# 📚 IMPORTANT EXCEPTIONS

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

# 🏆 DAY 18 MCQs COMPLETED

```text
30 MCQs
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
File Handling
    ↓
Input Validation
    ↓
Day 18 MCQs Completed ✅
```

---

# 🔥 365 DAYS OF GROWTH

**Day 18 / 365**

> Learn every day.
> Practice every day.
> Build every day.
> Become better every day.

**18 / 365 — Keep Growing 🚀**



