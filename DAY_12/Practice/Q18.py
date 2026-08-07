# Q18. User Input Loop
# Question:
# Keep asking the user for an integer
# until valid input is entered.

while True:

    try:

        number = int(input("Enter a number: "))

        print("Valid number:", number)

        break

    except ValueError:

        print("Invalid input. Please try again.")