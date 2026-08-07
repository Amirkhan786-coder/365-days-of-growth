# Q8. Use else
# Question:
# Create a program using try, except and else.
# The else block should execute when no exception occurs.

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Valid number:", number)
    print("No exception occurred.")