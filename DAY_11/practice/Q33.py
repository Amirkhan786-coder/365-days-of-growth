# Question:
# Search for a specific word in a file.

word = input("Enter Word to Search: ")

with open("data.txt", "r") as file:

    content = file.read().lower()

    if word.lower() in content:

        print("Word Found!")

    else:

        print("Word Not Found!")