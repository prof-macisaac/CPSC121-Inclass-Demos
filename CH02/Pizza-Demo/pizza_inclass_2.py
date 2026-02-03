"""
Goal: Based on how many people are eating, how many pizzas are ordered, and how many slices are in a pizza, give the amount of full slices per person and how many are left over.

- Assume slices per pizza is a constant and amount of people eating and amount of pizzas ordered will be supplied by the user of the program.

Additional Goal: Based on the cost of each pizza, how much should each person be charged? 
"""

SLICES_PER_ZA = 8

amt_eating = int(input("How are people are eating pizza? "))

amt_pizzas = int(input("How pizzas were ordered? "))

total_slices = SLICES_PER_ZA * amt_pizzas

slices_per_person = total_slices // amt_eating
slices_leftover = total_slices % amt_eating

print(f"Each person gets {slices_per_person} slices")
print(f"There will be {slices_leftover} slices leftover")



