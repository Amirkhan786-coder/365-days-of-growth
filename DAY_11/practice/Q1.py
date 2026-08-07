# Q1. Handle ValueError
# Question:
# Take an integer input from the user.
# If the user enters invalid input, handle ValueError.

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter an integer.")