"""
CH06 Demo: Files + Exceptions
1) Exception handling basics
2) Files (write/read/append/loops/with)
3) File exception handling (missing file, bad data, etc.)
"""

# x = "ten"
# x_int = int(x)


""" 
=========== Exception Handling Basics ===========
A quick reminder: some errors crash your program (exceptions)
- Divide by zero (ZeroDivisionError)
- converting a value to another type (ValueError)

Try/Excepts allow us to handle these errors ourselves
instead of just crashing the program!

This gives us more control of how our program runs
and makes it more durable (less prone to crash)
"""

"""
Formats:
1) 
try:
    <code that could cause an error>

except <exception type>:
    <code to run if there was an error>

2)
try:
    <code that could cause an error>

except <exception type> as <variable name to store error>:
    <code to run if there was an error>

Exception Types: 
    - Exception (General Case!)
    - ZeroDivisionError
    - ValueError
    - TypeError
    - FileNotFoundError
    - etc
"""


x = 10
y = 0
try:
    print("about to divide...")
    z = x/y
    print(f"result: {z}")
except Exception:
    print("caught zero division error")

print("program continues")


user_number = None
result = -1
try:
    user_number = int(input("Enter a whole number: "))
    result = 10 / user_number
    print(abc)
except ValueError as err:
    print("Not a valid number")
except ZeroDivisionError:
    print("Not a valid denominator")
except Exception as err:
    print("Other error occurred")


print(f"User num is current = {user_number}")
print(result)



















"""
=========== Files ===========
Concept: programs can save data to a file (write) and load it later (read)

Basic file workflow:
1) open the file
2) do stuff with it (write/read)
3) close the file

File Modes:
- "w" : write (If the file exists, it DELETES ALL CONTENTS before writing!!)
- "a" : append (adds to the end of the file)
- "r" : read
"""

"""
--- Writing to a file (mode "w") ---
This will create the file if it doesn't exist.
If it DOES exist, it will erase it and start over. 
(Just by opening with "w" mode, will erase the content)
"""

"""
IMPORTANT IDEA: What is out_file?

When we do:
    out_file = open("demo_numbers.txt", "w")

Python creates a FILE OBJECT and stores it in the variable out_file.


Think of it like this:
- open(...) gives us a special tool
- that tool knows how to talk to the file
- we store that tool in a variable

So:

out_file  --> is NOT the file itself
out_file  --> is an object that represents a connection to the file

Objects have built-in abilities called METHODS.

Example:
    out_file.write("10\n")

Here:
- out_file is the object
- .write() is a method (a function attached to that object)
- the object knows HOW to write to the actual file


Those methods belong to the file object.

So mentally:

open(...) → gives us a file object
variable = file object
file_object.method() → tells the file to do something
"""






"""
--- Looping over a file (for line in file) ---
This is the most common way to process a file line-by-line.

Each 'line' is text.
BUT: int(...) can convert lines like "10\\n" because it ignores whitespace/newlines.
So we can do numeric processing without teaching string methods.
"""




"""
--- Using 'with open(...) as f:' ---
The 'with' statement automatically closes the file for you.
This is safer because the file still closes even if an error happens.
"""



"""
=========== File Exception Handling ===========
Two common problems when using files:

1) FileNotFoundError:
   - trying to open a file that doesn't exist

2) ValueError:
   - file exists, but the DATA inside isn't what we expected
   - example: we try to convert a line to int(...) but it's not a number

Goal: prevent our program from crashing and handle the problem gracefully.
"""


"""
--- Handling a missing file (FileNotFoundError) ---
If the file doesn't exist, open(...) crashes.
So we wrap it in a try/except.
"""




"""
--- Handling bad data inside a file (ValueError) ---
We'll create a file that has mostly numbers, but one "bad" line.
Then we'll try to convert each line using int(...).
When we hit the bad line, int(...) will cause a ValueError.
"""



"""
--- Combining file errors + data errors ---
In real programs, both could happen:
- file might not exist
- file might exist but contain bad data

So we can catch BOTH.
"""
