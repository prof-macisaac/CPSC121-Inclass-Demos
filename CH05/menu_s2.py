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

TAX_RATE = 0.05

def show_menu():
    """
    Displays the program menu options
    """
    print("========= Utility Program =========")
    print("1. Add two numbers")
    print("2. Calculate square root")
    print("3. Roll a dice")
    print("4. Quit")

def add_two_numbers():
    """
    Prints out the sum of two user inputted numbers
    """
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 + num2}")

def roll_dice():
    """
    prints out the result of a six-sided dice
    """
    val = random.randint(1,6)
    print(f"the dice rolled a {val}")


def calc_sqrt():
    """
    prints out the square root of a user inputted number
    """
    num1 = float(input("Enter a number: "))
    print(f"Square root: {math.sqrt(num1):.2f}")

def main():
    """
    Control the flow of the program
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
            print("Invalid Choice")

main()