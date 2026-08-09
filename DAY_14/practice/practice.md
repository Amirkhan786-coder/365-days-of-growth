# 💻 Day 14 — Python OOP Practice Questions

## Topic: Classes, Objects, self, __init__, Attributes & Methods

---

# 📌 Instructions

- Pehle khud question solve karo.
- Code run karke output check karo.
- Har question ko alag Python file mein bhi practice kar sakte ho.
- Questions easy se difficult order mein hain.

---

# 🟢 LEVEL 1 — Basic OOP

## Q1. Create a Class

Create a class named `Student`.

Create an object of the class and print:

```text
Student object created
```

---

## Q2. Create a Car Class

Create a class `Car`.

Create an object and print:

```text
Car is created
```

---

## Q3. Create a Method

Create a class `Student` with a method:

```text
study()
```

The method should print:

```text
Student is studying
```

---

## Q4. Create a Method for a Car

Create a class `Car` with a method:

```text
drive()
```

Output:

```text
Car is driving
```

---

## Q5. Create a Mobile Class

Create a class `Mobile`.

Create a method:

```text
call()
```

Output:

```text
Calling...
```

---

# 🟢 LEVEL 2 — self Keyword

## Q6. Use self

Create a class `Student`.

Create a method that uses `self` to print:

```text
Hello Student
```

---

## Q7. Store Name Using self

Create a class `Student`.

Use `self.name` to store a student's name.

Print the name.

Expected output:

```text
Name: Amir
```

---

## Q8. Store Age Using self

Create a class `Student`.

Store:

```text
name
age
```

using `self`.

Print both values.

---

## Q9. Student Information

Create a class `Student`.

Store:

```text
name
age
course
```

Print all information.

Example:

```text
Name: Amir
Age: 20
Course: CSE
```

---

## Q10. Employee Information

Create a class `Employee`.

Store:

```text
name
salary
department
```

Display all information.

---

# 🟡 LEVEL 3 — __init__()

## Q11. Basic Constructor

Create a class `Student` with an `__init__()` method.

When the object is created, print:

```text
Student object created
```

---

## Q12. Constructor with Name

Create a class `Student`.

Use `__init__()` to accept a student's name.

Example:

```text
Name: Amir
```

---

## Q13. Constructor with Two Values

Create a class `Student`.

Accept:

```text
name
age
```

using the constructor.

Display both.

---

## Q14. Constructor with Three Values

Create a class `Student`.

Accept:

```text
name
age
marks
```

Display all values.

---

## Q15. Employee Constructor

Create an `Employee` class.

Accept:

```text
name
salary
department
```

using `__init__()`.

Display employee information.

---

# 🟡 LEVEL 4 — Methods

## Q16. Addition Method

Create a class `Calculator`.

Create a method:

```text
add()
```

that accepts two numbers and prints their sum.

Example:

```text
10 + 20 = 30
```

---

## Q17. Subtraction Method

Create a `Calculator` class with:

```text
subtract()
```

Calculate:

```text
50 - 20
```

---

## Q18. Multiplication Method

Create a `Calculator` class with:

```text
multiply()
```

Calculate:

```text
10 × 5
```

---

## Q19. Division Method

Create a `Calculator` class with:

```text
divide()
```

Calculate:

```text
100 / 5
```

---

## Q20. Calculator Class

Create a class `Calculator` containing:

```text
add()
subtract()
multiply()
divide()
```

Test all methods.

---

# 🟡 LEVEL 5 — Multiple Objects

## Q21. Two Students

Create two objects:

```text
student1
student2
```

Store different names and ages.

Display both students.

---

## Q22. Three Students

Create three student objects:

```text
student1
student2
student3
```

Store:

```text
name
marks
```

Display all three.

---

## Q23. Multiple Employees

Create three employee objects.

Store:

```text
name
salary
```

Display employee information.

---

## Q24. Multiple Cars

Create three `Car` objects.

Store:

```text
brand
model
price
```

Display all cars.

---

## Q25. Multiple Mobile Phones

Create three `Mobile` objects.

Store:

```text
brand
model
price
```

Display all information.

---

# 🟠 LEVEL 6 — Class Variables

## Q26. School Name

Create a class `Student`.

Create a class variable:

```text
school = "ABC School"
```

Create two students and display the school name.

---

## Q27. Company Name

Create an `Employee` class.

Create a class variable:

```text
company = "Tech Company"
```

Create two employees and display the company name.

---

## Q28. College Name

Create a `Student` class with:

```text
college = "Shobhit University"
```

Create three students.

Display:

```text
Name
College
```

for each student.

---

# 🟠 LEVEL 7 — Attribute Modification

## Q29. Change Student Age

Create a student object with age:

```text
20
```

Change the age to:

```text
21
```

Print the updated age.

---

## Q30. Update Employee Salary

Create an employee with salary:

```text
40000
```

Update it to:

```text
50000
```

Display the updated salary.

---

## Q31. Add New Attribute

Create a `Student` object.

Initially store:

```text
name
age
```

Later add:

```text
course
```

Display all three.

---

# 🔴 LEVEL 8 — Logic with OOP

## Q32. Calculate Student Grade

Create a `Student` class.

Store:

```text
name
marks
```

Create a method:

```text
calculate_grade()
```

Use:

```text
90+  → A+
80+  → A
70+  → B
60+  → C
Below 60 → D
```

Display the grade.

---

## Q33. Calculate Average Marks

Create a class `Student`.

Store marks of three subjects:

```text
Python
Math
English
```

Create a method:

```text
calculate_average()
```

Display the average.

---

## Q34. Check Pass or Fail

Create a `Student` class.

Store marks.

Create:

```text
check_result()
```

If marks are 40 or above:

```text
Pass
```

Otherwise:

```text
Fail
```

---

## Q35. Bank Account

Create a class:

```text
BankAccount
```

Attributes:

```text
name
balance
```

Methods:

```text
deposit()
withdraw()
display_balance()
```

Example:

```text
Initial Balance: 5000
Deposit: 2000
New Balance: 7000
```

---

# 🔥 BONUS CHALLENGE QUESTIONS

## Q36. Rectangle

Create a class `Rectangle`.

Store:

```text
length
width
```

Create methods:

```text
area()
perimeter()
```

Calculate both.

---

## Q37. Circle

Create a class `Circle`.

Store:

```text
radius
```

Create a method:

```text
area()
```

Use:

```text
π × r × r
```

---

## Q38. Product

Create a class `Product`.

Store:

```text
name
price
quantity
```

Create a method:

```text
total_price()
```

Calculate:

```text
price × quantity
```

---

## Q39. Employee Salary

Create an `Employee` class.

Store:

```text
name
salary
```

Create a method:

```text
annual_salary()
```

Calculate:

```text
salary × 12
```

---

## Q40. Student Gradebook

Create a class:

```text
Student
```

Attributes:

```text
name
marks
```

Methods:

```text
calculate_grade()
display()
```

Create at least three student objects.

Display:

```text
Name
Marks
Grade
```

---

# 🏆 FINAL CHALLENGE

## Q41. Bank Management System

Create a class:

```text
BankAccount
```

Attributes:

```text
account_holder
account_number
balance
```

Methods:

```text
deposit()
withdraw()
check_balance()
display_account()
```

The program should allow:

```text
1. Deposit
2. Withdraw
3. Check Balance
4. Account Details
5. Exit
```

---

# 🎯 Practice Checklist

```text
Q1   ⬜
Q2   ⬜
Q3   ⬜
Q4   ⬜
Q5   ⬜
Q6   ⬜
Q7   ⬜
Q8   ⬜
Q9   ⬜
Q10  ⬜
Q11  ⬜
Q12  ⬜
Q13  ⬜
Q14  ⬜
Q15  ⬜
Q16  ⬜
Q17  ⬜
Q18  ⬜
Q19  ⬜
Q20  ⬜
Q21  ⬜
Q22  ⬜
Q23  ⬜
Q24  ⬜
Q25  ⬜
Q26  ⬜
Q27  ⬜
Q28  ⬜
Q29  ⬜
Q30  ⬜
Q31  ⬜
Q32  ⬜
Q33  ⬜
Q34  ⬜
Q35  ⬜
Q36  ⬜
Q37  ⬜
Q38  ⬜
Q39  ⬜
Q40  ⬜
Q41  ⬜

Total: 41 Questions
```

---

# 🚀 Day 14 Practice Goal

Minimum:

```text
Basic Questions      → 10
Intermediate         → 20
Logic Questions      → 5
Challenge Questions  → 3
Final Challenge      → 1
```

## Target

```text
41 Questions
↓
Practice
↓
Build Confidence
↓
Apply OOP
↓
Build Mini Project
```

# 🏆 DAY 14 — PRACTICE COMPLETE

**Next File:** `mcqs.md`