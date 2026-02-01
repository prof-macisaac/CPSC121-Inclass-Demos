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
slices = int(input("How many slices are you eating today? "))
# Input Validation

# if slices < 0:
#     print("That is not a reasonable amount of slices.")
#     exit()
# if slices > 25:
#     print("That is not a reasonable amount of slices.")
#     exit()

if slices < 0 or slices > 25: 
    print("That is not a reasonable amount of slices.")
    exit()

# More Pizza?
slices = slices + int(input("How many more slices do you want? "))

# Still hungry?
still_hungry = input("Are you still hungry (yes/no)? ") == "yes"
still_hungry = True
still_hungry  = False
# Pizza Level

pizza_level = ""

if slices == 0:
    pizza_level = "pizza pacifist"
elif slices < 3:
    pizza_level = "light snacker"
elif slices < 6:
    pizza_level = "pizza enjoyer"
else: 
    pizza_level = "pizza monster"

# Pizza print outs
print(f"You are a {pizza_level}")


print("and your pizza mantra is...\n")
# lots of slices and still hungry: Pizza fears you
if slices > 5 and still_hungry:
    print("Pizza Fears Me!")
# hungry and no slices: No Peace No Pizza
elif still_hungry and slices == 0:
    print("No Peace No Pizza!")
# not hungry: A pizza level never eats too much. Nor eats too little. They eat precisely how much they mean to.
elif not still_hungry:
    print(f"A {pizza_level} never eats too much. Nor eats too little. They eat precisely how much they mean to.")
# else: need more za
else:
    print("Need more pizza!")