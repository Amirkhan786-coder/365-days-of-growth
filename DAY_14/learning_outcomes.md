# 🎯 Day 14 — Learning Outcomes

## 🐍 Topic: Python OOP Part 1

After completing Day 14, I can understand and use the basic concepts of Object-Oriented Programming in Python.

---

# 1. OOP Fundamentals

I can explain:

- What OOP means
- Why OOP is used
- Advantages of OOP
- Real-world applications of OOP

---

# 2. Classes

I can create a class in Python.

Example:

```python
class Student:
    pass
```

I understand that a class acts as a blueprint for creating objects.

---

# 3. Objects

I can create objects from a class.

Example:

```python
student1 = Student()
```

I understand that an object is an instance of a class.

---

# 4. self Keyword

I understand that `self` refers to the current object.

I can use `self` to access:

- Instance variables
- Instance methods

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

# 5. __init__() Method

I understand the purpose of `__init__()`.

I can use it to initialize object attributes.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 6. Attributes

I understand what attributes are.

I can create and access object attributes.

Example:

```python
student1.name
student1.age
```

---

# 7. Methods

I can create methods inside classes.

Example:

```python
class Student:

    def study(self):
        print("Student is studying")
```

---

# 8. Instance Variables

I understand that instance variables belong to individual objects.

Example:

```python
student1.name = "Amir"
student2.name = "Rahul"
```

Each object can have different values.

---

# 9. Class Variables

I understand that class variables are shared by objects of a class.

Example:

```python
class Student:

    school = "ABC School"
```

---

# 10. Multiple Objects

I can create multiple objects from the same class.

Example:

```python
student1 = Student("Amir")
student2 = Student("Rahul")
student3 = Student("Priya")
```

---

# 11. Modify Attributes

I can modify an object's attribute.

Example:

```python
student1.age = 21
```

---

# 12. Delete Attributes

I understand how to remove an object attribute.

Example:

```python
del student1.age
```

---

# 13. Class vs Object

I can explain the difference:

```text
Class
 ↓
Blueprint

Object
 ↓
Instance of Class
```

---

# 14. Function vs Method

I understand that:

```text
Function
↓
Can exist independently

Method
↓
Function defined inside a class
```

---

# 15. Real-World Modeling

I can represent real-world entities using classes.

Examples:

```text
Student
Employee
BankAccount
Car
Product
Mobile
```

---

# 16. Practical Skills

After Day 14, I can build basic OOP programs such as:

- Student Management
- Gradebook
- Calculator
- Bank Account
- Employee Management
- Product Management

---

# 🛠️ Mini Project Outcome

## Student Gradebook

I successfully practiced OOP by creating a Student Gradebook.

The project uses:

```text
Class
   ↓
Object
   ↓
Attributes
   ↓
Methods
   ↓
Grade Calculation
   ↓
Student Information
```

---

# 📊 Skill Checklist

```text
[✓] Understand OOP
[✓] Create Classes
[✓] Create Objects
[✓] Use self
[✓] Use __init__()
[✓] Create Attributes
[✓] Create Methods
[✓] Use Instance Variables
[✓] Use Class Variables
[✓] Create Multiple Objects
[✓] Modify Attributes
[✓] Delete Attributes
[✓] Build Basic OOP Programs
```

---

# 🎯 Day 14 Final Outcome

By completing Day 14, I have built a strong foundation in Python OOP Part 1.

I am now ready to learn advanced OOP concepts such as:

- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

---

# 🚀 NEXT STEP

## DAY 15 — PYTHON OOP PART 2

```text
Inheritance
     ↓
super()
     ↓
Method Overriding
     ↓
Polymorphism
     ↓
Encapsulation
     ↓
Abstraction
```

---

# 🏆 DAY 14 COMPLETE

**Progress: 14 / 365 🚀**

> Learn → Practice → Build → Improve → Repeat