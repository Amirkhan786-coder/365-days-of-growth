# Q31 - Student Registration System

students = set()

while True:

    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        name = input("Enter Student Name: ")

        students.add(name)

        print("Student Added Successfully!")

    elif choice == 2:

        print("\nRegistered Students:")

        for student in students:
            print(student)

    elif choice == 3:

        print("Thank You!")

        break

    else:

        print("Invalid Choice")