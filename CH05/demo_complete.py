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
# demo_function_exists_but_does_not_run()


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
    print("\n=== Welcome ===")
    print("Today: Functions! (void vs return, args, scope, modules)")

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

greet_name("Dominic")
greet_name("Ada")
greet_name("Linus")

# GOAL: show that you can pass variables as arguments.
user = "Student"
greet_name(user)


# ============================================================
# 3) MULTIPLE PARAMETERS (POSITION MATTERS)
# ============================================================

# GOAL: function with 2 parameters; arguments map by POSITION.
def add_and_print(a, b):
    print("a:", a, "b:", b, "sum:", a + b)

add_and_print(10, 5)
add_and_print(5, 10)  # different ordering -> different mapping

# GOAL: show a common "mistake"—passing wrong order.
def print_full_name(first, last):
    print(last + ", " + first)

print_full_name("Dominic", "MacIsaac")
print_full_name("MacIsaac", "Dominic")  # wrong order -> awkward output


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
# 5) PASSING ARGUMENTS: "PASS BY VALUE" FEELING (REASSIGNMENT)
# ============================================================

# GOAL: show that reassigning a parameter does not change caller variable.
def change_me(n):
    print("Inside change_me BEFORE:", n)
    n = 0
    print("Inside change_me AFTER:", n)

value = 99
print("\nIn main BEFORE:", value)
change_me(value)
print("In main AFTER:", value)  # still 99


# ============================================================
# 6) KEYWORD ARGUMENTS
# ============================================================

# GOAL: show keyword args let you pass by NAME instead of position.
def describe_pet(animal, name):
    print("Animal:", animal)
    print("Name:", name)

describe_pet("dog", "Luna")
describe_pet(name="Luna", animal="dog")  # order doesn't matter now

# GOAL: show you can mix positional then keyword (positional must come first).
describe_pet("cat", name="Mochi")

# Try this: SyntaxError (positional after keyword)
# describe_pet(animal="cat", "Mochi")


# ============================================================
# 7) DEFAULT ARGUMENTS
# ============================================================

# GOAL: define a function with a default parameter value.
def show_tax(price, tax_rate=0.07):
    tax = price * tax_rate
    print("Price:", price, "Tax rate:", tax_rate, "Tax:", tax)

show_tax(100)        # uses default 0.07
show_tax(100, 0.08)  # overrides default

# GOAL: show rule: non-default params must come before default params.
# This is INVALID (don’t run; it won’t even parse):
# def bad_example(a=10, b):
#     pass

# GOAL: default for ALL params means you can call with none.
def greet_with_defaults(name="friend", punctuation="!"):
    print("Hello", name + punctuation)

greet_with_defaults()
greet_with_defaults("Dominic")
greet_with_defaults("Dominic", "!!!")
greet_with_defaults(punctuation="??", name="Class")


# ============================================================
# 8) GLOBAL VARIABLES (WHY THEY’RE RISKY)
# ============================================================

# GOAL: show that globals can be read inside functions.
counter = 0  # global variable (avoid in real code when possible)

def show_counter():
    print("counter is:", counter)

show_counter()

# GOAL: show that assigning to a global inside a function requires 'global'.
def increment_counter():
    global counter
    counter += 1

increment_counter()
increment_counter()
show_counter()

# GOAL: show why globals are confusing (many places can change them).
def reset_counter():
    global counter
    counter = 0

reset_counter()
show_counter()


# ============================================================
# 9) GLOBAL CONSTANTS (OKAY USE)
# ============================================================

# GOAL: demonstrate a global constant (convention: ALL_CAPS).
SALES_TAX = 0.092  # pretend WA-ish tax; for demo only

def show_sales_tax_on(price):
    tax = price * SALES_TAX
    print("Price:", price, "Tax:", tax, "Total:", price + tax)

show_sales_tax_on(50)


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
# 13) RETURNING MULTIPLE VALUES
# ============================================================

# GOAL: return multiple values (Python returns a tuple).
def min_and_max(a, b, c):
    smallest = min(a, b, c)
    largest = max(a, b, c)
    return smallest, largest

lo, hi = min_and_max(5, 100, 12)
print("\nmin_and_max returned:", lo, hi)


# ============================================================
# 14) RETURNING None TO SIGNAL AN ERROR
# ============================================================

# GOAL: return None when an operation can’t be performed.
def safe_divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

print("\nsafe_divide(10, 2):", safe_divide(10, 2))
print("safe_divide(10, 0):", safe_divide(10, 0))

result = safe_divide(10, 0)
if result is None:
    print("Division failed (cannot divide by zero).")
else:
    print("Division result:", result)


# ============================================================
# 15) THE pass KEYWORD (PLACEHOLDER WHILE DESIGNING)
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
# 16) IMPORTING MODULES + DOT NOTATION (random)
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
# 17) THE math MODULE
# ============================================================

# GOAL: use math module constants and functions.
import math

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
# 18) MINI “TOP-DOWN DESIGN” EXAMPLE (PUTTING IT TOGETHER)
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
# hours = get_hours_worked()
# rate = get_hourly_rate()
# gross = calc_gross_pay(hours, rate)
# print_pay_stub(hours, rate, gross)


# ============================================================
# 19) MENU-DRIVEN PROGRAM (LOOP + FUNCTIONS)
# ============================================================

# GOAL: show a simple menu program that calls functions based on user choice.
def menu_option_1():
    print("Option 1: Roll a die (1..6):", random.randint(1, 6))

def menu_option_2():
    n = int(input("Enter a number to double: "))
    print("Double is:", double(n))

def menu_option_3():
    n = int(input("Enter a number to test even/odd: "))
    print("Even?" , is_even(n))

# Uncomment to run menu:
# choice = ""
# while choice != "4":
#     print("\nMenu:")
#     print("1) Roll a die")
#     print("2) Double a number")
#     print("3) Even/odd test")
#     print("4) Quit")
#     choice = input("Choose: ")
# 
#     if choice == "1":
#         menu_option_1()
#     elif choice == "2":
#         menu_option_2()
#     elif choice == "3":
#         menu_option_3()
#     elif choice == "4":
#         print("Goodbye!")
#     else:
#         print("Invalid choice.")


# ============================================================
# 20) MODULES IDEA + __name__ == "__main__"
# ============================================================

# GOAL: show how to prevent "main code" from running when imported.
def main():
    print("\nRunning main() demo...")
    show_intro()
    greet_name("Class")
    print("double(8) ->", double(8))
    show_outro()

if __name__ == "__main__":
    main()

"""
Teaching note:
- If you run this file directly: __name__ == "__main__" so main() runs.
- If you import this file from another script: __name__ becomes the module name,
  so main() does NOT auto-run.
"""