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


# --- Mini Task ---
# Change the function so that it updates index 1 instead of index 0.
# Then run it again and see what changes.


"""
=========== Example 2: Appending to a List ===========
append mutates the existing list object.
That means the caller sees the change too.
"""


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


# --- Mini Task ---
# Add a print statement inside each function so you can compare
# what the list looks like inside the function vs outside.


"""
=========== Example 5: Tuples in Functions ===========
Tuples are immutable.

So a function cannot change the tuple in place.
"""



# --- Mini Task ---
# Uncomment the line inside the function that tries to change the tuple.
# Run it and observe the error, then comment it back out.


"""
=========== Example 6: Rebinding a Tuple Parameter ===========
Even though tuples cannot be changed,
a function can rebind its local parameter to a new tuple.

But again: that does NOT affect the caller.
"""


# --- Mini Task ---
# Change the new tuple inside the function to ("x", "y").
# Does the original tuple outside the function change?


"""
=========== Example 7: Returning a New Tuple ===========
Because tuples are immutable, if we want a different tuple,
we usually return a new one.
"""


# --- Mini Task ---
# Write a function that takes a 3-item tuple of numbers
# and returns a new tuple with each value doubled.


"""
=========== Example 8: Mutable Object Inside a Tuple ===========
A tuple itself is immutable,
but it can store a mutable object like a list.

That means the list INSIDE can still change.
"""



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
