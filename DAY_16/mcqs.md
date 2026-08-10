# 🧠 DAY 16 — Python Decorators & Higher-Order Functions
# MCQs

---

## Q1. In Python, functions are treated as:

A. Variables only  
B. First-class objects  
C. Strings  
D. Keywords  

**Answer:** B

---

## Q2. Which of the following can a function do in Python?

A. Be stored in a variable  
B. Be passed as an argument  
C. Be returned from another function  
D. All of the above  

**Answer:** D

---

## Q3. What is a Higher-Order Function?

A. A function with many lines  
B. A function that takes or returns another function  
C. A built-in function  
D. A private function  

**Answer:** B

---

## Q4. What is the output?

```python
def greet():
    print("Hello")


x = greet
x()
```

A. Error  
B. greet  
C. Hello  
D. None  

**Answer:** C

---

## Q5. A function defined inside another function is called:

A. Higher function  
B. Nested function  
C. Main function  
D. Parent function  

**Answer:** B

---

## Q6. What does a decorator do?

A. Deletes a function  
B. Changes Python syntax  
C. Extends or modifies a function's behavior  
D. Converts a function to a class  

**Answer:** C

---

## Q7. Which symbol is commonly used to apply a decorator?

A. #  
B. @  
C. $  
D. &  

**Answer:** B

---

## Q8. What does this mean?

```python
@decorator
def greet():
    pass
```

A. `greet` is deleted  
B. `decorator` is ignored  
C. `greet` is passed through `decorator`  
D. `decorator` becomes a variable  

**Answer:** C

---

## Q9. Which function is usually returned by a basic decorator?

A. Main function  
B. Wrapper function  
C. Class function  
D. Built-in function  

**Answer:** B

---

## Q10. What is the purpose of `*args`?

A. Accept multiple positional arguments  
B. Accept multiple files  
C. Create a class  
D. Create a decorator  

**Answer:** A

---

## Q11. What is the purpose of `**kwargs`?

A. Accept multiple positional arguments  
B. Accept multiple keyword arguments  
C. Create a loop  
D. Create a list  

**Answer:** B

---

## Q12. Which module provides `wraps`?

A. time  
B. os  
C. functools  
D. random  

**Answer:** C

---

## Q13. Why is `functools.wraps` used?

A. To speed up Python  
B. To preserve metadata of the original function  
C. To create a class  
D. To delete decorators  

**Answer:** B

---

## Q14. What does `function.__name__` return?

A. Function result  
B. Function arguments  
C. Function name  
D. Function type  

**Answer:** C

---

## Q15. Which statement is correct?

A. A decorator must always accept two arguments  
B. A decorator can wrap another function  
C. Decorators can only be used with classes  
D. Decorators cannot return values  

**Answer:** B

---

## Q16. What is the output?

```python
def double(x):
    return x * 2


def calculate(function, value):
    return function(value)


print(calculate(double, 5))
```

A. 5  
B. 7  
C. 10  
D. 25  

**Answer:** C

---

## Q17. Which is a real-world use of decorators?

A. Logging  
B. Authentication  
C. Performance monitoring  
D. All of the above  

**Answer:** D

---

## Q18. A decorator can be used without changing:

A. The original function's code  
B. Python's interpreter  
C. The operating system  
D. The programming language  

**Answer:** A

---

## Q19. What should a flexible decorator generally use?

A. `*args` and `**kwargs`  
B. `if` and `else` only  
C. `for` only  
D. `list` only  

**Answer:** A

---

## Q20. What does this return?

```python
def outer():

    def inner():
        return "Hello"

    return inner
```

A. `"Hello"`  
B. `inner` function  
C. `outer` string  
D. Error  

**Answer:** B

---

## Q21. Which statement about decorators is TRUE?

A. A decorator can add functionality to a function  
B. A decorator can only work with numbers  
C. A decorator cannot accept arguments  
D. A decorator cannot return anything  

**Answer:** A

---

## Q22. What does `time.time()` commonly help with?

A. Authentication  
B. Measuring execution time  
C. Creating decorators  
D. Creating classes  

**Answer:** B

---

## Q23. Which decorator could be used to check whether a user is logged in?

A. `@login_required`  
B. `@math`  
C. `@number`  
D. `@python`  

**Answer:** A

---

## Q24. What is the purpose of returning `result` from a wrapper?

A. To preserve the decorated function's result  
B. To stop Python  
C. To create a class  
D. To delete the function  

**Answer:** A

---

## Q25. Which code correctly defines a decorator?

A.

```python
def decorator():
    pass
```

B.

```python
def decorator(function):

    def wrapper():
        function()

    return wrapper
```

C.

```python
decorator = class()
```

D.

```python
@function
```

**Answer:** B

---

## Q26. What happens with multiple decorators?

```python
@decorator1
@decorator2
def greet():
    pass
```

A. Both decorators can be applied  
B. Only decorator1 works  
C. Only decorator2 works  
D. Syntax error  

**Answer:** A

---

## Q27. Which decorator can be used to repeat a function?

A. `@repeat`  
B. `@loop`  
C. `@again`  
D. `@run`  

**Answer:** A

---

## Q28. Which concept allows a function to be passed to another function?

A. Inheritance  
B. First-class functions  
C. Encapsulation  
D. Polymorphism  

**Answer:** B

---

## Q29. Which is NOT a common use of decorators?

A. Logging  
B. Authentication  
C. Performance monitoring  
D. Changing the Python interpreter  

**Answer:** D

---

## Q30. What is the main benefit of decorators?

A. Code reusability  
B. Code deletion  
C. Removing functions  
D. Avoiding Python  

**Answer:** A

---

# 🔥 BONUS MCQs

## Q31. Which statement is correct about `*args`?

A. It stores arguments as a tuple  
B. It stores arguments as a dictionary  
C. It stores arguments as a list  
D. It stores only one argument  

**Answer:** A

---

## Q32. Which statement is correct about `**kwargs`?

A. It stores keyword arguments as a dictionary  
B. It stores arguments as a tuple  
C. It stores only integers  
D. It creates a class  

**Answer:** A

---

## Q33. What does this decorator do?

```python
@logger
def calculate():
    pass
```

A. Adds logging behavior  
B. Deletes calculate  
C. Converts calculate into a variable  
D. Stops the function  

**Answer:** A

---

## Q34. Which import is correct for `wraps`?

A.

```python
from functools import wraps
```

B.

```python
import wraps
```

C.

```python
from decorator import wraps
```

D.

```python
import functools.wraps
```

**Answer:** A

---

## Q35. Decorators are especially useful because they promote:

A. Code duplication  
B. Code reusability  
C. Code deletion  
D. Syntax errors  

**Answer:** B

---

# 🏆 DAY 16 MCQ SCORE

Total Questions:

```text
35
```

My Score:

```text
____ / 35
```

Percentage:

```text
____ %
```

---

# 🎯 Target

```text
30+  → Excellent 🔥
25-29 → Very Good 💪
20-24 → Good 👍
Below 20 → Revise Topics 📚
```

## 🚀 Day 16 MCQ Practice Complete