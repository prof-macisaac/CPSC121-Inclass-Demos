# dicts_sets_demo.py
# A single file that grows with the lecture.
from rich import print

empty_dict = {}

# key-value pairs
# key but immutable data type: string, int, float, bool, tuple
grades = {"sara": 98, 
          "john": 74, 
          "sierra": 83}

print("grades:", grades)

print(f"sara -> {grades["sara"]}")
print(f"john -> {grades["john"]}")

print(f"len = {len(grades)}")

grades["dominic"] = 100
print(grades)

grades["dominic"] = ("test1", 102)
print(grades)

if "ominic" in grades:
    print(grades["ominic"])
else:
    print("out")

grades["sierra"] = [90,83,100]
print(grades["sierra"])

grades["sierra"][2] = 103
print(grades)


# # print("\n=== 3) Values can be collections; keys must be hashable ===")
stud_scores = {
    "dom": [76, 85.5, 91], 
    "sam": [96, 93, 99]
    }

stud_scores["dom"].append(106)
print("dom scores:", stud_scores["dom"])

# # # Invalid: list as a key (uncomment to see error)
# bad = {[1, 2]: "hi"}

# # # Valid: tuple as a key (immutable & hashable)
ok = {(1, 2): "hi"}

ok[(1,2)] = "goodbye"
print(ok)
# print("tuple-key dict works:", ok)


# # # TODO (Mini-Challenge C):
# # # Create courses_by_student mapping name -> list of 2 courses.
# # # Append a course for one student and print it.


courses_by_student = {
    "john": ["CPSC121", "LIT101"],
    "dom":["CPSC222", "CPSC122"]}


courses_by_student["john"].append("RELI203")
print(courses_by_student["john"])






# # print("\n=== 4) Iterating & helpful methods ===")
# # # Iterate over keys
for student_name in stud_scores:
    stud_scores[student_name].append(100)
    
    print(f"{student_name} got scores {stud_scores[student_name]}")

# # # # keys() and items()
students = list(stud_scores.keys())
# print(students[0])
# print(type(students))
print("keys():", list(students))

student_score_items = stud_scores.items()
print("items():", list(student_score_items))

if "john" in stud_scores:
    print(stud_scores["john"])

# # # Safe access with get()
maybe_john = stud_scores.get("john", [])
print("john ->", maybe_john)

maybe_sam = stud_scores.get("sam", [])
print(f"maybe sam -> {maybe_sam}")


# # # Remove with pop()
removed = stud_scores.pop("sam",
        "No record")  # second arg avoids KeyError if missing


print("removed sam:", 
      removed, 
      "now grades:", 
      stud_scores)

# # # TODO (Mini-Challenge D):
# # # Print "name has score X" for each (name,score) using items().


def update_dict(d, name, scores):
    d[name] = scores

x = {}
update_dict(x, "k", [1,2,3])
print(x)






"""
Task 1 --------------
Given:

    scores = {"Alice": 85, "Bob": 92, "Charlie": 88}

Find the student with the highest score.

Task 2 --------------
Combine:
    store1 = {"apple": 5, "banana": 3}
    store2 = {"banana": 4, "orange": 2}

Result:
    {"apple": 5, "banana": 7, "orange": 2}

"""
# """
# SETS!
# like lists but only unique items
# """
print("\n=== 6) Sets: uniqueness, membership, ops ===")

s = set([1, 2, 3, 3])
print("starting set:", s)  # {1, 2, 3}

s.add("s")
print(s)
s.update(["a", "as", 1])
print("after adds:", s)

s.remove("as")  # KeyError if missing; use discard() to avoid
print("after remove 'as':", s)

for x in s:
    print(x)
#      # iterate (no guaranteed order)
s.add(4)
if 4 in s:
    print("4 is in s")
else:
    print("4 is not in s")

# # Common set ops
# a = set(["sara", "john", "sierra", "dom"])
# b = set(["dom", "nina", "sam", "dom"])
# print(b)
