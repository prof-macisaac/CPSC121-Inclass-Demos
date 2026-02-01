"""
- and operator
- or operator
- not operator
- numeric ranges
- boolean variables
- conditional expressions

Description: Pizza Pal! It asks you about your pizza eating and gives you a pizza level and pizza mantra

"""

# How much pizza are you eating
slices_eaten = int(input("How much za you eating? "))

# Input Validation
if slices_eaten < 0 or slices_eaten > 30:
    print("that is not a realistic pizza slice count!! >:(")
    exit()


# More Pizza?
slices_eaten = slices_eaten + int(input("How many more slices would you like? "))

# Still hungry?
still_hungry = input("Are you still hungry(yes/no)") == "yes"

# Pizza Level
pizza_level = ""
if slices_eaten == 0:
    pizza_level = "pizza pacifist"
elif slices_eaten < 3:
    pizza_level = "light snacker"
elif slices_eaten < 6:
    pizza_level = "pizza enjoyer"
else:
    pizza_level = "pizza monster"

print(f"You are a {pizza_level}")

# Pizza print outs
print("Your Pizza Slogan Is:....")
# lots of slices and still hungry: Pizza fears you
if slices_eaten > 5 and still_hungry:
    print("Pizza Fears Me")

# hungry and no slices: eat some more slices!
elif still_hungry and slices_eaten == 0:
    print("No Peace No Pizza")

# not hungry: Don't forget to take your leftovers home!
elif not still_hungry:
    print(f"A {pizza_level} never eats too much. Nor eats too little. They eat precisely how much they mean to.")
else:
    print("Need More Za!")
