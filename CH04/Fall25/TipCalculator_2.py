"""
Tip Calculator:

Description: get the total and tip percentage that user wants to calculate. Let them do multiple transactions during the program runtime
"""

another_transaction = input("Would you like to calculate a tip (yes/no)? ") ==  "yes"

while another_transaction:
    subtotal = float(input("How much was your bill? "))

    # input validation for subtotal
    while subtotal < 0:
        print("That is not a valid subtotal!")
        subtotal = float(input("How much was your bill? "))

    # how much to tip
    tip_rate = float(input("How much would you like to tip (15,20,22)? "))
    # calculate the tip amount
    tip_amount = subtotal * (tip_rate/100)
    # calculate the total cost after tip
    total = tip_amount + subtotal
    # display tip amount and total cost after tip
    print(f"You will tip ${tip_amount:.2f}")
    print(f"Your total after tip is ${total:.2f}")

    another_transaction = input("Would you like to calculate another a tip (yes/no)? ") == "yes"


print("Exiting the program. Goodbye!")

