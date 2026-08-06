# Question:
# Count the total number of words in a file.

with open("students.txt", "r") as file:

    data = file.read()

    words = data.split()

    print("Total Words:", len(words))