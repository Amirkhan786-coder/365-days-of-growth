# ============================================================
# Q16. SAFE DICTIONARY ACCESS
# Ask for a student key and handle KeyError.
# ============================================================

student = {
    "name": "Aman",
    "age": 20,
    "branch": "CSE"
}

try:
    key = input("Enter key: ")
    print("Value:", student[key])

except KeyError:
    print("Key not found.")