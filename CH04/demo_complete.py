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

n = 0
while n < 5:
    print("n:", n)
    n += 1

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

# TASK:
# - Explain what would cause the loop above to end (if anything)


# ======================================================
# Using while as a Count-Controlled Loop
# ======================================================
# A count-controlled while loop has three required parts:
# 1) Initialization
# 2) Comparison
# 3) Update

# Initialization
counter = 1

# Comparison
while counter <= 5:
    print("counter:", counter)

    # Update
    counter += 1

# TASK:
# - Change this loop to count DOWN from 5 to 1
# - Identify where each of the three required parts appears


# ======================================================
# Input Validation with while
# ======================================================
# Input validation repeats while the input is BAD.
# This prevents garbage-in, garbage-out (GIGO).

# Uncomment for live demo:
# score = int(input("Enter a non-negative score: "))
# while score < 0:
#     print("Invalid score.")
#     score = int(input("Enter a non-negative score: "))
# print("Score accepted:", score)

# TASK:
# - Modify this so valid scores are between 0 and 100 inclusive


# ======================================================
# Single-Line while Loops
# ======================================================
# If the body of the loop is ONE statement,
# it can be written on a single line.

x = 0
while x < 3: x += 1
print("x after loop:", x)

# NOTE:
# This is legal, but multi-line loops are usually clearer.


# ======================================================
# for Loop: Count-Controlled Loop
# ======================================================
# A for loop iterates once for each item in a sequence.
#
# General form:
# for target_variable in sequence:
#     statements

for num in [1, 2, 3, 4, 5]:
    print("num:", num)

# TASK:
# - Change the list
# - Use num in a calculation (square, cube, etc.)


# ======================================================
# Using range() with for Loops
# ======================================================
# range(stop)            → 0 to stop-1
# range(start, stop)     → start to stop-1
# range(start, stop, step)

for n in range(5):
    print(n)

for n in range(2, 6):
    print(n)

for n in range(2, 10, 2):
    print(n)

for n in range(10, 1, -2):
    print(n)

# TASK:
# - Print 5, 4, 3, 2, 1
# - Print multiples of 3 from 3 to 30


# ======================================================
# Using the Target Variable Inside the Loop
# ======================================================
# The target variable is just a normal variable.
# It can be used in expressions and calculations.

for x in range(1, 6):
    print(x, "squared is", x ** 2)

# TASK:
# - Print whether each x is even or odd
# - Print x cubed


# ======================================================
# Letting the User Control Loop Iterations
# ======================================================
# We can pass variables into range().

# Uncomment for live demo:
# start = int(input("Start: "))
# stop = int(input("Stop (exclusive): "))
# step = int(input("Step: "))
#
# for n in range(start, stop, step):
#     print(n)

# TASK:
# - What happens if step is negative?
# - What happens if start >= stop?


# ======================================================
# Calculating a Running Total (Accumulator)
# ======================================================
# An accumulator keeps a running total of values.

total = 0
for n in range(1, 6):
    total = total + n
print("total:", total)

# TASK:
# - Rewrite this using +=
# - Sum only even numbers
# - Ask the user how many numbers to sum


# ======================================================
# Augmented Assignment Operators
# ======================================================
# These are shorthand operators:
# +=  -=  *=  /=  %=

total = 0
for n in range(1, 6):
    total += n
print("total:", total)

value = 10
value -= 3
value *= 2
value %= 4
print("value:", value)

# TASK:
# - Explain why += is common with accumulators


# ======================================================
# Sentinels
# ======================================================
# A sentinel is a special value that signals "stop".
# It must be distinct from valid data.

# Uncomment for live demo:
# total = 0
# number = int(input("Enter a number (-1 to stop): "))
# while number != -1:
#     total += number
#     number = int(input("Enter a number (-1 to stop): "))
# print("total:", total)

# TASK:
# - Count how many numbers were entered
# - Use a string sentinel like "quit"



# ======================================================
# Nested Loops
# ======================================================
# A nested loop is a loop inside another loop.
# The inner loop completes ALL iterations for each
# iteration of the outer loop.

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# TASK:
# - Print (i, j) pairs instead of products
# - Make a 5x5 multiplication table
# - Count total inner loop executions


# ======================================================
# break Statement
# ======================================================
# break immediately exits the loop.

n = 0
while n < 100:
    print(n)
    if n == 5:
        break
    n += 1

# TASK:
# - Move n += 1 above the if
# - Use break in a for loop to stop early


# ======================================================
# continue Statement
# ======================================================
# continue skips the rest of the current iteration.

for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n)

# TASK:
# - Skip even numbers instead
# - Use continue to ignore invalid input
