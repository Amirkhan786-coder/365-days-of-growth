# Q13. Marks Validation
# Question:
# Ask the user to enter marks.
# Marks must be between 0 and 100.
# If marks are invalid, raise ValueError.

try:

    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Valid marks:", marks)

except ValueError as e:

    print("Error:", e)