"""
Program: Math & Dice Utility Program
Author: Your Name
Course: CPSC 121
Description:
    This program demonstrates how to build a menu-driven application
    using functions, a main control loop, and imported modules.

    The user can choose to:
        1. Add two numbers
        2. Calculate the square root of a number
        3. Roll a dice with a user-specified number of sides
        4. Quit the program

    The program continues running until the user chooses to quit.
"""

import math
import random


def show_menu():
    """
    Displays the program menu options to the user.
    """
    print("=== Math & Dice Utility Program ===")
    print("1. Add two numbers")
    print("2. Calculate square root")
    print("3. Roll a dice")
    print("4. Quit")


def add_numbers():
    """
    Prompts the user for two numbers,
    calculates their sum, and prints the result.
    """
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"Result: {result}")


def calculate_square_root():
    """
    Prompts the user for a number,
    calculates its square root using the math module,
    and prints the result.
    """
    num = float(input("Enter a number: "))
    result = math.sqrt(num)
    print(f"Square root: {result:.2f}")


def roll_dice():
    """
    Prompts the user for the number of sides on a dice,
    generates a random roll between 1 and that number,
    and prints the result.
    """
    sides = int(input("Enter number of sides on the dice: "))
    roll = random.randint(1, sides)
    print(f"You rolled: {roll}")


def main():
    """
    Controls the overall flow of the program.
    Repeatedly displays the menu and processes
    the user's selection until they choose to quit.
    """
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_numbers()
        elif choice == "2":
            calculate_square_root()
        elif choice == "3":
            roll_dice()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Program execution starts here
main()