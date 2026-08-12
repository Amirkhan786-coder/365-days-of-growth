# ============================================================
# Q9. FILE NOT FOUND
# Try opening data.txt.
# Handle FileNotFoundError.
# ============================================================

try:
    with open("data.txt", "r") as file:
        content = file.read()

    print("File Content:")
    print(content)

except FileNotFoundError:
    print("File not found.")