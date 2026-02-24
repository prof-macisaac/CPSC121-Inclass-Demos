# Local variable shadows global variable
x = 10

def shadow():
    x = 5
    print(x)

shadow()
print(x)


# Local variable does not exist outside function
def local_only():
    y = 42
    return y

local_only()
print(y)


# Function can read a global variable
message = "hello"

def read_global():
    print(message)

read_global()


# Assigning makes variable local (causes error)
count = 0

def bad_increment():
    count = count + 1

bad_increment()
print(count)

# Using global keyword to modify global variable
count = 0

def good_increment():
    global count
    count = count + 1

good_increment()
print(count)


# Function parameter is a local variable
n = 7

def parameter_demo(n):
    n = n + 1
    return n

parameter_demo(n)
print(n)


# Preferred design: return new value instead of using global
def increment(number):
    return number + 1

count = 0
count = increment(count)
count = increment(count)
print(count)


# Different functions can use the same variable name independently
x = 5

def first_function():
    x = 2
    print(x)

def second_function():
    print(x)

first_function()
second_function()
print(x)


# Multiple functions modifying shared global state
score = 0

def add_points(points):
    global score
    score = score + points

def reset_score():
    global score
    score = 0

add_points(10)
score
reset_score()
score