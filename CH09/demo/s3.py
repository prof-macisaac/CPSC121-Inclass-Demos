# this module overrides the print method
# it makes it so that print statements are 
# color coded for better readability
from rich import print

empty_dict = {}

# key-value pairs
# key has to be immutable: string, int, float, bool, tuple, etc

grades = {"sara": 98,
          "john": 74.5,
          "sierra": 82}

print(grades)

# access values via key
johns_score = grades["john"]
print(f"john's score -> {johns_score}")

# Task: print out sara and sierra's scores

print(f"sara's score -> {grades["sara"]}")
print(f"sierra's score -> {grades["sierra"]}")

# what if the key doesn't exist on access?
# -> KeyError!
# print(grades["tom"])

# safe access
print(grades.get("tom", -1))
print(grades.get("sierra", -1))

# len()
print(len(grades))

# update a value associated with a key
grades["sara"] = 100
print(grades)

# add a key-value pair
grades["dominic"] = 63

grades[10] = "tim"
print(grades[10])
print(grades)

if 100 in grades:
    print(grades["dominic"])
else:
    print("key does not exist")

# values can be lists! (or dictionaries, etc)

stud_scores = {
    "sam": [100, 87, 91],
    "spike": [62, 42, 99.9]
}

print(stud_scores["sam"][1])

# Spike got a 94 on the latest exam, add that score!
stud_scores["spike"].append(94)
print(stud_scores)

# tuples can be keys, lists can't

# bad = {[1,2]: "bad"}

good = {(1,2): "good"}
print(good[(1,2)])

# iterate over keys
for stud_name in stud_scores:
    print(f"stud_name = {stud_name}")
    print(f"scores = {stud_scores[stud_name]}")

# retrieving all keys/items

students = list(stud_scores.keys())
print(students)
x = list(stud_scores.values())
print(x)
scores = list(stud_scores.items())

print(scores)

# TASK print "NAME received the following scores: SCORES" using the scores list from above

# sam received the following scores: [100, 87, 91]
# spike received the following scores: [62, 42, 99.9, 94]

for stud_info in scores:
    # print(stud_info)
    name = stud_info[0]
    sc = stud_info[1]
    # print(name)
    # print(stud_scores)
    print(f"{name} received the following scores {sc}")


spike_scores = stud_scores.pop("spike", None)
print(stud_scores)
print(spike_scores)


def update_dict(d, key, new_value):
    d[key] = new_value


update_dict(stud_scores, "sam", [100,100,100])
print(stud_scores)



# Sets
# - only unique values
# - mutable
# - UNORDERED
# - good for things like: membership checks, set operations (Union, Intersections)

empty_set = set()
empty_set.add(1)

print(empty_set)

nums = [1,1,2,3,4,4,5,5,5,5,5]
num_set = set(nums)
print(num_set)
num_set.add("a")
num_set.add("ab")
num_set.add("a")

print(num_set)

for item in num_set:
    print(item)

num_set.remove("a")

print(num_set)
if 4 in num_set:
    print("FOUND")
else:
    print("NOT FOUND")

# Task 1
scores = {"Alice": 85, "Bob": 92, "Charlie": 88}
# Find the student with the highest score and print out their name and the score

max_score = -1
max_stud = ""
for key in scores:
    # print(key)
    # print(scores[key])
    stud_score = scores[key]
    if stud_score > max_score:
        max_score = stud_score
        max_stud = key
print(f"{max_stud} had the highest score of {max_score}")

# Task 2
# Combine
store_1 = {"apples": 5, "bananas": 3}
store_2 = {"bananas": 4, "oranges": 2}

# Result:
grocery_items = {"apples": 5, "bananas": 7, "oranges": 2}

gi = {}
for key_fruit in store_1:
    gi[key_fruit] = store_1[key_fruit]
print(gi)

for key_fruit in store_2:
    if key_fruit in gi: # update if the key already exists
        gi[key_fruit] = gi[key_fruit] + store_2[key_fruit]
    else: # add the key-value pair if it doesn't exists yet
        gi[key_fruit] = store_2[key_fruit]

print(gi)

