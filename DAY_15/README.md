# 🚀 DAY 15 / 365 — Python OOP Part 2

> Continuing my 365 Days of Growth journey 🚀

---

## 📅 Day 15

Today I continued learning **Object-Oriented Programming (OOP) in Python** and moved from basic classes and objects toward more advanced OOP concepts.

---

# 📚 Topics Covered

- Inheritance
- Parent & Child Classes
- `super()`
- Method Overriding
- Multilevel Inheritance
- Multiple Inheritance
- Polymorphism
- Encapsulation
- Getters & Setters
- Abstraction
- Abstract Classes
- Abstract Methods
- Method Resolution Order (MRO)

---

# 🧠 Key Concepts

## 1. Inheritance

Inheritance allows a child class to reuse functionality from a parent class.

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.bark()
```

---

## 2. `super()`

`super()` is used to access functionality from the parent class.

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

A child class can provide its own implementation of a parent method.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")
```

---

## 4. Polymorphism

Different objects can use the same method name but behave differently.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

---

## 5. Encapsulation

Encapsulation helps control access to data inside a class.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

---

## 6. Abstraction

Abstraction hides unnecessary implementation details and exposes essential functionality.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

# 🧪 Practice

Today I completed:

- ✅ 30 Practice Questions
- ✅ Inheritance Practice
- ✅ `super()` Practice
- ✅ Polymorphism Practice
- ✅ Encapsulation Practice
- ✅ Abstraction Practice

---

# 🎯 Interview Preparation

I prepared **35 interview questions** covering:

```text
Inheritance
super()
Method Overriding
Multilevel Inheritance
Multiple Inheritance
Polymorphism
Encapsulation
Getter & Setter
Abstraction
Abstract Class
Abstract Method
MRO
```

---

# 📂 Files in This Folder

```text
Day15/
│
├── notes.md
├── practice_questions.md
├── practice_codes.md
├── mcqs.md
├── interview_questions.md
├── reflection.md
├── learning_outcomes.md
├── README.md
├── project.md
└── mini_project/
```

---

# 💡 Key Learning

OOP helps me write programs that are:

- Reusable
- Organized
- Maintainable
- Scalable
- Easier to understand

The four major OOP concepts are:

```text
Encapsulation
Inheritance
Polymorphism
Abstraction
```

---

# 🏆 Day 15 Achievement

```text
Python OOP Part 2
        ↓
30 Practice Questions
        ↓
35 Interview Questions
        ↓
Advanced OOP Concepts
        ↓
Day 15 Completed ✅
```

---

# 📈 365 Days of Growth

**Day 15 / 365**

```text
████░░░░░░░░░░░░░░░░  4.1%
```

---

# 🚀 What's Next?

Continue Python learning with more practical problem-solving and gradually move toward building real-world projects.

---

## 🔥 My Goal

> Learn every day.  
> Practice every day.  
> Build every day.  
> Become better every day.

**15 / 365 — Keep Growing 🚀**