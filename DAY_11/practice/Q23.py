# Question:
# Copy data from one file to another file.

with open("source.txt", "r") as source:

    data = source.read()

with open("destination.txt", "w") as destination:

    destination.write(data)

print("File Copied Successfully!")