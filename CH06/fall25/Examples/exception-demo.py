"""
exception_handling_demo.py

This file introduces exception handling step-by-step.
Run each section separately as you learn.
"""

# -------------------------------
# 1. The Problem: Unhandled Error
# -------------------------------
# Try running this and entering a non-number like "cat"

try:
    age = int(input("Enter your age: "))
    print(f"you are {age} years old")
except ValueError:
    print("Invalid input")
    exit()
else:
    print(f"you are {age} years old")


# It crashes with a ValueError! Let's fix that below.


# -------------------------------
# 2. Basic try/except
# -------------------------------
# try:
#     age = int(input("Enter your age: "))
#     print(f"You are {age} years old.")
# except ValueError:
#     print("Please enter a valid number for your age!")


# -------------------------------
# 3. Multiple except blocks
# -------------------------------
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ValueError:
#     print("One of the inputs was not a number.")
# except ZeroDivisionError:
#     print("You can’t divide by zero!")


# -------------------------------
# 4. Using else
# -------------------------------
# try:
#     num = int(input("Enter a number: "))
#     x = num/0
# except ValueError:
#     print("That wasn't a number!")
# except ZeroDivisionError:
#     print("no dividing by zero!")
# else:
#     print(f"Good! You entered {num}.")


# -------------------------------
# 5. Using finally
# -------------------------------
# try:
#     f = open("example.txt", "r")
#     data = f.read()
#     print("File contents:", data)
# except FileNotFoundError:
#     print("example.txt not found!")
# finally:
#     print("Attempted to open example.txt — done.")


# -------------------------------
# 6. Combining it all: Input validation loop
# # -------------------------------
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age < 0:
#             raise ValueError("Age cannot be negative.")
#     except ValueError as e:
#         print("Invalid input:", e)
#     else:
#         print("Age recorded:", age)
#         break
#     finally:
#         print("Validation attempt complete.\n")
