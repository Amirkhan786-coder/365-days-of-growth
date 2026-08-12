# ============================================================
# Q29. USER REGISTRATION VALIDATOR
# Validate username, age, email and password.
# ============================================================

try:
    username = input("Enter username: ")

    if len(username) < 3:
        raise ValueError(
            "Username must contain at least 3 characters."
        )

    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError(
            "User must be at least 18 years old."
        )

    email = input("Enter email: ")

    if "@" not in email:
        raise ValueError("Invalid email address.")

    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters."
        )

    print("\nRegistration successful!")
    print("Username:", username)
    print("Age:", age)
    print("Email:", email)

except ValueError as e:
    print("Registration Error:", e)