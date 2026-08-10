# 🧪 DAY 16 — Python Decorators & Higher-Order Functions
# 30 Practice Questions

---

## 🟢 BASIC LEVEL

### Q1. First-Class Function
Create a function `greet()` and store it in another variable. Call the function using the new variable.

---

### Q2. Function as Argument
Create a function `square()` and pass it as an argument to another function.

---

### Q3. Function Returning Function
Create a function `outer()` that returns an `inner()` function.

---

### Q4. Nested Function
Create a function containing another function and call the inner function from the outer function.

---

### Q5. Higher-Order Function
Create a higher-order function that accepts a function and a number, then applies the function to the number.

---

### Q6. Addition Function
Create an `add()` function and pass it to a higher-order function.

---

### Q7. Multiplication Function
Create a `multiply()` function and execute it through another function.

---

### Q8. Function Reference
Create a function `hello()` and assign it to three different variables. Call all three.

---

### Q9. List of Functions
Create a list containing three functions and execute all functions using a loop.

---

### Q10. Function Factory
Create a function that returns different functions for addition and multiplication.

---

# 🟡 INTERMEDIATE LEVEL

### Q11. Basic Decorator
Create a decorator that prints:

```text
Before Function
After Function
```

around another function.

---

### Q12. Greeting Decorator
Create a decorator that prints:

```text
Welcome!
```

before executing a greeting function.

---

### Q13. Logging Decorator
Create a decorator that prints the name of the function whenever it is called.

---

### Q14. Decorator with Arguments
Create a decorator that works with a function accepting a name.

Example:

```text
Hello Amir
```

---

### Q15. Decorator with `*args`
Create a decorator that can handle any number of positional arguments.

---

### Q16. Decorator with `**kwargs`
Create a decorator that can handle keyword arguments.

---

### Q17. Flexible Decorator
Create a decorator using both:

```python
*args
**kwargs
```

---

### Q18. Return Value
Create a decorator that preserves and returns the result of the decorated function.

---

### Q19. Addition Decorator
Create a decorator for an addition function.

The decorator should print:

```text
Calculating...
```

before the calculation.

---

### Q20. Execution Time
Create a decorator that measures the execution time of a function using the `time` module.

---

# 🟠 ADVANCED LEVEL

### Q21. Multiple Decorators
Create two decorators and apply both to the same function.

---

### Q22. Authentication Decorator
Create a decorator that allows a function to execute only when the username is:

```text
admin
```

Otherwise print:

```text
Access Denied
```

---

### Q23. Permission Decorator
Create a decorator that checks whether the user has permission before accessing a function.

---

### Q24. Repeat Decorator
Create a decorator that executes a function a specified number of times.

Example:

```python
@repeat(3)
def hello():
    print("Hello")
```

Expected:

```text
Hello
Hello
Hello
```

---

### Q25. Validation Decorator
Create a decorator that checks whether a number is positive before executing the function.

---

### Q26. Even Number Decorator
Create a decorator that allows a function to execute only when the given number is even.

---

### Q27. `functools.wraps`
Create a decorator using:

```python
from functools import wraps
```

and preserve the original function's name and docstring.

---

### Q28. Logging to File
Create a decorator that writes the function name and arguments to:

```text
logs.txt
```

---

### Q29. Performance Monitor
Create a decorator that:

- Records start time
- Executes the function
- Records end time
- Calculates execution time
- Prints the execution time

---

### Q30. Real-World Challenge
Create a mini decorator system containing:

```text
@logger
@performance
@authentication
```

The program should:

1. Check authentication.
2. Log the function call.
3. Measure execution time.
4. Execute the function.
5. Return the result.

---

# 🎯 CHALLENGE RULES

For every question:

- Write the code yourself.
- Run the program.
- Check the output.
- Fix errors.
- Understand the logic.
- Save the code separately.

---

# 📂 Recommended Practice Structure

```text
Day16/
│
├── practice_questions.md
│
└── practice/
    ├── q01.py
    ├── q02.py
    ├── q03.py
    ├── q04.py
    ├── q05.py
    ├── q06.py
    ├── q07.py
    ├── q08.py
    ├── q09.py
    ├── q10.py
    ├── q11.py
    ├── q12.py
    ├── q13.py
    ├── q14.py
    ├── q15.py
    ├── q16.py
    ├── q17.py
    ├── q18.py
    ├── q19.py
    ├── q20.py
    ├── q21.py
    ├── q22.py
    ├── q23.py
    ├── q24.py
    ├── q25.py
    ├── q26.py
    ├── q27.py
    ├── q28.py
    ├── q29.py
    └── q30.py
```

# 🏆 Target

```text
30 Questions
     ↓
30 Separate Programs
     ↓
Practice
     ↓
Debugging
     ↓
Better Python Skills 🚀
```

**Day 16 Practice: 30 Questions ✅**