"""
Program: Simple Utility Menu Program
Author: Your Name
Course: CPSC 121
Description:
    This program demonstrates how to build a menu-driven application using functions and a main control loop.

    The user can choose to:
        1. Add two numbers
        2. Square a number
        3. Check whether a number is even
        4. Roll a dice
        5. Quit the program

    The program continues running until the user chooses to quit.
"""
import random
import math

def add_two_numbers():
    """
    prints the sum of two user inputted values
    """
    num1 = float(input("Enter the first value: "))
    num2 = float(input("Enter the second value: "))
    print(f"Sum = {num1 + num2}")

def calc_sqrt():
    """
    prints the sqrt of a user inputted value
    """
    num = float(input("Enter a value: "))
    sq = math.sqrt(num)
    print(f"Square root = {sq:.2f}")

def roll_dice():
    """
    prints the result of a 6-sided dice roll
    """
    dice = random.randint(1,6)
    print(f"Roll = {dice}")

def show_menu():
    print("===== Utility Program =====")
    print("1. Add two numbers")
    print("2. Calculate square root")
    print("3. Roll a dice")
    print("4. Quit")

def main():
    """
    control the overall flow of the program

    repeatedly show the menu and process user selections
    """
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_two_numbers()
        elif choice == "2":
            calc_sqrt()
        elif choice == "3":
            roll_dice()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

main()