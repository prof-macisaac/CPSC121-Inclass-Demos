"""
Object Oriented Programming

"""

"""
Classes
"""
import random
from rich import print

class Coin:
    def __init__(self):
        self.sideup = "Heads"
        print("a new coin has been minted")


    def toss(self):
        if random.randint(0,1)==0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

        return self.sideup

    # def get_sideup(self):
    #     return self.sideup

    # def __str__(self):
    #     return f"coin is {self.sideup} up"


 
def main():
    # sideup = 'Heads'
    # sideup = toss_coin(sideup)
    # print(sideup)  
    my_coin = Coin()
    print(f"coin sideup at start {my_coin.sideup}")

    print(f"after the toss {my_coin.toss()}")
    your_coin = Coin()
    print(f"your coin: {your_coin.sideup}")
    print(f"my coin:   {my_coin.sideup}")

    # # print(my_coin.get_sideup())

    # print(my_coin.toss())

    # coin_2 = Coin()
    # print(coin_2.sideup)
main()