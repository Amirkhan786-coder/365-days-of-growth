# 🧪 DAY 15 — Python OOP Part 2
# Practice Questions

## Topic:
Inheritance, super(), Method Overriding, Multilevel Inheritance,
Multiple Inheritance, Polymorphism, Encapsulation & Abstraction

---

# Q1. Create a Parent Class

Create a class `Animal` with a method `eat()` that prints `"Animal is eating"`.

```python
class Animal:

    def eat(self):
        print("Animal is eating")


animal1 = Animal()

animal1.eat()
```

---

# Q2. Create a Child Class

Create a `Dog` class that inherits from `Animal` and has a method `bark()`.

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

---

# Q3. Vehicle Inheritance

Create a `Vehicle` class with a `start()` method and a `Car` class that inherits from it.

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

---

# Q4. Person and Student

Create a `Person` class containing a name and a `Student` class that inherits from it.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def display(self):
        print("Student Name:", self.name)


student1 = Student("Amir")

student1.display()
```

---

# Q5. Employee Inheritance

Create an `Employee` parent class and a `Developer` child class.

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def display_employee(self):
        print("Employee:", self.name)


class Developer(Employee):

    def code(self):
        print(self.name, "is coding")


developer1 = Developer("Amir")

developer1.display_employee()
developer1.code()
```

---

# Q6. Use super()

Create a parent class `Person` and use `super()` inside the child class `Student`.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student1 = Student("Amir", "CSE")

student1.display()
```

---

# Q7. super() with Parent Method

Use `super()` to call a parent class method.

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

---

# Q8. Method Overriding

Create a parent class `Animal` with `sound()` and override it in `Dog`.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()
```

---

# Q9. Method Overriding with Cat

Create `Animal`, `Dog`, and `Cat` classes and override `sound()`.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog1 = Dog()
cat1 = Cat()

dog1.sound()
cat1.sound()
```

---

# Q10. Multilevel Inheritance

Create three classes:

Grandparent → Parent → Child

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

---

# Q11. Multilevel Student System

Create:

Person → Student → CollegeStudent

```python
class Person:

    def person_info(self):
        print("This is a person")


class Student(Person):

    def student_info(self):
        print("This is a student")


class CollegeStudent(Student):

    def college_info(self):
        print("This is a college student")


student1 = CollegeStudent()

student1.person_info()
student1.student_info()
student1.college_info()
```

---

# Q12. Multiple Inheritance

Create two parent classes `Father` and `Mother` and one child class `Child`.

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

---

# Q13. Multiple Inheritance with Constructors

Create a `Father` and `Mother` class with separate attributes.

```python
class Father:

    def __init__(self, father_name):
        self.father_name = father_name


class Mother:

    def __init__(self, mother_name):
        self.mother_name = mother_name


class Child(Father, Mother):

    def __init__(self, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)


child1 = Child("Ramesh", "Sunita")

print("Father:", child1.father_name)
print("Mother:", child1.mother_name)
```

---

# Q14. Polymorphism

Create two classes with the same method name but different behavior.

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

# Q15. Polymorphism with Function

Create a function that accepts different objects.

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

---

# Q16. Shape Polymorphism

Create different classes with an `area()` method.

```python
class Rectangle:

    def area(self):
        print("Rectangle area")


class Circle:

    def area(self):
        print("Circle area")


class Square:

    def area(self):
        print("Square area")


shapes = [
    Rectangle(),
    Circle(),
    Square()
]

for shape in shapes:
    shape.area()
```

---

# Q17. Encapsulation

Create a class with a private-style `__balance` attribute.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(10000)

account.show_balance()
```

---

# Q18. Getter Method

Create a getter method to access private-style data.

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student1 = Student(85)

print("Marks:", student1.get_marks())
```

---

# Q19. Setter Method

Create a setter method to update marks.

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student1 = Student(80)

print("Old Marks:", student1.get_marks())

student1.set_marks(95)

print("New Marks:", student1.get_marks())
```

---

# Q20. Setter with Validation

Create a setter that accepts marks only between 0 and 100.

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
            print("Invalid Marks")


student1 = Student(80)

student1.set_marks(95)

print("Marks:", student1.get_marks())
```

---

# Q21. Encapsulated Bank Account

Create a bank account with private-style balance and deposit/withdraw methods.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(2000)

account.withdraw(1000)

print("Balance:", account.get_balance())
```

---

# Q22. Abstraction

Create an abstract `Animal` class.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

# Q23. Abstract Class Implementation

Create a `Dog` class that implements the abstract method.

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

---

# Q24. Abstract Shape

Create an abstract `Shape` class and implement it using `Circle`.

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


circle1 = Circle(5)

print("Area:", circle1.area())
```

---

# Q25. Abstract Payment System

Create an abstract payment class with different payment methods.

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card")


upi = UPI()
card = Card()

upi.pay(500)
card.pay(1000)
```

---

# Q26. Single Inheritance Real-World Example

Create a `Vehicle` parent class and a `Bike` child class.

```python
class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "vehicle started")


class Bike(Vehicle):

    def ride(self):
        print(self.brand, "bike is riding")


bike1 = Bike("Honda")

bike1.start()
bike1.ride()
```

---

# Q27. Multilevel Inheritance Real-World Example

Create:

Vehicle → Car → ElectricCar

```python
class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


class ElectricCar(Car):

    def charge(self):
        print("Electric car is charging")


car1 = ElectricCar()

car1.start()
car1.drive()
car1.charge()
```

---

# Q28. Polymorphism with Vehicles

Create different vehicles with the same `start()` method.

```python
class Car:

    def start(self):
        print("Car starts with a key")


class Bike:

    def start(self):
        print("Bike starts with a button")


class ElectricCar:

    def start(self):
        print("Electric car starts silently")


vehicles = [
    Car(),
    Bike(),
    ElectricCar()
]

for vehicle in vehicles:
    vehicle.start()
```

---

# Q29. Employee OOP System

Create an employee hierarchy using inheritance.

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working")


class Developer(Employee):

    def work(self):
        print(self.name, "is writing code")


class Designer(Employee):

    def work(self):
        print(self.name, "is designing")


developer = Developer("Amir")
designer = Designer("Rahul")

developer.work()
designer.work()
```

---

# Q30. Complete OOP Practice Program

Create a simple system using inheritance, polymorphism and encapsulation.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def work(self):
        print(self.name, "is working")


class Developer(Employee):

    def work(self):
        print(self.name, "is developing software")


class Designer(Employee):

    def work(self):
        print(self.name, "is designing UI")


developer = Developer("Amir", 50000)
designer = Designer("Rahul", 45000)

developer.work()
designer.work()

print("Developer Salary:", developer.get_salary())
print("Designer Salary:", designer.get_salary())
```

---

# 🎯 Day 15 Practice Checklist

- [ ] Q1 Parent Class
- [ ] Q2 Child Class
- [ ] Q3 Vehicle Inheritance
- [ ] Q4 Person and Student
- [ ] Q5 Employee Inheritance
- [ ] Q6 `super()`
- [ ] Q7 Parent Method with `super()`
- [ ] Q8 Method Overriding
- [ ] Q9 Animal Polymorphism
- [ ] Q10 Multilevel Inheritance
- [ ] Q11 Student Multilevel Inheritance
- [ ] Q12 Multiple Inheritance
- [ ] Q13 Multiple Inheritance Constructors
- [ ] Q14 Basic Polymorphism
- [ ] Q15 Polymorphism Function
- [ ] Q16 Shape Polymorphism
- [ ] Q17 Encapsulation
- [ ] Q18 Getter
- [ ] Q19 Setter
- [ ] Q20 Setter Validation
- [ ] Q21 Bank Encapsulation
- [ ] Q22 Abstraction
- [ ] Q23 Abstract Class
- [ ] Q24 Abstract Shape
- [ ] Q25 Abstract Payment
- [ ] Q26 Vehicle Inheritance
- [ ] Q27 Multilevel Vehicle
- [ ] Q28 Vehicle Polymorphism
- [ ] Q29 Employee OOP
- [ ] Q30 Complete OOP Program

---

# 🏆 Day 15 Practice Goal

Complete all 30 questions and understand:

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
Polymorphism
      ↓
Encapsulation
      ↓
Abstraction
```

## 🚀 Progress

**Day 15 / 365 — Practice Questions: 30**