# ============================================================
# Q17. FILE READING
# Read a file and handle file-related exceptions.
# ============================================================

try:
    with open("student.txt", "r") as file:
        content = file.read()

    print("File Content:")
    print(content)

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("Permission denied.")