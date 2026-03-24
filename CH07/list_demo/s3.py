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
- other lists
"""
list_x = [1,2,3, "hello", "goodbye", 101.12, 82.7, True, False, None]
empty_list = []
animals = ["cat", "dog", "frog", "cat"]

print(list_x)
print(empty_list)
print(animals)
# --- Mini Task ---
# Create a list called favorite_foods with 3 foods in it.
# Print the whole list.

fav_foods = ["Pizza", "Sushi", "Milkshake"]
print(fav_foods)

"""
=========== Indexing ===========
Each element has a position called an INDEX.

Index starts at 0.

[10, 20, 30, 40]
  0   1   2   3
"""
print(animals[3])
x = list_x[0]
x+= 5
print(x)
print(list_x[0])

# --- Mini Task ---
# Print out your second favorite food from the foods list
print(fav_foods[1])

"""
=========== len() Function ===========
len(list) returns the number of elements
"""
print(len(animals))

len_animals = len(animals)

# --- Mini Task ---
# Print the length of your favorite_foods list.
print(f"fav foods len: {len(fav_foods)}")

# Then print the last item of your favorite_foods list using the len() function
print(fav_foods[len(fav_foods)-1])


"""
=========== Lists are MUTABLE ===========
This means we can change elements.
"""
animals[2] = "fish"
print(animals)


# --- Mini Task ---
# Change one value in your favorite_foods list.
fav_foods[0] = "Gnocchi"
# Then print the updated list.
print(fav_foods)

"""
=========== List Methods ===========
Methods are actions attached to an object.

Format:
list_name.method()
"""

# append
animals.append("Gecko")
print(animals)

# insert at a location
animals.insert(2, "horse")
print(animals)

# remove by element
# animals.remove("cat")
# print(animals)

# remove by index
print(animals.pop(4))
print(animals)

# rearranging the list
# sort
nums = [5,2,5,8,12,1]
nums.sort()
print(nums)

# reverse
nums.reverse()
print(nums)

# --- Mini Task ---
# Edit your favorite_foods list
# 1) append one item
fav_foods.append("Nachos")
# 2) remove one item
fav_foods.pop(1)
# 3) print the final list
print(fav_foods)


"""
=========== Iterating Through Lists ===========
We can loop through lists.

Style 1:
for item in list:

Style 2:
use an index variable
"""
counter = 0
for animal in animals:
    print(animal)

for i in range(len(animals)):
    print(f"{i} {animals[i]}")
    if animals[i] == "cat":
        animals[i] = "kitten"
print(animals)
# --- Mini Task ---
# use a for loop with indexing to print your favorite foods
# Write a loop that prints: (Note that the items are numbered)
# 1. <Food 1>
# 2. <Food 2>
# 3. <Food 3> 
# etc.
for i in range(len(fav_foods)):
    print(f"{i+1}. {fav_foods[i]}")

"""
=========== Built-in Functions ===========
These work with numeric lists.
"""
print(sum(nums))
print(max(nums))
print(min(nums))

# --- Mini Task ---
# Make a list of at least 4 test scores.
# Print the sum, min, max, range(max-min), and average.
scores = [85, 89, 74, 97]
print(f"sum: {sum(scores)}")

min_score = min(scores)
max_score = max(scores)

print(f"top score: {max_score}")

print(f"low score: {min_score}")

print(f"score range: {max_score-min_score}")

print(f"avg score: {sum(scores)/len(scores)}")

"""
=========== Membership (in operator) ===========
Check if an item exists in a list
"""

# --- Mini Task ---
# Take some user input that asks what the user's favorite food is.
# Then print out whether you like that food as well or if you don't using membership with you favorite_foods list


"""
=========== Copying a List ===========
Be careful:
If you do this:
list2 = list1

Both variables refer to the SAME list.
"""


# --- Mini Task ---
# Create a list called nums1 with 3 numbers.
# Make nums2 = nums1
# Change one value in nums2
# Print both lists and see what happens.
