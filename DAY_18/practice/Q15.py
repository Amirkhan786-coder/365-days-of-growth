# ============================================================
# Q15. SAFE LIST ACCESS
# Take an index and safely access a list.
# ============================================================

numbers = [100, 200, 300, 400]

try:
    index = int(input("Enter index: "))
    print("Selected value:", numbers[index])

except ValueError:
    print("Please enter an integer.")

except IndexError:
    print("Index is outside the list.")