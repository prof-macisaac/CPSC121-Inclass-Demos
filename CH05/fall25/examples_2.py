# review on function inputs (parameters)

def print_sum(x,y):
    z = x + y
    print(f"the sum is {z}")

def calculate_total(subtotal, tip_percent):
    tip = subtotal * (tip_percent/100)
    return tip + subtotal

def full_name(first_name, last_name):
    return first_name + " " + last_name

print_sum(1,2)

a,b = 4,5
print_sum(a,b)

def sum(x,y):
    z = x + y
    return z 

val = sum(1,2) # this will return the value 3
print(f"the val is {val}")



cost = 5.0
print(f"My total is ${calculate_total(cost, 20)}")

first = "dominic"
last = "macisaac"
full = full_name(first, last)
print(f"My name is {full}")