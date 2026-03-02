"""Files and Exceptions"""
# Writing data to a file
# outfile = open("pets.txt", "w")

# outfile.write("Bella\n")
# outfile.write("Max\n")
# outfile.write("Luna\n")
# outfile.close()

# # # Reading data back
# infile = open("pets.txt", "r")
# x = infile.read()
# # print(x)
# infile.close()

# # # # Appending new data to a file
# x = open("pets.txt", "a")
# x.write("Charlie\n")
# # x.close()

# with open("pets.txt", "a") as x:
#     x.write("Charlie\n")



# # # # Reading line-by-lines
# with open("pets.txt", "r") as infile:
#     i = 0
#     for line in infile:
#         i+= 1
#         print(f"{i}: {line.rstrip()}")

#     print(f"there are {i} pet")

# Counting the number of pets in the file
# count = 0
# with open("pets.txt", "r") as infile:
#     for _ in infile:
#         count += 1
# print(f"There are {count} pets in the file.")

# # # Writing numbers to a file
# with open("numbers.txt", "w") as num_file:
#     for i in range(1, 6):
#         num_file.write(str(i) + "\n")

# # # # Reading and summing
# total = 0
# with open("numbers.txt", "r") as num_file:
#     for line in num_file:
#         total += int(line)
# print("Total of numbers:", total)

# # # Simulating a small record file
# out = open("students.csv", "w")
# out.write("Alice,90\n")
# out.write("Bob,78\n")
# out.write("Carmen,88\n")
# out.close()

# with open("students.csv", "w") as out:
#     out.write("Alice,90\n")
#     out.write("Bob,78\n")
#     out.write("Carmen,88\n")

# try:
#     x = 5/0
#     with open("missing.txt", "r") as infile:
#         print(infile.read())
# except ValueError as err:
#     print("Error:", err)
# except:
#     print("oh no!")
# # except FileNotFoundError:
# #     print("Cant find that file!")

# print("code continues")

# try:
#     value = int("abc")
# except ValueError as err:
#     print("Conversion failed:", err)
# else:
#     print("Conversion succeeded.")
# finally:
#     print("Program complete.")

try:
    # x = int("abc")
    # x = 5/0
    file1 = open("missing.txt", "r")
except ZeroDivisionError:
    print("that can't be the denominator")
except FileNotFoundError as x:
    print(x)
    print("that file does not exist")
    opened_file = False
except:
    print("error")
else:
    print("all good")
    opened_file = True
# finally:
#     print("do this no matter what")

print("THIS IS THE END OF THE FILE")