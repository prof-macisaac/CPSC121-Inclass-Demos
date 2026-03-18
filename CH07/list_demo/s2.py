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



# --- Mini Task ---
# Print out your second favorite food from the foods list


"""
=========== len() Function ===========
len(list) returns the number of elements
"""




# --- Mini Task ---
# Print the length of your favorite_foods list.
# Then print the last item of your favorite_foods list using the len() function


"""
=========== Lists are MUTABLE ===========
This means we can change elements.
"""



# --- Mini Task ---
# Change one value in your favorite_foods list.
# Then print the updated list.


"""
=========== List Methods ===========
Methods are actions attached to an object.

Format:
list_name.method()
"""

# --- Mini Task ---
# Edit your favorite_foods list
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


# --- Mini Task ---
# use a for loop with indexing to print your favorite foods
# Write a loop that prints: (Note that the items are numbered)
# 1. <Food 1>
# 2. <Food 2>
# 3. <Food 3> 
# etc.


"""
=========== Built-in Functions ===========
These work with numeric lists.
"""


# --- Mini Task ---
# Make a list of 4 test scores.
# Print the sum, min, max, and average.


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
