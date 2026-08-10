# 🚀 DAY 16 / 365 — Python Decorators & Higher-Order Functions

> Continuing my 365 Days of Growth journey 🚀

---

## 📅 Day 16

Today I continued learning **Python Functions** and moved toward advanced concepts like **Higher-Order Functions, Closures, and Decorators**.

I learned how functions can be passed as arguments, returned from other functions, and extended with additional functionality using decorators.

---

# 📚 TOPICS COVERED

1. First-Class Functions
2. Higher-Order Functions
3. Nested Functions
4. Closures
5. Decorators
6. `@` Decorator Syntax
7. Wrapper Functions
8. `*args`
9. `**kwargs`
10. Flexible Decorators
11. `functools.wraps`
12. Multiple Decorators
13. Decorators with Arguments
14. Authentication Decorator
15. Logging Decorator
16. Performance Decorator
17. Validation Decorator
18. Real-World Applications

---

# 🧠 1. FIRST-CLASS FUNCTIONS

In Python, functions are treated as first-class objects.

This means a function can be:

- Stored in a variable
- Passed as an argument
- Returned from another function
- Stored inside a data structure

### Example

```python
def greet():
    print("Hello Python!")


message = greet

message()
Output
Hello Python!
🧠 2. HIGHER-ORDER FUNCTIONS

A Higher-Order Function is a function that accepts another function as an argument or returns another function.

Example
def square(number):
    return number * number


def calculate(function, value):
    return function(value)


result = calculate(square, 5)

print(result)
Output
25
🧠 3. NESTED FUNCTIONS

A function defined inside another function is called a Nested Function.

Example
def outer():

    def inner():
        print("Hello from inner function!")

    inner()


outer()
Output
Hello from inner function!
🧠 4. CLOSURES

A closure occurs when an inner function remembers values from its enclosing function even after the outer function has finished executing.

Example
def outer(message):

    def inner():
        print(message)

    return inner


function = outer("Hello Python!")

function()
Output
Hello Python!
🧠 5. DECORATORS

A decorator is a function that adds extra functionality to another function without changing its original code.

Example
def decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")

    return wrapper
🧠 6. @ DECORATOR SYNTAX

Instead of writing:

greet = decorator(greet)

we can use the @decorator syntax.

Example
def decorator(function):

    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper


@decorator
def greet():

    print("Hello!")


greet()
Output
Before
Hello!
After
🧠 7. WRAPPER FUNCTIONS

A wrapper function is an inner function used inside a decorator.

It allows us to execute additional code before and after the original function.

Example
def decorator(function):

    def wrapper():

        print("Starting function")

        function()

        print("Function completed")

    return wrapper
🧠 8. *args

*args allows a function to accept multiple positional arguments.

Example
def show(*args):

    print(args)


show(10, 20, 30)
Output
(10, 20, 30)

args stores positional arguments as a tuple.

🧠 9. **kwargs

**kwargs allows a function to accept multiple keyword arguments.

Example
def show(**kwargs):

    print(kwargs)


show(name="Amir", age=19)
Output
{'name': 'Amir', 'age': 19}

kwargs stores keyword arguments as a dictionary.

🧠 10. FLEXIBLE DECORATORS

Using *args and **kwargs, we can create decorators that work with different functions and arguments.

Example
def decorator(function):

    def wrapper(*args, **kwargs):

        print("Function started")

        result = function(*args, **kwargs)

        print("Function completed")

        return result

    return wrapper
🧠 11. functools.wraps

functools.wraps helps preserve information about the original function when using a decorator.

Example
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        return function(*args, **kwargs)

    return wrapper
🧠 12. MULTIPLE DECORATORS

Python allows multiple decorators to be applied to the same function.

Example
@decorator_one
@decorator_two
def greet():

    print("Hello!")

This is approximately equivalent to:

greet = decorator_one(decorator_two(greet))
🧠 13. DECORATORS WITH ARGUMENTS

A decorator can also accept arguments.

Example
def repeat(times):

    def decorator(function):

        def wrapper():

            for i in range(times):

                function()

        return wrapper

    return decorator
Usage
@repeat(3)
def hello():

    print("Hello!")


hello()
Output
Hello!
Hello!
Hello!
🧠 14. AUTHENTICATION DECORATOR

Decorators can be used to control access to a function.

Example
def login_required(function):

    def wrapper(username):

        if username == "admin":

            return function(username)

        print("Access Denied")

    return wrapper

Authentication decorators can be useful in:

Websites
APIs
Admin dashboards
User management systems
🧠 15. LOGGING DECORATOR

A logging decorator can display information about function execution.

Example
def logger(function):

    def wrapper(*args, **kwargs):

        print("Function Called:", function.__name__)

        return function(*args, **kwargs)

    return wrapper
🧠 16. PERFORMANCE DECORATOR

A performance decorator can measure how long a function takes to execute.

Example
import time


def performance(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper
🧠 17. VALIDATION DECORATOR

Decorators can validate input before executing a function.

Example
def positive_only(function):

    def wrapper(number):

        if number > 0:

            return function(number)

        print("Number must be positive.")

    return wrapper
🌍 18. REAL-WORLD APPLICATIONS

Decorators are commonly used for:

Authentication
Authorization
Logging
Performance Monitoring
Input Validation
Caching
Error Handling
Monitoring
Access Control
🧪 PRACTICE

Today I completed:

✅ 30 Practice Questions
✅ 30 Separate Python Programs
✅ Higher-Order Function Practice
✅ Nested Function Practice
✅ Closure Practice
✅ Decorator Practice
✅ *args Practice
✅ **kwargs Practice
✅ Multiple Decorator Practice
✅ Real-World Decorator Practice
🎯 INTERVIEW PREPARATION

I prepared 35 Interview Questions covering:

First-Class Functions
Higher-Order Functions
Nested Functions
Closures
Decorators
@ Decorator Syntax
Wrapper Functions
*args
**kwargs
functools.wraps
Multiple Decorators
Decorators with Arguments
Authentication Decorators
Logging Decorators
Performance Decorators
Validation Decorators
Real-World Applications
🚀 MINI PROJECT
Performance Monitor & Access Logger
Project Description

Built a Python decorator-based mini project that combines authentication, logging, and performance monitoring.

Features
🔐 User Authentication
📝 Function Logging
⏱️ Performance Monitoring
📊 Calculation Result
🔄 Multiple Decorators
Project Workflow
User Login
      ↓
Authentication Decorator
      ↓
Logger Decorator
      ↓
Performance Decorator
      ↓
Dashboard Function
      ↓
Calculation
      ↓
Result
💻 MINI PROJECT CODE
import time
from functools import wraps


def authentication(function):

    @wraps(function)
    def wrapper(username, *args, **kwargs):

        if username != "admin":

            print("\nAuthentication Failed")
            print("Access Denied!")

            return None

        print("\nAuthentication Successful")

        return function(username, *args, **kwargs)

    return wrapper


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Function Called:", function.__name__)

        return function(*args, **kwargs)

    return wrapper


def performance(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time:.6f} seconds")

        return result

    return wrapper


@authentication
@logger
@performance
def dashboard(username):

    print(f"\nWelcome to the Dashboard, {username}!")

    total = 0

    for number in range(1, 1000000):

        total += number

    return total


print("=" * 50)
print("      PERFORMANCE MONITOR & ACCESS LOGGER")
print("=" * 50)


username = input("\nEnter username: ")

result = dashboard(username)


if result is not None:

    print("\nCalculation Result:", result)

    print("\nProgram completed successfully.")

else:

    print("\nProgram stopped because authentication failed.")


print("\n" + "=" * 50)
print("             THANK YOU")
print("=" * 50)
▶️ HOW TO RUN
python main.py
💻 SAMPLE OUTPUT
==================================================
      PERFORMANCE MONITOR & ACCESS LOGGER
==================================================

Enter username: admin

Authentication Successful
Function Called: dashboard

Welcome to the Dashboard, admin!

Execution Time: 0.045231 seconds

Calculation Result: 499999500000

Program completed successfully.

==================================================
             THANK YOU
==================================================
❌ INVALID LOGIN OUTPUT
Enter username: user

Authentication Failed
Access Denied!

Program stopped because authentication failed.
📂 FILES IN THIS FOLDER
Day16/
│
├── README.md
├── notes.md
├── practice_questions.md
├── practice_codes/
├── mcqs.md
├── interview_questions.md
├── reflection.md
├── learning_outcomes.md
├── project.md
└── mini_project/
🎯 LEARNING OUTCOMES

After completing Day 16, I can:

 Explain First-Class Functions
 Create Higher-Order Functions
 Create Nested Functions
 Understand Closures
 Create Decorators
 Use @ Decorator Syntax
 Create Wrapper Functions
 Use *args
 Use **kwargs
 Create Flexible Decorators
 Use functools.wraps
 Create Multiple Decorators
 Create Decorators with Arguments
 Create Authentication Decorators
 Create Logging Decorators
 Create Performance Decorators
 Create Validation Decorators
 Build a Practical Decorator Project
💡 KEY LEARNING

Decorators allow us to add reusable functionality to existing functions without changing their core logic.

They make Python programs:

Reusable
Modular
Maintainable
Scalable
Easier to understand
🏆 DAY 16 ACHIEVEMENT
Python Decorators & Higher-Order Functions
                  ↓
        30 Practice Questions
                  ↓
        35 Interview Questions
                  ↓
         Advanced Functions
                  ↓
            Decorators
                  ↓
           Mini Project
                  ↓
          Day 16 Completed ✅
📈 365 DAYS OF GROWTH

Day 16 / 365

████░░░░░░░░░░░░░░░░  4.4%
🚀 WHAT'S NEXT?

Continue Python learning with:

Iterators
Generators
iter()
next()
yield
Generator Expressions
Lazy Evaluation
Memory Efficiency
🔥 MY GOAL

Learn every day.
Practice every day.
Build every day.
Become better every day.

16 / 365 — Keep Growing 🚀