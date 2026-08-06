# Question:
# Handle FileNotFoundError using try-except.

try:

    file = open("student.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File Not Found!")