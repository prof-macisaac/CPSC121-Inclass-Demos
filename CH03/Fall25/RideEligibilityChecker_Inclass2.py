"""
Description: This program asks for a person's age and height and determines if they can ride

The ride has the following qualifications:
- Must be at least 12 years old or taller than 54 inches
- IF under 5 years old, they can't ride at all, regardless of height
"""
MIN_AGE = 5
QUALIFIED_MIN_AGE = 12
QUALIFIED_MIN_HEIGHT = 54

age = int(input("How old are you? "))
height = int(input("How tall are you (inches)? "))

if age < MIN_AGE:
    qualified = False
else:
    
    if age >= QUALIFIED_MIN_AGE:
        qualified = True
    else:
       
        if height > QUALIFIED_MIN_HEIGHT:
            qualified = True
        else:
            qualified = False

if qualified:
    print("You can ride!")
else:
    print("You cannot ride! :(")