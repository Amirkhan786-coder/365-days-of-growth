# ============================================================
# Q26. NUMBER GUESSING VALIDATION
# Handle invalid user input.
# ============================================================

secret_number = 25

try:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct guess!")

    else:
        print("Wrong guess.")

except ValueError:
    print("Please enter a valid integer.")