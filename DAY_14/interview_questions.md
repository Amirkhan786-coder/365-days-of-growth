# 🎤 Day 14 — Python OOP Interview Questions

## Topic: OOP Part 1

---

### Q1. What is OOP?

**Answer:**

OOP stands for Object-Oriented Programming. It is a programming approach based on classes and objects.

OOP helps organize data and functions together and makes programs reusable and easier to maintain.

---

### Q2. What is a class?

**Answer:**

A class is a blueprint or template used to create objects.

Example:

```python
class Student:
    pass
```

---

### Q3. What is an object?

**Answer:**

An object is an instance of a class.

Example:

```python
class Student:
    pass

student1 = Student()
```

Here `student1` is an object of the `Student` class.

---

### Q4. What is the difference between a class and an object?

**Answer:**

A class is a blueprint, while an object is an actual instance created from that blueprint.

Example:

```text
Class  → Student
Object → student1
Object → student2
Object → student3
```

---

### Q5. What is `self` in Python?

**Answer:**

`self` refers to the current object.

It is used to access the object's attributes and methods.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Here `self.name` belongs to the current object.

---

### Q6. Is `self` a keyword in Python?

**Answer:**

No.

`self` is a conventional name used to refer to the current object.

Although another valid parameter name can technically be used, `self` is the standard and recommended convention.

---

### Q7. What is `__init__()`?

**Answer:**

`__init__()` is a special method that is automatically called when an object is created.

It is commonly used to initialize object attributes.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

### Q8. Is `__init__()` a constructor?

**Answer:**

It is commonly called the constructor in Python, although technically Python's object creation and initialization involve separate mechanisms.

For beginner-level Python, `__init__()` can be understood as the method used to initialize a newly created object.

---

### Q9. What is an attribute?

**Answer:**

An attribute is data associated with an object or class.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here `name` and `age` are instance attributes.

---

### Q10. What is a method?

**Answer:**

A method is a function defined inside a class.

Example:

```python
class Student:

    def study(self):
        print("Student is studying")
```

Here `study()` is a method.

---

### Q11. What is an instance variable?

**Answer:**

An instance variable is a variable that belongs to a particular object.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Different objects can have different values.

```python
student1 = Student("Amir")
student2 = Student("Rahul")
```

---

### Q12. What is a class variable?

**Answer:**

A class variable is a variable defined inside a class and shared by objects of that class.

Example:

```python
class Student:

    school = "ABC School"
```

---

### Q13. Difference between class variable and instance variable?

**Answer:**

| Class Variable | Instance Variable |
|---|---|
| Shared by objects | Belongs to individual object |
| Defined at class level | Usually defined using `self` |
| Same value can be shared | Can have different values |

Example:

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

Here:

```text
school → Class Variable
name   → Instance Variable
```

---

### Q14. Can a class create multiple objects?

**Answer:**

Yes.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Amir")
student2 = Student("Rahul")
student3 = Student("Priya")
```

One class can create many objects.

---

### Q15. Why do we use OOP?

**Answer:**

OOP is useful because it provides:

- Code reusability
- Better organization
- Easier maintenance
- Data organization
- Scalability
- Real-world modeling

---

### Q16. What is code reusability?

**Answer:**

Code reusability means writing code once and using it multiple times.

For example, one `Student` class can be used to create hundreds of student objects.

---

### Q17. How do you access an object's attribute?

**Answer:**

Using the dot `.` operator.

Example:

```python
student1.name
```

---

### Q18. How do you call an object's method?

**Answer:**

Using the dot operator followed by the method name.

Example:

```python
student1.display()
```

---

### Q19. Can object attributes be modified?

**Answer:**

Yes.

Example:

```python
student1.age = 21
```

This changes the `age` attribute of `student1`.

---

### Q20. Can we add a new attribute to an object?

**Answer:**

Yes.

Example:

```python
student1.course = "CSE"
```

Python allows attributes to be added dynamically to individual objects.

---

### Q21. How do you delete an object attribute?

**Answer:**

Use the `del` statement.

Example:

```python
del student1.age
```

---

### Q22. What are dunder methods?

**Answer:**

Dunder methods are special methods whose names begin and end with double underscores.

"Dunder" means **double underscore**.

Examples:

```python
__init__()
__str__()
__len__()
```

---

### Q23. Why is `__init__()` useful?

**Answer:**

It allows us to initialize object attributes automatically when an object is created.

Example:

```python
student1 = Student("Amir", 20)
```

The values can be stored automatically through `__init__()`.

---

### Q24. What happens when we create an object?

**Answer:**

Python creates an instance of the class.

If the class defines `__init__()`, Python calls it to initialize the object.

Example:

```python
student1 = Student("Amir", 20)
```

---

### Q25. What is the dot operator in OOP?

**Answer:**

The dot operator `.` is used to access attributes and methods.

Example:

```python
student1.name
student1.display()
```

---

### Q26. What is an instance of a class?

**Answer:**

An object created from a class is called an instance of that class.

Example:

```python
class Student:
    pass

student1 = Student()
```

`student1` is an instance of `Student`.

---

### Q27. What is the difference between a function and a method?

**Answer:**

A function can exist independently.

A method is a function defined inside a class and is generally called through an object or class.

Example:

```python
def add(a, b):
    return a + b
```

Function.

```python
class Calculator:

    def add(self, a, b):
        return a + b
```

Method.

---

### Q28. What is object-oriented programming useful for in real projects?

**Answer:**

OOP is useful for applications such as:

- Student Management Systems
- Banking Applications
- E-commerce Applications
- Employee Management Systems
- Games
- AI Applications
- Machine Learning Projects
- Web Applications

---

### Q29. Can two objects have different attribute values?

**Answer:**

Yes.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Amir")
student2 = Student("Rahul")
```

Here:

```text
student1.name → Amir
student2.name → Rahul
```

---

### Q30. Why is OOP important for large applications?

**Answer:**

OOP helps divide a large application into smaller, manageable classes and objects.

This makes the code:

- Easier to understand
- Easier to maintain
- Reusable
- Scalable
- Easier to test

---

# 🔥 Rapid-Fire Interview Revision

### 1. OOP stands for?

**Object-Oriented Programming**

### 2. Blueprint of an object?

**Class**

### 3. Instance of a class?

**Object**

### 4. Current object reference?

**self**

### 5. Object initialization method?

**`__init__()`**

### 6. Function inside a class?

**Method**

### 7. Data associated with an object?

**Attribute**

### 8. Shared class-level data?

**Class Variable**

### 9. Object-specific data?

**Instance Variable**

### 10. Access attributes using?

**Dot `.` operator**

---

# 🎯 Interview Preparation Checklist

```text
[ ] What is OOP?
[ ] What is a class?
[ ] What is an object?
[ ] Class vs Object
[ ] What is self?
[ ] Is self a keyword?
[ ] What is __init__()?
[ ] What is an attribute?
[ ] What is a method?
[ ] Instance variable
[ ] Class variable
[ ] Class vs instance variable
[ ] Multiple objects
[ ] Object attributes
[ ] Dunder methods
[ ] Dot operator
[ ] Function vs Method
[ ] Advantages of OOP
[ ] Real-world applications
```

# 🏆 Day 14 Interview Goal

By the end of Day 14, you should be able to explain:

```text
Class
   ↓
Object
   ↓
self
   ↓
__init__()
   ↓
Attributes
   ↓
Methods
   ↓
Class Variables
   ↓
Instance Variables
```

**Day 14 Interview Preparation Complete ✅**