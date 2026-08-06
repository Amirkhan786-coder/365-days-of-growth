# Question:
# Read all lines of a file using readlines().

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()