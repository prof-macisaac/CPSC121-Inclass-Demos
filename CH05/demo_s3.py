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
# GPH: Main Functions
# ============================================================
def print_plus_one(x):
    print(x+1)

def main():
    x = int(input("enter your age"))
    print_plus_one(x)
    x += 1
    print(f"next year you will be {x}")

# main()

# ============================================================
# GPH: Function Docstrings
# ============================================================

def calculate_area(radius):
    """
    Calculates the area of a circle

    Parameters:
        radius (float): radius of a circle
    Returns:
        float: the area of the circle
    """
    return 3.14 * radius ** 2

print(calculate_area(10))




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
        str: The final letter grade ("A", "B", "C", "D", or "F")

        or None if score is invalid

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
# DEFAULT ARGUMENTS
# ============================================================

