# 📝 Day 12 — MCQs
# Python Exception Handling

# 365 Days of Growth

---

## Q1. Which keyword is used to handle exceptions in Python?

A. error  
B. catch  
C. except  
D. handle  

**Answer: C. except**

---

## Q2. Which block contains code that may generate an exception?

A. except  
B. try  
C. finally  
D. else  

**Answer: B. try**

---

## Q3. Which block always executes whether an exception occurs or not?

A. try  
B. except  
C. else  
D. finally  

**Answer: D. finally**

---

## Q4. Which block executes when no exception occurs?

A. except  
B. else  
C. finally  
D. error  

**Answer: B. else**

---

## Q5. Which exception occurs when dividing a number by zero?

A. ValueError  
B. TypeError  
C. ZeroDivisionError  
D. ArithmeticError  

**Answer: C. ZeroDivisionError**

---

## Q6. What exception occurs when converting an invalid string to an integer?

```python
int("hello")
```

A. TypeError  
B. ValueError  
C. NameError  
D. IndexError  

**Answer: B. ValueError**

---

## Q7. What exception occurs in this code?

```python
numbers = [10, 20, 30]

print(numbers[5])
```

A. KeyError  
B. ValueError  
C. IndexError  
D. TypeError  

**Answer: C. IndexError**

---

## Q8. What exception occurs when accessing a dictionary key that does not exist?

A. IndexError  
B. KeyError  
C. ValueError  
D. NameError  

**Answer: B. KeyError**

---

## Q9. What exception occurs in this code?

```python
result = "10" + 5
```

A. ValueError  
B. TypeError  
C. KeyError  
D. SyntaxError  

**Answer: B. TypeError**

---

## Q10. Which keyword is used to manually raise an exception?

A. throw  
B. error  
C. raise  
D. exception  

**Answer: C. raise**

---

## Q11. Which keyword is used to define a custom exception class?

A. class  
B. exception  
C. custom  
D. define  

**Answer: A. class**

---

## Q12. A custom exception should normally inherit from:

A. object  
B. Error  
C. Exception  
D. Runtime  

**Answer: C. Exception**

---

## Q13. What does `as e` do?

```python
except ValueError as e:
```

A. Creates a new exception  
B. Stores the exception object in `e`  
C. Deletes the exception  
D. Stops the program  

**Answer: B. Stores the exception object in `e`**

---

## Q14. What will be the output?

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Error")
```

A. 10  
B. 0  
C. Error  
D. Nothing  

**Answer: C. Error**

---

## Q15. What will be the output?

```python
try:
    number = int("10")

except ValueError:
    print("Invalid")

else:
    print("Valid")
```

A. Invalid  
B. Valid  
C. Error  
D. Nothing  

**Answer: B. Valid**

---

## Q16. What will be the output?

```python
try:
    print("Hello")

finally:
    print("Python")
```

A. Hello  
B. Python  
C. Hello then Python  
D. Error  

**Answer: C. Hello then Python**

---

## Q17. Which syntax is correct?

A.

```python
try:
    code()
catch:
    error()
```

B.

```python
try:
    code()

except:
    error()
```

C.

```python
try:
    code()

handle:
    error()
```

D.

```python
try:
    code()

error:
    error()
```

**Answer: B**

---

## Q18. Can Python have multiple `except` blocks?

A. Yes  
B. No  
C. Only two  
D. Only three  

**Answer: A. Yes**

---

## Q19. Which is better than using a bare `except`?

A. Specific exception  
B. No exception  
C. SyntaxError  
D. print statement  

**Answer: A. Specific exception**

---

## Q20. What is a bare except?

A. `except ValueError:`  
B. `except TypeError:`  
C. `except:`  
D. `except Exception:`  

**Answer: C. `except:`**

---

## Q21. Which exception occurs when a variable is not defined?

A. NameError  
B. ValueError  
C. TypeError  
D. KeyError  

**Answer: A. NameError**

---

## Q22. Which exception occurs when a file does not exist?

A. FileError  
B. FileNotFoundError  
C. IOErrorOnly  
D. MissingFileError  

**Answer: B. FileNotFoundError**

---

## Q23. What will happen?

```python
try:
    x = 10
    print(x)

except:
    print("Error")
```

A. Error  
B. 10  
C. None  
D. SyntaxError  

**Answer: B. 10**

---

## Q24. What will happen?

```python
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Done")
```

A. Cannot divide  
B. Done  
C. Cannot divide then Done  
D. Error  

**Answer: C. Cannot divide then Done**

---

## Q25. Which block should normally come after `try`?

A. except  
B. class  
C. import  
D. def  

**Answer: A. except**

---

## Q26. Which exception is raised here?

```python
age = int("abc")
```

A. TypeError  
B. ValueError  
C. IndexError  
D. KeyError  

**Answer: B. ValueError**

---

## Q27. Which exception is raised here?

```python
result = 10 / 0
```

A. ValueError  
B. TypeError  
C. ZeroDivisionError  
D. IndexError  

**Answer: C. ZeroDivisionError**

---

## Q28. Which exception is raised here?

```python
data = {"name": "Amir"}

print(data["age"])
```

A. IndexError  
B. KeyError  
C. ValueError  
D. NameError  

**Answer: B. KeyError**

---

## Q29. Which exception is raised here?

```python
numbers = [1, 2, 3]

print(numbers[10])
```

A. KeyError  
B. IndexError  
C. ValueError  
D. TypeError  

**Answer: B. IndexError**

---

## Q30. Which exception is raised here?

```python
"10" + 20
```

A. TypeError  
B. ValueError  
C. KeyError  
D. NameError  

**Answer: A. TypeError**

---

## Q31. What does `raise` do?

A. Handles an exception  
B. Creates or manually triggers an exception  
C. Deletes an exception  
D. Ignores an exception  

**Answer: B. Creates or manually triggers an exception**

---

## Q32. What is Exception Propagation?

A. Deleting an exception  
B. Passing an unhandled exception to the calling code  
C. Creating a custom exception  
D. Ignoring an exception  

**Answer: B. Passing an unhandled exception to the calling code**

---

## Q33. What is Exception Chaining?

A. Handling multiple lists  
B. One exception causing another exception  
C. Deleting exceptions  
D. Creating multiple classes  

**Answer: B. One exception causing another exception**

---

## Q34. Which syntax is used for exception chaining?

A.

```python
raise error
```

B.

```python
raise ... from e
```

C.

```python
chain error
```

D.

```python
except from e
```

**Answer: B. `raise ... from e`**

---

## Q35. Which statement is TRUE about `finally`?

A. It executes only when an exception occurs  
B. It executes only when no exception occurs  
C. It generally executes whether an exception occurs or not  
D. It never executes  

**Answer: C. It generally executes whether an exception occurs or not**

---

# ⭐ QUICK REVISION

| Concept | Keyword / Exception |
|---|---|
| Risky code | `try` |
| Handle exception | `except` |
| No exception | `else` |
| Cleanup | `finally` |
| Manually raise | `raise` |
| Exception object | `as e` |
| Invalid value | `ValueError` |
| Wrong data type operation | `TypeError` |
| Division by zero | `ZeroDivisionError` |
| Invalid list index | `IndexError` |
| Missing dictionary key | `KeyError` |
| Undefined variable | `NameError` |
| Missing file | `FileNotFoundError` |

---

# 🎯 DAY 12 MCQ SCORE

```text
31–35 = 🔥 Excellent
26–30 = ⭐ Very Good
20–25 = 👍 Good
15–19 = 📚 Need More Practice
Below 15 = 🔄 Revise Exception Handling
```

---

# 🏆 DAY 12 — MCQs COMPLETE

## Topic: Python Exception Handling

**35 MCQs Completed ✅**

# DAY 12 / 365 🚀