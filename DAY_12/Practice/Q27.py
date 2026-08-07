# Q27. ATM Withdrawal
# Question:
# Create an ATM withdrawal program.
# Check balance.
# Reject negative amounts.
# Reject withdrawal greater than balance.
# Use a custom exception for insufficient balance.

class InsufficientBalanceError(Exception):
    pass


balance = 10000

try:

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:

        raise ValueError(
            "Withdrawal amount must be greater than zero."
        )

    if amount > balance:

        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    balance -= amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except ValueError as e:

    print("Error:", e)

except InsufficientBalanceError as e:

    print("Error:", e)