"""
error_demo.py
"""

print("=== Python Error Demo ===")

# --------------------------------------------------
# 1. SyntaxError
# Happens when Python can't even understand the code
# (missing colon, bad indentation, etc.)
# --------------------------------------------------

# Uncomment to see:
if True:
    print("Hello")

# --------------------------------------------------
# 2. NameError
# Using a variable that has not been defined
# --------------------------------------------------

# Uncomment to see:
scoer = 10
print(scoer)

# --------------------------------------------------
# 3. TypeError
# Doing an operation on incompatible types
# --------------------------------------------------

# Uncomment to see:
age = "20"
print(age + "1")

# --------------------------------------------------
# 4. ValueError
# Correct type, but invalid value
# --------------------------------------------------

# Uncomment to see:
user_input = "12"
number = int(user_input)
print(number)



# --------------------------------------------------
# 5. Logical Error (NO exception raised)
# Program runs, but result is wrong
# --------------------------------------------------

score = 85

# Intent: check if student passed (>= 60)
if score > 90:
    print("Passed")
else:
    print("Failed (but this logic is wrong!)")

# print("=== End of Demo ===")
