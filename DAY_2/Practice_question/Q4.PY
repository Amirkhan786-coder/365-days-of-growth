# Program: Largest of Three Numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print(f"{a} is the Largest Number.")
elif b >= a and b >= c:
    print(f"{b} is the Largest Number.")
else:
    print(f"{c} is the Largest Number.")