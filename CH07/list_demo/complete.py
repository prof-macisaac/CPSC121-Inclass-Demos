"""
CH07 Demo: Lists
1) What is a list?
2) Indexing
3) Mutability (changing values)
4) List methods
5) Iterating through lists
6) Useful built-in functions
7) Membership with in
"""

"""
=========== What is a List ===========
A LIST is a sequence that stores multiple values.

Format:
list_name = [item1, item2, item3]

Lists can store:
- numbers
- strings
- mixed data types
"""

numbers = [10, 20, 30, 40]
names = ["Alice", "Bob", "Charlie"]
mixed = ["Dom", 27, 180.5]

print(f"numbers: {numbers}")
print(f"names: {names}")
print(f"mixed: {mixed}")

# --- Mini Task ---
# Create a list called favorite_foods with 3 foods in it.
# Print the whole list.


"""
=========== Indexing ===========
Each element has a position called an INDEX.

Index starts at 0.

[10, 20, 30, 40]
  0   1   2   3
"""

print(f"\nFirst element: {numbers[0]}")
print(f"Second element: {numbers[1]}")
print(f"Last element: {numbers[3]}")

# --- Mini Task ---
# Make a list called colors with at least 4 colors.
# Print the first color and the third color.


"""
=========== len() Function ===========
len(list) returns the number of elements
"""

print(f"\nLength of numbers: {len(numbers)}")

last_index = len(numbers) - 1
print(f"Last element using len: {numbers[last_index]}")

# --- Mini Task ---
# Print the length of your colors list.
# Then print the last item using len(colors) - 1.


"""
=========== Lists are MUTABLE ===========
This means we can change elements.
"""

print(f"\nOriginal list: {numbers}")

numbers[1] = 999

print(f"After modification: {numbers}")

# --- Mini Task ---
# Change one value in your colors list.
# Then print the updated list.


"""
=========== List Methods ===========
Methods are actions attached to an object.

Format:
list_name.method()
"""

animals = ["dog", "cat", "bird"]

print(f"\nAnimals: {animals}")

# append
animals.append("turtle")
print(f"After append: {animals}")

# insert
animals.insert(1, "hamster")
print(f"After insert: {animals}")

# remove
animals.remove("cat")
print(f"After remove: {animals}")

# pop
animals.pop(2)
print(f"After pop: {animals}")

# sort
letters = ["d", "a", "c", "b"]
print(f"\nBefore sort: {letters}")
letters.sort()
print(f"After sort: {letters}")

# reverse
letters.reverse()
print(f"After reverse: {letters}")

# --- Mini Task ---
# Make a list called games with 3 game names.
# 1) append one item
# 2) remove one item
# 3) print the final list


"""
=========== Iterating Through Lists ===========
We can loop through lists.

Style 1:
for item in list

Style 2:
use an index variable
"""

scores = [88, 92, 79, 95, 84]

print(f"\nScores: {scores}")

print("\nLooping directly through the list:")
for score in scores:
    print(f"Score: {score}")

print("\nLooping through the list using indexes:")
for index in range(len(scores)):
    print(f"Index {index} has value {scores[index]}")

# --- Mini Task ---
# Make a list called pets with at least 3 pets/animals.
# Write a loop that prints:
# Index 0 has ...
# Index 1 has ...
# etc.


"""
=========== Built-in Functions ===========
These work with numeric lists.
"""

print(f"\nScores list: {scores}")
print(f"sum: {sum(scores)}")
print(f"min: {min(scores)}")
print(f"max: {max(scores)}")

average = sum(scores) / len(scores)
print(f"average: {average}")

# --- Mini Task ---
# Make a list of 4 test scores.
# Print the sum, min, max, and average.


"""
=========== Membership (in operator) ===========
Check if an item exists in a list
"""

print(f"\nIs 92 in scores? {92 in scores}")
print(f"Is 50 in scores? {50 in scores}")
print(f"Is 84 not in scores? {84 not in scores}")

# --- Mini Task ---
# Check whether one of your pets is in the pets list.
# Then check whether some animal that is NOT in the list is in the list.


"""
=========== Copying a List ===========
Be careful:
If you do this:
list2 = list1

Both variables refer to the SAME list.
"""

list1 = [1, 2, 3]
list2 = list1

print(f"\nBefore change:")
print(f"list1: {list1}")
print(f"list2: {list2}")

list2[0] = 999

print(f"\nAfter changing list2:")
print(f"list1: {list1}")
print(f"list2: {list2}")

print("\nTo actually copy, we can build a new list with a loop.")

original = [5, 10, 15]
copied = []

for item in original:
    copied.append(item)

print(f"original: {original}")
print(f"copied: {copied}")

copied[1] = 777

print(f"\nAfter changing copied:")
print(f"original: {original}")
print(f"copied: {copied}")

# --- Mini Task ---
# Create a list called nums1 with 3 numbers.
# Make nums2 = nums1
# Change one value in nums2
# Print both lists and see what happens.
