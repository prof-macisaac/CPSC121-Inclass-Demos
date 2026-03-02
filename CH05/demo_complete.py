"""
CH 5 FUNCTIONS

Topics covered:
- What functions are, why we use them
- Defining + calling (void)
- Parameters/arguments (1 and many)
- Local scope
- "Pass by value" behavior (reassignment doesn't change caller variable)
- Keyword arguments
- Default arguments
- Global variables + why to avoid them
- Global constants (reasonable use)
- Value-returning functions (+ return None for error)
- Returning multiple values
- random module (randint, random, uniform, seed)
- math module (pi, sqrt, etc.)
- Storing functions in modules idea + __name__ guard
"""

# ============================================================
# 0) QUICK WARMUP: WHAT IS A FUNCTION?
# ============================================================

# GOAL: show that a function is "stored code" until you call it.
def demo_function_exists_but_does_not_run():
    print("This only prints if the function is CALLED.")

# Try this: nothing prints until you call it.
demo_function_exists_but_does_not_run()


# ============================================================
# 1) VOID FUNCTIONS (DO SOMETHING, RETURN NOTHING)
# ============================================================

# GOAL: define and call a simple void function that prints "hello".
def say_hello():
    print("Hello!")

say_hello()

# GOAL: show that void functions return None by default.
result = say_hello()
print("Return value from say_hello():", result)  # None


# GOAL: show "main-like" flow using multiple helper functions.
def show_intro():
    print("=== Welcome ===")
    print("Today: Learning about functions")

def show_outro():
    print("=== Done ===\n")

show_intro()
say_hello()
show_outro()


# ============================================================
# 2) PARAMETERS + ARGUMENTS
# ============================================================

# GOAL: function with 1 parameter; call it with different arguments.
def greet_name(name):
    print("Hello,", name)

greet_name("John")
greet_name("Sam")

# GOAL: show that you can pass variables as arguments.
user = "Student"
greet_name(user)

def print_one_more(num):
    print(num+1)



# ============================================================
# 3) MULTIPLE PARAMETERS (POSITION MATTERS)
# ============================================================

# GOAL: function with 2 parameters; arguments map by POSITION.
def add_and_print(a, b):
    print("a:", a, "b:", b, "sum:", a + b)

add_and_print(10, 5)
add_and_print(5, 10)  # different ordering -> different mapping

# GOAL: show a common "mistake"—passing wrong order.
def print_repeat(statement, times):
    for i in range(times):
        print(statement)

print_repeat("Hello", 4)
print_repeat(4,"Hello")

# TASK: write a function that takes two values, and prints out the larger value


# ============================================================
# 4) LOCAL VARIABLES + SCOPE
# ============================================================

# GOAL: demonstrate a local variable only exists inside the function.
def local_scope_demo():
    x = 10
    print("Inside function, x =", x)

local_scope_demo()

# Try this: causes NameError because x doesn't exist here.
# print(x)

# GOAL: show that different functions can have locals with same name.
def scope_a():
    value = "A"
    print("scope_a value:", value)

def scope_b():
    value = "B"
    print("scope_b value:", value)

scope_a()
scope_b()


# ============================================================
# 5) PASSING ARGUMENTS
# ============================================================

# GOAL: show that reassigning a parameter does not change caller variable.
def change_me(n):
    print("Inside change_me BEFORE:", n)
    n = 0
    print("Inside change_me AFTER:", n)

value = 99
print("In main BEFORE:", value)
change_me(value)
print("In main AFTER:", value)  # still 99



# ============================================================
# 10) VALUE-RETURNING FUNCTIONS (RETURNING A NUMBER)
# ============================================================

# GOAL: write a function that doubles a number and RETURNS it.
def double(n):
    return n * 2

d = double(21)
print("\ndouble(21) returned:", d)

# GOAL: show that return values can be used directly in expressions.
print("double(10) + double(5) =", double(10) + double(5))


# TASK: write a function that takes two values and subtracts the smaller value from the larger value (and returns that value)

# ============================================================
# 11) RETURNING STRINGS
# ============================================================

# GOAL: return a string from a function (instead of printing it).
def make_greeting(name):
    return "Hello, " + name

message = make_greeting("Dominic")
print(message)


# ============================================================
# 12) BOOLEAN FUNCTIONS (RETURN True/False)
# ============================================================

# GOAL: create a boolean function to test if a number is even.
def is_even(n):
    return n % 2 == 0

print("\nis_even(10):", is_even(10))
print("is_even(11):", is_even(11))

# GOAL: show boolean return used in an if.
num = 17
if is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")


# ============================================================
# GPH: Main Functions
# ============================================================

# GOAL: show how to prevent "main code" from running when imported.
def main():
    print("\nRunning main() demo...")
    show_intro()
    greet_name("Class")
    print("double(8) ->", double(8))
    show_outro()
    
# main()

# ============================================================
# GPH: Function Headers
# ============================================================

def calculate_area(radius):
    """
    Calculate the area of a circle

    Parameters:
        radius (float): radius of the circle
    
    Returns:
        float: the area of the circle
    """
    return 3.14 * radius ** 2

def calculate_letter_grade(score, is_extra_credit):
    """
    Determine the final letter grade for a student.

    If extra credit is True, 5 points are added to the score.
    The score is capped at 100 after extra credit is applied.
    Letter grades are assigned using a standard 10-point scale.

    Parameters:
        score (float): The student's numeric score (0-100).
        is_extra_credit (bool): Whether extra credit should be applied.

    Returns:
        str: The final letter grade ("A", "B", "C", "D", or "F").

    """
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if is_extra_credit:
        score += 5
        if score > 100:
            score = 100

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# ============================================================
# RETURNING MULTIPLE VALUES
# ============================================================

# GOAL: return multiple values (Python returns a tuple).
def add_sub(a,b):
    added = a + b
    subtracted = a - b
    return added, subtracted
a, s = add_sub(5,2)


# ============================================================
# RETURNING None TO SIGNAL AN ERROR
# ============================================================

# GOAL: return None when an operation can’t be performed.
def safe_divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

result = safe_divide(10, 0)
if result is None:
    print("Division failed (cannot divide by zero).")
else:
    print("Division result:", result)


# ============================================================
# THE pass KEYWORD (PLACEHOLDER WHILE DESIGNING)
# ============================================================

# GOAL: show how pass lets you stub out a function during design.
def step1():
    pass

def step2():
    pass

# Later you fill them in.
# step1()
# step2()


# ============================================================
# IMPORTING MODULES + DOT NOTATION (random)
# ============================================================

# GOAL: use the random module and dot notation.
import random

# GOAL: randint(a, b) returns an int in [a, b].
print("\nRandom int 1..10:", random.randint(1, 10))

# GOAL: random() returns a float in [0.0, 1.0).
print("Random float 0..1:", random.random())

# GOAL: uniform(a, b) returns a float in [a, b].
print("Random float 5..7:", random.uniform(5, 7))

# GOAL: demonstrate seeding for repeatable pseudo-random results.
random.seed(123)
print("\nSeeded randint:", random.randint(1, 100))
print("Seeded randint:", random.randint(1, 100))

random.seed(123)
print("Seeded again (same sequence):", random.randint(1, 100))
print("Seeded again (same sequence):", random.randint(1, 100))


# ============================================================
# THE math MODULE
# ============================================================

# GOAL: use math module constants and functions.
import math
# https://docs.python.org/3/library/math.html
radius = 3
area = math.pi * radius**2
print("\nCircle area with r=3:", area)

print("sqrt(144):", math.sqrt(144))
print("ceil(3.14):", math.ceil(3.14))
print("floor(3.99):", math.floor(3.99))

# GOAL: show radians/degrees conversion.
degrees = 180
rads = math.radians(degrees)
print("180 degrees in radians:", rads)
print("pi radians in degrees:", math.degrees(math.pi))


# ============================================================
# MINI “TOP-DOWN DESIGN” EXAMPLE (PUTTING IT TOGETHER)
# ============================================================

# GOAL: show how functions can divide a task into smaller steps.
def get_hours_worked():
    return float(input("\nEnter hours worked: "))

def get_hourly_rate():
    return float(input("Enter hourly rate: "))

def calc_gross_pay(hours, rate):
    return hours * rate

def print_pay_stub(hours, rate, gross):
    print("\n--- Pay Stub ---")
    print("Hours:", hours)
    print("Rate:", rate)
    print("Gross Pay:", gross)

# Uncomment to run interactively:
hours = get_hours_worked()
rate = get_hourly_rate()
gross = calc_gross_pay(hours, rate)
print_pay_stub(hours, rate, gross)




# ============================================================
# DEFAULT ARGUMENTS
# ============================================================

# GOAL: define a function with a default parameter value.
def show_tax(price, tax_rate=0.07):
    tax = price * tax_rate
    print("Price:", price, "Tax rate:", tax_rate, "Tax:", tax)

show_tax(100)        # uses default 0.07
show_tax(100, 0.08)  # overrides default


# GOAL: default for ALL params means you can call with none.
def greet_with_defaults(name="friend", punctuation="!"):
    print(f"Hello, {name}{punctuation}")

greet_with_defaults()
greet_with_defaults("Dominic")
greet_with_defaults("Dominic", "!!!")
greet_with_defaults(punctuation="??", name="Class")

