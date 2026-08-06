# Question:
# Read the content of a file using the with statement.

with open("students.txt", "r") as file:

    print(file.read())