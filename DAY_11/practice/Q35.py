# Question:
# Create a simple file management menu with Read, Write, and Append options.

while True:

    print("\n===== FILE MANAGER =====")
    print("1. Write File")
    print("2. Read File")
    print("3. Append File")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        text = input("Enter Text: ")

        with open("notes.txt", "w") as file:

            file.write(text)

        print("Data Written Successfully!")

    elif choice == "2":

        try:

            with open("notes.txt", "r") as file:

                print("\nFile Content:")
                print(file.read())

        except FileNotFoundError:

            print("File Not Found!")

    elif choice == "3":

        text = input("Enter Text to Append: ")

        with open("notes.txt", "a") as file:

            file.write("\n" + text)

        print("Data Appended Successfully!")

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")