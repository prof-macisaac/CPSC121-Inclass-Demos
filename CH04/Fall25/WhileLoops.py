"""
Tip Calculator:

Description: get the total and tip percentage that user wants to calculate. Let them do multiple transactions during the program runtime
"""

another_transaction = input("Would you like to calculate a tip? ") == "yes"

while another_transaction:
    subtotal = float(input("How much was your bill? "))
    
    while subtotal < 0:
        print("That is not a valid subtotal.")
        subtotal = float(input("How much was your bill? "))

    tip_rate = float(input("How much are you going to tip (15%, 20%, 25%, etc)? "))
    tip_amount = subtotal * (tip_rate/100)
    total = subtotal + tip_amount
    print(f"Tipping {tip_rate:.2f}% will be ${tip_amount:.2f} for a total of ${total:.2f}!")

    another_transaction = input("Would you like to calculate another tip? ") == "yes"

print("Goodbye!")