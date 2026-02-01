"""
Chapter 2: Input, Processing, and Output
---------------------------------------

This file is meant to be used DURING class.
Students should follow along and write the code,
but ALL explanations are already included as comments.

Topics covered:
- Designing a program
- Input, processing, output
- print()
- Variables
- Input from the keyboard
- Calculations
- Strings and formatting
- Named constants
"""

# ======================================================
# Designing a Program
# ======================================================
# Before writing code, we should understand the task.
# Most programs follow the same basic pattern:
#
#   1. Input      → get data from the user or another source
#   2. Processing → perform calculations or transformations
#   3. Output     → display results to the user
#
# This chapter focuses on learning how to do each of these
# steps in Python.


# ======================================================
# Comments
# ======================================================
# Comments are ignored by Python.
# They are written for humans, not the computer.
# In Python, comments start with the # symbol.

print("Hello World") # this prints out hello world
# ======================================================
# Displaying Output with print()
# ======================================================
# The print function displays text or values to the screen.
# A function is a reusable block of code that performs a task.
# The data passed into a function is called an argument.

# TODO: Print the message Hello world to the screen

# ======================================================
# Program Execution Order
# ======================================================
# Python executes statements from TOP to BOTTOM.
# Each line runs in order, unless we explicitly change the flow.

# TODO: Print three words on three separate lines:
# Programming
# is
# fun!
print("Programming")
print("is")
print("fun!")
# ======================================================
# Variables
# A variable is a name that refers to a value in memory.
# Variables are created using an assignment statement.
#
#   variable_name = value
#
# The = symbol is called the assignment operator.
# ======================================================
# Variable Naming Rules
# Variable names:
# - Cannot be Python keywords
# - Cannot contain spaces
# - Must start with a letter or underscore
# - Are case-sensitive
# - Should describe what the variable represents
# !!!Good Programming Habits #1: Name variables the thing they represent
# TODO: Create variables for:
# - temperature (an integer)
# - cost (a floating-point number)
# - name (a string)
temperature = 36
cost = 5.99
name = "Dominic MacIsaac"

print(temperature)
print(cost)
print(name)
# ======================================================
# Data Types
# ======================================================
# Strings:
#   A string is a sequence of characters
#   Strings must be surrounded by quotes: ' ' or " "
# Integers:
#   Whole numbers (positive, negative, or zero)
# Float:
#   Decimal/Real Numbers
# Bool (or Boolean):
#   Logical values: True or False

is_student = False



# ======================================================
# Variable Reassignment
# ======================================================
# Variables can be reassigned while the program is running.
# Python variables do not have a fixed type.
name = 40
print(name)
name = "dominic"
print(name)

print(temperature)

# TODO: Assign a number to a variable
# TODO: Reassign the same variable to a string



# ======================================================
# Performing Calculations
# ======================================================
# Math expressions combine:
# - Operators (+, -, *, /, //, %, **)
# - Operands (numbers or variables)
x = 10
y = 3
print(x + 100)
z = y - x
print(z)
print(type(x/y))

print(x % y)

print(17 % 5)

# TODO: Demonstrate each arithmetic operator

# ======================================================
# Operator Precedence
# ======================================================
# Python follows standard math rules:
# 1. Parentheses
# 2. Exponents
# 3. Multiplication / Division
# 4. Addition / Subtraction

# TODO: Show how parentheses change the result
print(10 * (5 + 1))

# ======================================================
# String Concatenation
# ======================================================
# Strings can be joined together using the + operator.

# TODO: Concatenate two strings and print the result

x = "hello" + "goodbye" + "hi"
print(x)

y = "1"
z = "2"
print(y + z)
# TODO: TASK! Create two strings, first_name, and last_name
# concatenate them together into full_name and then print it
# What did you notice about its formatting? How could
# you improve the formatting?
fst_n = "Dominic"
lst_n = "MacIsaac"
fll_n = fst_n + " " + lst_n
print(fll_n)

# ======================================================
# More About print()
# ======================================================
# print() automatically adds:
# - A space between items
# - A newline at the end
#
# These can be changed using:
# - end= (line ending)
# TODO: Use end= to prevent a newline
print("cold", end = "...")
print("hot")
# TODO: TASK! Print three words on the same line using 3 different
# print statements
# try to use a different end line string for each
print("Programming", end = "\n")
print("is", end = "\n")
print("fun!")

# print multiple things in a single statement be separating
# arguments with commas
# print(item1, item2, item3)
# each item will be printed with a space in between them
x = 39
print(x, "thirty-nine", "!!!!")

# ======================================================
# Escape Characters
# ======================================================
# Escape characters start with a backslash:
# \n → newline
# \t → tab

# TODO: Print text using a newline and a tab
# x = "hello\n\n\ngood\thi"
# print(x)
# x = "hello\n\n\ngoodbye\thi"
# print(x)
# # TODO: TASK! Print your first and last name on two separate lines
# # with a single print statement
# print("Dominic\nMacIsaac")

# ======================================================
# Formatted Output with f-strings
# ======================================================
# f-strings allow us to embed variables inside strings.
# Format specifiers control how values appear.
age = 25
f_str = f"you are {age + 1}"
print(f_str)
# TODO: Print a number rounded to two decimals

x = 10/3
print(f"the answer is {999999876.99999:.2f}")
# TODO: TASK! Write out as many digits of pi as you know
# then print out that pi variable with 1 decimal point
# make sure to have the print out label the number
pi = 3.141592653
print(f"pi is {pi:.1f}")
# ======================================================
# Reading Input from the Keyboard
# ======================================================
# The input() function:
# - Displays a prompt
# - Waits for the user to type
# - Always returns a STRING

# TODO: Ask the user for their name and store it in a variable
user = input("What is your name? ")
print(f"you are {user}")
# TODO: Print a greeting using that name


# ======================================================
# Reading Numeric Input
# ======================================================
# Since input() returns a string, we must convert it
# when we want numbers.
#
# int()   → converts to integer
# float() → converts to floating-point number
age = int(input("How old are you? "))

print(f"next year you will be {age + 1}")

# TODO: Ask the user for their age (integer)
# TODO: Ask the user for their score (float)

# TODO: TASK! Write a small program which calculates the
# total pay of a user. Assume the user knows how many
# hours they worked and what their hourly pay is.

# ======================================================
# Other Data Type Conversions
# ======================================================
# bool()    → converts to bool
#       - Converting to bool follows truthiness rules:
#       - 0, 0.0, "", and None become False
#       - almost everything else becomes True
# str()     → converts to string

# ======================================================
# !!!GPH #2: Named Constants
# ======================================================
# A magic number is an unexplained numeric value.
# Named constants make code readable and easier to maintain.
#
# Constants are written in ALL CAPS by convention.

# TODO: Create a constant interest rate
# TODO: Use it in a calculation

# ======================================================
# !!!GPH #3: Commenting Your Code
# ======================================================
# Comments should explain *why* code exists or clarify
# complex logic (loops, functions, tricky calculations).
# 
# If you follow GPH #1 (clear, descriptive variable names),
# much of your code will be self-explanatory and will not
# require heavy commenting.

# TODO TASK: read through this code and understand what each line of code is doing
# then try to add 1 to 2 comments to make it a bit easier to understand

# ANNUAL_INTEREST_RATE = 0.045   # 4.5% annual interest

# principal = float(input("Enter starting balance: "))
# years = int(input("Enter number of years: "))

# final_balance = principal * (1 + ANNUAL_INTEREST_RATE) ** years
# # Exponent applies compound interest once per year

# print("Final balance:", final_balance)