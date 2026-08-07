# Q21. Custom Balance Exception
# Question:
# Create a custom InsufficientBalanceError exception.
# If the withdrawal amount is greater than the balance,
# raise the custom exception.

class InsufficientBalanceError(Exception):
    pass


balance = 5000

try:

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")

    balance -= amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except ValueError as e:

    print("Error:", e)

except InsufficientBalanceError as e:

    print("Error:", e)