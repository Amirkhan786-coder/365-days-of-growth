# MENU DRIVEN PROGRAM

while True:

    print("\n===== MENU =====")
    print("1. Even Numbers")
    print("2. Odd Numbers")
    print("3. Multiplication Table")
    print("4. Factorial")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(2, 101, 2):
            print(i)

    elif choice == 2:
        for i in range(1, 100, 2):
            print(i)

    elif choice == 3:
        num = int(input("Enter number: "))
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    elif choice == 4:
        num = int(input("Enter number: "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print("Factorial =", fact)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")