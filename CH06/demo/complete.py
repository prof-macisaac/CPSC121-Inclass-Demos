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
# x = 10/0

# user_input = "ten"
# user_val = int(user_input)

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
    print("About to divide...")
    result = x / y
    print("Result:", result)  # this line is skipped if exception happens above
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: you cannot divide by 0.")

print("Program keeps going after try/except.")

user_number = None

try:
    user_number = int(input("Enter a whole number: "))
    print("You typed:", user_number)
except ValueError:
    print("Caught a ValueError: that input was not a whole number.")

print("user_number is currently:", user_number)

# --- Capturing the exception message (as err) ---
print("\nWe can capture the default error message using: except SomeError as err\n")

try:
    weird = int(input("Enter a whole number (try typing something like 3.14): "))
    print("Converted:", weird)
except ValueError as err:
    print("Caught ValueError as err.")
    print("Default message from Python:", err)

# --- General Exception Handling ---

try:
    number = int(input("Enter a whole number: "))
    result = 100 / number

    print("Result:", result)
except Exception as err:
    print("An exception occurred.")
    print("Error type:", type(err))
    print("Error message:", err)

# --- Multiple except clauses ---
print("\nMultiple exceptions can happen; we can catch different ones.\n")

a = 10

try:
    b = int(input("Enter a divisor (whole number): "))
    print(f"b is {b}")
    print(f"a / b ={a / b}")
except ValueError:
    print("That wasn't a whole number.")
except ZeroDivisionError:
    print("You entered 0; division by zero is not allowed.")

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

out_file = open("demo_numbers.txt", "w")
out_file.write("10\n")
out_file.write("20\n")
out_file.write("30\n")
out_file.close()

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
--- Appending to a file (mode "a") ---
This keeps the file and adds to the end.
"""

out_file = open("demo_numbers.txt", "a")
out_file.write("40\n")
out_file.close()

print("Appended to demo_numbers.txt using mode 'a'.")


"""
--- Reading a whole file at once (.read()) ---
.read() gives you the entire file contents as ONE value.

repr(...) helps us SEE hidden characters like \n.
"""

in_file = open("demo_numbers.txt", "r")
contents = in_file.read()
in_file.close()

print("\nContents of demo_numbers.txt using .read():")
print(contents)
print(repr(contents))


"""
--- Reading one line at a time (.readline()) ---
.readline() returns ONE line each time you call it.
Lines usually include the newline character at the end.
"""

in_file = open("demo_numbers.txt", "r")

line1 = in_file.readline()
line2 = in_file.readline()

in_file.close()

print("line1 printed normally:")
print(line1)

print("line1 using repr(...) so we can see the newline:")
print(repr(line1))

print("\nline2 printed normally:")
print(line2)

print("line2 using repr(...):")
print(repr(line2))


print(f"{line1} is the first number")
line1_updated = line1.strip()
print(f"{line1_updated} is the first number")

"""
--- Looping over a file (for line in file) ---
This is the most common way to process a file line-by-line.

Each 'line' is text.
BUT: int(...) can convert lines like "10\\n" because it ignores whitespace/newlines.
So we can do numeric processing without teaching string methods.
"""

total = 0

in_file = open("demo_numbers.txt", "r")

for line in in_file:
    value = int(line)
    total += value
    print(f"Read value = {value}, running total = {total}")

in_file.close()

print(f"\nFinal total from demo_numbers.txt = {total}")


"""
--- Using 'with open(...) as f:' ---
The 'with' statement automatically closes the file for you.
This is safer because the file still closes even if an error happens.
"""

with open("demo_numbers_with.txt", "w") as f:
    f.write("1\n")
    f.write("2\n")
    f.write("3\n")

print("Wrote demo_numbers_with.txt using 'with' (auto-close).")

with open("demo_numbers_with.txt", "r") as f:
    for line in f:
        print("Line from demo_numbers_with.txt:", repr(line))


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

try:
    f = open("this_file_probably_does_not_exist.txt", "r")
    data = f.read()
    f.close()
    print("Somehow the file existed! Here is the data:")
    print(data)
except FileNotFoundError:
    print("\nCaught FileNotFoundError: that file was not found.")


"""
--- Handling bad data inside a file (ValueError) ---
We'll create a file that has mostly numbers, but one "bad" line.
Then we'll try to convert each line using int(...).
When we hit the bad line, int(...) will cause a ValueError.
"""

with open("demo_mixed_data.txt", "w") as f:
    f.write("100\n")
    f.write("200\n")
    f.write("oops\n")   # this will cause int(...) to fail
    f.write("300\n")

total = 0

try:
    with open("demo_mixed_data.txt", "r") as f:
        for line in f:
            value = int(line)     # crashes on "oops\n"
            total += value
            print(f"Read value = {value}, running total = {total}")

except ValueError as err:
    print("\nCaught ValueError: a line was not a valid whole number.")
    print("Error message:", err)



"""
--- Combining file errors + data errors ---
In real programs, both could happen:
- file might not exist
- file might exist but contain bad data

So we can catch BOTH.
"""

total = 0

try:
    with open("demo_mixed_data.txt", "r") as f:
        for line in f:
            total += int(line)

    print("\nTotal computed successfully =", total)

except FileNotFoundError:
    print("\nThat file doesn't exist.")
except ValueError:
    print("\nThat file exists, but it contains non-numeric data.")

print("\nEnd of CH06 demo.")