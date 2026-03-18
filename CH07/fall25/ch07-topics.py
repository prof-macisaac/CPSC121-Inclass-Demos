# # """
# # CHAPTER 7 TOPICS
# # - Sequences
# # - Lists
# # - Finding Items in Lists with the 'in' Operator
# # - List Methods and Useful Built-in Functions
# # - Copying Lists
# # - Processing Lists
# # - Two Dimensional Lists
# # - Tuples
# # """

# # """
# # SEQUENCE: an object that contains multiple items of data, in an order
# # - Python sequences: lists, tuples

# # MUTABLE: can be changed after it is created

# # Tuples = immutable (can't change it's values after creation)
# # Lists = mutable (can change it's values after creation)
# # """ 

# # """
# # LISTS: an object that contains multiple data items

# # ELEMENT: an item in the list
# # """
# # # list stored as variable name 'new_list'
# # # list contains the int values 1, 2, and 3
# # new_list = [1,2,3] 


# # # prints out "[1,2,3]"
# # print(new_list)

# # # list of strings
# # friends = ["Colin", "Brooke", "Chiana", "Avery"]


# # # list of different data types
# # things = [3.14, "John", 100, False, None]



# # """
# # INDEXING: a number specifying the position of an element in a list
# # - enables access to an individual element in a list
# # - first element in the list is index 0, second element is index 1, n'th element is n-1
# #     - this is referred to as zero indexed, since the first item is at index 0
# # - Use brackets and then the index to get that element from the list
# # - example: new_list[0] gets the first element of new_list

# # """

# # # regular indexing example
# # even_nums = [2,4,6,8,10]
# # print(f"even_nums: {even_nums}")
# # print(f"even_nums[0]: {even_nums[0]}") # prints 2 (the first element of the list)
# # print(f"even_nums[1]: {even_nums[1]}") # prints 4 (the second element of the list)
# # print(f"even_nums[2]: {even_nums[2]}") # prints 6 (the third element of the list)
# # print(f"even_nums[3]: {even_nums[3]}") # prints 8 (the fourth element of the list)
# # print(f"even_nums[4]: {even_nums[4]}") # prints 10 (the fifth element of the list)

# # x = 2
# # print(even_nums[x])
# # """
# # len function: returns the length of a sequence such as a list
# # - how many items are in that list
# # """

# # size = len(even_nums)
# # print(f"even_nums list has length of {size}") # prints "the three element list has length of 3"


# # # can use length to get the last value of a list
# # # the last element is the length minus 1 (since we are zero indexed)
# # print(  even_nums[  len(even_nums)  -1   ]   )

# # last_element = even_nums[size-1]
# # print(f"the last element in even_nums is {last_element}")



# # """
# # MINI Challenge: 
# # - What happens if you try to index the list with the size of the list?
# # - Why?
# # """














# # """
# # IndexError: exception raised if an invalid index is used (index equal to or greater than the amount of elements)
# # """

# # try:
# #     one_too_many = even_nums[size]
# # except IndexError as index_err:
# #     print(f"Index Error! ")




# # """
# # Mini Challenge: Create a new list called top 3 foods and insert your favorite three foods in order
# # - Then, use a loop (for loop or while loop) to print out each item of the list with the place it came in

# # Example Output:
# # My top 3 foods are:
# # 1. Sushi
# # 2. Burger
# # 3. Drumstick (ice cream)

# # """

# # """
# # Lists are Mutable!

# # - change the value of elements in a list

# # ex: list[0] = 5 
# # - changes the first item in that list to the integer 5

# # """

# # odds = [1,2,5]
# # print(f"odds before updating the second index: {odds}")
# # odds[1] = 3
# # print(f"odds after updating the second index: {odds}")


# # """
# # Concatenating Lists
# # - Concatenate: join two things together
# # - use the + operator to concatenate two lists together
# # - must be two lists, not a list and another data type

# # example: list_3 = list_1 + list_2

# # """

# # list_1 = [1,2,3]
# # list_2 = [4,5,6]
# # list_3 = list_1 + list_2
# # print(list_3)

# # # Order Matters!
# # list_2 += list_1
# # print(list_2)

# """
# Mini Challenge: Create two lists (list_a and list_b) of integers (with the same amount of values in both list)
# Then do two tasks:
# 1. Create a new list concatenating those together and print it out (call it list_c)
# 2. Loop through the lists, updating each element in list_a by adding to that element the value at the corresponding index in list_b
#     - example: if list_a = [1,2] and list_b = [3,4], list_a, after this loop, should be [4,6]

# """


# """
# Useful Methods

# Adding and Removing Items:
#     - .append(<item>)
#     - .insert(<index>, <item>)
#     - .remove(<item>)
#     - .pop(<index>)

# Analyzing Items:
#     - .count(<item>)
#     - .index(<item>)

# Modifying Order: 
#     - .sort()
#     - .reverse()
# """
# list_a = [3,2,1]
# # list_a.append("dog")
# print(f"list a after : {list_a}")

# # # # we can create an empty list and then append to it
# list_b = [  ]
# list_b.append("a")
# list_b.append("b")
# list_b.append("c")
# list_b.append("b")
# print(list_b)

# # # # lets remove b from list_b

# # list_b.remove("b")
# x = 3
# list_b.pop(3)
# print(list_b)

# list_a.insert(1, 1)
# print(list_a)

# ones_counts = list_a.count(1)
# print(f"there are {ones_counts} ones(s) in {list_a}")

# three_index = list_a.index(1)
# print(f"the first three is at index {three_index}")

# # # # lets sort the list
# # # # by default it sorts in ascending order
# list_a.sort()
# print(f"the list is now sorted {list_a}")

# # # # now that a is sorted, maybe we want to reverse the order
# list_a.reverse()
# print(f"the list is now reversed {list_a}")

# """
# Useful Functions
#     - len(<list>)
# numeric:
#     - sum(<list>)
#     - min(<list>)
#     - max(<list>)
# """
# list_a = [1,2,3,1.5, 1]
# # has to be all numerics (floats/ints) 
# print(sum(list_a))
# print(min(list_a))
# print(max(list_a))

# """
# Finding Items in Lists
# """

# if 1.5 in list_a:
#     print("1.5 is in list_a")

# if 6 not in list_a:
#     print("6 is not in list_a")

# """
# Tuples
# """
# t = (1, 2, 3)
# # single-element tuple (note the trailing comma!)
# one = (42,)
# print(type(t),type(one))
# # # indexing works the same
# print(t[2])        # 1

# # # # tuples can be mixed types
# point = ("x", 10)

# pair = (5, 9)       # packing without parentheses
# a, b = pair        # unpacking
# print(a, b)        # 5 9

# lst = [ "a", "b", "c" ]
# tpl = tuple(lst)
# print(tpl)
# back = list(tpl)
# print(back)


# # # concatenation makes a new tuple
# t2 = (4, 5)
# t3 = t + t2
# print(t3)          # (1, 2, 3, 4, 5)


# course_1 = ("CPSC 121", "Fall 2025", 3)
# course_2 = ("CPSC 346", "Fall 2025", 3)

# print(course_1)

# print(course_1[1])

# list_of_tuples = [
#     course_1,
#     course_2
# ]
# list_of_tuples.append(  ("CPSC 222", "Spring 2026",3)  )
# print(list_of_tuples)
# print()
# print()
# print(list_of_tuples[2][1])






# line = "mochi,cat,12\n"
# line = line.rstrip().split(',')
# print(line)



"""
Activity:
Use the following starter code to implement the following features.

Create a list of students on the roster.

Let the user do the following actions: 
    - check if a student is on the roster
    - add a student to the roster
    - print out the entire roster

"""





"""
Copying Lists

"""
# list_1 = [1,2,3]
# list_2 = list_1 # Reference/Alias

# # both list_1 and list_2 refer to the same list
# list_2[0] = 5
# print(f"list_1: {list_1} | list_2: {list_2}")

# # # # Option 1: concatenation trick
# list_1 = [1,2,3]
# list_2 = list_1 + []
# list_2[0] = 5
# print(f"list_1: {list_1} | list_2: {list_2}")

# # # # Option 2: looping copy

# list_2 = []
# for i in range(len(list_1)):
#     list_2.append(list_1[i])
# list_2[0] = 5
# print(f"list_1: {list_1} | list_2: {list_2}")




# """
# Processing Lists
# - Pass by object reference
# """
# def update_list(l):
#     for i in range(len(l)):
#         l[i] += 1

# def not_updating_list(l):
#     l = ["a", "b", "c"]

# def create_list():
#     list_a = [1,2,3]
#     return list_a

# def main():
#     x = create_list()
#     # y = create_list()
#     print(x)
#     z = [4,5,6]
#     print(z)
#     update_list(z)
#     print(z)
    # update_list(x)
    # print(x)
    # print(y)
    # print(z)
    # not_updating_list(x)
    # print(x)

# main()

# t = [("a",1), ("b",2)]
# x = t + []
# x[0] = ("c", 3)
# print(x)
# print(t)
# def update_scream_meter_with_stats(records):
#     updated = []  # new list — manual, no .copy()

#     for room, screams in records:
#         if room == "Hall of Mirrors":
#             continue  # remove it
#         if room == "Witch's Kitchen":
#             updated.append((room, 85))  # new tuple for the changed entry
#         else:
#             updated.append((room, screams))  # can reuse or rebuild tuple; both fine

#     scores = [s for _, s in updated]
#     avg = sum(scores) / len(scores)
#     mn = min(scores)
#     mx = max(scores)
#     return updated, avg, mn, mx


# scream_meter = [
#     ('Foyer of Fog', 88),
#     ('Hall of Mirrors', 94),
#     ('Basement Chains', 73),
#     ("Witch's Kitchen", 91),
#     ('Attic Shadows', 85),
#     ('Crypt Corridor', 90),
#     ('Spider Den', 42)
# ]


# updated_scream_meter, avg_scream, min_scream, max_scream = update_scream_meter_with_stats(scream_meter)

# print(scream_meter)
# print(updated_scream_meter)
# print(avg_scream)
# print(min_scream)
# print(max_scream)
"""
Repetition Operator
- iterate over a list helper
"""
# list_1 = [4, 8, 3, 12]
# total = 0

# mn = list_1[0]
# for item in list_1:
#     print(item)
#     if item < mn:
#         mn = item
#     total += item

# print(list_1)
# print(f"total is {total}")
# print(f"min is {mn}")

# names = ["remi", "robi"]

# for name in names:
#     print(f"names item: {name}")


# groups = [["Joe", "Kim"],
#           ["Sam", "Sue"],
#           ["Kelly", "Chris"]]

# """
# Two Dimensional Lists
# """
matrix = [ [1,3,5,7],
           [2,4,6,8,10,12,14] ]

for i in range(len(matrix)):
    print(matrix[i])
# print(matrix)
# print(matrix[0])
# print(matrix[1])
# matrix.append([0.5,1.5,2.5])
# print(matrix)

# print(matrix[0][0])
# matrix[0][0] = 9
# print(matrix)
# # list_1 = matrix[0]
# # print(list_1[0])

# print(matrix[1][0])
# print(matrix[2][0])

# # # # looping with indexes
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         matrix[i][j] = 5 + i
#         print(f"matrix[{i}][{j}]: {matrix[i][j]}")
        
# print(matrix)
# # # looping without indexing
# for matrix_list in matrix:
#     print(matrix_list)
#     for item in matrix_list:
#         print(item)

# """
# Activity Time!
# """


"""
Extra Topics:
    - Slicing Lists
    - List Comprehension
"""


file_x = open("pets_in.csv", "a")
line = file_x.write("hello")