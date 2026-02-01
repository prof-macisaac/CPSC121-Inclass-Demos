"""
Topics:
- and operator
- or operator
- not operator

- numeric ranges

- boolean variables

- conditional expressions

- walrus operator

Problem Description: A program that takes information about a person and gives a description of them
"""

age = int(input("How old are you? "))

if age > 130 or age < 0:
    print("That is not your age!")
    exit()

student_yn = input("Are you a student (yes/no)? ")

student = True if student_yn == "yes" else False

age_category = ""

if age < 2:
    age_category = "baby"
elif age < 4:
    age_category = "toddler"
elif age < 10:
    age_category = "child"
elif age < 13:
    age_category = "pre-teen"
elif age < 20:
    age_category = "teenager"
elif age < 36:
    age_category = "young adult"
elif age < 65:
    age_category = "adult"
else:
    age_category = "elderly person"

receives_age_discounts = True

if age > 18 and age < 65:
    if not student:
        receives_age_discounts = False

print(f"You are a {age_category}. ", end="")
if receives_age_discounts:
    print("You receive lots of discounts.",end="")
else:
    print("You don't receive many discounts.",end="")


if age_category == "baby" or age_category == "elderly":
    print("You often require lots of precise medical care",end="")

if (age > 4 and age < 18) or student:
    print("You probably have a backpack with you right now.",end="")
print()