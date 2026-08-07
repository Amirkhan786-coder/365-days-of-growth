# Q20. Custom Exception
# Question:
# Create a custom AgeError exception.
# Raise it when the user's age is below 18.

class AgeError(Exception):
    pass


try:

    age = int(input("Enter your age: "))

    if age < 18:

        raise AgeError("Age must be 18 or above.")

    print("You are eligible.")

except ValueError:

    print("Please enter a valid age.")

except AgeError as e:

    print("Age Error:", e)