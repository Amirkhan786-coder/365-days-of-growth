# Question:
# Replace a word in a file.

with open("data.txt", "r") as file:

    content = file.read()

content = content.replace("Python", "Java")

with open("data.txt", "w") as file:

    file.write(content)

print("Word Replaced Successfully!")