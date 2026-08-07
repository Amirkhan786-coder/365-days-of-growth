# Q31. Student Result Validation
# Question:
# Create a program that takes marks of 5 subjects.
# Validate every mark.
# Marks must be between 0 and 100.
# Calculate total, average and percentage.
# Handle invalid input using Exception Handling.

try:

    marks = []

    for i in range(1, 6):

        mark = float(input(f"Enter marks for Subject {i}: "))

        if mark < 0 or mark > 100:
            raise ValueError(
                "Marks must be between 0 and 100."
            )

        marks.append(mark)

    total = sum(marks)

    average = total / len(marks)

    percentage = total / 5

    print("\n===== RESULT =====")
    print("Total:", total)
    print("Average:", average)
    print("Percentage:", percentage, "%")

except ValueError as e:

    print("Error:", e)