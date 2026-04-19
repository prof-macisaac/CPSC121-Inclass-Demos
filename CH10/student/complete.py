class Student:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    def add_credits(self, amount):
        self.credits += amount

    def can_graduate(self):
        return self.credits >= 180
    
s1 = Student("Ava", 90)
s2 = Student("Ben", 150)

# two ways to call the method
# long way
Student.add_credits(s1, 15)

# better way
s1.add_credits(15)

print(s1.name, s1.credits, s1.can_graduate())
print(s2.name, s2.credits, s2.can_graduate())