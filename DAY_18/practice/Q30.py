# ============================================================
# Q30. LOGIN SYSTEM
# Create a custom AuthenticationError.
# Raise it when credentials are incorrect.
# ============================================================

class AuthenticationError(Exception):
    pass


try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin" or password != "admin123":
        raise AuthenticationError(
            "Invalid username or password."
        )

    print("\nLogin Successful!")
    print("Welcome,", username)

except AuthenticationError as e:
    print("\nLogin Failed!")
    print("Error:", e)