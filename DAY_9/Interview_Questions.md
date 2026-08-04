# 🎤 Day 9 - Interview Questions (Python Functions)

## 1. What is a Function in Python?

**Answer:**

A Function is a reusable block of code that performs a specific task. It helps reduce code duplication and improves readability.

---

## 2. Why do we use Functions?

**Answer:**

Functions are used to:

- Reuse code
- Reduce duplication
- Improve readability
- Make programs modular
- Simplify debugging and maintenance

---

## 3. What is the syntax of a Function?

**Answer:**

```python
def function_name():
    # code
```

---

## 4. What is the difference between a Function Definition and a Function Call?

**Answer:**

Function Definition creates the function.

```python
def hello():
    print("Hello")
```

Function Call executes the function.

```python
hello()
```

---

## 5. What are Parameters?

**Answer:**

Parameters are variables written inside the function definition that receive values.

Example

```python
def greet(name):
    print(name)
```

---

## 6. What are Arguments?

**Answer:**

Arguments are the actual values passed while calling a function.

Example

```python
greet("Amir")
```

---

## 7. What is the difference between Parameters and Arguments?

**Answer:**

| Parameter | Argument |
|------------|----------|
| Placeholder | Actual Value |
| Used in Function Definition | Used in Function Call |

---

## 8. What are Positional Arguments?

**Answer:**

Arguments passed according to their position.

Example

```python
student("Amir", 19)
```

---

## 9. What are Keyword Arguments?

**Answer:**

Arguments passed using parameter names.

Example

```python
student(age=19, name="Amir")
```

---

## 10. What are Default Arguments?

**Answer:**

Parameters that already have a default value.

Example

```python
def greet(name="Guest"):
    print(name)
```

---

## 11. What is *args?

**Answer:**

`*args` allows a function to accept multiple positional arguments.

Example

```python
def add(*numbers):
    print(numbers)
```

---

## 12. What is **kwargs?

**Answer:**

`**kwargs` allows a function to accept multiple keyword arguments.

Example

```python
def student(**data):
    print(data)
```

---

## 13. What is the return statement?

**Answer:**

The `return` statement sends a value back from the function.

Example

```python
def add(a, b):
    return a + b
```

---

## 14. What is the difference between print() and return?

**Answer:**

`print()` displays output on the screen.

`return` sends a value back so it can be reused later.

---

## 15. What is a Local Variable?

**Answer:**

A variable declared inside a function.

It can only be accessed inside that function.

---

## 16. What is a Global Variable?

**Answer:**

A variable declared outside a function.

It can be accessed throughout the program.

---

## 17. What is the global keyword?

**Answer:**

The `global` keyword allows a function to modify a global variable.

Example

```python
count = 0

def increase():
    global count
    count += 1
```

---

## 18. What is Variable Scope?

**Answer:**

Variable Scope defines where a variable can be accessed.

Types:

- Local Scope
- Global Scope

---

## 19. What is Recursion?

**Answer:**

Recursion is a process in which a function calls itself until a base condition is met.

---

## 20. What is a Base Condition?

**Answer:**

A Base Condition stops recursion and prevents infinite function calls.

---

## 21. What is a Lambda Function?

**Answer:**

A Lambda Function is a small anonymous function written in one line.

Example

```python
square = lambda x: x*x
```

---

## 22. What are Built-in Functions?

**Answer:**

Built-in Functions are already available in Python.

Examples

- print()
- len()
- max()
- min()
- type()
- input()
- range()
- sum()

---

## 23. What is a User-Defined Function?

**Answer:**

A User-Defined Function is created by the programmer using the `def` keyword.

Example

```python
def greet():
    print("Hello")
```

---

## 24. What are the advantages of Functions?

**Answer:**

- Code Reusability
- Better Readability
- Easy Debugging
- Easy Maintenance
- Modular Programming
- Less Code Duplication

---

## 25. Where are Functions used in Real-Life Projects?

**Answer:**

Functions are used in almost every software application, such as:

- Banking Systems
- ATM Software
- Student Management Systems
- Hospital Management Systems
- E-commerce Websites
- AI & Machine Learning Projects
- Web Development
- Mobile Applications
- Data Analysis
- Automation Scripts

---

# 🎯 Interview Tip

Always write small, reusable functions that perform **one specific task**. This improves code quality, readability, testing, and maintenance.