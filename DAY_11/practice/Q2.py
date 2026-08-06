# Question:
# Write three lines into a text file.

file = open("data.txt", "w")

file.write("Python\n")
file.write("AI\n")
file.write("Machine Learning")

file.close()

print("File Created Successfully!")