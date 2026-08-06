# Question:
# Move the file pointer to the beginning using seek().

file = open("data.txt", "r")

file.read(10)

file.seek(0)

print(file.read())

file.close()