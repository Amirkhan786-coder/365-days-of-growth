# Q34. Safe Student Management System
# Question:
# Create a simple student management program.
#
# Features:
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Exit
#
# Handle:
# ValueError
# Missing student
# Invalid menu choice

students = {}


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            student_id = int(
                input("Enter student ID: ")
            )

            name = input("Enter student name: ")

            if name == "":
                raise ValueError(
                    "Student name cannot be empty."
                )

            students[student_id] = name

            print("Student added successfully.")

        elif choice == 2:

            if not students:

                print("No students available.")

            else:

                print("\n===== STUDENTS =====")

                for student_id, name in students.items():

                    print(
                        "ID:",
                        student_id,
                        "| Name:",
                        name
                    )

        elif choice == 3:

            student_id = int(
                input("Enter student ID to search: ")
            )

            if student_id not in students:

                raise KeyError(
                    "Student not found."
                )

            print(
                "Student Name:",
                students[student_id]
            )

        elif choice == 4:

            print("Program closed.")

            break

        else:

            raise ValueError(
                "Invalid menu choice."
            )

    except ValueError as e:

        print("Input Error:", e)

    except KeyError as e:

        print("Search Error:", e)

    except Exception as e:

        print("Unexpected Error:", e)

    finally:

        print("Operation completed.")