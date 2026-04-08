
"""
Accessing individual characters in a string
"""

name = "Dominic"
# print first letter of name
# print(name[3])

"""
looping
"""

# for letter in name:
#     print(letter)

"""
Length of a String
"""

letters_in_name = len(name)
print(letters_in_name)

"""
Concatenation
"""
last_name = "MacIsaac"

full_name = name+ " " +last_name
# print(full_name)
# # full_name = name + " " + last_name
# print(full_name)

"""
Membership
"""

part = "zaga"
full_name = "gonz.aga"

if part in full_name:
    print(f"{part} is in {full_name}")

"""
String methods
- Important! Strings are immutable. Methods will not change the string, it will merely return a new string that we must assign to a variable
"""

# .strip()

# .lower()/.upper()

# .split()

# .replace()

# .isdigit()/.islower()/.isupper()


response = "Yes"
response_updated = response.lower()
if response_updated == "yes":
    print("they said yes!")
print(response_updated)
print(response)

if response.isdigit():
    val = int(response)
    print(val)
else:
    print("That input is not an integer")

# test = "aacaaacaaaa"
# no_a = test.strip("a")
# print(test)
# print(no_a)

# uncensored = "fiirick"
# censored = uncensored.replace("fiir", "")
# print(censored)
# # animal = "the dog barked"
# animal_cat = animal.replace("dog", "cat")
# print(animal_cat)

















def count_capitals(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count+= 1
    return count

def main():
    sentence = input("Enter a sentence: ")
    print(count_capitals(sentence))

main()