"""
CH 5 FUNCTIONS — ONE BIG LIVE DEMO FILE (BLANK VERSION)

Instructor flow:
- Scroll top to bottom, typing everything live.
- Examples are grouped and labeled.
- Each example starts with a GOAL comment.

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
    pass

# Try this:
# demo_function_exists_but_does_not_run()


# ============================================================
# 1) VOID FUNCTIONS (DO SOMETHING, RETURN NOTHING)
# ============================================================

# GOAL: define and call a simple void function that prints "hello".
def say_hello():
    pass

# say_hello()

# GOAL: show that void functions return None by default.
# result = say_hello()
# print(result)


# GOAL: show "main-like" flow using multiple helper functions.
def show_intro():
    pass

def show_outro():
    pass

# show_intro()
# say_hello()
# show_outro()


# ============================================================
# 2) PARAMETERS + ARGUMENTS
# ============================================================

# GOAL: function with 1 parameter; call it with different arguments.
def greet_name(name):
    pass

# greet_name("Dominic")
# greet_name("Ada")
# greet_name("Linus")

# GOAL: show that you can pass variables as arguments.
# user = "Student"
# greet_name(user)


# ============================================================
# 3) MULTIPLE PARAMETERS (POSITION MATTERS)
# ============================================================

# GOAL: function with 2 parameters; arguments map by POSITION.
def add_and_print(a, b):
    pass

# add_and_print(10, 5)
# add_and_print(5, 10)

# GOAL: show a common "mistake"—passing wrong order.
def print_full_name(first, last):
    pass

# print_full_name("Dominic", "MacIsaac")
# print_full_name("MacIsaac", "Dominic")


# ============================================================
# 4) LOCAL VARIABLES + SCOPE
# ============================================================

# GOAL: demonstrate a local variable only exists inside the function.
def local_scope_demo():
    pass

# local_scope_demo()

# Try this:
# print(x)

# GOAL: show that different functions can have locals with same name.
def scope_a():
    pass

def scope_b():
    pass

# scope_a()
# scope_b()


# ============================================================
# 5) PASSING ARGUMENTS: "PASS BY VALUE" FEELING
# ============================================================

# GOAL: show that reassigning a parameter does not change caller variable.
def change_me(n):
    pass

# value = 99
# print(value)
# change_me(value)
# print(value)


# ============================================================
# 6) KEYWORD ARGUMENTS
# ============================================================

# GOAL: show keyword args let you pass by NAME instead of position.
def describe_pet(animal, name):
    pass

# describe_pet("dog", "Luna")
# describe_pet(name="Luna", animal="dog")

# GOAL: show mixing positional then keyword.
# describe_pet("cat", name="Mochi")


# ============================================================
# 7) DEFAULT ARGUMENTS
# ============================================================

# GOAL: define a function with a default parameter value.
def show_tax(price, tax_rate=0.07):
    pass

# show_tax(100)
# show_tax(100, 0.08)

# GOAL: default for ALL params means you can call with none.
def greet_with_defaults(name="friend", punctuation="!"):
    pass

# greet_with_defaults()
# greet_with_defaults("Dominic")
# greet_with_defaults("Dominic", "!!!")
# greet_with_defaults(punctuation="??", name="Class")


# ============================================================
# 8) GLOBAL VARIABLES (WHY THEY’RE RISKY)
# ============================================================

# GOAL: show that globals can be read inside functions.
counter = 0

def show_counter():
    pass

# show_counter()

# GOAL: show that assigning to a global inside a function requires 'global'.
def increment_counter():
    pass

# increment_counter()
# show_counter()

# GOAL: show why globals are confusing.
def reset_counter():
    pass

# reset_counter()
# show_counter()


# ============================================================
# 9) GLOBAL CONSTANTS (OKAY USE)
# ============================================================

# GOAL: demonstrate a global constant.
SALES_TAX = 0.0

def show_sales_tax_on(price):
    pass

# show_sales_tax_on(50)


# ============================================================
# 10) VALUE-RETURNING FUNCTIONS
# ============================================================

# GOAL: write a function that doubles a number and RETURNS it.
def double(n):
    pass

# d = double(21)
# print(d)

# GOAL: show return values used directly in expressions.
# print(double(10) + double(5))


# ============================================================
# 11) RETURNING STRINGS
# ============================================================

# GOAL: return a string from a function.
def make_greeting(name):
    pass

# message = make_greeting("Dominic")
# print(message)


# ============================================================
# 12) BOOLEAN FUNCTIONS
# ============================================================

# GOAL: create a boolean function to test if a number is even.
def is_even(n):
    pass

# print(is_even(10))
# print(is_even(11))

# GOAL: show boolean return used in an if.
# num = 17
# if is_even(num):
#     pass
# else:
#     pass


# ============================================================
# 13) RETURNING MULTIPLE VALUES
# ============================================================

# GOAL: return multiple values.
def min_and_max(a, b, c):
    pass

# lo, hi = min_and_max(5, 100, 12)
# print(lo, hi)


# ============================================================
# 14) RETURNING None TO SIGNAL AN ERROR
# ============================================================

# GOAL: return None when an operation can’t be performed.
def safe_divide(num1, num2):
    pass

# print(safe_divide(10, 2))
# print(safe_divide(10, 0))


# ============================================================
# 15) THE pass KEYWORD
# ============================================================

# GOAL: show how pass lets you stub out a function.
def step1():
    pass

def step2():
    pass


# ============================================================
# 16) IMPORTING MODULES + DOT NOTATION (random)
# ============================================================

# GOAL: use the random module.
# import random

# Try:
# random.randint(...)
# random.random()
# random.uniform(...)
# random.seed(...)


# ============================================================
# 17) THE math MODULE
# ============================================================

# GOAL: use math module constants and functions.
# import math

# Try:
# math.pi
# math.sqrt(...)
# math.ceil(...)
# math.floor(...)
# math.radians(...)
# math.degrees(...)


# ============================================================
# 18) MINI “TOP-DOWN DESIGN” EXAMPLE
# ============================================================

# GOAL: show how functions divide a task.
def get_hours_worked():
    pass

def get_hourly_rate():
    pass

def calc_gross_pay(hours, rate):
    pass

def print_pay_stub(hours, rate, gross):
    pass


# ============================================================
# 19) MENU-DRIVEN PROGRAM
# ============================================================

# GOAL: show a simple menu program.
def menu_option_1():
    pass

def menu_option_2():
    pass

def menu_option_3():
    pass


# ============================================================
# 20) MODULES IDEA + __name__ == "__main__"
# ============================================================

# GOAL: show how to prevent "main code" from running when imported.
def main():
    pass

if __name__ == "__main__":
    main()