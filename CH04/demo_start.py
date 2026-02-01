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

# TASK:
# - Modify this so valid scores are between 0 and 100 inclusive


# ======================================================
# Single-Line while Loops
# ======================================================
# If the body of the loop is ONE statement,
# it can be written on a single line.

# TODO:
# - Create a variable x starting at 0
# - Write a single-line while loop that increments x until x reaches 3
# - Print x after the loop ends

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
# - Print multiples of 3 from 3 to 30


# ======================================================
# Using the Target Variable Inside the Loop
# ======================================================
# The target variable is just a normal variable.
# It can be used in expressions and calculations.

# TODO:
# - Write a for loop from 1 to 5
# - Inside the loop, print each number and its square

# TASK:
# - Print whether each number is even or odd
# - Print the cube of each number


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

# TODO:
# - Create a variable total starting at 0
# - Write a loop that adds numbers from 1 to 5 into total
# - Print the final total

# TASK:
# - Rewrite this using +=
# - Sum only even numbers
# - Ask the user how many numbers to sum


# ======================================================
# Augmented Assignment Operators
# ======================================================
# These are shorthand operators:
# +=  -=  *=  /=  %=

# TODO:
# - Rewrite a running total example using +=
# - Demonstrate -=, *=, and %= on a variable
# - Print the variable after each operation

# TASK:
# - Explain why += is common with accumulators


# ======================================================
# Sentinels
# ======================================================
# A sentinel is a special value that signals "stop".
# It must be distinct from valid data.

# TODO:
# - Ask the user to enter numbers repeatedly
# - Use a sentinel value (like -1) to stop the loop
# - Keep a running total of all entered numbers
# - Print the total after the loop ends

# TASK:
# - Count how many numbers were entered
# - Use a string sentinel like "quit"


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


# ======================================================
# break Statement
# ======================================================
# break immediately exits the loop.

# TODO:
# - Write a loop that counts upward
# - Use break to exit the loop when a certain value is reached
# - Print values before the break occurs

# TASK:
# - Move the counter update before the break condition
# - Use break in a for loop


# ======================================================
# continue Statement
# ======================================================
# continue skips the rest of the current iteration.

# TODO:
# - Write a loop from 1 to 10
# - Use continue to skip numbers divisible by 3
# - Print all other numbers

# TASK:
# - Skip even numbers instead
# - Use continue to ignore invalid input

