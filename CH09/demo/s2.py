# this module overrides the print method
# it makes it so that print statements are 
# color coded for better readability
from rich import print

empty_dict = {}

# key-value pairs
# key has to be immutable
#   - string
#   - int, float, bool, tuple

grades = {"sara": 98, 
          "john": 74, 
          "sierra": 83}

print(grades)

# access values via key
grade = grades["sara"]
johns_grade = grades["john"]
print(f"sara -> {grade}")
print(f"john -> {johns_grade}")

# len()
print(f"len = {len(grades)}")

# update a value
grades["sara"] = 94
print(grades["sara"])

# add a key-value pair

grades["sarah"] = 101

# grades[10] = 999

print(grades)

# check if a key is in a dictionary
if "sarah" in grades:
    print(grades["sarah"])

stud_scores = {
    "sam": [96, 93, 99],
    "spike": [62, 42, 99.9]
}

print(stud_scores["sam"][1])

stud_scores["spike"].append(94)
print(stud_scores)

ok = {(1,2): "hi"}
print(ok[(1,2)])

# bad = {[1,2]: "hi"}

# Task
# create a courses_by_stud mapping name -> list of 2 courses
# append a course to one of the student and print it


courses_by_stud = {
    "tim" : ["CPSC121", "LIT101"],
    "tom" : ["CPSC222", "CPSC122"]
}

courses_by_stud["tim"].append("RELI203")

print(courses_by_stud)


# Iterate over keys
for student_name in courses_by_stud:
    print(f"key: {student_name}")
    print(f"courses: {courses_by_stud[student_name]}")

# retrieving all keys/items

students = list(courses_by_stud.keys())
print(students)

courses = list(courses_by_stud.items())
print(courses)

# print "name is taking X" for each (name, courses) tuple using courses list

# example
# tim is taking ["CPSC121", "LIT101", "RELI203"]



# GO OVER ANSWER TO TASK (MONDAY)