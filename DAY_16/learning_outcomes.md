# 🎯 DAY 16 — Learning Outcomes

## Python Decorators & Higher-Order Functions

After completing Day 16, I can:

---

## 1. First-Class Functions

I understand that Python functions are first-class objects.

I can:

- Store functions in variables.
- Pass functions as arguments.
- Return functions from other functions.
- Store functions inside collections.

---

## 2. Higher-Order Functions

I can identify and create functions that:

- Accept another function as an argument.
- Return another function.

Example:

```python
def execute(function, value):
    return function(value)
```

---

## 3. Nested Functions

I understand how to define a function inside another function.

```python
def outer():

    def inner():
        print("Hello")

    inner()
```

---

## 4. Closures

I understand the basic concept of closures.

An inner function can remember values from its enclosing function.

```python
def outer(message):

    def inner():
        print(message)

    return inner
```

---

## 5. Decorators

I can create a custom decorator.

```python
def decorator(function):

    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper
```

---

## 6. `@` Decorator Syntax

I understand that:

```python
@decorator
def greet():
    pass
```

is approximately equivalent to:

```python
greet = decorator(greet)
```

---

## 7. `*args`

I can use `*args` to accept multiple positional arguments.

```python
def show(*args):
    print(args)
```

---

## 8. `**kwargs`

I can use `**kwargs` to accept multiple keyword arguments.

```python
def show(**kwargs):
    print(kwargs)
```

---

## 9. Flexible Decorators

I can create decorators that work with different types and numbers of arguments.

```python
def decorator(function):

    def wrapper(*args, **kwargs):

        return function(*args, **kwargs)

    return wrapper
```

---

## 10. Multiple Decorators

I understand that multiple decorators can be applied to one function.

```python
@decorator_one
@decorator_two
def greet():
    pass
```

---

## 11. Decorators with Arguments

I understand the basic structure of decorator factories.

```python
def repeat(times):

    def decorator(function):

        def wrapper():

            for i in range(times):
                function()

        return wrapper

    return decorator
```

---

## 12. `functools.wraps`

I understand why `functools.wraps` is useful.

```python
from functools import wraps
```

It helps preserve the original function's metadata.

---

## 13. Real-World Applications

I can explain how decorators can be used for:

```text
✅ Logging
✅ Authentication
✅ Authorization
✅ Validation
✅ Performance Monitoring
✅ Access Control
✅ Caching
```

---

# 🛠️ Practical Skills

After Day 16, I can:

- [x] Create higher-order functions.
- [x] Create nested functions.
- [x] Create closures.
- [x] Create basic decorators.
- [x] Use `@` syntax.
- [x] Use `*args`.
- [x] Use `**kwargs`.
- [x] Create reusable decorators.
- [x] Use multiple decorators.
- [x] Create decorators with arguments.
- [x] Use `functools.wraps`.
- [x] Build a performance monitor.
- [x] Build a logging system.
- [x] Build an authentication decorator.

---

# 🏆 Day 16 Final Outcome

```text
Functions
    ↓
First-Class Functions
    ↓
Higher-Order Functions
    ↓
Nested Functions
    ↓
Closures
    ↓
Decorators
    ↓
Advanced Decorators
    ↓
Real-World Applications
```

---

# 🚀 Mini Project Skills

### Performance Monitor & Access Logger

The project demonstrates:

```text
Authentication
      ↓
Function Logging
      ↓
Performance Monitoring
      ↓
Function Execution
      ↓
Result
```

---

# 📊 Day 16 Progress

| Skill | Status |
|---|---|
| First-Class Functions | ✅ |
| Higher-Order Functions | ✅ |
| Nested Functions | ✅ |
| Closures | ✅ |
| Decorators | ✅ |
| `@` Syntax | ✅ |
| `*args` | ✅ |
| `**kwargs` | ✅ |
| Multiple Decorators | ✅ |
| `functools.wraps` | ✅ |
| Practical Decorators | ✅ |
| Mini Project | ✅ |

---

# 🎯 Next Step

## DAY 17

### Python Iterators & Generators

Topics:

- Iterable vs Iterator
- `iter()`
- `next()`
- Custom Iterators
- `yield`
- Generators
- Generator Expressions
- Memory Efficiency
- Practical Applications

---

# 🔥 DAY 16 COMPLETE

**Learned → Practiced → Built → Improved**

## 🚀 DAY 16 / 365 ✅