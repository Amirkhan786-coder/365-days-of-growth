# Question:
# Access the name of student 101 from a nested dictionary.

students = {
    101: {
        "Name": "Amir",
        "Age": 19
    },
    102: {
        "Name": "Rahul",
        "Age": 20
    }
}

print(students[101]["Name"])
