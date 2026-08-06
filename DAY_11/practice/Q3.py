# Question:
# Read the complete content of a file using read().

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()