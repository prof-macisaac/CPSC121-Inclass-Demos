"""
CHAPTER 7 TOPICS
- Sequences
- Lists
- Finding Items in Lists with the 'in' Operator
- List Methods and Useful Built-in Functions
- Copying Lists
- Processing Lists
- Two Dimensional Lists
- Tuples
"""

"""
SEQUENCE: an object that contains multiple items of data, in an order
- Python sequences: lists, tuples

MUTABLE: can be changed after it is created

Tuples = immutable (can't change it's values after creation)
Lists = mutable (can change it's values after creation)
""" 

"""
LISTS: an object that contains multiple data items

ELEMENT: an item in the list
"""
# list stored as variable name 'new_list'
# list contains the int values 1, 2, and 3
new_list = [1,2,3]
# prints out "[1,2,3]"
print(new_list)

# list of strings
names = ["Dominic", "Colin", "Brooke"]
print(names)
# list of different data types
info = ["Chiana", 24, 3.9]
print(info)


"""
INDEXING: a number specifying the position of an element in a list
- enables access to an individual element in a list
- first element in the list is index 0, second element is index 1, n'th element is n-1
    - this is referred to as zero indexed, since the first item is at index 0
- Use brackets and then the index to get that element from the list
- example: new_list[0] gets the first element of new_list

"""

# regular indexing example
even_nums = [2,4,6,8,10]
print(f"even_nums = {even_nums}")
print(f"the first element is {even_nums[0]}")
print(f"the second element is {even_nums[1]}")
print(f"the third element is {even_nums[2]}")


# print(f"even_nums: {even_nums}")
# print(f"even_nums[0]: {even_nums[0]}") # prints 2 (the first element of the list)
# print(f"even_nums[1]: {even_nums[1]}") # prints 4 (the second element of the list)
# print(f"even_nums[2]: {even_nums[2]}") # prints 6 (the third element of the list)
# print(f"even_nums[3]: {even_nums[3]}") # prints 8 (the fourth element of the list)
# print(f"even_nums[4]: {even_nums[4]}") # prints 10 (the fifth element of the list)


"""
len function: returns the length of a sequence such as a list
- how many items are in that list
"""

size = len(even_nums)
print(f"even_nums list has length of {size}") # prints "the three element list has length of 3"


# can use length to get the last value of a list
# the last element is the length minus 1 (since we are zero indexed)
print(f"the last element is {even_nums[len(even_nums)-1]}")


# last_element = even_nums[size-1]
# print(f"the last element in even_nums is {last_element}")



"""
MINI Challenge: 
- What happens if you try to index the list with the size of the list?
- Why?
"""

# # a = even_nums[-6]
# print(f"negative indexing:{a}")


"""
IndexError: exception raised if an invalid index is used (index equal to or greater than the amount of elements)
"""

try:
    one_too_many = even_nums[size]
except IndexError as index_err:
    print(f"Index Error! ")


"""
Mini Challenge: Create a new list called top 3 foods and insert your favorite three foods in order

- Then, use a loop (for loop or while loop) to print out each item of the list 
with the place it came in

Example Output:
My top 3 foods are:
1. Sushi
2. Burger
3. Drumstick (ice cream)

"""
foods = ["Sushi", "Burger", "Drumstick"]
index = 0
while index < len(foods):
    print(f"{index + 1}. {foods[index]}")
    index += 1

"""
Lists are Mutable!

- change the value of elements in a list

ex: list[0] = 5 
- changes the first item in that list to the integer 5

"""

odds = [1,2,5]
print(f"odds before updating the second element: {odds}")

odds[1] = 3
print(f"odds after updating the second element: {odds}")


"""
Concatenating Lists
- Concatenate: join two things together
- use the + operator to concatenate two lists together
- must be two lists, not a list and another data type

example: list_3 = list_1 + list_2

"""

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = list_1 + list_2
print(list_3)
# # Order Matters!
list_4 = list_2 + list_1
list_4 = list_4 + [7]
print(list_4)
"""
Mini Challenge: Create two lists (list_a and list_b) of integers (with the same amount of values in both list)
Then do two tasks:
1. Create a new list concatenating those together and print it out (call it list_c)

2. Loop through the lists, updating each element in list_a by adding to that element the value at the corresponding index in list_b
    - example: 
    if list_a = [1,2] and 
       list_b = [3,4]
    
    list_a, after this loop, should be [4,6]

"""


"""
Useful Methods
"""

# list_a = [3,2,1]
# list_a.append(3)
# print(f"list a after append: {list_a}")

# # we can create an empty list and then append to it
# list_b = []
# list_b.append("a")
# list_b.append("b")
# list_b.append("c")

# three_count = list_a.count(3)
# print(f"there are {three_count} threes in {list_a}")

# three_index = list_a.index(3)
# print(f"the first three is at index {three_index}")

# # lets sort the list
# # by default it sorts in ascending order
# list_a.sort()
# print(f"the list is now sorted {list_a}")


"""
Useful Functions
"""



"""
Finding Items in Lists
"""



"""
Copying Lists
"""


"""
Processing Lists
"""



"""
Repetition Operator
"""





"""
Two Dimensional Lists
"""



"""
Tuples
"""

"""
Extra Topics:
    - Slicing Lists
    - List Comprehension
"""


