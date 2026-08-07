# Q32. Password Validation
# Question:
# Create a program that asks the user for a password.
# Raise an exception if:
# 1. Password is empty.
# 2. Password length is less than 8 characters.
# Handle the custom exception.

class WeakPasswordError(Exception):
    pass


try:

    password = input("Enter password: ")

    if password == "":
        raise ValueError("Password cannot be empty.")

    if len(password) < 8:
        raise WeakPasswordError(
            "Password must contain at least 8 characters."
        )

    print("Password accepted.")

except ValueError as e:

    print("Error:", e)

except WeakPasswordError as e:

    print("Weak Password:", e)