# Question:
# Append a new line to an existing file.

file = open("data.txt", "a")

file.write("\nData Science")

file.close()

print("Data Appended Successfully!")