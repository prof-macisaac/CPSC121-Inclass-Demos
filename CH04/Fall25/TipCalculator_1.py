"""
Tip Calculator:

Description: get the total and tip percentage that user wants to calculate. Let them do multiple transactions during the program runtime
"""

another_transaction = input("Would you like to calculate a tip (yes/no)? ")

while another_transaction == "yes":
    subtotal = float(input("How much was your bill? "))

    # input validation!
    while subtotal < 0:
        print("Subtotal cannot be negative!")
        subtotal = float(input("How much was your bill? "))

    tip_rate = float(input("How much would you like to tip (15, 20, 22)? "))

    tip_amount = subtotal * (tip_rate/100)
    print(f"You will tip ${tip_amount}")

    total = tip_amount + subtotal
    print(f"Your final total is ${total:.2f}")

    another_transaction = input("Would you like to calculate another tip (yes/no)? ")

print("Goodbye!")
