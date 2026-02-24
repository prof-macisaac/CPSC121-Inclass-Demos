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

# ============================================================
# 1) VOID FUNCTIONS (DO SOMETHING, RETURN NOTHING)
# ============================================================




# ============================================================
# 2) PARAMETERS + ARGUMENTS
# ============================================================


# ============================================================
# 3) MULTIPLE PARAMETERS (POSITION MATTERS)
# ============================================================


# ============================================================
# 4) LOCAL VARIABLES + SCOPE
# ============================================================



# ============================================================
# 5) PASSING ARGUMENTS
# ============================================================



# ============================================================
# 6) VALUE-RETURNING FUNCTIONS (RETURNING A NUMBER)
# ============================================================

# ============================================================
# 7) RETURNING STRINGS
# ============================================================

# ============================================================
# 8) BOOLEAN FUNCTIONS (RETURN True/False)
# ============================================================



# ============================================================
# GPH: Main Functions
# ============================================================



# ============================================================
# GPH: Function Headers
# ============================================================



def calculate_letter_grade(score, is_extra_credit):
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



# ============================================================
# THE pass KEYWORD (PLACEHOLDER WHILE DESIGNING)
# ============================================================



# ============================================================
# IMPORTING MODULES + DOT NOTATION (random)
# ============================================================


# ============================================================
# THE math MODULE
# ============================================================



# ============================================================
# MINI “TOP-DOWN DESIGN” EXAMPLE (PUTTING IT TOGETHER)
# ============================================================





# ============================================================
# DEFAULT ARGUMENTS
# ============================================================

