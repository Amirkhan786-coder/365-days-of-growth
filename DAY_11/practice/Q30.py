# Question:
# Count the frequency of words in a file.

with open("data.txt", "r") as file:

    content = file.read().lower()

    words = content.split()

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print(frequency)