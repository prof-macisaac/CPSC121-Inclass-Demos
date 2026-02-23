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
def hi():
    print("Hello from the hi function!")

hi()
hi()
# ============================================================
# 1) VOID FUNCTIONS (DO SOMETHING, RETURN NOTHING)
# ============================================================


# print() -> None
# input() -> String
result = print("Hello")
print(result)

# ============================================================
# 2) PARAMETERS + ARGUMENTS
# ============================================================


def greet_name(name):
    print(f"Hello {name}!")

greet_name("John")
name = "Sarah"
greet_name(name)

def print_one_more(num):
    print(num + 1)

print_one_more(10)
print_one_more(10 + 3)
# ============================================================
# 3) MULTIPLE PARAMETERS (POSITION MATTERS)
# ============================================================
def add_and_print(a, b):
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"the sum is {a + b}")

x = 25
add_and_print(x, 10)
add_and_print(10, x)

def print_repeat(statement, times):
    """
    takes a statement and prints it out times amount of times
    """
    for _ in range(times):
        print(statement)

print_repeat("hello from repeat", 3)



# ============================================================
# 4) LOCAL VARIABLES + SCOPE
# ============================================================
def local_scope_demo():
    xyz = 10
    print(f"inside the function x is {xyz}")
xyz = 33
local_scope_demo()
print(xyz)

# ============================================================
# 5) PASSING ARGUMENTS
# ============================================================
def change_me(n):
    n = 5

n = 99
change_me(n)
print(n)


# ============================================================
# 6) VALUE-RETURNING FUNCTIONS (RETURNING A NUMBER)
# ============================================================
def double(n):
    db = n * 2
    return db
 
x = 10
num = double(x)
print(num)
# print(double(float(input("Enter a value to double "))))

# ============================================================
# 7) RETURNING STRINGS
# ============================================================
def make_greeting(name):
    s =  f"Hello, {name}"
    return s

greeting = make_greeting("John")
print(greeting)
# ============================================================
# 8) BOOLEAN FUNCTIONS (RETURN True/False)
# ============================================================
def is_even(n):
    return n % 2 == 0
num = 17
if is_even(n):
    print(f"{num} is even")
else:
    print(f"{num} is odd")
# ============================================================
# 9) MODULES IDEA 
# ============================================================




# ============================================================
# 10) RETURNING MULTIPLE VALUES
# ============================================================


# ============================================================
# 11) RETURNING None TO SIGNAL AN ERROR
# ============================================================


# ============================================================
# 12) THE pass KEYWORD (PLACEHOLDER WHILE DESIGNING)
# ============================================================



# ============================================================
# 13) IMPORTING MODULES + DOT NOTATION (random)
# ============================================================



# ============================================================
# 14) THE math MODULE
# ============================================================



# ============================================================
# 15) MINI “TOP-DOWN DESIGN” EXAMPLE (PUTTING IT TOGETHER)
# ============================================================



# ============================================================
# 16) MENU-DRIVEN PROGRAM (LOOP + FUNCTIONS)
# ============================================================


# ============================================================
# 17) KEYWORD ARGUMENTS
# ============================================================



# ============================================================
# 18) DEFAULT ARGUMENTS
# ============================================================




# ============================================================
# 19) GLOBAL VARIABLES (WHY THEY’RE RISKY)
# ============================================================




# ============================================================
# 20) GLOBAL CONSTANTS (OKAY USE)
# ============================================================

