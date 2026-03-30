# Lecture Demonstration Plan — Chapter 8: More About Strings
**Duration:** 30 minutes  
**Textbook:** *Starting Out with Python, 6th Edition* (Gaddis)  
**Format:** Instructor-led demonstration with live coding and discussion

---

## 0–5 min: Overview and Warm-up
**Slides:** 2–3  
**Goals:** Reinforce that strings are sequences; introduce indexing and iteration.

### Talking Points
- Strings are *sequences* (like lists), meaning each element has an index.
- You can loop through strings using `for ch in string`.
- The `len()` function gives the number of characters.

### Code Demo
```python
name = "Juliet"
for ch in name:
    print(ch)
print("Length:", len(name))

print("Index of 'l':", name[2])
```
**Prompt students:** "What will happen if I try `name[10]`?" (Discuss `IndexError`.)

---

## 5–10 min: Concatenation and Immutability
**Slides:** 8–10  
**Goals:** Show how to join strings and explain why strings cannot be changed.

### Talking Points
- `+` joins two strings; `+=` appends to an existing variable.
- Strings are *immutable*—once created, they cannot be directly modified.

### Code Demo
```python
first = "Carmen"
last = "Brown"
full = first + " " + last
print(full)

# Demonstrate immutability
# first[0] = 'K'  # This will cause an error
```
**Ask:** "If we can’t change a string, how does concatenation still work?"
(Answer: It creates a *new* string.)

---

## 10–15 min: String Slicing
**Slide:** 11  
**Goals:** Learn how to extract substrings and use negative indexes.

### Talking Points
- Format: `string[start:end]` returns characters from `start` up to but not including `end`.
- Negative indexes count from the end of the string.
- You can also reverse strings using slice syntax.

### Code Demo
```python
word = "strawberry"
print(word[0:5])    # straw
print(word[5:])     # berry
print(word[-5:])    # berry
print(word[::-1])   # reverse
```
**Prompt:** Ask students what `word[::2]` would output.

---

## 15–20 min: String Methods for Testing and Modification
**Slides:** 13–16  
**Goals:** Demonstrate key Boolean and modification methods.

### Talking Points
- Common testing methods: `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`, `islower()`, `isupper()`.
- Modification methods: `lower()`, `upper()`, `strip()`, `lstrip()`, `rstrip()`.

### Code Demo
```python
code = "abc123"
print(code.isalnum())  # True

phrase = "   Hello There!   "
print(phrase.strip())  # Remove spaces
print(phrase.upper())  # Convert to uppercase
```
**Ask:** "Where would you use `.strip()` in a real program?" (Example: cleaning user input.)

---

## 20–25 min: Searching and Replacing
**Slides:** 17–19  
**Goals:** Show search and replace operations.

### Talking Points
- `.find(substring)` returns the starting index or -1 if not found.
- `.replace(old, new)` creates a modified copy.
- `.startswith()` and `.endswith()` return Boolean results.

### Code Demo
```python
email = "student@gonzaga.edu"
print(email.endswith(".edu"))
print(email.find("@"))
print(email.replace("student", "instructor"))
```
**Mini-Challenge:** Ask students to check if an email starts with "admin".

---

## 25–30 min: Splitting and Tokenizing Strings
**Slides:** 21–26  
**Goals:** Show how `.split()` divides strings into tokens (substrings).

### Talking Points
- `.split()` turns a string into a list of tokens.
- Default separator is whitespace; a custom delimiter can be specified.
- Tokenizing is essential for parsing structured text like CSV data.

### Code Demo
```python
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)
for fruit in fruits:
    print(fruit.title())
```
**Discussion:** Connect to real-world uses—splitting CSV fields, log parsing, etc.

---

## Wrap-Up and Reflection
**Review Questions:**
- Why are strings immutable?
- What’s the difference between `.find()` and `in`?
- How can `.split()` and `.replace()` simplify data processing?

**Follow-up Exercise:**
Write a program that:
1. Asks the user for a sentence.
2. Prints the number of words (using `.split()`).
3. Displays the sentence in all caps.
4. Prints the reversed sentence using slicing.

---
**End of Lecture Demo — Chapter 8: More About Strings**

