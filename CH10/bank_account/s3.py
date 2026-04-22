class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            return
        if self.__balance >= amount:
            self.__balance -= amount

    def get_balance(self):
        # getter/accessor
        return self.__balance

    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner):
        # setter/mutator
        self.__owner = new_owner

    def __str__(self):
        return f"{self.__owner}'s bank account has ${self.__balance}"

def transfer(from_account, to_account, amount):
    if amount > 0 and from_account.get_balance() >= amount:
        from_account.withdraw(amount)
        to_account.deposit(amount)

b1 = BankAccount("Fred", 25)
b2 = BankAccount("Scooby", 500)
transfer(b2, b1, 50)
print(b1)
print(b2)

# b1.balance = 10000000000
print(b1.get_balance())
# print(b1.__owner)
print(b1)