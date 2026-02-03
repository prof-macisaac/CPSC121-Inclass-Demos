"""
Goal: Based on how many people are eating, how many pizzas are ordered, and how many slices are in a pizza, give the amount of full slices per person and how many are left over.


- Assume slices per pizza is a hard-coded constant and amount of people eating and amount of pizzas ordered will be supplied by the user of the program.

Additional Goal: Based on the cost of each pizza, how much should each person be charged? 

"""
SLICES_PER_ZA = 8
# input: amount of people, amount of pizzas
amt_people = int(input("How many people are eating? "))
amt_pizzas = int(input("How many pizzas were ordered? "))

# processing

total_slices = amt_pizzas * SLICES_PER_ZA

slices_per_person = total_slices // amt_people
slices_leftover = total_slices % amt_people

# output: slices per person, slices left over
print(f"Each person gets {slices_per_person} slices")
print(f"There are {slices_leftover} slices leftover")