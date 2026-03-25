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
- other lists!!
"""
list_x = [1,2,3,"hello", "goodbye", True, None, 101.11, 33.11]

# --- Mini Task ---
# Create a list called favorite_foods with 3 foods in it.

favorite_foods = ["Burger", "Sushi", "French Fries"]

print(list_x)
# Print the whole list.
print(favorite_foods)

"""
=========== Indexing ===========
Each element has a position called an INDEX.

Index starts at 0.

[10, 20, 30, 40]
  0   1   2   3
"""
print(list_x[3])

x = list_x[1]
x += 5
print(x)
print(list_x[1])


# --- Mini Task ---
# Print out your second favorite food from the foods list
print(favorite_foods[1])

"""
=========== len() Function ===========
len(list) returns the number of elements
"""
len_list = len(list_x)
print(f"len: {len_list}")


# --- Mini Task ---
# Print the length of your favorite_foods list.
print(len(favorite_foods))
# Then print the last item of your favorite_foods list using the len() function
len_fav_foods = len(favorite_foods)
print(favorite_foods[len_fav_foods-1])


"""
=========== Lists are MUTABLE ===========
This means we can change elements.
"""

list_x[0] = "hi"
print(list_x)


# --- Mini Task ---
# Change one value in your favorite_foods list.
favorite_foods[2] = "Pizza"
# Then print the updated list.
print(favorite_foods)

"""
=========== List Methods ===========
Methods are actions attached to an object.

Format:
list_name.method()
"""

list_x.append(5)
list_x.append("gonzaga")
print(list_x)

list_y = ["cat", "dog", "frog", "cat"]

# list_y.remove("")
z = list_y.pop(3)
print(z)

print(list_y)

# insert
list_y.insert(1, "fish")
print(list_y)

# methods that reorder the list
nums = [6,3,6,8,4,2,9]
nums.sort()
print(nums)

nums.reverse()
print(nums)

# --- Mini Task ---
# Edit your favorite_foods list
# 1) append one item
favorite_foods.append("French Fries")
# 2) remove one item
favorite_foods.remove("Burger")
# 3) print the final list
print(favorite_foods)


"""
=========== Iterating Through Lists ===========
We can loop through lists.

Style 1:
for item in list:

Style 2:
use an index variable
"""

# For Each loop
for animal in list_y:
    print(animal)

for i in range(len(list_y)):
    print(i)
    print(list_y[i])
    if list_y[i] == "cat":
        list_y[i] = "kitten"

print(list_y)

# --- Mini Task ---
# use a for loop with indexing to print your favorite foods
# Write a loop that prints: (Note that the items are numbered)
# 1. <Food 1>
# 2. <Food 2>
# 3. <Food 3> 
# etc.
for i in range(len(favorite_foods)):
    print(f"{i + 1}. {favorite_foods[i]}")

"""
=========== Built-in Functions ===========
These work with numeric lists.
"""

# sum

print(sum(nums))
print(max(nums))
print(min(nums))


# --- Mini Task ---
# Make a list of 4 test scores.
# Print the sum, min, max, and average.

scores = [99, 85, 74, 88]

print(f"sum: {sum(scores)}")
print(f"low score: {min(scores)}")
print(f"top score: {max(scores)}")
print(f"avg: {sum(scores)/len(scores)}")
"""
=========== Membership (in operator) ===========
Check if an item exists in a list
"""
if "fish" in list_y:
    print("theres a fish!")

print("kitte" in list_y)

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
x = 5
y = x

x = 4
print(x,y)

list_a = [1,2,3]
list_b = list_a

list_b[0] = 100

print(list_a)
print(list_b)

list_c = []
for item in list_a:
    list_c.append(item)

list_c[0] = 200
print(list_a)
print(list_b)
print(list_c)



list_1 = [1,2,3]
list_2 = list_1
list_1 = []
print("1",list_1)
print("2", list_2)

# --- Mini Task ---
# Create a list called nums1 with 3 numbers.
# Make nums2 = nums1
# Change one value in nums2
# Print both lists and see what happens.

list_c = list_a + list_b
print(list_c)
list_c = list_a + []
st = "Last updated: 11/21/2025"
parts = st.split(":")
print(parts)
print(parts[1])
