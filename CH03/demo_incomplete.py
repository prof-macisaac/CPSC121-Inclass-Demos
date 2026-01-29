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


# TODO: Print the result of each comparison between x and y

# TASK:
# Change x and y values and predict which comparisons become True/False.


# ======================================================
# The if Statement (Single Alternative)
# ======================================================
# The "if" statement runs a block ONLY if the condition is True.
# Indentation matters! Everything indented under if is the block.

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

# gpa = 3.4
# has_internship = True
# print("gpa:", gpa, "has_internship:", has_internship)

# if gpa >= 3.0:
#     print("Meets GPA requirement.")
#     if has_internship:
#         print("Eligible for honors interview.")
#     else:
#         print("Consider getting experience for honors interview.")
# else:
#     print("Does not meet GPA requirement.")



# TASK:
# Change gpa and has_internship. Walk through which lines run.


# ======================================================
# if-elif-else Chains (Multiple Alternatives)
# ======================================================
# Use elif when there are MORE than two possibilities.
# Only ONE branch in the chain runs.

# grade = 83
# print("grade:", grade)

# if grade >= 90:
#     letter = "A"
# elif grade >= 80:
#     letter = "B"
# elif grade >= 70:
#     letter = "C"
# elif grade >= 60:
#     letter = "D"
# else:
#     letter = "F"

# print("letter grade:", letter)

# TASK:
# Change grade to 59, 60, 70, 80, 90 and confirm results.


# ======================================================
# Logical Operators: and / or / not
# ======================================================
# Combine boolean expressions:
# - and  -> True only if BOTH are True
# - or   -> True if AT LEAST ONE is True
# - not  -> flips True <-> False
#
# These are extremely common in conditionals.

# hours = 15
# is_weekend = False
# print("hours:", hours, "is_weekend:", is_weekend)

# # TODO: and example: eligible if hours >= 10 AND not weekend
# if hours >= 10 and not is_weekend:
#     print("Eligible for weekday perk.")

# # TODO: or example: eligible if weekend OR hours >= 20
# if is_weekend or hours >= 20:
#     print("Eligible for bonus perk.")
# else:
#     print("Not eligible for bonus perk.")

# TASK:
# Try values where one side is True and the other False.
# Predict outputs before running.


# ======================================================
# Ranges with Logical Operators
# ======================================================
# A range check usually looks like:
#   if low <= x <= high:
# or with explicit and:
#   if x >= low and x <= high:

# temp = 72
# print("temp:", temp)

# # TODO: range using chained comparisons
# if 68 <= temp <= 75:
#     print("Comfortable range.")

# # TODO: range using and
# if temp >= 68 and temp <= 75:
#     print("Still comfortable range (same idea).")

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

# is_logged_in = True
# is_admin = False

# # TODO: Use flags in conditions
# if is_logged_in:
#     print("Welcome back!")
# else:
#     print("Please log in.")

# if is_logged_in and is_admin:
#     print("Admin controls enabled.")
# else:
#     print("Standard user mode.")

# TASK:
# Flip is_admin to True and explain what changed.



# ======================================================
# Mini "Putting it Together" Program
# ======================================================
# This is a small end-to-end example using:
# input, conversion, if/elif/else, and logical ops.

# Uncomment and run at the end of class:

# print("\n--- Mini Program: Ticket Price ---")
# age = int(input("Enter your age: "))
# is_student = input("Are you a student? (y/n): ").lower() == "y"
#
# if age < 5:
#     price = 0
# elif age <= 12:
#     price = 7
# elif age >= 65:
#     price = 8
# else:
#     price = 10
#
# # Student discount for ages 13-64
# if 13 <= age <= 64 and is_student:
#     price -= 2
#
# print("Ticket price: $", price)

print("\nEnd of Chapter 3 demo file.")
