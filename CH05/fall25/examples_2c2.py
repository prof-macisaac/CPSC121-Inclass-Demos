def print_sum(x, y):
    result = x + y
    print(f"the sum is {result}")

def sum(x, y):
    result = x + y
    return result

def calculate_rate(percentage):
    return percentage/100

def hello():
    print(f"Hello {first_name}")


def calculate_tip(subtotal, tip_percentage):
    """
    Calculates the tip based on the subtotal and tip percentage

    Input:
        subtotal (float | int)
        tip_percentage (float | int) - value is 20 for 20%
    Output:
        tip_amount (float)
    """
    tip_amount = subtotal * (tip_percentage/100)
    tip_amount = subtotal * calculate_rate(tip_percentage)
    return tip_amount

def main():
    print_sum(1,2)
    a, b = 3, 4
    print_sum(a,b)
    val = sum(1,2)
    print(f"the sum is {val}")
    print(f"the sum is {sum(a,b)}")

    sub = 5.99
    percent = 20

    tip_amount = calculate_tip(sub, percent)
    print(f"the tip amount is ${tip_amount:.2f}")

    global first_name
    first_name = "chiana"
    hello()

first_name = "dominic"
main()