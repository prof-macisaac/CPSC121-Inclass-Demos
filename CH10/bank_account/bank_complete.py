class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        # make "private"
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
    
    

    def __str__(self):
        # tells Python how to turn an object into a readable string.
        return f"{self.owner}: ${self.__balance}"


def transfer(from_account, to_account, amount):
    if from_account.get_balance() >= amount:
        from_account.withdraw(amount)
        to_account.deposit(amount)


a = BankAccount("Ava", 40)
a.deposit(10)
a.withdraw(15)

# print(a.balance)

print(a)

# without private
a.owner = "John"

# with private
# print(a.__balance)
print(a.get_balance())
print(a.__dict__)

# TASK: Make owner "private" and create getter and setter methods for it. 

b = BankAccount("tom", 100)
print(a.get_balance())
print(b.get_balance())
transfer(b, a, 20)
print(a.get_balance())
print(b.get_balance())