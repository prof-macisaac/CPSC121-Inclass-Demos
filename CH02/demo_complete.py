"""
Chapter 2: Input, Processing, and Output
---------------------------------------
Filled reference version with all explanations.
"""

# ======================================================
# Displaying Output
# ======================================================
print("Hello world")

print("Programming")
print("is")
print("fun!")


# ======================================================
# Strings
# ======================================================
name = "Monty"
print(name)


# ======================================================
# Variables
# ======================================================
temperature = 75
cost = 87.99
person_name = "Alice"

print(temperature)
print(cost)
print(person_name)


# ======================================================
# Multiple Assignment
# ======================================================
x, y, z = 0, 1, 2
print(x, y, z)


# ======================================================
# Variable Reassignment
# ======================================================
value = 99
print(value)

value = "Take me to your leader"
print(value)


# ======================================================
# Input
# ======================================================
user_name = input("What is your name? ")
print("Hello", user_name)


# ======================================================
# Numeric Input
# ======================================================
age = int(input("Enter your age: "))
score = float(input("Enter your score: "))

print(age)
print(score)


# ======================================================
# Calculations
# ======================================================
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# ======================================================
# Operator Precedence
# ======================================================
print(10 + 2 * 5)
print((10 + 2) * 5)


# ======================================================
# Long Statements
# ======================================================
total = (10 + 20 +
         30 + 40 +
         50)
print(total)


# ======================================================
# String Concatenation
# ======================================================
message = "Hello " + "world"
print(message)


# ======================================================
# print() Options
# ======================================================
print("A", "B", "C", sep="-")
print("No newline here...", end="")
print(" now there is.")


# ======================================================
# Escape Characters
# ======================================================
print("Line 1\nLine 2")
print("Col1\tCol2")


# ======================================================
# f-Strings
# ======================================================
num = 12345.6789
discount = 0.5

print(f"{num:.2f}")
print(f"{num:,.2f}")
print(f"{discount:.0%}")
print(f"{num:^12,.2f}")


# ======================================================
# Named Constants
# ======================================================
INTEREST_RATE = 0.069
balance = 1000
interest = balance * INTEREST_RATE

print(f"Interest: ${interest:.2f}")


print("\nChapter 2 demo complete.")
