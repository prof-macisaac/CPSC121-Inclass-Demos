# SENTINEL = -1
# print(f"Enter integers to add. Type {SENTINEL} to finish.")

# total = 0 # accumulator

# while True:
#     score = int(input("integer: "))
#     if score == SENTINEL:
#         break
#     total += score

# print(f"Total: {total}")


# score = int(input("enter a score (0-100): "))
# while score < 0 or score > 100:
#     print(f"{score} is invalid!")
#     score = int(input("enter a score (0-100): "))

# print(f"Score accepted! ({score})")

rows, cols = 3, 4
print(cols)
for row in range(1, rows+1): # rows
    for col in range (1, cols+1): # cols
        print(f"[row: {row}, col: {col}]", end=" ")
    print()

# for num in range(1,11):
#     if num % 3 == 0:
#         continue
#     print(num)


people_count = int(input("How many people are eating pizza: "))
pizza_count = int(input("How many pizzas were ordered: "))
slices_per_pie = 8

total_slices = pizza_count * slices_per_pie
slices_per_person = total_slices // people_count
leftover_slices = total_slices % people_count
print(f"Each person gets {slices_per_person} and there will be {leftover_slices} slices leftover.")


# sentinel total loop with break

# ranged input validation

# nested loop with multiple assignment

# loop with modulus continue statement

# integer division and modulus pizza example


# activity 1 answer