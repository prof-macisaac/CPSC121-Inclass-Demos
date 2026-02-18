"""
Chapter 3: Decision Structures and Boolean Logic
-----------------------------------------------

This file is meant to be used DURING class.
Students should follow along and write the code,
but ALL explanations are already included as comments.

Goal:
- You should be able to teach this chapter WITHOUT slides.
- We will build up conditionals step-by-step.

Topics covered:
- Boolean expressions + relational operators
- if statement (single alternative)
- if-else statement (dual alternative)
- Comparing strings
- Nested decision structures
- if-elif-else chains
- Logical operators: and / or / not
- Ranges using logical operators
- Boolean variables (flags)
- Conditional expressions (ternary operator)

"""

# ======================================================
# Program Flow: "Decision Structures"
# ======================================================
# By default, Python runs top-to-bottom.
# Conditionals let our program CHOOSE which lines to run.


# ======================================================
# Boolean Values and Boolean Expressions
# ======================================================
# A bool is either True or False (notice capital T and F).
# A Boolean expression is an expression that evaluates to True/False.
# Examples:
#   3 < 5        -> True
#   10 == 2      -> False
#   "a" != "b"   -> True

# TODO: Print a few boolean literals and boolean expressions
is_student = True
print(is_student)
print(type(is_student))


# ======================================================
# Relational Operators (Comparisons)
# ======================================================
# Relational operators compare two values:
#   >   greater than
#   <   less than
#   >=  greater than or equal to
#   <=  less than or equal to
#   ==  equal to
#   !=  not equal to
#
# IMPORTANT:
#   =   is assignment
#   ==  is comparison
x = 12.5
y = 11.5
print(f"x < y {x < y}")
print(f"x > y {x > y}")
print(f"x <= y {x <= y}")
print(f"x >= y {x >= y}")
print(f"x == y {x == y}")
print(f"x != y {x != y}")

# TODO: Print the result of each comparison between x and y

# TASK:
# Change x and y values and predict which comparisons become True/False.


# ======================================================
# The if Statement (Single Alternative)
# ======================================================
# The "if" statement runs a block ONLY if the condition is True.
# Indentation matters! Everything indented under if is the block.

temperature = 60

if temperature < 70:
    print("you should probably bring a jacket.")
    print("...")
else:
    print("good day for a t-shirt!")

print("The weather report is complete")

# ex: temperature print outs

# TASK:
# Change temperature to 60. What prints now?
# Change the condition to (temperature <= 40). What changes?


# ======================================================
# Common Mistakes with if
# ======================================================
# 1) Using = instead of ==
#    if temperature = 40:   <-- syntax error
#
# 2) Forgetting indentation
#
# 3) Expecting the if-block to run when condition is False

# (No code here—just warnings students will definitely hit.)


# ======================================================
# The if-else Statement (Dual Alternative)
# ======================================================
# if-else chooses between TWO paths:
# - if block runs when condition is True
# - else block runs when condition is False

# ex: age, ticket price

# TASK:
# Change age to 12 and run again.


# ======================================================
# Comparing Strings
# ======================================================
# Strings can be compared:
# - Equality: == and !=
# - Alphabetical order: <, >, <=, >=  (lexicographic order)
#
# IMPORTANT:
# Comparisons are case-sensitive.
# "Z" < "a" is True because ASCII/Unicode ordering places capital letters earlier.


# is_student = input("Are you a student (yes/no)? ")
# if is_student == "yes":
#     print("You are eligible for the student discount!")
#     price = 11
# else:
#     print("You are not eligible for the student discount")
#     price = 15
# print(f"You ticket costs ${price}")

# TODO: Compare strings for equality


# TODO: Compare strings alphabetically

# TASK:
# Ask the user for a word and compare it to "mango".
# Does it come before or after alphabetically?
# word = input("Enter a word: ")
# print(word < "mango")


# ======================================================
# Nested Decision Structures (Nested if)
# ======================================================
# A nested if is an if INSIDE another if.
# Useful when you only want to check something
# after another condition is already true.

gpa = 3.4
has_internship = True
print("gpa:", gpa, "has_internship:", has_internship)

if gpa >= 3.0:
    print("Meets GPA requirement.")
    if has_internship:
        print("Eligible for honors interview.")
    else:
        print("Consider getting experience for honors interview.")
else:
    print("Does not meet GPA requirement.")



# TASK:
# Change gpa and has_internship. Walk through which lines run.


# ======================================================
# if-elif-else Chains (Multiple Alternatives)
# ======================================================
# Use elif when there are MORE than two possibilities.
# Only ONE branch in the chain runs.

grade = 86
print("grade:", grade)

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
print("letter grade:", letter)

# Participation Assignment: 
# Ask for the temperature (in °F) and print advice:
# - Below 32 → "It's freezing"
# - 32–59 → "Wear a jacket"
# - 60–79 → "Nice weather"
# - 80+ → "It's hot"


# ======================================================
# Logical Operators: and / or / not
# ======================================================
# Combine boolean expressions:
# - and  -> True only if BOTH are True
# - or   -> True if AT LEAST ONE is True
# - not  -> flips True <-> False
#
# These are extremely common in conditionals.

hours = 15
is_weekend = False
print("hours:", hours, "is_weekend:", is_weekend)

if hours >= 10 and not is_weekend:
    print("Eligible for weekday perk.")

if is_weekend or hours >= 20:
    print("Eligible for bonus perk.")
else:
    print("Not eligible for bonus perk.")

# TASK:
# Try values where one side is True and the other False.
# Predict outputs before running.


# ======================================================
# Ranges with Logical Operators
# ======================================================

# or with explicit and:
#   if x >= low and x <= high:

temp = 72
print("temp:", temp)

# # TODO: range using and
if temp >= 68 and temp <= 75:
    print("Still comfortable range (same idea).")

# TASK:
# Create a variable speed.
# Print "speeding" if speed is outside 0..65 (inclusive).
# speed = 70
# if speed < 0 or speed > 65:
#     print("speeding")


# ======================================================
# Boolean Variables (Flags)
# ======================================================
# A boolean variable often represents a condition/state.
# We call these "flags" because they flip True/False.

is_logged_in = True
is_admin = False
if is_logged_in:
    print("1. Welcome back!")
else:
    print("2. Please log in.")

if is_logged_in and is_admin:
    print("3. Admin controls enabled.")
else:
    print("4. Standard user mode.")

# what are the outputs of the following conditions:
# is_logged_in  |   is_admin    | Result
# True          |   True        | 1 3
# True          |   False       | 1 4
# False         |   True        | 2 4
# False         |   False       | 2 4


# ======================================================
# Truthiness and Converting to bool
# ======================================================
# Any value can be converted to True/False with bool(value).
# In an if-statement, Python uses this automatically.
# ------------------------------------------------------
# Common falsy values:
#   False, 0, 0.0, "", [], {}, set(), None
# Almost everything else is truthy.

print("\n=== bool() examples ===")
print(bool(-1), bool(0))
print(bool(3.14), bool(0.0))
print(bool("hi"), bool(""))
print(bool(None))
x= "  "
if x:
    print(f"x: {x}")


# Truthiness in if-statements
# name = ""   # try "Dom"
# if name:
#     print("Name provided")
# else:
#     print("No name provided")


# ======================================================
# None: "no value"
# ======================================================
# None represents the absence of a value.
# It is NOT 0, NOT "", and NOT False.
# It means: "nothing has been assigned yet" or "no result".

x = None
print(x)
