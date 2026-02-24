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


# ============================================================
# 1) VOID FUNCTIONS (DO SOMETHING, RETURN NOTHING)
# print()
# ============================================================
def say_hello():
    print("Hello from say_hello()")

say_hello()
say_hello()


# ============================================================
# 2) PARAMETERS + ARGUMENTS
# ============================================================
def greet_name(name):
    print(f"Hello, {name}")

greet_name("John")
greet_name("Sarah")
n = "Sam"
greet_name(n)

def print_one_more(num):
    print(num + 1)

print_one_more(22.2)

# ============================================================
# 3) MULTIPLE PARAMETERS (POSITION MATTERS)
# ============================================================
def add_and_print(a, b):
    print(f"a is {a}, b is {b}, sum is {a + b}")

x = 10
add_and_print(x, 25)
add_and_print(25, x)

def print_repeat(statement, times):
    """
    print out the statement times amount times
    """
    # for i in range(times):
    #     print(statement)
    while times > 0:
        print(statement)
        times -= 1

# print_repeat("Hello again", 3)
# print_repeat(3, "Hello again")

result = print_repeat("Hello",3)
print(result)

# ============================================================
# 4) LOCAL VARIABLES + SCOPE
# ============================================================

def local_scope_demo():
    star = 82
    print(f"inside the function, star is {star}")

def local_2():
    star = 92
    print(f"local 2 : {star}")

star = 72
local_scope_demo()
local_2()
print(star)

# ============================================================
# 5) PASSING ARGUMENTS
# ============================================================
def change_me(n):
    n = 0

value = 99
change_me(value)
print(value)


# ============================================================
# 6) VALUE-RETURNING FUNCTIONS (RETURNING A NUMBER)

# input()
# s = input()
# ============================================================
def double(n):
    return n * 2
   

d = double(21)
print(d)
# x = float(input("Enter a value: "))

# print(double(float(input("Enter a value: "))))


# ============================================================
# 7) RETURNING STRINGS
# ============================================================
def make_greeting(name):
    s = f"Hello, {name}"
    return s

message = make_greeting("Sam")
print(message)
# ============================================================
# 8) BOOLEAN FUNCTIONS (RETURN True/False)
# ============================================================
def is_even(n):
    return n % 2 == 0


num = 17
if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")
# ============================================================
# 9) Main Function
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

