# 🚀 Day 007 - Mini Project

# 📌 Project Name

Student Registration System Using Python Sets

---

# 🎯 Objective

Build a simple Student Registration System that stores unique student names using Python Sets.

Since Sets automatically remove duplicate values, the same student cannot be registered twice.

---

# 📚 Concepts Used

- Set
- add()
- remove()
- discard()
- len()
- if-else
- while loop
- Membership Operator
- Functions (Basic)

---

# 💻 Python Code

```python
students = set()

while True:

    print("\n========== Student Registration ==========")

    print("1. Register Student")

    print("2. Show Students")

    print("3. Search Student")

    print("4. Remove Student")

    print("5. Total Students")

    print("6. Exit")

    choice = int(input("\nEnter Choice : "))

    if choice == 1:

        name = input("Enter Student Name : ")

        if name in students:

            print("Student Already Registered!")

        else:

            students.add(name)

            print("Registration Successful!")

    elif choice == 2:

        if len(students) == 0:

            print("No Students Registered.")

        else:

            print("\nRegistered Students:")

            for student in students:

                print(student)

    elif choice == 3:

        name = input("Enter Student Name : ")

        if name in students:

            print("Student Found.")

        else:

            print("Student Not Found.")

    elif choice == 4:

        name = input("Enter Student Name : ")

        if name in students:

            students.remove(name)

            print("Student Removed Successfully.")

        else:

            print("Student Not Found.")

    elif choice == 5:

        print("Total Registered Students :", len(students))

    elif choice == 6:

        print("Thank You!")

        break

    else:

        print("Invalid Choice.")
```

---

# 📌 Sample Output

```
========== Student Registration ==========

1. Register Student

2. Show Students

3. Search Student

4. Remove Student

5. Total Students

6. Exit

Enter Choice : 1

Enter Student Name : Amir

Registration Successful!
```

---

# 📌 Features

✔ Register Student

✔ Prevent Duplicate Registration

✔ Display All Students

✔ Search Student

✔ Remove Student

✔ Count Total Students

✔ Menu Driven Program

---

# 📌 Learning Outcomes

After completing this project you will understand:

- How Sets work
- Why Sets remove duplicates
- Membership Operators
- Set Methods
- Menu Driven Programs
- Basic Project Structure

---

# 🚀 Challenge

Try adding these features:

- Save data in a file
- Sort names alphabetically
- Store Student Roll Number
- Export data to CSV
- Create GUI using Tkinter

---

# ⭐ Difficulty

⭐⭐☆☆☆ (Beginner)

---

# 📂 Project Folder

```
DAY_7/
│
├── Mini_Project/
│   ├── student_registration.py
│   └── README.md
```

---

# 🎯 Project Completed

Congratulations!

You have successfully built your first Set-based Student Registration System.