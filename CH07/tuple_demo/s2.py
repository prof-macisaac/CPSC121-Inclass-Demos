# part a

list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

list_c = list_a + list_b

print(list_c)

# part b 

# list_a[0] = list_a[0] + list_b[0]

for i in range(len(list_a)):
    list_a[i] = list_a[i] + list_b[i]

print(list_a)


# TUPLES!

# What is a tuple? A sequence similar to a list
# BUT: tuples are IMMUTABLE

# format: tuple_name = (item_1, item_2, item_3)

dog_1 = "Spike", 36, "Bulldog"

dog_2 = ("Mac", 8, "Burmese Mountain Dog")

nums = (1,2,3,4,5)

# INDEXING!
print(dog_1[0])
print(dog_2[2])

# Functions!
print(len(nums))
print(len(dog_2))

print(min(nums))

for item in dog_2:
    print(item)


# tuples are immutable!
# dog_2[0] = "Hoop"



# Create a new tuple
dog_2 = ("Hop", dog_2[1], dog_2[2])

print(dog_2)


# membership

if "Gary" in dog_2:
    print("Good boy")
else:
    print("Gary come home")


# Convert List and Tuples

dog_2 = list(dog_2)
dog_2.append("Bones")

dog_2 = tuple(dog_2)
print(dog_2)

# List of tuples
num_groups = [(1,3,5),
              (2,4,6), 
              (-1,-3,-5),
              (-2,-4,-6)]

print(num_groups[0][1])

for item in num_groups:
    print(item[0])


# Passing Lists to Functions


def change_first_val(num_list):
    num_list[0] = 999


def append_val(in_list,value):
    in_list.append(value)

def clear_list_bad(in_list):
    in_list = []

def clear_list_good(in_list):
    for i in range(len(in_list)):
        in_list.pop(0)

def main():
    numbers = [1,2,3,4,5]
    print(numbers)
    change_first_val(numbers)
    print(numbers)

    append_val(numbers, 7)
    print(numbers)
    
    numbers.clear()
    # clear_list_good(numbers)
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

# remove bo's score
bo_index = None
bo_entry = None

for i in range(len(exam_grades)):
    if exam_grades[i][0] == "Bo":
        exam_grades.pop(i)
        break
        # bo_index = i
        # bo_entry = exam_grades[i]
# exam_grades.pop(bo_index)
# exam_grades.reamove(bo_entry)
print(exam_grades)

fern_index = 2
exam_grades[fern_index] = ("Fern", 85)
print(exam_grades)


min_val = None

for exam_item in exam_grades:
    score = exam_item[1]
    if min_val == None or score < min_val:
        min_val = score

print(min_val)