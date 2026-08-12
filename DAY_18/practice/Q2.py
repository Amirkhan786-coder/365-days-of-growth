# ============================================================
# Q1. SAFE INTEGER INPUT
# Ask the user to enter an integer.
# Handle ValueError if invalid input is entered.
# ============================================================

try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input. Please enter an integer.")