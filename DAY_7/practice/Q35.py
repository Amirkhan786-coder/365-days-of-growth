# Q35 - Menu Driven Set Operations

A = {10, 20, 30, 40}

B = {30, 40, 50, 60}

while True:

    print("\n------ MENU ------")

    print("1. Union")

    print("2. Intersection")

    print("3. Difference")

    print("4. Symmetric Difference")

    print("5. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:

        print("Union :", A.union(B))

    elif choice == 2:

        print("Intersection :", A.intersection(B))

    elif choice == 3:

        print("Difference :", A.difference(B))

    elif choice == 4:

        print("Symmetric Difference :", A.symmetric_difference(B))

    elif choice == 5:

        print("Program Ended")

        break

    else:

        print("Invalid Choice")