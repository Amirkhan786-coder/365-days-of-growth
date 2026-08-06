# Question:
# Count the number of uppercase letters in a file.

with open("data.txt", "r") as file:

    content = file.read()

    count = 0

    for char in content:

        if char.isupper():
            count += 1

    print("Uppercase Letters:", count)