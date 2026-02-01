"""
Description: This program asks for a person's age and height and determines if they can ride

The ride has the following qualifications:
- Must be at least 12 years old or taller than 54 inches
- If under 5 years old, they can't ride at all, regardless of height
"""

AGE_MIN = 5
HEIGHT_QUALIFIED_MIN = 54
AGE_QUALIFIED_MIN = 12


age = int(input("How old are you?: "))
height = int(input("How tall are you?: "))


# option 1, with nested ifs
qualified = False

if age < AGE_MIN:
    qualified = False
else:
    if height > HEIGHT_QUALIFIED_MIN:
        qualified = True
    else:
        if age >= AGE_QUALIFIED_MIN:
            qualified = True
        else:
            qualified = False

# option 2, with OR operator

qualified = False

if age < AGE_MIN:
    qualified = False
else:
    if height > HEIGHT_QUALIFIED_MIN or age >= AGE_QUALIFIED_MIN:
        qualified = True

# Option 3, as a single line
qualified = True if ((age >= AGE_MIN) and (height > HEIGHT_QUALIFIED_MIN) or (age >= AGE_QUALIFIED_MIN)) else False

if qualified:
    print("You qualify, Enjoy the ride!")
else:
    print("Sadly, you are not qualified to ride")




