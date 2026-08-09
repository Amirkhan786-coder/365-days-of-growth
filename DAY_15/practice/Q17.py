# Q17. Demonstrate encapsulation using a private-style attribute.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(10000)
account.show_balance()