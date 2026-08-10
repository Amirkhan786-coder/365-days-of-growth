# 🚀 DAY 16 / 365 — Python Decorators & Higher-Order Functions

## 🐍 Python Advanced Concepts

> **Learn • Practice • Build • Grow**

---

# 📚 Today's Topics

1. Functions as First-Class Objects
2. Higher-Order Functions
3. Functions as Arguments
4. Functions Returning Functions
5. Nested Functions
6. What is a Decorator?
7. Decorator Syntax
8. Creating a Custom Decorator
9. Decorators with `*args` and `**kwargs`
10. Multiple Decorators
11. `functools.wraps`
12. Decorators with Arguments
13. Real-World Applications
14. Common Mistakes
15. Practice Examples

---

# 1️⃣ Functions as First-Class Objects

In Python, functions are treated as **first-class objects**.

This means a function can be:

- Stored in a variable
- Passed as an argument
- Returned from another function
- Stored inside a list, tuple, or dictionary

### Example

```python
def greet():
    print("Hello!")


message = greet

message()
```

### Output

```text
Hello!
```

Here:

```python
message = greet
```

stores the function inside the variable `message`.

---

# 2️⃣ Function as a Variable

A function can be assigned to another variable.

```python
def add():
    print("Addition")


operation = add

operation()
```

### Output

```text
Addition
```

Both variables refer to the same function.

---

# 3️⃣ Higher-Order Functions

A **Higher-Order Function** is a function that:

1. Takes another function as an argument, OR
2. Returns another function.

### Example

```python
def greet():
    print("Hello!")


def execute(function):
    function()


execute(greet)
```

### Output

```text
Hello!
```

Here:

```python
execute()
```

is a higher-order function because it receives another function.

---

# 4️⃣ Passing a Function as an Argument

A function can be passed to another function.

```python
def square(number):
    return number * number


def calculate(function, value):
    return function(value)


result = calculate(square, 5)

print(result)
```

### Output

```text
25
```

---

# 5️⃣ Function Returning Another Function

A function can also return another function.

### Example

```python
def outer():

    def inner():
        print("Hello from inner function")

    return inner


result = outer()

result()
```

### Output

```text
Hello from inner function
```

---

# 6️⃣ Nested Functions

A function defined inside another function is called a **nested function**.

### Example

```python
def outer():

    print("Outer function")

    def inner():
        print("Inner function")

    inner()


outer()
```

### Output

```text
Outer function
Inner function
```

---

# 7️⃣ What is a Decorator?

A **decorator** is a function that modifies or extends the behavior of another function without changing its original code.

In simple words:

```text
Original Function
       ↓
    Decorator
       ↓
Enhanced Function
```

Decorators are heavily used in real-world Python applications.

---

# 8️⃣ Basic Decorator

### Example

```python
def decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")

    return wrapper
```

Now apply it:

```python
@decorator
def greet():

    print("Hello!")


greet()
```

### Output

```text
Before function
Hello!
After function
```

---

# 9️⃣ Understanding `@` Syntax

This:

```python
@decorator
def greet():
    print("Hello")
```

is equivalent to:

```python
def greet():
    print("Hello")


greet = decorator(greet)
```

The `@` symbol makes decorator syntax cleaner.

---

# 🔟 Decorator Flow

Suppose we have:

```python
@decorator
def greet():
    print("Hello")
```

The flow is:

```text
greet()
   ↓
wrapper()
   ↓
Before function
   ↓
greet()
   ↓
Hello
   ↓
After function
```

---

# 1️⃣1️⃣ Decorator with `*args`

If the original function accepts arguments, the wrapper should also be able to accept them.

### Example

```python
def decorator(function):

    def wrapper(*args):

        print("Function is starting")

        function(*args)

        print("Function is finished")

    return wrapper


@decorator
def greet(name):

    print("Hello", name)


greet("Amir")
```

### Output

```text
Function is starting
Hello Amir
Function is finished
```

---

# 1️⃣2️⃣ Decorator with `*args` and `**kwargs`

For a flexible decorator, use:

```python
*args
**kwargs
```

### Example

```python
def decorator(function):

    def wrapper(*args, **kwargs):

        print("Function started")

        result = function(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper
```

This decorator can work with functions having different parameters.

---

# 1️⃣3️⃣ Returning a Value from a Decorated Function

A decorator should return the original function's result when needed.

### Example

```python
def decorator(function):

    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs)

        return result

    return wrapper


@decorator
def add(a, b):

    return a + b


result = add(10, 20)

print(result)
```

### Output

```text
30
```

---

# 1️⃣4️⃣ Multiple Decorators

A function can have multiple decorators.

### Example

```python
def decorator_one(function):

    def wrapper():

        print("Decorator One")

        function()

    return wrapper


def decorator_two(function):

    def wrapper():

        print("Decorator Two")

        function()

    return wrapper


@decorator_one
@decorator_two
def greet():

    print("Hello!")


greet()
```

Decorators are applied from the bottom upward.

---

# 1️⃣5️⃣ `functools.wraps`

When creating decorators, `functools.wraps` helps preserve metadata of the original function.

### Example

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        return function(*args, **kwargs)

    return wrapper
```

Without `wraps`, the wrapper function can replace useful metadata such as the original function's name and docstring.

---

# 1️⃣6️⃣ Decorator with Arguments

A decorator itself can also receive arguments.

This requires an additional function level.

### Example

```python
def repeat(times):

    def decorator(function):

        def wrapper():

            for i in range(times):

                function()

        return wrapper

    return decorator
```

Usage:

```python
@repeat(3)
def greet():

    print("Hello!")
```

### Output

```text
Hello!
Hello!
Hello!
```

---

# 1️⃣7️⃣ Real-World Use of Decorators

Decorators are useful in many applications.

### Common Uses

```text
Logging
Authentication
Authorization
Performance Monitoring
Caching
Validation
Access Control
Retry Mechanisms
Error Handling
```

---

# 1️⃣8️⃣ Logging Decorator

A logging decorator can record when a function is called.

### Example

```python
def logger(function):

    def wrapper(*args, **kwargs):

        print("Function called:", function.__name__)

        return function(*args, **kwargs)

    return wrapper


@logger
def greet(name):

    print("Hello", name)


greet("Amir")
```

---

# 1️⃣9️⃣ Performance Monitoring Decorator

Decorators can measure how long a function takes to execute.

### Example

```python
import time


def performance(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print("Execution time:",
              end - start,
              "seconds")

        return result

    return wrapper
```

Usage:

```python
@performance
def calculate():

    total = 0

    for i in range(1000000):

        total += i

    return total


calculate()
```

---

# 2️⃣0️⃣ Authentication Decorator

Decorators can also be used to check whether a user is authorized.

### Example

```python
def login_required(function):

    def wrapper(user):

        if user == "admin":

            return function(user)

        else:

            print("Access Denied")

    return wrapper


@login_required
def dashboard(user):

    print("Welcome to Dashboard")


dashboard("admin")
```

---

# 2️⃣1️⃣ Decorator vs Normal Function

### Normal Function

A normal function performs a specific task.

```python
def greet():

    print("Hello")
```

### Decorator

A decorator modifies or extends another function.

```python
def decorator(function):

    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper
```

---

# 2️⃣2️⃣ Advantages of Decorators

Decorators provide:

### ✅ Code Reusability

Write common functionality once.

### ✅ Cleaner Code

Keep additional functionality separate.

### ✅ Maintainability

Changes can be made inside the decorator.

### ✅ Modularity

Different behaviors can be added independently.

---

# 2️⃣3️⃣ Common Mistakes

## Mistake 1 — Forgetting to return wrapper

Wrong:

```python
def decorator(function):

    def wrapper():

        function()
```

Correct:

```python
def decorator(function):

    def wrapper():

        function()

    return wrapper
```

---

## Mistake 2 — Not passing arguments

If the original function requires arguments:

```python
def greet(name):
    print(name)
```

the wrapper should support them.

Use:

```python
def wrapper(*args, **kwargs):
```

---

## Mistake 3 — Forgetting the result

If the original function returns something:

```python
result = function(*args, **kwargs)
```

and return it:

```python
return result
```

---

# 2️⃣4️⃣ Important Syntax

### Basic Decorator

```python
def decorator(function):

    def wrapper():

        function()

    return wrapper
```

### Applying Decorator

```python
@decorator
def function():

    pass
```

### Flexible Decorator

```python
def decorator(function):

    def wrapper(*args, **kwargs):

        return function(*args, **kwargs)

    return wrapper
```

---

# 2️⃣5️⃣ Quick Revision

## First-Class Function

```text
Function can be stored,
passed and returned.
```

## Higher-Order Function

```text
Takes a function
OR
Returns a function
```

## Nested Function

```text
Function inside another function
```

## Decorator

```text
Adds or modifies behavior
of another function.
```

## `@`

```text
Cleaner decorator syntax
```

## `*args`

```text
Accept multiple positional arguments
```

## `**kwargs`

```text
Accept multiple keyword arguments
```

## `functools.wraps`

```text
Preserves original function metadata
```

---

# 🧠 Important Example

```python
from functools import wraps


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Calling:", function.__name__)

        result = function(*args, **kwargs)

        print("Completed:", function.__name__)

        return result

    return wrapper


@logger
def add(a, b):

    return a + b


result = add(10, 20)

print("Result:", result)
```

### Output

```text
Calling: add
Completed: add
Result: 30
```

---

# 🎯 Day 16 Key Takeaways

```text
Functions
    ↓
First-Class Functions
    ↓
Higher-Order Functions
    ↓
Nested Functions
    ↓
Decorators
    ↓
*args / **kwargs
    ↓
functools.wraps
    ↓
Real-World Applications
```

---

# 🏆 DAY 16 GOAL

By the end of today, I should be able to:

- [ ] Explain first-class functions
- [ ] Explain higher-order functions
- [ ] Pass functions as arguments
- [ ] Return functions from functions
- [ ] Create nested functions
- [ ] Create custom decorators
- [ ] Use `@` syntax
- [ ] Use `*args` and `**kwargs`
- [ ] Create decorators with arguments
- [ ] Use multiple decorators
- [ ] Understand `functools.wraps`
- [ ] Build practical decorators

---

# 🚀 MINI PROJECT

## Performance Monitor & Access Logger

Build a practical decorator-based project that:

- Measures function execution time
- Logs function calls
- Stores logs in a file
- Uses `*args` and `**kwargs`
- Uses `functools.wraps`
- Demonstrates reusable decorators

---

# 🔥 DAY 16 MOTIVATION

> **"Don't just write functions. Learn how to make functions work smarter."**

## 🚀 Learn → Practice → Build → Grow

**DAY 16 / 365 ✅**