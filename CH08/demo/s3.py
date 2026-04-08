"""
Accessing individual characters in a string
"""
name = "Dominic"
print(name[4])

"""
Strings are IMMUTABLE!
They cannot be changed
"""

# name[0] = "B"

"""
Looping
"""

for letter in name:
    print(letter)
    print(repr(letter))
    print(type(letter))


"""
Membership
"""

part = "zaga"
full = "gonz.aga"

print(part in full)

line = "Last Updated: 4/8/2026"
if "Last Updated" in line:
    print("reached the last line")


"""
Concatenation
"""
fn = "Dominic"
ln = "MacIsaac"
fn = fn + " " + ln
print(fn)

"""
String Methods

Because strings are immutable -> methods will not change the string!
It will merely return a new string that we must assign to a variable
"""

# .lower()/.upper()
response = "Yes 123!!$^*&"
response = response.upper()
print(response)

response = "YES"
response_lower = response.lower()
print(response_lower)

if response.strip().lower() == "yes":
    print("do something")

x = "   he \nllo  \n"
print(x)
x_s = x.strip()
print(x_s)
x_r = x.rstrip()
print(x_r)
x_l = x.lstrip()
print(x_l)


# replace()

uncensored = "frick"
censored = uncensored.replace("i", "!!!")
print(censored)

animal = "the dog barked and the dog ran"
animal_cat = animal.replace("dog", "cat")
animal_cat = animal_cat.replace("barked", "meowed")
print(animal_cat)


# split()

items = "dog, 1, George"
item_list = items.split(",")
print(item_list)

last_line = "Last Updated: 4/8/2026"
last_line_list = last_line.split(":")
print(last_line_list)
date = last_line_list[1].strip()
print(date)

# isdigit()/islower()/isupper()
y = "10   "
print(y.isdigit())

z = "HELlO"
print(z.isupper())