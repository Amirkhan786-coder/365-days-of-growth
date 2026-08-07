# Q12. Age Validation
# Question:
# Ask the user to enter their age.
# Age must be an integer.
# Age cannot be negative.
# If age is 18 or above, display Eligible.
# Otherwise display Not Eligible.

try:

    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age >= 18:
        print("You are Eligible.")

    else:
        print("You are Not Eligible.")

except ValueError as e:

    print("Error:", e)