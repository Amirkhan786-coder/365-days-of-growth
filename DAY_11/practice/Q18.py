# Question:
# Write data using w+ mode and then read it.

file = open("demo.txt", "w+")

file.write("Python File Handling")

file.seek(0)

print(file.read())

file.close()