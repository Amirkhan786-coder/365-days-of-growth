# ============================================================
# Q28. SAFE FILE MANAGER
# Create, read, write, append and delete files.
# ============================================================

import os


def safe_file_manager():

    while True:

        print("\n===== SAFE FILE MANAGER =====")
        print("1. Create File")
        print("2. Read File")
        print("3. Write File")
        print("4. Append File")
        print("5. Delete File")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:

                filename = input("Enter filename: ")

                with open(filename, "x") as file:
                    file.write("")

                print("File created successfully.")

            elif choice == 2:

                filename = input("Enter filename: ")

                with open(filename, "r") as file:
                    print(file.read())

            elif choice == 3:

                filename = input("Enter filename: ")
                data = input("Enter data: ")

                with open(filename, "w") as file:
                    file.write(data)

                print("File written successfully.")

            elif choice == 4:

                filename = input("Enter filename: ")
                data = input("Enter data: ")

                with open(filename, "a") as file:
                    file.write(data)

                print("Data appended successfully.")

            elif choice == 5:

                filename = input("Enter filename: ")

                os.remove(filename)

                print("File deleted successfully.")

            elif choice == 6:

                print("Exiting File Manager.")
                break

            else:

                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")

        except FileNotFoundError:
            print("File not found.")

        except FileExistsError:
            print("File already exists.")

        except PermissionError:
            print("Permission denied.")

        except OSError as e:
            print("File system error:", e)


safe_file_manager()