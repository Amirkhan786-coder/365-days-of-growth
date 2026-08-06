# Question:
# Read and write using r+ mode.

file = open("students.txt", "r+")

print(file.read())

file.write("\nPython Developer")

file.close()