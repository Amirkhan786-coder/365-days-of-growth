# 🎯 DAY 15 / 365
# Python OOP Part 2 — Interview Questions & Answers

---

## Q1. What is inheritance in Python?

Inheritance is an OOP concept in which a child class can acquire properties and methods from a parent class.

### Example:

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    pass


dog = Dog()

dog.eat()
```

Here, `Dog` inherits from `Animal`.

---

## Q2. What is a parent class?

A parent class is the class whose properties and methods are inherited by another class.

### Example:

```python
class Animal:

    def eat(self):
        print("Eating")
```

Here, `Animal` is the parent class.

---

## Q3. What is a child class?

A child class is a class that inherits properties and methods from another class.

### Example:

```python
class Dog(Animal):

    def bark(self):
        print("Barking")
```

Here, `Dog` is the child class.

---

## Q4. What is the syntax of inheritance?

```python
class Parent:

    pass


class Child(Parent):

    pass
```

The child class inherits from the parent class.

---

## Q5. What is `super()` in Python?

`super()` is used to access methods or the constructor of the parent class.

### Example:

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name):
        super().__init__(name)
```

---

## Q6. Why do we use `super()`?

`super()` helps us reuse parent class functionality without rewriting the same code.

It is commonly used when:

- Calling the parent constructor
- Calling a parent method
- Extending parent functionality

---

## Q7. What is method overriding?

Method overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

### Example:

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()
```

Output:

```text
Dog barks
```

---

## Q8. What is multilevel inheritance?

Multilevel inheritance means inheritance happens at multiple levels.

### Structure:

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

### Example:

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass
```

---

## Q9. What is multiple inheritance?

Multiple inheritance means one child class inherits from more than one parent class.

### Example:

```python
class Father:

    def skill1(self):
        print("Father's skill")


class Mother:

    def skill2(self):
        print("Mother's skill")


class Child(Father, Mother):

    pass


child = Child()

child.skill1()
child.skill2()
```

---

## Q10. Does Python support multiple inheritance?

Yes.

Python supports multiple inheritance.

### Example:

```python
class A:
    pass


class B:
    pass


class C(A, B):
    pass
```

---

## Q11. What is polymorphism?

Polymorphism means **one interface with different behavior**.

Different classes can have methods with the same name but different implementations.

### Example:

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

## Q12. Give a real-world example of polymorphism.

A payment system is a good example.

```text
Payment
   ↓
 ┌───────┬───────┐
 ↓       ↓       ↓
UPI     Card    Cash
```

Each payment type can have its own `pay()` method.

---

## Q13. What is encapsulation?

Encapsulation means keeping data and related methods together inside a class and controlling access to the data.

### Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

---

## Q14. What does `__` mean before an attribute?

Double underscore triggers Python's name-mangling mechanism.

It is commonly used when an attribute is intended to be private to the class.

### Example:

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks
```

---

## Q15. What is a getter?

A getter is a method used to access or retrieve the value of an encapsulated attribute.

### Example:

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
```

---

## Q16. What is a setter?

A setter is a method used to modify or update the value of an encapsulated attribute.

### Example:

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        self.__marks = marks
```

---

## Q17. Why are getters and setters useful?

They allow us to control how data is read or modified.

For example, we can validate data before storing it.

### Example:

```python
def set_marks(self, marks):

    if 0 <= marks <= 100:
        self.__marks = marks
    else:
        print("Invalid marks")
```

---

## Q18. What is abstraction?

Abstraction means exposing essential functionality while hiding unnecessary implementation details.

Python provides the `abc` module for creating abstract classes.

---

## Q19. What is an abstract class?

An abstract class is a class that can contain abstract methods that subclasses are expected to implement.

### Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## Q20. What is an abstract method?

An abstract method is a method declared using `@abstractmethod`.

The subclass is expected to provide its implementation.

### Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## Q21. Which module is used for abstraction?

Python provides the `abc` module.

### Example:

```python
from abc import ABC, abstractmethod
```

---

## Q22. What is `ABC`?

`ABC` stands for **Abstract Base Class**.

It is used as a base class for defining abstract classes.

### Example:

```python
from abc import ABC


class Animal(ABC):

    pass
```

---

## Q23. What is `@abstractmethod`?

`@abstractmethod` is a decorator used to declare an abstract method.

### Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## Q24. Can an abstract class contain normal methods?

Yes.

An abstract class can contain both:

- Abstract methods
- Normal methods

### Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    def eat(self):
        print("Animal is eating")

    @abstractmethod
    def sound(self):
        pass
```

---

## Q25. What happens if a child class does not implement an abstract method?

The child class remains abstract and cannot normally be instantiated until it implements all required abstract methods.

### Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    pass
```

`Dog()` cannot normally be created because `sound()` is not implemented.

---

## Q26. What is MRO?

MRO stands for:

**Method Resolution Order**

It determines the order in which Python searches classes for methods and attributes.

### Example:

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
```

---

## Q27. What is the difference between `self` and `super()`?

### `self`

`self` refers to the current object.

```python
self.name
```

### `super()`

`super()` provides access to parent class functionality.

```python
super().__init__()
```

---

## Q28. What are the four major pillars of OOP?

The four commonly discussed pillars are:

```text
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
```

---

## Q29. What is the difference between inheritance and polymorphism?

### Inheritance

Inheritance focuses on reusing functionality from another class.

```text
Parent
  ↓
Child
```

### Polymorphism

Polymorphism focuses on different objects providing different behavior through a common interface.

```text
Dog.sound() → Bark
Cat.sound() → Meow
```

---

## Q30. What is the difference between encapsulation and abstraction?

### Encapsulation

Encapsulation focuses on organizing and controlling access to data.

### Abstraction

Abstraction focuses on hiding unnecessary implementation details and exposing essential functionality.

---

# 🔥 BONUS INTERVIEW QUESTIONS

## Q31. What is single inheritance?

Single inheritance occurs when one child class inherits from one parent class.

```python
class Parent:

    pass


class Child(Parent):

    pass
```

---

## Q32. What is hierarchical inheritance?

Hierarchical inheritance occurs when multiple child classes inherit from the same parent class.

```text
        Animal
        /    \
      Dog    Cat
```

---

## Q33. What is the main advantage of inheritance?

The main advantage is **code reusability**.

It reduces duplicate code and makes programs easier to maintain.

---

## Q34. What are the advantages of OOP?

Major advantages include:

- Code reusability
- Modularity
- Better organization
- Maintainability
- Scalability
- Data organization
- Easier testing

---

## Q35. Why is OOP important in real-world applications?

OOP allows developers to represent real-world entities as objects.

For example:

```text
College System
     ↓
Student
Teacher
Course
Department
```

Each entity can have its own properties and methods.

---

# ⚡ RAPID-FIRE REVISION

## Inheritance

```text
Parent → Child
```

Used for code reuse.

---

## `super()`

```text
Access Parent Functionality
```

---

## Method Overriding

```text
Parent Method
      ↓
Child provides new implementation
```

---

## Polymorphism

```text
Same Interface
      ↓
Different Behavior
```

---

## Encapsulation

```text
Data
 ↓
Controlled Access
```

---

## Getter

```text
Read Data
```

---

## Setter

```text
Update Data
```

---

## Abstraction

```text
Hide Implementation Details
```

---

## ABC

```text
Abstract Base Class
```

---

## MRO

```text
Method Resolution Order
```

---

# 🎯 DAY 15 INTERVIEW CHECKLIST

- [ ] Inheritance
- [ ] Parent Class
- [ ] Child Class
- [ ] `super()`
- [ ] Method Overriding
- [ ] Single Inheritance
- [ ] Multilevel Inheritance
- [ ] Multiple Inheritance
- [ ] Hierarchical Inheritance
- [ ] Polymorphism
- [ ] Encapsulation
- [ ] Getter
- [ ] Setter
- [ ] Abstraction
- [ ] Abstract Class
- [ ] Abstract Method
- [ ] `ABC`
- [ ] `@abstractmethod`
- [ ] MRO
- [ ] Four Pillars of OOP

---

# 🏆 DAY 15 RESULT

**35 Interview Questions Completed ✅**

### Topics Covered:

Python OOP Part 2 ✅  
Inheritance ✅  
`super()` ✅  
Method Overriding ✅  
Multiple Inheritance ✅  
Multilevel Inheritance ✅  
Polymorphism ✅  
Encapsulation ✅  
Getters & Setters ✅  
Abstraction ✅  
Abstract Classes ✅  
MRO ✅  

---

# 🚀 PROGRESS

## DAY 15 / 365

**Learn → Practice → Interview Preparation → Build**