# 🚀 DAY 15 / 365 — Python OOP Part 2

## 🐍 Advanced Object-Oriented Programming

Today I am learning advanced concepts of Object-Oriented Programming (OOP) in Python.

---

# 📚 Topics Covered

1. Inheritance
2. Parent Class
3. Child Class
4. `super()`
5. Method Overriding
6. Multilevel Inheritance
7. Multiple Inheritance
8. Polymorphism
9. Encapsulation
10. Getters and Setters
11. Abstraction
12. Abstract Class
13. Real-World OOP Applications

---

# 1. Inheritance

Inheritance allows one class to use the properties and methods of another class.

The existing class is called the:

- Parent Class
- Base Class

The new class is called the:

- Child Class
- Derived Class

### Example

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.bark()
```

Here:

```text
Animal → Parent Class
Dog    → Child Class
```

The `Dog` class inherits the `eat()` method from `Animal`.

---

# 2. Parent Class

A parent class is the class whose properties and methods are inherited by another class.

### Example

```python
class Animal:

    def eat(self):
        print("Animal is eating")
```

Here `Animal` is the parent class.

---

# 3. Child Class

A child class inherits properties and methods from a parent class.

### Example

```python
class Dog(Animal):

    def bark(self):
        print("Dog is barking")
```

Here `Dog` is the child class.

---

# 4. Syntax of Inheritance

```python
class Parent:

    pass


class Child(Parent):

    pass
```

The child class can access the members of the parent class.

---

# 5. Simple Inheritance Example

```python
class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


car1 = Car()

car1.start()
car1.drive()
```

### Output

```text
Vehicle started
Car is driving
```

The `Car` object can use `start()` because `Car` inherits from `Vehicle`.

---

# 6. Benefits of Inheritance

Inheritance provides:

- Code reusability
- Less duplicate code
- Better organization
- Easier maintenance
- Relationship between classes

Example:

```text
Vehicle
   ↓
Car
   ↓
SportsCar
```

---

# 7. `super()`

`super()` is used to access the parent class implementation from a child class.

It is commonly used to call the parent class constructor or methods.

### Example

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


student1 = Student("Amir", "CSE")

print(student1.name)
print(student1.course)
```

### Output

```text
Amir
CSE
```

Here:

```python
super().__init__(name)
```

calls the parent class constructor.

---

# 8. Why Use `super()`?

Suppose the parent class already has initialization logic.

Instead of writing the same code again, we can use:

```python
super().__init__()
```

This helps avoid duplicate code.

---

# 9. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

### Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()
```

### Output

```text
Dog barks
```

The child class method overrides the parent class method.

---

# 10. Calling Parent Method with `super()`

A child class can also call the parent version of an overridden method.

### Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog1 = Dog()

dog1.sound()
```

### Output

```text
Animal makes a sound
Dog barks
```

---

# 11. Multilevel Inheritance

Multilevel inheritance means inheritance occurs across multiple levels.

### Structure

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

### Example

```python
class Grandparent:

    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):

    def car(self):
        print("Parent's car")


class Child(Parent):

    def bike(self):
        print("Child's bike")


child1 = Child()

child1.house()
child1.car()
child1.bike()
```

### Output

```text
Grandparent's house
Parent's car
Child's bike
```

The child can access methods from both parent and grandparent.

---

# 12. Multiple Inheritance

Multiple inheritance means a child class inherits from more than one parent class.

### Example

```python
class Father:

    def father_skill(self):
        print("Father's skill")


class Mother:

    def mother_skill(self):
        print("Mother's skill")


class Child(Father, Mother):

    def child_skill(self):
        print("Child's skill")


child1 = Child()

child1.father_skill()
child1.mother_skill()
child1.child_skill()
```

### Output

```text
Father's skill
Mother's skill
Child's skill
```

---

# 13. Method Resolution Order (MRO)

When multiple inheritance is used, Python needs to determine which class should be searched first.

This order is called Method Resolution Order or MRO.

We can see it using:

```python
ClassName.mro()
```

### Example

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
```

Python shows the order in which it searches for methods.

---

# 14. Polymorphism

Polymorphism means:

```text
One Interface
      ↓
Different Behaviors
```

Different classes can have methods with the same name but different behavior.

### Example

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

### Output

```text
Bark
Meow
```

Both classes have the same method:

```python
sound()
```

but they behave differently.

---

# 15. Polymorphism with a Common Function

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
```

### Output

```text
Bark
Meow
```

The function works with different objects that provide the required `sound()` method.

---

# 16. Encapsulation

Encapsulation means keeping data and the methods that operate on that data together inside a class, while controlling how the data is accessed.

Python uses naming conventions to indicate intended access levels.

### Public Attribute

```python
class Student:

    def __init__(self, name):
        self.name = name
```

`name` is a public attribute.

---

# 17. Protected Convention

A single underscore is commonly used to indicate that an attribute is intended for internal or subclass use.

### Example

```python
class Student:

    def __init__(self, marks):
        self._marks = marks
```

`_marks` is a protected-style naming convention.

It is not strict access control in Python.

---

# 18. Private-Style Attribute

A double underscore triggers Python's name-mangling mechanism.

### Example

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks
```

Here `__marks` is treated as a private-style attribute.

---

# 19. Getter Method

A getter method is used to access encapsulated data.

### Example

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student1 = Student(85)

print(student1.get_marks())
```

---

# 20. Setter Method

A setter method is used to update encapsulated data.

### Example

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        self.__marks = marks


student1 = Student(85)

student1.set_marks(90)

print(student1.get_marks())
```

---

# 21. Getter and Setter Together

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


student1 = Student(80)

print("Old Marks:", student1.get_marks())

student1.set_marks(95)

print("New Marks:", student1.get_marks())
```

---

# 22. Abstraction

Abstraction means hiding unnecessary implementation details and exposing only the essential functionality.

Python supports abstraction using the `abc` module.

---

# 23. Abstract Class

An abstract class is a class that contains one or more abstract methods.

### Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

The abstract method does not provide the complete implementation in the base class.

---

# 24. Implementing an Abstract Class

A child class provides the implementation of the abstract method.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()
```

### Output

```text
Dog barks
```

---

# 25. Four Major OOP Concepts

The four major concepts commonly discussed in OOP are:

```text
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
```

### Easy Revision

```text
Encapsulation
      ↓
Controlled Access to Data


Inheritance
      ↓
Code Reuse


Polymorphism
      ↓
Different Behavior


Abstraction
      ↓
Hide Implementation Details
```

---

# 26. Inheritance vs Polymorphism

## Inheritance

Inheritance focuses on:

```text
Parent
  ↓
Child
```

It allows the child class to reuse functionality from the parent class.

## Polymorphism

Polymorphism focuses on:

```text
Same Method
     ↓
Different Behavior
```

Example:

```text
Dog.sound() → Bark
Cat.sound() → Meow
```

---

# 27. `self` vs `super()`

## self

`self` refers to the current object.

Example:

```python
self.name
```

## super()

`super()` provides access to the parent class implementation.

Example:

```python
super().__init__()
```

---

# 28. Types of Inheritance

Python supports several common inheritance structures.

### Single Inheritance

```text
Parent
  ↓
Child
```

### Multilevel Inheritance

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

### Multiple Inheritance

```text
Parent 1     Parent 2
     \         /
       Child
```

### Hierarchical Inheritance

```text
       Parent
       /    \
    Child1  Child2
```

---

# 29. Real-World Example — Vehicle System

Consider:

```text
             Vehicle
                ↓
      ┌─────────┼─────────┐
      ↓         ↓         ↓
     Car       Bike      Bus
```

The common functionality can be placed inside `Vehicle`.

The child classes can provide their own specific behavior.

---

# 30. Real-World Example — Employee System

```text
Employee
   ↓
   ├── Developer
   ├── Designer
   └── Manager
```

Each child class can have its own methods while reusing common employee information.

---

# 31. Real-World Example — Payment System

```text
Payment
   ↓
   ├── CreditCard
   ├── UPI
   └── Cash
```

Each payment type can implement a common method such as:

```python
pay()
```

but the behavior can be different.

This is an example of polymorphism.

---

# 32. Advantages of OOP

OOP provides:

- Code reusability
- Modularity
- Better organization
- Easier maintenance
- Scalability
- Data organization
- Easier testing
- Real-world modeling

---

# 33. OOP Concepts Quick Revision

```text
Class
↓
Blueprint


Object
↓
Instance of Class


Inheritance
↓
Reuse Parent Features


super()
↓
Access Parent Implementation


Method Overriding
↓
Child Changes Parent Behavior


Polymorphism
↓
Same Interface, Different Behavior


Encapsulation
↓
Controlled Data Access


Abstraction
↓
Hide Implementation Details
```

---

# 🎯 Day 15 Learning Goals

By the end of Day 15, I should be able to:

- Create parent classes
- Create child classes
- Implement inheritance
- Use `super()`
- Override methods
- Implement multilevel inheritance
- Implement multiple inheritance
- Understand MRO
- Understand polymorphism
- Implement encapsulation
- Use getters and setters
- Understand abstraction
- Create abstract classes
- Apply OOP to real-world problems

---

# 🏆 Day 15 Summary

Today I learned advanced Python OOP concepts:

```text
Inheritance
      ↓
super()
      ↓
Method Overriding
      ↓
Multilevel Inheritance
      ↓
Multiple Inheritance
      ↓
MRO
      ↓
Polymorphism
      ↓
Encapsulation
      ↓
Getters & Setters
      ↓
Abstraction
```

---

# 🚀 NEXT STEP

After completing these concepts, I will solve practical questions based on Python OOP Part 2.

Then I will build a real-world OOP mini project.

---

# 🔥 DAY 15

## Learn → Practice → Build → Improve

### Progress: 15 / 365 🚀