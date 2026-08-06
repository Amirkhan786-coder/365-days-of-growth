# Question:
# Write student details into a CSV file.

import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Amir", 20, "Meerut"])
    writer.writerow(["Rahul", 21, "Delhi"])

print("CSV File Created Successfully!")