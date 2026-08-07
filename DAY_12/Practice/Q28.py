# Q28. Student Marks System
# Question:
# Take marks for multiple subjects.
# Validate that marks are between 0 and 100.
# Calculate total and average.
# Handle invalid input.

try:

    math = float(input("Enter Math marks: "))
    python = float(input("Enter Python marks: "))
    english = float(input("Enter English marks: "))

    marks = [math, python, english]

    for mark in marks:

        if mark < 0 or mark > 100:

            raise ValueError(
                "Marks must be between 0 and 100."
            )

    total = sum(marks)

    average = total / len(marks)

    print("Total:", total)
    print("Average:", average)

except ValueError as e:

    print("Error:", e)