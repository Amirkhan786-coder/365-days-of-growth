# Q26. Login System
# Question:
# Create a simple login system.
# Ask for username and password.
# Handle empty input and invalid login.

correct_username = "amir"
correct_password = "1234"

try:

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "" or password == "":
        raise ValueError(
            "Username and password cannot be empty."
        )

    if username == correct_username and password == correct_password:

        print("Login successful.")

    else:

        print("Invalid username or password.")

except ValueError as e:

    print("Error:", e)