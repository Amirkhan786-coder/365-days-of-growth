# Q33. Safe File Copy
# Question:
# Read data from source.txt and copy it into backup.txt.
# Handle:
# FileNotFoundError
# PermissionError
# Other file-related errors.

try:

    with open("source.txt", "r") as source_file:

        data = source_file.read()

    with open("backup.txt", "w") as backup_file:

        backup_file.write(data)

    print("File copied successfully.")

except FileNotFoundError:

    print("Error: source.txt was not found.")

except PermissionError:

    print("Error: Permission denied.")

except OSError as e:

    print("File error:", e)