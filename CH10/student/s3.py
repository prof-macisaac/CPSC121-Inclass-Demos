

class Student:
    def __init__(self, student_name, current_credits):
        print("I am in init!")
        self.name = student_name
        self.credits = current_credits

    def can_graduate(self):
        return self.credits >= 180
    
    def add_credits(self, amount):
        if amount > 0:
            self.credits += amount

s1 = Student("Ava", 90)
s1.add_credits(25)
s1.credits += 10
print(s1.name, s1.credits)
s2 = Student("Ben", 210)
print(s2.name, s2.credits)

print(s1.can_graduate())
print(Student.can_graduate(s1))
print(s2.can_graduate())