# Program: Discount Calculator

amount = float(input("Enter Amount: "))
discount = float(input("Enter Discount Percentage: "))

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print(f"Discount = {discount_amount}")
print(f"Final Amount = {final_amount}")