# Question:
# Write multiple lines to a file using writelines().

file = open("students.txt", "w")

data = [
    "Amir\n",
    "Rahul\n",
    "Aman\n"
]

file.writelines(data)

file.close()

print("Multiple Lines Written Successfully!")