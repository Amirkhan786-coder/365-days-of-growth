# Question:
# Count the total number of characters in a file.

with open("students.txt", "r") as file:

    data = file.read()

    print("Total Characters:", len(data))