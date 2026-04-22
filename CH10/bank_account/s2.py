class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            return
        if self.__balance > amount:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner):
        self.__owner = new_owner

    def __str__(self):
        # tells Python how to turn an object into a readable string
        s = f"{self.__owner}'s bank account has ${self.__balance}"

        return s

def transfer(from_account, to_account, amount):
    if from_account.get_balance() >= amount:
        from_account.withdraw(amount)
        to_account.deposit(amount)


b1 = BankAccount("Ava", 40)
b2 = BankAccount("Scooby", 250)

transfer(b2, b1, 100)
print(b1)
print(b2)

b1.deposit(10)
print(b1.get_balance())
b1.withdraw(100)
print(b1.get_balance())

print(b1.get_owner())
b1.set_owner("Tom")
print(b1.get_owner())
# b1.__balance = 10000000000

print(b1)
        