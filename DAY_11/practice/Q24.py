# Question:
# Count the number of vowels in a file.

with open("data.txt", "r") as file:

    content = file.read().lower()

    vowels = "aeiou"

    count = 0

    for char in content:

        if char in vowels:
            count += 1

    print("Total Vowels:", count)