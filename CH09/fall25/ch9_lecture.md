here’s a tight 60-minute lesson plan with built-in questions, mini-challenges, and a single demo file that grows step-by-step. you can copy the demo file as-is and reveal sections as you go.

# 60-minute plan: Dictionaries & Sets (Python)

## learning goals

* model real-world data using dictionaries (create, read, update, delete, iterate).
* understand valid/invalid keys (hashability & immutability).
* use common dict methods effectively (`keys()`, `items()`, `pop()`, `get()`, `len()`).
* use sets to deduplicate, test membership, and do simple set operations.

## materials

* projector + live coding
* starter file: `dicts_sets_demo.py` (below)
* 3–5 short “checkpoint” prompts students submit (hands up / poll / LMS quick entry)

---

## agenda (60 min)

### 0–5 min — hook & warm-up

* prompt: “you’re tracking student grades. how would you store (name → score) so you can look up quickly by name?”
* think-pair-share (1 min), then: show dict literal.

**check-for-understanding (CFU)**

* Q: “what makes a dictionary the right tool vs a list of tuples?”

**mini-challenge A (1 min)**

* “write a dict mapping 3 cities to average temps.”

---

### 5–15 min — dictionary basics (create, read, update)

* live code: create `grades`, read `grades["sara"]`, add/overwrite keys.

**CFU**

* Q: “what happens if we do `grades["alex"]` when 'alex' isn’t a key?”
* Q: “after `grades["john"] = 83`, how many pairs?”

**mini-challenge B (2–3 min)**

* “add yourself to `grades` with a score. update john’s score +5. print the dict and `len(grades)`.”

---

### 15–25 min — values as collections; key rules (hashability)

* show values can be lists; explain keys must be immutable/hashable; lists cannot be keys.
* show `test_scores_by_student`.

**CFU**

* Q: “why is a list an invalid key but a tuple of ints is OK?”

**mini-challenge C (3 min)**

* “create `courses_by_student` mapping a name → list of 2 courses. append another course to one student and print the change.”

---

### 25–35 min — iterating & methods (`keys`, `items`, `get`, `pop`, `len`)

* iterate over keys; use `items()` to get `(key, value)` tuples.
* show `get(key, default)` for safe access; show `pop(key)` to remove.

**CFU**

* Q: “when would you prefer `get("sara", 0)` over `grades["sara"]`?”

**mini-challenge D (3 min)**

* “print each student: ‘sierra has 83’ style using `items()`.”
* stretch: “remove a key safely: if present, pop it; otherwise print ‘not found’ (use `get` or `in`).”

---

### 35–45 min — quick practice: small dict tasks

Give 3 rapid tasks (students code; you walk & help):

1. “compute class average from `grades`.”
2. “find the student(s) with the max grade.”
3. “build `letter_counts` from a string and print top 3 letters.”
   (steer them to `in` test, `get(k, 0) + 1` pattern)

Share one short solution for #2 using a running max.

---

### 45–55 min — sets: uniqueness, membership, basic ops

* show set creation, `add`, `update`, `remove`, membership `in`.
* connect to real use: deduplicate names from a roster, or find overlap between two classes.

**CFU**

* Q: “why is membership often faster with sets than lists?”
* Q: “what prints for `set([1,2,2,3])` and why?”

**mini-challenge E (3–4 min)**

* “given two lists of student names, make sets and print:

  1. all unique students,
  2. students in both lists,
  3. students only in list A (not in B).”

---

### 55–60 min — wrap-up & exit ticket

* recap: dicts (CRUD, iteration, methods), key rules; sets (unique, membership, ops).
* exit ticket (1–2 min):

  * “write one line of code that safely reads `grades['nina']` and gives 0 if missing.”
  * “turn a list `nums` into a deduped list while keeping no particular order.”

---

## the growing demo file (`dicts_sets_demo.py`)

> paste this once. as you teach, scroll down and run section-by-section. mini-challenges are inline as TODOs.

```python
# dicts_sets_demo.py
# A single file that grows with the lecture.

print("\n=== 1) Dictionaries: create & read ===")
grades = {"sara": 98, "john": 74, "sierra": 83}
empty_dict = {}
print("grades:", grades)
print("sara ->", grades["sara"])
print("john ->", grades["john"])

# TODO (Mini-Challenge A):
# Make a dict mapping 3 cities to average temps. Print len().

print("\n=== 2) Add / update key-value pairs ===")
grades["dom"] = 100       # add new key
print("after adding dom:", grades)
print("dom ->", grades["dom"])

grades["john"] = 83       # update existing key
print("after updating john:", grades)
print("john ->", grades["john"])
print("count pairs:", len(grades))

print("\n=== 3) Values can be collections; keys must be hashable ===")
test_scores_by_student = {"dom": [76, 85, 91], "sam": [96, 93, 99]}
print("dom scores:", test_scores_by_student["dom"])

# Invalid: list as a key (uncomment to see error)
# bad = {[1, 2]: "hi"}

# Valid: tuple as a key (immutable & hashable)
ok = {(1, 2): "hi"}
print("tuple-key dict works:", ok)

# TODO (Mini-Challenge C):
# Create courses_by_student mapping name -> list of 2 courses.
# Append a course for one student and print it.

print("\n=== 4) Iterating & helpful methods ===")
# Iterate over keys
for student_name in test_scores_by_student:
    print(f"{student_name} got scores {test_scores_by_student[student_name]}")

# keys() and items()
students = test_scores_by_student.keys()
print("keys():", list(students))

student_score_items = test_scores_by_student.items()
print("items():", list(student_score_items))

# Safe access with get()
maybe_alex = grades.get("alex", "NO RECORD")
print("alex ->", maybe_alex)

# Remove with pop()
removed = grades.pop("dom", None)  # second arg avoids KeyError if missing
print("removed dom:", removed, "now grades:", grades)

# TODO (Mini-Challenge D):
# Print "name has score X" for each (name,score) using items().
# Then try to pop a key only if present; otherwise print "not found".

print("\n=== 5) Quick practice helpers ===")
def class_average(d):
    return sum(d.values()) / len(d) if d else 0.0

def max_students(d):
    if not d:
        return []
    mx = max(d.values())
    return [k for k, v in d.items() if v == mx]

print("class average:", round(class_average(grades), 2))
print("max grade student(s):", max_students(grades))

# TODO (Practice):
# Build letter_counts from this string using dict and get():
text = "mississippi river"
letter_counts = {}
for ch in text:
    if ch != " ":
        letter_counts[ch] = letter_counts.get(ch, 0) + 1
print("letter counts:", letter_counts)

print("\n=== 6) Sets: uniqueness, membership, ops ===")
s = set([1, 2, 3, 3])
print("starting set:", s)  # {1, 2, 3}

s.add("s")
s.update(["a", "as"])
print("after adds:", s)

s.remove("as")  # KeyError if missing; use discard() to avoid
print("after remove 'as':", s)

for x in s:
    pass  # iterate (no guaranteed order)

if 4 in s:
    print("4 is in s")
else:
    print("4 is not in s")

# Common set ops
a = set(["sara", "john", "sierra", "dom"])
b = set(["dom", "nina", "sam"])

print("union a|b:", a | b)
print("intersection a&b:", a & b)
print("a - b:", a - b)
print("b - a:", b - a)

# TODO (Mini-Challenge E):
# Given two lists of names, make sets and print:
# 1) all unique students, 2) students in both lists, 3) students only in list A.
```

---

## ready-to-ask questions (sprinkle throughout)

**concept checks**

* “what error do we get if we access a missing key with `[]`? how do we avoid it?”
* “are dicts ordered? (py3.7+ preserves insertion order—should we *rely* on it for algorithms?)”
* “why can’t a list be a dict key, but a tuple can?”
* “when might `pop(key, default)` be safer than `pop(key)`?”

**mini whiteboard prompts**

* “draw a small diagram: `name → [scores]`. where do you apply an update to change a single score?”
* “write a line that prints all `(key, value)` pairs cleanly.”

**quick polls**

* “choosing a structure for: (1) usernames → last login, (2) bag of words counting, (3) deduping email list. which data types?”

---

## small graded moments (if you want them)

1. **checkpoint 1 (dict read/update):** “create `prices` with 3 items. increase the price of one item by 10% and print the new dict.”
2. **checkpoint 2 (safe access):** “print `orders['jane']` but show 0 if not found.”
3. **checkpoint 3 (set ops):** “given two lists with duplicates, print the intersection as a sorted list.”

---

## common pitfalls to call out

* KeyError from `dict[key]` on missing keys → prefer `in` or `get`.
* Mutating a list stored as a dict value mutates the *same* list object (expected—but surprises students).
* `set.remove(x)` raises on missing; `discard(x)` doesn’t.
* Sets are unordered; don’t rely on iteration order.

---

## optional stretch (if time)

* compute frequency of letter bigrams with a dict of dicts.
* invert a dictionary with unique values (`{student: grade} → {grade: student}`) and discuss risks when values aren’t unique.

---

want this as a printable handout or a starter zip with the demo file? I can package it.
