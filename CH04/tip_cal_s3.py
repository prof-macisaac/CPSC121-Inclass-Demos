"""
Tip Calculator:

Description: get the total and tip percentage that user wants to calculate. Let them do multiple transactions during the program runtime
"""

while True:
    total = float(input("What is your total? "))


    tip_per = float(input("How much (percent) would you like to tip? "))
    # 20 -> 20%, 5-> 5%
    while tip_per <= 0 or tip_per > 100:
        print("That is not a valid tip percentage")
        tip_per = float(input("How much (percent) would you like to tip? "))
    

    tip_amt = total * (tip_per/100)

    print(f"You should tip ${tip_amt:.2f}")
    
    user_cont = input("Would you like to calculate another tip? (yes/no) ")

    if user_cont == "no":
        break

print("Thank you for using the tip calculator!")
