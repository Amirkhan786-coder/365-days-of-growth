# ============================================================
# Q5. DICTIONARY KEY HANDLING
# Ask the user for a dictionary key.
# Handle KeyError.
# ============================================================

student = {
    "name": "Aman",
    "age": 20,
    "course": "CSE"
}

try:
    key = input("Enter student key: ")
    print("Value:", student[key])

except KeyError:
    print("Key does not exist.")