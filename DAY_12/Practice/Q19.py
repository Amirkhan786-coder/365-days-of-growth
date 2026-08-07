# Q19. File Reader
# Question:
# Open and read a text file.
# Handle FileNotFoundError and PermissionError.
# Use the with statement.

try:

    with open("student.txt", "r") as file:

        data = file.read()

        print(data)

except FileNotFoundError:

    print("File not found.")

except PermissionError:

    print("Permission denied.")