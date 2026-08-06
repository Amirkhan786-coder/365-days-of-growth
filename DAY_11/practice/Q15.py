# Question:
# Count the total number of lines in a file.

with open("students.txt", "r") as file:

    lines = file.readlines()

    print("Total Lines:", len(lines))