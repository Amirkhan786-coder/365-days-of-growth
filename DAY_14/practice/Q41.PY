# Bank Management System

class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited:", amount)
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)

    def display_account(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


account = BankAccount("Amir", "1234567890", 10000)

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.display_account()

    elif choice == "5":
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid Choice!")