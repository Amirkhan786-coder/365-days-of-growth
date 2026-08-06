# Question:
# Read a file and display only even-numbered lines.

with open("data.txt", "r") as file:

    lines = file.readlines()

    for i in range(len(lines)):

        if (i + 1) % 2 == 0:

            print(lines[i], end="")