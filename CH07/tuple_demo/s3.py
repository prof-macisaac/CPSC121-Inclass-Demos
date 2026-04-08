# part a

list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

list_c = list_a + list_b
print(list_c)

# part b

# list_a[0] = list_a[0] + list_b[0]
print(list_a)
for i in range(len(list_a)):
    list_a[i] = list_a[i] + list_b[i]

print(list_a)

# TUPLES!
# What is a tuple?
# A sequence of items similar to a list
# BUT! tuples are immutable

# format: tuple_name = (item1, item2, item3, ...)

dog_1 = ("Spike", 36, "Bulldog")
dog_2 = "Mac", 8, "Burmese Mountain Dog"

print(dog_1)
print(dog_2)

nums = (1,2,3,4,5)

# Indexing
print(dog_1[0])
print(dog_2[2])

# Functions!
print(len(nums))
print(len(dog_1))

print(sum(nums))

# Iterate

for item in dog_2:
    print(item)

# Membership

if "Mac" in dog_2:
    print("Good boy")
else:
    print("Come Home")

# Tuples are immutable
# nums.remove(1)
# dog_2[0] = "Hop"


# Workaround
dog_2 = ("Hop", dog_2[1], dog_2[2])
print(dog_2)

# Convert Lists and Tuples
nums = list(nums)
nums.append(7)

nums = tuple(nums)
print(nums)

# List of Tuples 
# and 2-Dimensional Lists

num_groups = [(1,3,5),
              (2,4,6, 8, 10),
              (-1,-3,-5),
              (-2,-4,-6)]

# print(num_groups[0][0])
# print(num_groups[1][0])
# print(num_groups[2][0])

# Task! Write a loop that prints the first element in each tuple in num_groups
for i in range(len(num_groups)):
    print(num_groups[i][0])


# Passing List to Functions
# list_a = [1,2,3]
# list_b = list_a 

def change_first_val(num_list):
    num_list[0] = 999
def add_val(in_list, val):
    in_list.append(val)

def clear_list_bad(in_list):
    in_list = []

def clear_list_good(in_list):
    for i in range(len(in_list)):
        in_list.pop(0)

def main():
    numbers = [2,4,6,8,10]
    print(numbers)
    change_first_val(numbers)
    print(numbers)
    add_val(numbers, 12)
    print(numbers)

    clear_list_good(numbers)
    print(numbers)
main()

"""
Objective: You are given the following list of exam grades, where each element is a tuple containing a student's name and score:

exam_grades = [
    ('Aya', 88),
    ('Bo', 94),
    ('Eli', 73),
    ('Fern', 91),
    ('Gus', 85),
    ('Jane', 90),
    ('John', 42)
]

*copy and paste the code above into your program

Write the Python code that does the following:

    Remove Bo's exam record from the list.

    Replace Fern's score with 85, keeping her record in the same position in the list. 

    Calculate and display the average, minimum, and maximum exam scores.

    Show the updated list and the summary statistics.
"""

exam_grades = [
    ('Aya', 88),
    ('Bo', 94),
    ('Eli', 73),
    ('Fern', 91),
    ('Gus', 85),
    ('Jane', 90),
    ('John', 42)
]

# Remove Bo's Score

# exam_grades.remove(("Bo", 94))
# exam_grades.pop(1)
entry_to_delete = None
for i in range(len(exam_grades)):
    if exam_grades[i][0] == "Bo":
        entry_to_delete = exam_grades[i]

exam_grades.remove(entry_to_delete)

exam_grades[2] = ("Fern", 85)
print(exam_grades)

min_val = None
max_val = None
total = 0

for item in exam_grades:
    score = item[1]
    if min_val == None or score < min_val:
        min_val = score
    if max_val == None or score > max_val:
        max_val = score
    
    total += score

print(min_val)
print(max_val)
print(total/len(exam_grades))    
