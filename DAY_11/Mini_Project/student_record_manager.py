# ==========================================
# Mini Project: Student Record Manager
# Day 11 - Python File Handling
# ==========================================

import os

FILE_NAME = "students.txt"


def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("\n✅ Student Added Successfully!\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:

            data = file.readlines()

            if not data:
                print("\nNo Records Found!\n")
                return

            print("\n========== STUDENT RECORDS ==========")

            for i, student in enumerate(data, start=1):
                name, age, course = student.strip().split(",")
                print(f"{i}. Name   : {name}")
                print(f"   Age    : {age}")
                print(f"   Course : {course}")
                print("-" * 35)

    except FileNotFoundError:
        print("\nNo Records Found!\n")


def search_student():
    keyword = input("Enter Student Name: ").lower()

    found = False

    try:
        with open(FILE_NAME, "r") as file:

            for student in file:

                if keyword in student.lower():

                    name, age, course = student.strip().split(",")

                    print("\nStudent Found\n")

                    print("Name :", name)
                    print("Age :", age)
                    print("Course :", course)

                    found = True

        if not found:
            print("\nStudent Not Found!")

    except FileNotFoundError:
        print("\nNo Records Found!")


def update_student():
    keyword = input("Enter Student Name to Update: ")

    try:

        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        updated = False

        with open(FILE_NAME, "w") as file:

            for student in students:

                name, age, course = student.strip().split(",")

                if name.lower() == keyword.lower():

                    print("\nEnter New Details")

                    name = input("Name : ")
                    age = input("Age : ")
                    course = input("Course : ")

                    updated = True

                file.write(f"{name},{age},{course}\n")

        if updated:
            print("\nStudent Updated Successfully!")
        else:
            print("\nStudent Not Found!")

    except FileNotFoundError:
        print("\nNo Records Found!")


def delete_student():
    keyword = input("Enter Student Name to Delete: ")

    try:

        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        deleted = False

        with open(FILE_NAME, "w") as file:

            for student in students:

                name, age, course = student.strip().split(",")

                if name.lower() != keyword.lower():
                    file.write(student)
                else:
                    deleted = True

        if deleted:
            print("\nStudent Deleted Successfully!")
        else:
            print("\nStudent Not Found!")

    except FileNotFoundError:
        print("\nNo Records Found!")


while True:

    print("\n==============================")
    print(" STUDENT RECORD MANAGER ")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("==============================")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank You for Using Student Record Manager ❤️")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")