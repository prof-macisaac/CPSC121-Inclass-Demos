from datetime import datetime
from rich import print

class BankAccount:
    def __init__(self, balance=0.0, account_type="Savings"):
        self.__balance = float(balance)
        self.account_type = account_type
        self.__transactions = []
    
    def deposit(self, amount):
        if amount < 0: 
            print("amount must be >= 0")
            return
        self.__balance += amount
        self.__transactions.append((datetime.now().strftime("%B %d, %Y at %I:%M %p"),amount))
    
    def withdraw(self, amount):
        if amount < 0 or amount > self.__balance:
            print("invalid withdrawal")
            return
        self.__balance -= amount
        self.__transactions.append((datetime.now().strftime("%B %d, %Y at %I:%M %p"),-1*amount))
    
    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"BankAccount ({self.account_type})(balance=${self.__balance:,.2f})"

    def get_transactions(self):
        return self.__transactions




def main():
    johns_bank = BankAccount(balance = 200, account_type="Checking")
    johns_bank.__balance = 100000
    print(johns_bank.get_balance())
    johns_bank.deposit(100.00)
    print(johns_bank.get_balance())
    johns_bank.withdraw(250.00)
    print(johns_bank.get_balance())
    johns_bank.withdraw(250.00)
    print(johns_bank.get_balance())
    print(johns_bank)

    # print(johns_bank.get_transactions())

    # sams_bank = BankAccount(balance = 400, account_type="Checking")
    # print(sams_bank.get_balance())
    # print(johns_bank.get_balance())
    # # print(johns_bank)


main()