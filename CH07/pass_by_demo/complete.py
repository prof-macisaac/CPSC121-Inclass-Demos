"""
CH07 Demo: Lists and Tuples in Functions
1) Pass by object reference
2) Mutating a list inside a function
3) Rebinding a list parameter inside a function
4) Tuples in functions
5) Mutable object inside a tuple
"""

"""
=========== Big Idea ===========
Python uses pass by object reference.

That means:
- the function gets access to the same object
- if the function MUTATES a mutable object like a list,
  the original object changes too
- if the function REBINDS the parameter to a new object,
  the caller does NOT change

For immutable objects like tuples:
- you cannot change the tuple in place
- if you do something like t = (...), you are just making
  the parameter name refer to a new object
"""

"""
=========== Example 1: Mutating a List ===========
Lists are mutable.

So if a function changes a list element or uses append/remove,
the original list changes too.
"""

def change_first_value(num_list):
    print(f"Inside function, before change: {num_list}")
    num_list[0] = 999
    print(f"Inside function, after change: {num_list}")

numbers = [10, 20, 30]

print(f"Before function call: {numbers}")
change_first_value(numbers)
print(f"After function call: {numbers}")

# --- Mini Task ---
# Change the function so that it updates index 1 instead of index 0.
# Then run it again and see what changes.


"""
=========== Example 2: Appending to a List ===========
append mutates the existing list object.
That means the caller sees the change too.
"""

def add_score(score_list):
    print(f"Inside function, before append: {score_list}")
    score_list.append(100)
    print(f"Inside function, after append: {score_list}")

scores = [88, 92, 79]

print(f"\nBefore function call: {scores}")
add_score(scores)
print(f"After function call: {scores}")

# --- Mini Task ---
# Write a function that removes one item from a list using pop().
# Call it with a test list.


"""
=========== Example 3: Rebinding a List Parameter ===========
Watch out:
If we do something like this inside the function:

num_list = [1, 2, 3]

that does NOT change the caller's list.
It only makes the local parameter name refer to a new list.
"""

def rebind_list(num_list):
    print(f"Inside function, at start: {num_list}")
    num_list = [1, 2, 3]
    print(f"Inside function, after rebinding: {num_list}")

values = [50, 60, 70]

print(f"\nBefore function call: {values}")
rebind_list(values)
print(f"After function call: {values}")

# --- Mini Task ---
# Change the function so it rebinds num_list to ["a", "b", "c"].
# Does the original list outside the function change?


"""
=========== Example 4: Mutating vs Rebinding ===========
These two ideas are VERY different.

Mutating:
- changes the object itself

Rebinding:
- changes what the local variable refers to
"""

def mutate_list(data):
    data[0] = -1

def rebind_list_again(data):
    data = [-1, -2, -3]

list_a = [5, 10, 15]
list_b = [5, 10, 15]

print(f"\nBefore mutate_list: {list_a}")
mutate_list(list_a)
print(f"After mutate_list: {list_a}")

print(f"\nBefore rebind_list_again: {list_b}")
rebind_list_again(list_b)
print(f"After rebind_list_again: {list_b}")

# --- Mini Task ---
# Add a print statement inside each function so you can compare
# what the list looks like inside the function vs outside.


"""
=========== Example 5: Tuples in Functions ===========
Tuples are immutable.

So a function cannot change the tuple in place.
"""

def try_to_change_tuple(my_tuple):
    print(f"Inside function, got tuple: {my_tuple}")

    # This would crash if uncommented:
    # my_tuple[0] = 999

    print("Cannot do my_tuple[0] = 999 because tuples are immutable.")

coords = (3, 7)

print(f"\nBefore function call: {coords}")
try_to_change_tuple(coords)
print(f"After function call: {coords}")

# --- Mini Task ---
# Uncomment the line inside the function that tries to change the tuple.
# Run it and observe the error, then comment it back out.


"""
=========== Example 6: Rebinding a Tuple Parameter ===========
Even though tuples cannot be changed,
a function can rebind its local parameter to a new tuple.

But again: that does NOT affect the caller.
"""

def rebind_tuple(my_tuple):
    print(f"Inside function, at start: {my_tuple}")
    my_tuple = (100, 200, 300)
    print(f"Inside function, after rebinding: {my_tuple}")

point = (1, 2)

print(f"\nBefore function call: {point}")
rebind_tuple(point)
print(f"After function call: {point}")

# --- Mini Task ---
# Change the new tuple inside the function to ("x", "y").
# Does the original tuple outside the function change?


"""
=========== Example 7: Returning a New Tuple ===========
Because tuples are immutable, if we want a different tuple,
we usually return a new one.
"""

def make_new_tuple(old_tuple):
    new_tuple = (old_tuple[0] * 10, old_tuple[1] * 10)
    return new_tuple

point1 = (2, 4)

print(f"\nOriginal tuple: {point1}")

point2 = make_new_tuple(point1)

print(f"Returned tuple: {point2}")
print(f"Original tuple after function call: {point1}")

# --- Mini Task ---
# Write a function that takes a 3-item tuple of numbers
# and returns a new tuple with each value doubled.


"""
=========== Example 8: Mutable Object Inside a Tuple ===========
A tuple itself is immutable,
but it can store a mutable object like a list.

That means the list INSIDE can still change.
"""

def add_to_inner_list(my_tuple):
    print(f"Inside function, before append: {my_tuple}")
    my_tuple[2].append("new item")
    print(f"Inside function, after append: {my_tuple}")

bundle = ("Dom", 25, ["pencil", "notebook"])

print(f"\nBefore function call: {bundle}")
add_to_inner_list(bundle)
print(f"After function call: {bundle}")

# --- Mini Task ---
# Make a tuple with:
# - a string
# - a number
# - a list
# Write a function that appends to the list inside the tuple.


"""
=========== Example 9: Comparing List and Tuple Behavior ===========
Lists:
- mutable
- can be changed in place inside a function

Tuples:
- immutable
- cannot be changed in place inside a function
- usually need to return a new tuple if you want different values
"""

def add_item_to_list(items):
    items.append("added")

def try_to_add_item_to_tuple(items):
    items = items + ("added",)
    print(f"Inside function, tuple became: {items}")

my_list = ["a", "b"]
my_tuple = ("a", "b")

print(f"\nBefore list function: {my_list}")
add_item_to_list(my_list)
print(f"After list function: {my_list}")

print(f"\nBefore tuple function: {my_tuple}")
try_to_add_item_to_tuple(my_tuple)
print(f"After tuple function: {my_tuple}")

# --- Mini Task ---
# Predict the output before running this section.
# Which one changes outside the function, and why?


"""
=========== Key Takeaways ===========
1) Functions receive references to objects
2) If the object is mutable (like a list), mutations affect the caller
3) Rebinding a parameter does not affect the caller
4) Tuples are immutable, so they cannot be changed in place
5) A tuple can still contain a mutable object, and that inner object can change
"""
