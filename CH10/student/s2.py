
class Student:
    def __init__(self, student_name, current_credits):
        print("I am in init!")
        self.name = student_name
        self.credits = current_credits

    def add_credits(self, amount):
        if amount > 0:
            self.credits += amount

    def can_graduate(self):
        return self.credits >= 180

s1 = Student("Ava", 90)
s2 = Student("Ben", 150)
print(s1.name, s1.credits)
print(s2.name, s2.credits)
# s1.credits += 100
s1.add_credits(100)
print(s1.credits)

print(s1.can_graduate())
print(Student.can_graduate(s1))
