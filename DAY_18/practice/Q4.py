# ============================================================
# Q4. LIST INDEX HANDLING
# Access an element from a list using user input.
# Handle IndexError.
# ============================================================

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter list index: "))
    print("Value:", numbers[index])

except ValueError:
    print("Index must be an integer.")

except IndexError:
    print("Index does not exist.")