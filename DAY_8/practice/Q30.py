# Question:
# Print each key and value in a formatted way.

student = {
    "Name": "Amir",
    "Age": 19,
    "City": "Meerut"
}

for key, value in student.items():
    print(f"{key} : {value}")