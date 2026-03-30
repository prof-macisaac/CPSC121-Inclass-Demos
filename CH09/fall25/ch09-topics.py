"""
Dictionaries
"""

"""
Initialize a dictionary
"""
grades = {"sara":98, "john": 74, "sierra": 83}

empty_dict = {}

"""
Access values in a dictionary
- Need the key to get the value
"""
sara_grade = grades["sara"]
print(sara_grade)

print(grades["john"])


"""
Adding key-value pairs and updating key-value pairs
"""

# If the key doesn't exist, that key-value pair is added
# this add the key-value pair "dom":100
grades["dom"] = 100

# dict now has that kv pair
print(grades)

# we can now access dom's grade
print(grades["dom"])

# if the key does exist, its value is updated
grades["john"] = 83
print(grades)
print(grades["john"])

"""
Amount of kv pairs in a dict
    - len functions
"""
print(len(grades))

"""
Values can be lists (and other mutables!)

"""
test_scores_by_student = {"dom":[76,85, 91], "sam": [96,93,99]}
print(test_scores_by_student["dom"])

# but we can't have a list be the key 
# test_scores_by_student = {[76,85, 91]:"dom", [96,93,99]:"sam"}
# print(test_scores_by_student)


"""
Looping through dictionary
"""

for student_name in test_scores_by_student:
    print(f"{student_name} got the scores {test_scores_by_student[student_name]}")


"""
Helpful methods
"""
# get all the keys
students = test_scores_by_student.keys()
print(students)

# get all the items
# each kv pair is a tuple (key, value)
# returns a sequence of these tuples
student_score_items = test_scores_by_student.items()
print(student_score_items)

# remove a kv pair from the dictionary using the key
grades.pop("dom")
print(grades)



"""
Sets
"""
# create a set
s = set([1,2,3,3])
print(s)

# add item to a set
s.add("s")

# add multiple items to a set
s.update(["a", "as"])


# remove a value from the set
s.remove("as")

# looping through a set
for x in s:
    print(x)

if 4 in s:
    print("4 is s")
else:
    print("4 is not in s")


    

print(s)