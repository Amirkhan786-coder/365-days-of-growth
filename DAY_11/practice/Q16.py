# Question:
# Create a new file using x mode.

try:

    file = open("newfile.txt", "x")

    file.write("Welcome to Python")

    file.close()

    print("File Created Successfully!")

except FileExistsError:

    print("File Already Exists!")