def print_sum(a,b):
    result = a + b
    print(f"the sum is {result}")

def sum(a,b):
    result = a + b
    return result

def calculate_percent(tip_rate):
    return tip_rate/100

def calculate_tip(subtotal, tip_rate):
    """
    Calculates the tip based on the subtotal and tip percentage

    inputs:
        subtotal - float
        tip_rate - float: the percentage of tip (20 for 20% for example)
    outputs:
        tip - float
    """
    tip = subtotal * calculate_percent(tip_rate)
    total = subtotal + tip
    return tip, total

def main():
    print_sum(1,2)
    x = 3
    y = 4
    print_sum(x,y)

    new_sum = sum(1,2)
    print(f"the new sum is {new_sum}")

    print(f"the tip is ${calculate_tip(5.50, 20)}")
    tip, total = calculate_tip(19.99, 15)
    print(f"the new tip is ${tip:.2f}")
    print(f"the total is ${total:.2f}")

main()