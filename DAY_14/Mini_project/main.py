# ============================================
# DAY 14 - STUDENT GRADEBOOK
# Python OOP Mini Project
# ============================================


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

        elif self.marks >= 40:
            return "D"

        else:
            return "F"

    def display(self):

        print("----------------------------")
        print("Name  :", self.name)
        print("Marks :", self.marks)
        print("Grade :", self.calculate_grade())
        print("----------------------------")


# Store all students
students = []


# Add Student
def add_student():

    print("\n===== ADD STUDENT =====")

    name = input("Enter student name: ")

    try:
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid marks.")
        return

    student = Student(name, marks)

    students.append(student)

    print("Student added successfully!")


# Display All Students
def display_students():

    print("\n===== ALL STUDENTS =====")

    if len(students) == 0:
        print("No students available.")
        return

    for student in students:
        student.display()


# Calculate Average
def show_average():

    print("\n===== AVERAGE MARKS =====")

    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for student in students:
        total += student.marks

    average = total / len(students)

    print("Average Marks:", round(average, 2))


# Find Highest Scorer
def highest_scorer():

    print("\n===== HIGHEST SCORER =====")

    if len(students) == 0:
        print("No students available.")
        return

    highest = students[0]

    for student in students:

        if student.marks > highest.marks:
            highest = student

    print("Highest Scorer:", highest.name)
    print("Marks:", highest.marks)
    print("Grade:", highest.calculate_grade())


# Total Students
def total_students():

    print("\n===== TOTAL STUDENTS =====")

    print("Total Students:", len(students))


# Main Menu
while True:

    print("\n")
    print("================================")
    print("       STUDENT GRADEBOOK")
    print("================================")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Show Average Marks")
    print("4. Show Highest Scorer")
    print("5. Show Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        display_students()

    elif choice == "3":

        show_average()

    elif choice == "4":

        highest_scorer()

    elif choice == "5":

        total_students()

    elif choice == "6":

        print("\nThank you for using Student Gradebook!")
        print("Day 14 Mini Project Completed 🚀")
        break

    else:

        print("Invalid choice. Please try again.")