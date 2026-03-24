"""
CH06 Demo: Files + Exceptions
1) Exception handling basics
2) Files (write/read/append/loops/with)
3) File exception handling (missing file, bad data, etc.)
"""



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
# x = 10
# y = 0
# # print(x/y)

# try: 
#     user_num = int(input("Enter a number: "))
# except:
#     user_num = 0

# print(user_num)





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

# x = 10
# y = 0
# error_occur = False
# try:
#     print("About to divide...")
#     y = int(input("Give a denominator"))
#     result = x/y
#     print(f"Result {result}")
# except ZeroDivisionError:
#     print("Cannot divide by zero!!")
#     error_occur = True
# except ValueError:
#     print("That is not a valid integer")
#     error_occur = True
# except:
#     print("Unknown error occurred")
#     error_occur = True

# if not error_occur:
#     print("division successful!")


# print("Program continues")

def int_input(prompt, error_msg = "Not a valid integer"):
    while True:
        try:
            user_val = input(prompt)
            num = int(user_val)
            return num
        except ValueError:
            print(error_msg)


# x = int_input("Give an integer: ")
# print(x)

def float_input(prompt, error_msg = "Not a valid floating point number"):
    while True:
        num = None
        try:
            num = float(input(prompt))
        except ValueError:
            print(error_msg)

        if num != None:
            return num

# float_val_from_user = float_input("Enter a floating point number")
# float_val_from_user2 = float_input("Enter a floating point number", "that is not the correct floating point number format")

def safe_division(num, denom, error_val = 0):
    try:
        result = num/denom
        return result
    except:
        return error_val
    
# print(safe_division(10, 0, -4))
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
outfile = open("demo_nums.txt", "w")

outfile.write("10\n")
outfile.write("20\n")
outfile.write("30\n")

outfile.close()


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

outfile = open("demo_nums.txt", "a")
outfile.write("abc\n")
outfile.write("40\n")
outfile.close()


# # Reading a whole file at once!
# # .read()

infile = open("demo_nums.txt", "r")
content = infile.read()
infile.close()

print(content)
print(repr(content))


# reading one line at a time
# .readline()
# try:
#     infile = open("demo_nums-4.txt", "r")
# except FileNotFoundError:
#     print("file does not exist")
#     exit()

# x = infile.readline()
# y = infile.readline()

# infile.close()
# print(x)
# print(y)

# print(repr(x))
# print(repr(y))

# x = x.strip()
# y = y.strip()
# print(repr(x))

# print(x)
# print(y)

"""
--- Looping over a file (for line in file) ---
This is the most common way to process a file line-by-line.

Each 'line' is text.
BUT: int(...) can convert lines like "10\\n" because it ignores whitespace/newlines.
So we can do numeric processing without teaching string methods.
"""
total = 0
infile = open("demo_nums.txt", "r")

for x in infile:
    print(x.strip())
    try:
        total += int(x)
    except ValueError:
        print("skipping value")

print(total)
infile.close()




"""
--- Using 'with open(...) as f:' ---
The 'with' statement automatically closes the file for you.
This is safer because the file still closes even if an error happens.
"""
# with open("demo_nums.txt", "r") as infile:
#     print(infile.readline())


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
# try:
#     infile = open("doesn't exist.txt", "r")
#     print(infile.read())
# except FileNotFoundError:
#     print("that file does not exist!")

"""
--- Handling a missing file (FileNotFoundError) ---
If the file doesn't exist, open(...) crashes.
So we wrap it in a try/except.
"""
# total = 0
# try:
#     with open("demo_nums.txt", "r") as infile:
#         for line in infile:
#             line_strip = line.strip()
#             print(line_strip)
#             total += int(line_strip)
# except ValueError:
#     print("caught error while reading file")

# print(total)


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
