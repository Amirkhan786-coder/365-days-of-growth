# Q5. Handle KeyError
# Question:
# Create a dictionary and try to access
# a key that does not exist.

student = {
    "name": "Amir",
    "age": 20,
    "course": "CSE"
}

try:
    print(student["city"])

except KeyError:
    print("Key does not exist.")