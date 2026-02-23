"""
Chapter 4: Repetition Structures
--------------------------------

This file is meant to be used DURING class.
Students should follow along and type the code as we go.

All explanations are in comments.
There are NO print statements whose only purpose
is to move us to the next topic.

Topics covered:
- Repetition structures
- Condition-controlled vs count-controlled loops
- while loop
- Infinite loops
- Using while as a count-controlled loop
- Single-line while loops
- for loop
- range()
- Using the target variable
- Letting the user control iterations
- Running totals (accumulators)
- Augmented assignment operators
- Sentinels
- Input validation loops
- Walrus operator in loops
- Nested loops
- break, continue, and else with loops
"""

# ======================================================
# Repetition Structures
# ======================================================
# Repetition structures (loops) allow code to run multiple times
# without duplicating lines.
#
# Two broad categories:
# - Condition-controlled loops (while)
# - Count-controlled loops (for)


# ======================================================
# while Loop: Condition-Controlled Loop
# ======================================================
# A while loop repeats as long as a condition is True.
#
# General form:
# while condition:
#     statements
#
# The condition is checked BEFORE each iteration.
# A count-controlled while loop has three required parts:
# 1) Initialization
# 2) Comparison
# 3) Update
# x = 0
# while x < 4:
#     print(f"Hello x is {x}")
#     x = x + 1

# print("while loop complete")



# TODO:
# - Create a variable n starting at 0
# - Write a while loop that runs while n is less than 5
# - Inside the loop, print the current value of n
# - Update n so the loop eventually stops

# TASK:
# - Change the condition to n <= 5
# - Change the starting value of n
# - Predict output before running


# ======================================================
# Infinite Loops
# ======================================================
# A loop must contain something that eventually
# makes the condition False.
#
# Example of an infinite loop (DO NOT RUN):
#
# while True:
#     print("This never stops")

# TODO:
# - Discuss why this loop never ends
# - Identify what is missing compared to the previous loop

# TASK:
# - Explain what would cause the loop above to end (if anything)



# ======================================================
# Input Validation with while
# ======================================================
# Input validation repeats while the input is BAD.
# This prevents garbage-in, garbage-out (GIGO).

# TODO:
# - Ask the user to enter a score
# - While the score is negative:
#     - Print an error message
#     - Ask for the score again
# - When the loop ends, print that the score was accepted


# score = int(input("Enter your score: "))
# while score < 0 or score > 100:
#     print("The score must be between 0 and 100 (inclusive)")
#     score = int(input("Enter your score: "))
# print(f"your score is {score}")
# TASK:
# - Modify this so valid scores are between 0 and 100 inclusive



# ======================================================
# for Loop: Count-Controlled Loop
# ======================================================
# A for loop iterates once for each item in a sequence.
#
# General form:
# for target_variable in sequence:
#     statements

# TODO:
# - Write a for loop that iterates over a list of numbers
# - Print each number using the target variable

# TASK:
# - Change the list
# - Use the target variable in a calculation (square, cube, etc.)


# ======================================================
# Using range() with for Loops
# ======================================================
# range(stop)            → 0 to stop-1
# range(start, stop)     → start to stop-1
# range(start, stop, step)

# TODO:
# - Write a for loop using range(5)
# for x in range(5):
#     print(x)
# - Write a for loop using range(2, 6)
# - Write a for loop using range(2, 10, 2)
# - Write a for loop that counts DOWN using a negative step

# TASK:
# - Print 5, 4, 3, 2, 1
# - Print multiples of 3 from 3 to 30


# ======================================================
# Calculating a Running Total (Accumulator)
# ======================================================
# An accumulator keeps a running total of values.

# goal: sum up all the values from 1 up to a number input by the user
# sum_total = 0
# upper = int(input("What number should be sum up to? "))
# for i in range(1, upper + 1):
#     # sum_total = sum_total + i
#     sum_total += i

# print(f"the total is {sum_total}")
# TASK:
# - Sum only even numbers
# - Ask the user how many numbers to sum


# ======================================================
# Augmented Assignment Operators
# ======================================================
# These are shorthand operators:
# +=  -=  *=  /=  %=
# short hand for:
# x += y 
# x = x + y
x = 10
x -= 2
print(x)
y = 3
x *= y
print(x)



# ======================================================
# Sentinels
# ======================================================
# A sentinel is a special value that signals "stop".
# It must be distinct from valid data.

# goal: sum up all values the user enters until they say stop

# user_val = input("Enter a value to add (enter stop to complete): ")
# sum_total = 0
# while True:
#     if user_val == "stop":
#         break
#     sum_total += float(user_val)
#     user_val = input("Enter a value to add (enter stop to complete): ")

# print(f"Your total is {sum_total}")
# ======================================================
# break Statement
# ======================================================
# break immediately exits the loop.

n = 0
while n < 10:
    print(n)
    if n == 5:
        break
    n += 1

print(f"n is {n}")
# ======================================================
# continue Statement
# ======================================================
# continue skips the rest of the current iteration.

# goal: print every number from 1 to 10, except those divisible by 3

for i in range(1,11):
    if i % 3 == 0:
        continue
    print(i)








# ======================================================
# Nested Loops
# ======================================================
# A nested loop is a loop inside another loop.
# The inner loop completes ALL iterations for each
# iteration of the outer loop.

# TODO:
# - Write an outer loop that runs from 1 to 3
# - Inside it, write an inner loop that runs from 1 to 3
# - Print the product of the two loop variables
# - Format the output so each row is on its own line
print()
for i in range(1, 4):
    # print(i)
    for j in range(1,4):
        print(f"{j*i}", end = " ")
    print()


# TASK:
# - Print (i, j) pairs instead of products
# - Make a 5x5 multiplication table
# - Count total inner loop executions


