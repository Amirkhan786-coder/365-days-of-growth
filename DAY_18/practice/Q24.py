# ============================================================
# Q24. ATM WITHDRAWAL
# Raise an exception if withdrawal exceeds balance.
# ============================================================

class InsufficientBalanceError(Exception):
    pass


try:
    balance = float(input("Enter account balance: "))
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
    print("Transaction Error:", e)