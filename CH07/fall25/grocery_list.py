# grocery_list_helper.py

# Start with two small grocery lists
fridge_items = ["milk", "eggs", "cheese"]
store_list = ["bread", "apples", "yogurt"]

# Print each list
print("Fridge items:", fridge_items)
print("Store list:", store_list)

# Accessing elements
print("First fridge item:", fridge_items[0])

# Updating an element
store_list[1] = "bananas"

# Combine them into one big list
full_list = fridge_items + store_list
print("Full grocery list:", full_list)

# Print length and last item
print(f"You have {len(full_list)} total items.")
print("Last item:", full_list[-1])
