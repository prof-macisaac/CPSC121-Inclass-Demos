class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # TODO: deposit(self, amount)
    # TODO: withdraw(self, amount)   
        # only if enough money

a = BankAccount("Ava", 40)
a.deposit(10)
a.withdraw(15)

print(a.balance)    # 35
print(a.is_empty()) # False

# TODO: create another Bank Account object that belongs to you
# make a few deposits and a few withdrawals
