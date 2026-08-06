# Question:
# Append data using a+ mode and then display the file content.

file = open("demo.txt", "a+")

file.write("\nMachine Learning")

file.seek(0)

print(file.read())

file.close()