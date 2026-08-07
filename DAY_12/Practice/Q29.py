# Q29. File Management System
# Question:
# Create a menu-driven file management system.
#
# 1. Read File
# 2. Write File
# 3. Append File
# 4. Exit
#
# Handle invalid input and file-related errors.

while True:

    print("\n===== FILE MANAGEMENT SYSTEM =====")

    print("1. Read File")
    print("2. Write File")
    print("3. Append File")
    print("4. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            try:

                with open("data.txt", "r") as file:

                    print("\nFile Content:")
                    print(file.read())

            except FileNotFoundError:

                print("File not found.")

            except PermissionError:

                print("Permission denied.")

        elif choice == 2:

            data = input("Enter data: ")

            with open("data.txt", "w") as file:

                file.write(data)

            print("Data written successfully.")

        elif choice == 3:

            data = input("Enter data: ")

            with open("data.txt", "a") as file:

                file.write("\n" + data)

            print("Data appended successfully.")

        elif choice == 4:

            print("Program closed.")

            break

        else:

            print("Invalid choice.")

    except ValueError:

        print("Please enter a valid number.")

    except PermissionError:

        print("Permission denied.")

    except OSError as e:

        print("File error:", e)