"""
accessing individual characters in the string
"""

name = "Dominic"
print(name[3])

"""
looping
"""
for letter in name:
    print(type(letter))
    print(repr(letter))

"""
Length of a string
"""
print(len(name))

"""
Membership
"""
part = "zaga"
full = "gonz.aga"

if part in full:
    print(f"{part} is in {full}")
else:
    print(f"{part} is NOT in {full}")

"""
String methods

IMPORTANT: Strings are immutable. Methods will not change the string, it will merely return a new string that we can then assign to a variable 
"""

response = "YES !!123"
# bad
response.lower()
print(response)
# good
response_lower = response.lower()
print(response_lower)
if response_lower == "yes":
    print("Do something")

response_upper = response_lower.upper()
print(response_upper)

user_input = "   hello\n\n\n"
user_input_stripped = user_input.rstrip()
print(user_input_stripped)

uncensored = "frick ic"
censored = uncensored.replace("ic", "!!!")
print(censored)

animal = "the dog barked"
animal_cat = animal.replace("dog", "cat")
print(animal_cat)

items = "dog, 1, George"
items_list = items.split("1,")
print(items_list)


# .isdigit()/.islower()/.isupper()

response = "10ten"
if response.isdigit():
    val = int(response)
    print(val)

word = "hello"
print(word.islower())

updated_line = "Last Updated: 4/8/2026"
update = updated_line.split(":")
print(update)
update = update[1].strip()
print(update)