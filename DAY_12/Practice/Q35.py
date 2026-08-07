# Q35. Complete Exception Handling Challenge
# Question:
# Create a program that demonstrates:
# 1. try
# 2. except
# 3. else
# 4. finally
# 5. raise
# 6. Custom Exception
#
# The program should take a student's age and marks.
#
# Rules:
# - Age must be between 5 and 100.
# - Marks must be between 0 and 100.
# - Invalid values should raise exceptions.
# - Display the student information if everything is valid.

class InvalidAgeError(Exception):
    pass


class InvalidMarksError(Exception):
    pass


try:

    name = input("Enter student name: ")

    if name == "":
        raise ValueError(
            "Student name cannot be empty."
        )

    age = int(
        input("Enter student age: ")
    )

    if age < 5 or age > 100:

        raise InvalidAgeError(
            "Age must be between 5 and 100."
        )

    marks = float(
        input("Enter student marks: ")
    )

    if marks < 0 or marks > 100:

        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )

except ValueError as e:

    print("Value Error:", e)

except InvalidAgeError as e:

    print("Age Error:", e)

except InvalidMarksError as e:

    print("Marks Error:", e)

else:

    print("\n===== STUDENT DETAILS =====")

    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)

    if marks >= 40:

        print("Result: PASS")

    else:

        print("Result: FAIL")

finally:

    print("\nStudent validation completed.")