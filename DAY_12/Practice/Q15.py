# Q15. Dictionary Access
# Question:
# Create a student dictionary.
# Ask the user for a key.
# Handle KeyError if the key does not exist.

student = {
    "name": "Amir",
    "age": 20,
    "course": "CSE"
}

try:

    key = input("Enter key: ")

    print("Value:", student[key])

except KeyError:

    print("Key does not exist.")