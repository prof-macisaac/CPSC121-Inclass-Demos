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




# TODO: Print out hello 4 times by using a loop
n = 0
while n < 4:
    print(f"Hello : n = {n}")
    n = n + 1

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
# Using while as a Count-Controlled Loop
# ======================================================
# A count-controlled while loop has three required parts:
# 1) Initialization
# 2) Comparison
# 3) Update

# TODO:
# - Initialize a counter variable
# - Write a while loop that counts from 1 to 5
# - Print the counter each iteration
# - Update the counter so the loop terminates

x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Blast off!")


# TASK:
# - Change this loop to count DOWN from 5 to 1
# - Identify where each of the three required parts appears


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

score = int(input("Enter your score: "))
while score < 0:
    print("The score cannot be negative!")
    score = int(input("Enter your score: "))

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
# - Write a for loop using range(2, 6)
# - Write a for loop using range(2, 10, 2)
# - Write a for loop that counts DOWN using a negative step

# TASK:
# - Print 5, 4, 3, 2, 1
sum = 0
n = 5
# for x in range(0,n+1):
#     print(f"x is now: {x}")
#     sum = sum + x
x = 0

# - Print multiples of 3 from 3 to 30


# ======================================================
# Letting the User Control Loop Iterations
# ======================================================
# We can pass variables into range().

# TODO:
# - Ask the user for a start value
# - Ask the user for a stop value
# - Ask the user for a step value
# - Use these values in a for loop with range()
# - Print each value in the loop

# TASK:
# - What happens if step is negative?
# - What happens if start >= stop?


# ======================================================
# Calculating a Running Total (Accumulator)
# ======================================================
# An accumulator keeps a running total of values.

# goal: sum up all the values from 1 up to a number input by the user

sum_total = 0
n = int(input("What number should we sum up to? "))

for i in range(1, n+1):
    # sum_total = sum_total + i
    sum_total += i
print(f"the sum total is {sum_total}")
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



# ======================================================
# Sentinels
# ======================================================
# A sentinel is a special value that signals "stop".
# It must be distinct from valid data.

# goal: sum up all values the user enters until they say stop

user_val = input('Enter a value (enter "stop" to finish entering values): ')
sum_total = 0
while True:
    if user_val == "stop":
        break
    sum_total += int(user_val)
    user_val = input('Enter a value (enter "stop" to finish entering values): ')
print(sum_total)

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
print(f'n is now {n}')
# TASK: try to rewrite the previous example using a break statement


# ======================================================
# continue Statement
# ======================================================
# continue skips the rest of the current iteration.

# goal: print every number from 1 to 10, except those divisible by 3


for i in range(1, 11):
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

# TASK:
# - Print (i, j) pairs instead of products
# - Make a 5x5 multiplication table
# - Count total inner loop executions


