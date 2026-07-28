# Program: Profit or Loss Calculator

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    print(f"Profit = {sp - cp}")
elif cp > sp:
    print(f"Loss = {cp - sp}")
else:
    print("No Profit No Loss")