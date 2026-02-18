"""
Tip Calculator:

Description: get the total and tip percentage that user wants to calculate. Let them do multiple transactions during the program runtime
"""

while True:
    total = float(input("What is the total? "))

    tip_per = float(input("What is the tip percentage? ")) # 20, 30 -> 30%
    while tip_per <= 0 or tip_per > 100:
        print("Tip Percentage invalid. Must be between 0 and 100")
        tip_per = float(input("What is the tip percentage? ")) 

    tip = total * (tip_per/100)

    print(f"You should tip ${tip:.2f}")

    user_continue = input("Would you like to enter another transaction (yes/no)? ")

    if user_continue == "no":
        break

print("Thanks for coming!")