# sentinel total loop with break

# add numbers the user enters
# use a sentinel to note when to stop taking input

# total = 0 # accumulator 
# while True:
#     input_number = int(input("enter a number (enter -1 to end): "))
#     if input_number == -1:
#         break
#     total += input_number

# print(f"your total is {total}")

# ranged input validation

# score = int(input("enter a score (0-100 inclusive): "))
# while score < 0 or score > 100: 
#     print("Score not valid")
#     score = int(input("enter a score (0-100 inclusive): "))

# print(f"score is {score}")

# nested loop with multiple assignment
# rows, cols = 2, 3
# for row in range(1,rows + 1):
#     for col in range(1, cols + 1):
#         print(f"[row: {row}, col: {col}]")
#     print()

# loop with modulus continue statement
# for i in range(1,11):
#     if i % 3 == 0:
#         continue
#     print(i)

# integer division and modulus pizza example
slices_per_pizza = 8
amount_people = int(input("How many are people are eating? "))
amount_pizzas = int(input("How many pizzas are you ordering? "))
# how many full slices does each person get
total_amt_slices = amount_pizzas * slices_per_pizza

slices_per_person = total_amt_slices//amount_people

print(f"Each person gets {slices_per_person} slices")
# how many leftover slices will there be
remaining_slices = total_amt_slices % amount_people
print(f"there will be {remaining_slices} leftover")

# activity 1 answer

