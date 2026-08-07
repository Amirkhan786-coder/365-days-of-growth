# Q6. Handle FileNotFoundError
# Question:
# Try to open a file that does not exist.
# Handle FileNotFoundError.

try:
    with open("student.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")