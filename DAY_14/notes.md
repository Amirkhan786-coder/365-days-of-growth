# 📚 Day 14 - Python OOP Part 1

# 🐍 Python Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming approach where we organize code using **classes and objects**.

OOP helps us write:

- Clean code
- Reusable code
- Organized code
- Scalable programs
- Real-world applications

---

# 🎯 Today's Topics

Today we will learn:

1. What is OOP?
2. Why OOP?
3. Class
4. Object
5. Class vs Object
6. Creating a Class
7. Creating an Object
8. `self` Keyword
9. `__init__()` Constructor
10. Attributes
11. Methods
12. Instance Variables
13. Class Variables
14. Accessing Attributes
15. Modifying Attributes
16. Deleting Attributes
17. Multiple Objects
18. Real-World Examples
19. Advantages of OOP
20. Practice Project

---

# 1. What is OOP?

OOP stands for:

**Object-Oriented Programming**

It is a programming concept based on **objects and classes**.

Instead of writing a large program as a collection of unrelated functions, OOP allows us to combine:

- Data
- Functions

inside a class.

Example:

```python
class Student:

    def display(self):
        print("Student Information")
```

---

# 2. Why Do We Need OOP?

Suppose we want to create a program for 100 students.

Without OOP, we may need many separate variables and functions.

With OOP, we can create one `Student` class and then create many student objects.

```text
Student Class
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
S1   S2    S3
```

Each object can have its own information.

---

# 3. Important OOP Terminology

| Term | Meaning |
|---|---|
| Class | Blueprint |
| Object | Instance of a class |
| Attribute | Data/Property |
| Method | Function inside a class |
| Constructor | Initializes an object |
| self | Refers to current object |

---

# 4. What is a Class?

A class is a **blueprint or template** for creating objects.

Example:

```python
class Student:
    pass
```

Here:

```text
Student
   ↓
Class
   ↓
Blueprint
```

The class itself is not a specific student.

It defines what a student object can contain.

---

# 5. What is an Object?

An object is an **instance of a class**.

Example:

```python
class Student:
    pass


student1 = Student()
```

Here:

```text
Student
   ↓
Class

student1
   ↓
Object
```

---

# 6. Creating a Class

Syntax:

```python
class ClassName:
    # attributes
    # methods
```

Example:

```python
class Car:

    def drive(self):
        print("Car is driving")
```

---

# 7. Creating an Object

We create an object by calling the class.

```python
class Car:

    def drive(self):
        print("Car is driving")


car1 = Car()
```

Here:

```text
Car() → creates an object
car1  → stores the object
```

---

# 8. Calling a Method

```python
class Car:

    def drive(self):
        print("Car is driving")


car1 = Car()

car1.drive()
```

Output:

```text
Car is driving
```

---

# 9. What is self?

`self` refers to the **current object**.

Example:

```python
class Student:

    def show(self):
        print("Student information")
```

When we call:

```python
student1.show()
```

Python internally connects `self` with `student1`.

---

# 10. Why is self Important?

Suppose we have two students:

```python
student1
student2
```

Each object needs its own data.

`self` helps Python identify which object's data is being accessed.

Example:

```python
class Student:

    def show(self):
        print(self)
```

```python
student1 = Student()
student2 = Student()

student1.show()
student2.show()
```

The `self` inside each call refers to the respective object.

---

# 11. What is __init__()?

`__init__()` is a special method that is automatically called when an object is created.

It is commonly called a **constructor**.

Example:

```python
class Student:

    def __init__(self):
        print("Student object created")


student1 = Student()
```

Output:

```text
Student object created
```

---

# 12. Constructor with Parameters

We can pass information while creating an object.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Amir", 20)

print(student1.name)
print(student1.age)
```

Output:

```text
Amir
20
```

---

# 13. Understanding self.name

Consider:

```python
self.name = name
```

The left side:

```python
self.name
```

means the object's attribute.

The right side:

```python
name
```

is the value received by the constructor.

Example:

```python
student1 = Student("Amir", 20)
```

Python stores:

```text
student1.name = "Amir"
student1.age = 20
```

---

# 14. Attributes

Attributes are variables associated with an object or class.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here:

```text
name → Attribute
age  → Attribute
```

---

# 15. Instance Variables

Instance variables belong to individual objects.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create objects:

```python
student1 = Student("Amir", 20)
student2 = Student("Rahul", 21)
```

Now:

```text
student1
name = Amir
age = 20

student2
name = Rahul
age = 21
```

Each object has separate values.

---

# 16. Accessing Attributes

We can access object attributes using the dot operator.

Syntax:

```python
object.attribute
```

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Amir", 20)

print(student1.name)
print(student1.age)
```

---

# 17. Modifying Attributes

We can change an object's attribute.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Amir", 20)

student1.age = 21

print(student1.age)
```

Output:

```text
21
```

---

# 18. Adding New Attributes

Python also allows us to add attributes to an object.

Example:

```python
class Student:
    pass


student1 = Student()

student1.name = "Amir"
student1.age = 20

print(student1.name)
print(student1.age)
```

---

# 19. Deleting an Attribute

We can delete an attribute using `del`.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Amir", 20)

del student1.age
```

After deleting:

```python
print(student1.age)
```

will cause an error because the attribute no longer exists.

---

# 20. Methods

A method is a function defined inside a class.

Example:

```python
class Student:

    def study(self):
        print("Student is studying")
```

Create object:

```python
student1 = Student()

student1.study()
```

Output:

```text
Student is studying
```

---

# 21. Method with Parameters

Methods can also accept parameters.

```python
class Calculator:

    def add(self, a, b):
        print(a + b)


calc = Calculator()

calc.add(10, 20)
```

Output:

```text
30
```

---

# 22. Method Using Object Attributes

Example:

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Amir", 85)

student1.display()
```

Output:

```text
Name: Amir
Marks: 85
```

---

# 23. Multiple Objects

A single class can create many objects.

Example:

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)


student1 = Student("Amir", 85)
student2 = Student("Rahul", 90)
student3 = Student("Priya", 92)

student1.display()
student2.display()
student3.display()
```

Output:

```text
Amir 85
Rahul 90
Priya 92
```

---

# 24. Class Variable

A class variable is shared by all objects of the class.

Example:

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name


student1 = Student("Amir")
student2 = Student("Rahul")

print(student1.school)
print(student2.school)
```

Both objects can access:

```text
ABC School
```

---

# 25. Instance Variable vs Class Variable

## Instance Variable

Different for each object.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Example:

```text
student1.name = Amir
student2.name = Rahul
```

---

## Class Variable

Shared by all objects.

```python
class Student:

    school = "ABC School"
```

---

# 26. Difference Between Class and Object

| Class | Object |
|---|---|
| Blueprint | Real instance |
| Defines structure | Uses structure |
| Does not represent one specific entity | Represents a specific entity |
| Example: Student | Example: Amir |
| Used to create objects | Created from a class |

Example:

```text
Class
Student
   ↓
   ↓
Objects
   ├── Amir
   ├── Rahul
   └── Priya
```

---

# 27. Real-World Example

Think about a **Car Factory**.

The factory has a blueprint for cars.

That blueprint is similar to a class.

Each actual car produced from that blueprint is an object.

```text
Car Class
    ↓
    ├── BMW Object
    ├── Audi Object
    ├── Tesla Object
    └── Toyota Object
```

---

# 28. Real-World OOP Examples

## Student Management System

Class:

```python
Student
```

Objects:

```text
Amir
Rahul
Priya
```

Attributes:

```text
name
age
marks
course
```

Methods:

```text
display()
calculate_grade()
```

---

## Bank Application

Class:

```python
BankAccount
```

Attributes:

```text
account_number
name
balance
```

Methods:

```text
deposit()
withdraw()
check_balance()
```

---

## E-Commerce Application

Class:

```python
Product
```

Attributes:

```text
name
price
quantity
```

Methods:

```text
add_to_cart()
remove_from_cart()
buy()
```

---

# 29. Complete OOP Example

```python
class Student:

    school = "ABC School"

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("School:", self.school)


student1 = Student("Amir", 20, 85)

student1.display()
```

Output:

```text
Name: Amir
Age: 20
Marks: 85
School: ABC School
```

---

# 30. OOP Structure

A basic OOP program looks like:

```text
Class
  ↓
Constructor
  ↓
Attributes
  ↓
Methods
  ↓
Objects
  ↓
Output
```

---

# 31. Advantages of OOP

## 1. Code Reusability

Classes can be reused.

## 2. Better Organization

Large programs can be divided into classes.

## 3. Easy Maintenance

Changes can be made more easily.

## 4. Scalability

OOP is useful for large applications.

## 5. Data Organization

Related data and behavior can be grouped together.

## 6. Real-World Modeling

Real-world entities can be represented using objects.

---

# 32. OOP vs Procedural Programming

## Procedural Programming

Focuses mainly on:

```text
Functions
+
Procedures
```

Example:

```python
def calculate_salary():
    pass
```

---

## Object-Oriented Programming

Focuses on:

```text
Objects
+
Classes
+
Methods
+
Attributes
```

Example:

```python
class Employee:

    def calculate_salary(self):
        pass
```

---

# 33. Common OOP Mistakes

## Mistake 1: Forgetting self

Incorrect:

```python
class Student:

    def display():
        print("Hello")
```

Correct:

```python
class Student:

    def display(self):
        print("Hello")
```

---

## Mistake 2: Incorrect Constructor

Incorrect:

```python
def init(self):
    pass
```

Correct:

```python
def __init__(self):
    pass
```

---

## Mistake 3: Forgetting Object

Example:

```python
class Student:

    def display(self):
        print("Hello")
```

We need an object:

```python
student1 = Student()

student1.display()
```

---

# 34. Important Special Methods

Python provides special methods called **dunder methods**.

Dunder means:

```text
Double Underscore
```

Examples:

```python
__init__()
__str__()
__len__()
__name__
```

Today our main focus is:

```python
__init__()
```

---

# 35. OOP Terminology Summary

```text
Class
    ↓
Blueprint

Object
    ↓
Instance of Class

Attribute
    ↓
Object Data

Method
    ↓
Function inside Class

self
    ↓
Current Object

__init__()
    ↓
Constructor
```

---

# 36. Complete Example — Bank Account

```python
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account1 = BankAccount("Amir", 5000)

account1.deposit(2000)

account1.display_balance()
```

Output:

```text
Account Holder: Amir
Balance: 7000
```

---

# 37. Complete Example — Mobile Phone

```python
class Mobile:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


phone1 = Mobile("Samsung", "S25", 80000)

phone1.display()
```

---

# 38. Complete Example — Employee

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Amir", 50000)

employee1.display()
```

---

# 39. OOP Learning Flow

```text
Learn Class
     ↓
Create Object
     ↓
Add Attributes
     ↓
Create Methods
     ↓
Use Constructor
     ↓
Create Multiple Objects
     ↓
Build Real Projects
```

---

# 40. Today's Mini Project

## 🎓 Student Gradebook

Create a Python program using OOP that can:

- Add student
- Store student name
- Store marks
- Calculate grade
- Display student information
- Calculate average marks
- Display all students

Basic structure:

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


student1 = Student("Amir", 88)

student1.display()
```

---

# 41. Important Interview Points

### What is OOP?

OOP is a programming paradigm based on classes and objects.

### What is a class?

A class is a blueprint for creating objects.

### What is an object?

An object is an instance of a class.

### What is self?

`self` refers to the current object.

### What is __init__()?

`__init__()` is a special method that is automatically called when an object is created.

### What is a method?

A function defined inside a class is called a method.

### What is an attribute?

A variable associated with an object or class is called an attribute.

---

# 42. Quick Revision

```text
OOP
 ↓
Object-Oriented Programming

Class
 ↓
Blueprint

Object
 ↓
Instance

self
 ↓
Current Object

__init__()
 ↓
Constructor

Attribute
 ↓
Data

Method
 ↓
Behavior / Function

Class Variable
 ↓
Shared by Objects

Instance Variable
 ↓
Unique to Object
```

---

# 43. Day 14 Key Takeaways

Today I learned:

- OOP
- Classes
- Objects
- `self`
- `__init__()`
- Attributes
- Methods
- Instance Variables
- Class Variables
- Multiple Objects
- Real-world OOP
- Advantages of OOP

---

# 🚀 Day 14 Progress

```text
Python OOP Part 1
        ↓
Classes
        ↓
Objects
        ↓
self
        ↓
Constructor
        ↓
Attributes
        ↓
Methods
        ↓
Mini Project
```

---

# 🎯 Tomorrow

## Day 15 — Python OOP Part 2

Topics:

- Inheritance
- `super()`
- Method Overriding
- Polymorphism
- Encapsulation
- Abstraction
- Multiple Inheritance
- Multilevel Inheritance

---

# 🏆 365 DAYS OF GROWTH

## DAY 14 COMPLETE

```text
LEARN → PRACTICE → BUILD → IMPROVE → REPEAT
```

> **Don't just write code. Learn how to design it.**

**Progress: 14 / 365 🚀**