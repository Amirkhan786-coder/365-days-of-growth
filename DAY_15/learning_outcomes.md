# 🎯 DAY 15 — Python OOP Part 2
# Learning Outcomes

## 📅 Day 15 / 365

---

## 🧠 What I Learned

After completing Day 15, I can understand and use advanced Object-Oriented Programming concepts in Python.

---

## 1. Inheritance

I can create a child class from a parent class.

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")
```

---

## 2. `super()`

I can use `super()` to access parent class functionality.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name):
        super().__init__(name)
```

---

## 3. Method Overriding

I understand how a child class can change the behavior of a parent method.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")
```

---

## 4. Multilevel Inheritance

I can create inheritance across multiple levels.

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

---

## 5. Multiple Inheritance

I understand how one child class can inherit from multiple parent classes.

```python
class Father:
    pass


class Mother:
    pass


class Child(Father, Mother):
    pass
```

---

## 6. Polymorphism

I understand how different objects can use the same method name with different behavior.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")
```

---

## 7. Encapsulation

I can protect class data using private-style attributes.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

---

## 8. Getter

I can create a method to access encapsulated data.

```python
def get_balance(self):
    return self.__balance
```

---

## 9. Setter

I can create a method to update encapsulated data.

```python
def set_balance(self, balance):
    self.__balance = balance
```

---

## 10. Abstraction

I understand how to hide unnecessary implementation details.

Python provides the `abc` module for implementing abstraction.

---

## 11. Abstract Class

I can create an abstract class using `ABC`.

```python
from abc import ABC


class Animal(ABC):

    pass
```

---

## 12. Abstract Method

I can create an abstract method using `@abstractmethod`.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## 13. MRO

I understand the basic concept of Method Resolution Order.

MRO determines the order in which Python searches classes for methods and attributes.

```python
print(MyClass.mro())
```

---

# 💻 Practical Skills Gained

After today's learning, I can:

- [x] Create parent classes
- [x] Create child classes
- [x] Implement inheritance
- [x] Use `super()`
- [x] Override methods
- [x] Implement multilevel inheritance
- [x] Implement multiple inheritance
- [x] Understand polymorphism
- [x] Use encapsulation
- [x] Create getters
- [x] Create setters
- [x] Create abstract classes
- [x] Create abstract methods
- [x] Understand MRO

---

# 🎯 Interview Skills

I can now answer basic interview questions about:

```text
Inheritance
super()
Method Overriding
Polymorphism
Encapsulation
Abstraction
Abstract Classes
Multiple Inheritance
Multilevel Inheritance
MRO
```

---

# 🚀 Project Readiness

These concepts will help me build larger Python projects because real applications often use:

```text
Classes
     ↓
Objects
     ↓
Inheritance
     ↓
Encapsulation
     ↓
Polymorphism
     ↓
Reusable Code
```

---

# 🏆 Day 15 Achievement

## Python OOP Part 2 Completed ✅

### Practice Questions: 30 ✅

### Interview Questions: 35 ✅

### Advanced OOP Concepts: Completed ✅

---

# 📊 365-Day Journey

**Completed:** 15 / 365

**Remaining:** 350

## 🚀 Learn → Practice → Build → Improve