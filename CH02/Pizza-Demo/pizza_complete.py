"""
Goal: Based on how many people are eating, how many pizzas are ordered, and how many slices are in a pizza, give the amount of slices per person and how many are left over.
Additional Goal: Based on the cost of each pizza, how much should each person be charged? 
"""

# Input
people_count = int(input("How many people are eating? "))
pizza_count = int(input("How many pizzas were ordered? "))
slices_per_za = int(input("How many slices does each pizza have? "))

# Processing
total_slices = pizza_count * slices_per_za

slices_per_person = total_slices // people_count
leftover_slice_count = total_slices % people_count

print(f"Each person gets {slices_per_person} slices")
print(f"This leaves {leftover_slice_count} slices leftover")
