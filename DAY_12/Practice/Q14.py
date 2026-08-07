# Q14. List Index Validator
# Question:
# Create a list.
# Ask the user for an index.
# Handle invalid integer input and invalid index.

numbers = [10, 20, 30, 40, 50]

try:

    index = int(input("Enter index: "))

    print("Value:", numbers[index])

except ValueError:

    print("Please enter a valid integer.")

except IndexError:

    print("Index is out of range.")