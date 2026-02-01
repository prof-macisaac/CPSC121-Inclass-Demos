# sentinel total loop with break
# the user can enter any amount of positive numbers and they will be added together
# SENTINEL = -1
# total = 0 # accumulator
# while True:
#     user_val = int(input("Enter a number (-1 to stop): "))
#     if user_val == SENTINEL:
#         break
#     total += user_val

# print(f"the total is {total}")

# ranged input validation

# score = int(input("Enter a score (0 to 100 inclusive): "))
# while score < 0 or score > 100:
#     print("That score is not valid")
#     score = int(input("Enter a score (0 to 100 inclusive): "))

# nested loop with multiple assignment

# rows, cols = 3, 3

# for row in range(1, 4):
#     for col in range(1, cols + 1):
#         print(f"[row: {row}, col: {col}]", end= " ")
#     print()


# loop with modulus continue statement

# for i in range(1,11):
#     if i % 3 == 0:
#         continue 
#     print(i)

# integer division and modulus pizza example

total_slices = 8
amount_people = 3

slices_per_person = total_slices//amount_people
print(f"slices per person: {slices_per_person}")


# activity 1 answer