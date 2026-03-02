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
if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# ============================================================
# GPH: Main Functions
# ============================================================


def x_2(x):
    return x + 1

def print2(x):
    print(x_2(x))

def main():
    print2(110)
    print("this is main")

main()
# ============================================================
# GPH: Function Docstrings
# ============================================================

def calculate_area(radius):
    """
    Calculate the area of a circle

    Parameters:
        radius (float): radius of a circle
    
    Returns:
        float: the area of the circle
    """
    return 3.14 * radius ** 2

print(calculate_area(10))

def calculate_letter_grade(score, is_extra_credit):
    """
    determine the final letter grade for a student

    if extra credit is True, 5 points are added to the score. 

    Letter grades are assigned using a 10-point scale

    Parameters:
        score (float): student's exam score (0-100)
        is_extra_credit (bool): whether extra credit should be applied

    Returns:
        str: final letter grade  (A,B,C,D, F)
    """
    if score < 0 or score > 100:
        return None

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
def add_sub(a, b):
    added = a + b
    subtracted = a - b
    return added, subtracted

x, y = add_sub(10, 3)
print(x)
print(y)


# ============================================================
# THE pass KEYWORD (PLACEHOLDER WHILE DESIGNING)
# ============================================================



# ============================================================
# IMPORTING MODULES + DOT NOTATION (random)
# ============================================================


# ============================================================
# THE math MODULE
# ============================================================

# https://docs.python.org/3/library/math.html


# ============================================================
# MINI “TOP-DOWN DESIGN” EXAMPLE (PUTTING IT TOGETHER)
# ============================================================





# ============================================================
# DEFAULT ARGUMENTS
# ============================================================

