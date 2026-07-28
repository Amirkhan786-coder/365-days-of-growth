# Program: Menu Driven Calculator

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Choose an Operation (1-4): "))

if choice == 1:
    print(f"Result = {a + b}")
elif choice == 2:
    print(f"Result = {a - b}")
elif choice == 3:
    print(f"Result = {a * b}")
elif choice == 4:
    if b != 0:
        print(f"Result = {a / b}")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid Choice!")