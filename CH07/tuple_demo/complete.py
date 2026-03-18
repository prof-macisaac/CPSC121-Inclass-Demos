"""
CH07 Demo: Tuples
1) What is a tuple?
2) Tuple indexing
3) Tuples vs lists
4) Immutability
5) Tuple functions
6) Tuples containing mutable objects
"""

"""
=========== What is a Tuple ===========
A TUPLE is a sequence similar to a list.

BUT: tuples are IMMUTABLE.

Format:
tuple_name = (item1, item2, item3)
"""

# --- Mini Task ---
# Create a tuple called days with 3 days of the week.
# Print the whole tuple.


"""
=========== Tuple Indexing ===========
Just like lists, tuples use indexes.
"""

# --- Mini Task ---
# Print the first and second values from your days tuple.


"""
=========== len() with Tuples ===========
Many list operations work with tuples too.
"""


# --- Mini Task ---
# Create a tuple of 4 numbers.
# Print its length, min, and max.


"""
=========== Tuple Iteration ===========
We can loop through tuples too.
"""


# --- Mini Task ---
# Write an index-based loop for your days tuple.


"""
=========== Tuples are IMMUTABLE ===========
We CANNOT modify tuple elements.

The following would cause an error if uncommented.
"""


# --- Mini Task ---
# Try  a line like:
# days[0] = "Friday"
# Run it and see what error you get.
# Then comment it back out.


"""
=========== Why Use Tuples? ===========
1) They are safer when data should not change
2) They are often used for fixed collections of values
"""


# --- Mini Task ---
# Make a tuple called location with two numbers.
# Print each value separately using indexes.


"""
=========== Tuple Membership ===========
We can check values using 'in'
"""


# --- Mini Task ---
# Check whether one of your days is in the days tuple.
# Then check a day that is not in it.


"""
=========== Converting Between Lists and Tuples ===========
We can convert:
- list -> tuple
- tuple -> list
"""


# --- Mini Task ---
# Make a list of 3 favorite movies.
# Convert it to a tuple and print it.


"""
=========== Tuples with Mutable Objects ===========
Tuples themselves cannot change,
but they can contain mutable objects like lists.
"""



# --- Mini Task ---
# Create a tuple that contains a string, a number, and a list.
# Append something to the list inside the tuple.
# Print the tuple before and after.
