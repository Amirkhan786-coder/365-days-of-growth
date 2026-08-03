# ==========================================
# Mini Project: Bank Account Management System
# ==========================================

accounts = {}

while True:
    print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Search Account")
    print("5. Display All Accounts")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            print("Account already exists!")
        else:
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))

            accounts[acc_no] = {
                "Name": name,
                "Balance": balance
            }

            print("Account Created Successfully.")

    elif choice == "2":
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            amount = float(input("Enter Deposit Amount: "))
            accounts[acc_no]["Balance"] += amount
            print("Amount Deposited Successfully.")
        else:
            print("Account Not Found.")

    elif choice == "3":
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            amount = float(input("Enter Withdraw Amount: "))

            if amount <= accounts[acc_no]["Balance"]:
                accounts[acc_no]["Balance"] -= amount
                print("Withdrawal Successful.")
            else:
                print("Insufficient Balance.")
        else:
            print("Account Not Found.")

    elif choice == "4":
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            print("\nAccount Details")
            print("-------------------------")
            print("Account Number :", acc_no)
            print("Name           :", accounts[acc_no]["Name"])
            print("Balance        :", accounts[acc_no]["Balance"])
        else:
            print("Account Not Found.")

    elif choice == "5":
        if len(accounts) == 0:
            print("No Accounts Available.")
        else:
            print("\n===== ACCOUNT LIST =====")

            for acc_no, details in accounts.items():
                print("----------------------------")
                print("Account Number :", acc_no)
                print("Name           :", details["Name"])
                print("Balance        :", details["Balance"])

    elif choice == "6":
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            del accounts[acc_no]
            print("Account Deleted Successfully.")
        else:
            print("Account Not Found.")

    elif choice == "7":
        print("Thank You for Using the System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")