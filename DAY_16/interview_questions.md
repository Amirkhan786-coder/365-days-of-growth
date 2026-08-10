# 🎤 DAY 16 — Python Decorators & Higher-Order Functions
# Interview Questions & Answers

---

## Q1. What is a first-class function in Python?

**Answer:**

In Python, functions are first-class objects.

This means a function can be:

- Stored in a variable
- Passed as an argument
- Returned from another function
- Stored in a data structure

Example:

```python
def greet():
    print("Hello")


message = greet

message()
```

---

## Q2. What is a Higher-Order Function?

**Answer:**

A Higher-Order Function is a function that either:

1. Accepts another function as an argument, or
2. Returns another function.

Example:

```python
def square(x):
    return x * x


def calculate(function, value):
    return function(value)


print(calculate(square, 5))
```

Output:

```text
25
```

---

## Q3. What is a nested function?

**Answer:**

A function defined inside another function is called a nested function.

Example:

```python
def outer():

    def inner():
        print("Hello")

    inner()


outer()
```

---

## Q4. What is a decorator?

**Answer:**

A decorator is a function that modifies or extends the behavior of another function without directly changing its source code.

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

## Q5. Why are decorators used?

**Answer:**

Decorators are commonly used for:

- Logging
- Authentication
- Authorization
- Performance monitoring
- Validation
- Caching
- Access control
- Error handling

---

## Q6. What does the `@` symbol mean in decorators?

**Answer:**

The `@` symbol is decorator syntax.

For example:

```python
@decorator
def greet():
    print("Hello")
```

is approximately equivalent to:

```python
def greet():
    print("Hello")


greet = decorator(greet)
```

---

## Q7. What is a wrapper function?

**Answer:**

A wrapper is an inner function inside a decorator that adds extra behavior before or after the original function executes.

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

## Q8. Why do decorators usually return the wrapper?

**Answer:**

Because the wrapper replaces the original function while providing the additional behavior.

Example:

```python
return wrapper
```

---

## Q9. What is `*args`?

**Answer:**

`*args` allows a function to accept any number of positional arguments.

Inside the function, `args` is stored as a tuple.

Example:

```python
def show(*args):
    print(args)


show(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

---

## Q10. What is `**kwargs`?

**Answer:**

`**kwargs` allows a function to accept any number of keyword arguments.

Inside the function, `kwargs` is stored as a dictionary.

Example:

```python
def show(**kwargs):
    print(kwargs)


show(name="Amir", age=19)
```

---

## Q11. Why are `*args` and `**kwargs` useful in decorators?

**Answer:**

They make decorators flexible enough to work with functions having different numbers and types of arguments.

Example:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

---

## Q12. What is `functools.wraps`?

**Answer:**

`functools.wraps` is a helper used inside decorators to preserve metadata of the original function.

Example:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

---

## Q13. What happens if we don't use `functools.wraps`?

**Answer:**

The decorated function may appear to have the wrapper's metadata instead of the original function's metadata.

For example:

```python
function.__name__
```

may return:

```text
wrapper
```

instead of the original function name.

---

## Q14. Can a decorator accept arguments?

**Answer:**

Yes.

A decorator can be designed to accept arguments.

Example:

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
def hello():
    print("Hello")
```

---

## Q15. Can we use multiple decorators on one function?

**Answer:**

Yes.

Example:

```python
@decorator1
@decorator2
def greet():
    print("Hello")
```

Multiple decorators can be applied to the same function.

---

## Q16. What is the order of multiple decorators?

**Answer:**

Decorators are applied from the bottom upward.

Example:

```python
@decorator1
@decorator2
def greet():
    pass
```

Conceptually:

```python
greet = decorator1(decorator2(greet))
```

---

## Q17. Can decorators return values?

**Answer:**

Yes.

The wrapper should return the result of the original function.

Example:

```python
def decorator(function):

    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs)

        return result

    return wrapper
```

---

## Q18. How can a decorator measure execution time?

**Answer:**

The decorator can record the time before and after the function executes.

Example:

```python
import time


def performance(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print("Time:", end - start)

        return result

    return wrapper
```

---

## Q19. How can decorators be used for authentication?

**Answer:**

A decorator can check whether the user is authorized before allowing the function to execute.

Example:

```python
def login_required(function):

    def wrapper(username):

        if username == "admin":
            return function(username)

        print("Access Denied")

    return wrapper
```

---

## Q20. What is the difference between a decorator and a normal function?

**Answer:**

A normal function performs a particular operation.

A decorator is designed to add or modify behavior of another function.

---

## Q21. Can one decorator work with multiple functions?

**Answer:**

Yes.

A properly designed decorator can be reused with multiple functions.

Example:

```python
@logger
def login():
    pass


@logger
def logout():
    pass
```

Both functions can use the same decorator.

---

## Q22. What is a function factory?

**Answer:**

A function factory is a function that creates and returns another function.

Example:

```python
def multiplier(number):

    def multiply(value):
        return value * number

    return multiply


double = multiplier(2)

print(double(5))
```

Output:

```text
10
```

---

## Q23. Can a function be stored in a list?

**Answer:**

Yes.

Example:

```python
def hello():
    print("Hello")


def welcome():
    print("Welcome")


functions = [hello, welcome]

for function in functions:
    function()
```

---

## Q24. What is closure in Python?

**Answer:**

A closure occurs when an inner function remembers values from its enclosing function even after the enclosing function has finished execution.

Example:

```python
def outer(message):

    def inner():
        print(message)

    return inner


function = outer("Hello")

function()
```

---

## Q25. Why are closures useful?

**Answer:**

Closures are useful when we want a function to remember some data from its surrounding environment.

They are commonly used in:

- Decorators
- Function factories
- Callbacks

---

## Q26. What is the difference between `*args` and `**kwargs`?

**Answer:**

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Arguments | Positional | Keyword |
| Data type | Tuple | Dictionary |
| Example | `10, 20` | `name="Amir"` |

---

## Q27. What is the purpose of `return function` in a decorator?

**Answer:**

It returns the wrapper function so that the decorated function can be replaced by the wrapper.

Example:

```python
def decorator(function):

    def wrapper():
        function()

    return wrapper
```

---

## Q28. How can a decorator log function calls?

**Answer:**

The decorator can print or store the function name and arguments before executing the function.

Example:

```python
def logger(function):

    def wrapper(*args, **kwargs):

        print("Called:", function.__name__)

        return function(*args, **kwargs)

    return wrapper
```

---

## Q29. Can decorators be used for validation?

**Answer:**

Yes.

A decorator can validate arguments before allowing a function to execute.

Example:

```python
def positive_only(function):

    def wrapper(number):

        if number > 0:
            return function(number)

        print("Invalid number")

    return wrapper
```

---

## Q30. What are the main advantages of decorators?

**Answer:**

Main advantages include:

- Code reusability
- Cleaner code
- Separation of concerns
- Better maintainability
- Easy addition of common functionality
- Reduced code duplication

---

# 🔥 ADVANCED INTERVIEW QUESTIONS

## Q31. Are decorators only used with functions?

**Answer:**

No.

Decorators can also be used with classes and methods.

For example:

```python
@property
def name(self):
    return self._name
```

---

## Q32. What is the difference between `@decorator` and `decorator()`?

**Answer:**

```python
@decorator
```

directly applies the decorator.

While:

```python
@decorator()
```

means the decorator itself is being called, usually because it is a decorator factory that accepts arguments.

---

## Q33. What does this code mean?

```python
@decorator
def test():
    pass
```

**Answer:**

It means approximately:

```python
test = decorator(test)
```

---

## Q34. Why should a decorator use `*args` and `**kwargs`?

**Answer:**

Because it allows the wrapper to accept the same variety of arguments as the original function.

This makes the decorator reusable.

---

## Q35. What is separation of concerns in decorators?

**Answer:**

Separation of concerns means keeping different responsibilities separate.

For example:

```text
Business Logic → Original Function

Logging → Logger Decorator

Authentication → Authentication Decorator

Performance → Performance Decorator
```

This makes the code easier to maintain.

---

# 🧠 QUICK INTERVIEW REVISION

### First-Class Function

```text
Function can be stored,
passed and returned.
```

### Higher-Order Function

```text
Accepts or returns a function.
```

### Nested Function

```text
Function inside another function.
```

### Decorator

```text
Adds/modifies function behavior.
```

### `@`

```text
Decorator syntax.
```

### `*args`

```text
Multiple positional arguments.
```

### `**kwargs`

```text
Multiple keyword arguments.
```

### `wraps`

```text
Preserves original function metadata.
```

### Closure

```text
Inner function remembers
outer function's values.
```

---

# 🎯 DAY 16 INTERVIEW TARGET

Before moving to Day 17, I should be able to explain:

- [ ] First-class functions
- [ ] Higher-order functions
- [ ] Nested functions
- [ ] Closures
- [ ] Decorators
- [ ] `@` syntax
- [ ] Wrapper functions
- [ ] `*args`
- [ ] `**kwargs`
- [ ] `functools.wraps`
- [ ] Multiple decorators
- [ ] Decorators with arguments
- [ ] Real-world decorator applications

---

# 🏆 DAY 16 INTERVIEW COMPLETE

**35 Questions → Concepts + Examples + Real-world Applications 🚀**