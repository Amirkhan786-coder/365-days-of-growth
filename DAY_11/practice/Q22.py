# Question:
# Display only student names from a CSV file.

import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)  # Skip Header

    for row in reader:
        print(row[0])