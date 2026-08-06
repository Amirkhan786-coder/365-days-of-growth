# Question:
# Create a backup copy of a text file.

with open("data.txt", "r") as source:

    content = source.read()

with open("backup.txt", "w") as backup:

    backup.write(content)

print("Backup Created Successfully!")
