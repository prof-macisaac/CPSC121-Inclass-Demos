"""
Expense Tracker (Starter Code)
File format (expenses.txt):
- Each transaction uses TWO lines:
    line 1: category (text)
    line 2: amount (number)

Menu:
1. View All Transactions
2. Add Transaction
3. Calculate Total Spending
4. Total Spending by Category
5. Export Category Transactions (BONUS)
6. Quit

This starter code RUNS as-is.
Your job is to fill in the TODO functions below.
"""




# ============================================================
# TODO FUNCTIONS (You will implement these)
# ============================================================

def view_all_transactions(filename):
    """
    Parameters
        - filename (str):   relative path to file that we are trying
                            to read from.
    TODO:
    Print every transaction stored in the file.
    
    - If file does not exist, print a friendly message and return.
    - If it does, open up that file
    - Read two lines at a time (category then amount).
    - Print in format:
        McDonalds - $12.50
    - Skip entries where amount cannot be converted to float.
    - close the file
    
    Returns:
        None
    """
    print("[TODO] view_all_transactions not implemented yet.")


def add_transaction(filename):
    """
    Parameters
        - filename (str):   relative path to file that we are trying
                            to write to.
    TODO:
    Ask user for category and amount.
    - Ensure amount is a valid float using try/except.
    - Append exactly TWO lines to the file:
        category
        amount
    Returns:
        None
    """
    print("[TODO] add_transaction not implemented yet.")


def calculate_total_spending(filename):
    """
    Parameters
        - filename (str):   relative path to file that we are trying
                            to read from.
    TODO:
    - Read file
    - Add all valid amounts
    - Print total spending
    - Skip invalid numeric lines
    Returns:
        None
    """
    print("[TODO] calculate_total_spending not implemented yet.")


def total_spending_by_category(filename):
    """
    Parameters
        - filename (str):   relative path to file that we are trying
                            to read from.
    TODO:
    - Ask user for a category
    - Read file
    - Add amounts only for that category
    - Skip invalid numeric lines
    - Print result
    Returns:
        None
    """
    print("[TODO] total_spending_by_category not implemented yet.")


def export_category_transactions(filename):
    """
    BONUS TODO:

    Ask the user for a category.

    Create a new file named:
        <category_name>_transactions.txt

    Example:
        If user enters "Food",
        create file:
            Food_transactions.txt

    Then:
    - Read through the original file.
    - For every transaction matching the chosen category,
      write it to the new file.
    - Each transaction in the new file should be written on ONE line,
      formatted like:
            12.50
            17.99

    Requirements:
    - If original file does not exist, print a message and return.
    - Skip invalid numeric lines using try/except.
    - Use with open(...) when writing.
    """
    print("[BONUS TODO] export_category_transactions not implemented yet.")


# ============================================================
# PROVIDED MENU / MAIN LOOP
# ============================================================

def print_menu():
    print()
    print("===== Expense Tracker Menu =====")
    print("1. View All Transactions")
    print("2. Add Transaction")
    print("3. Calculate Total Spending")
    print("4. Total Spending by Category")
    print("5. Export Category Transactions (BONUS)")
    print("6. Quit")


def get_menu_choice():
    while True:
        try:
            choice = int(input("Choose an option (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number from 1 to 6.")
        except ValueError:
            print("Invalid input. Please enter a whole number from 1 to 6.")


def main():
    EXPENSES_FILE = "expenses.txt"
    print("Welcome to the Expense Tracker!")
    print(f"Using data file: {EXPENSES_FILE}")

    while True:
        print_menu()
        choice = get_menu_choice()

        # TODO: Fill out the menu options
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            pass

# TODO: Call Main