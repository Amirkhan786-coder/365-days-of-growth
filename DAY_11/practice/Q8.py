# Question:
# Display the current file pointer position using tell().

file = open("data.txt", "r")

print(file.tell())

file.read(10)

print(file.tell())

file.close()