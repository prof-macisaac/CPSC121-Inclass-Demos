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
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        print("Could not open file.")
        return

    while True:
        category = infile.readline().strip()
        if category == "":
            break
        cost = infile.readline().strip()
        if cost == "":
            break

        try:
            value = float(cost)
        except ValueError:
            continue
        
        print(f"{category} - ${value:.2f}")
    infile.close()

def add_transaction(filename):
    """
    Parameters
        - filename (str):   relative path to file that we are trying
                            to write to.
    Ask user for category and amount.
    - Ensure amount is a valid float using try/except.
    - Append exactly TWO lines to the file:
        category
        amount
    Returns:
        None
    """
    try:
        outfile = open(filename, "a")
    except FileNotFoundError:
        print("Could not open file.")
        return
    
    category = input("Category name: ")
    cost = input("Cost of transactions: ")

    try:
        value = float(cost)
    except ValueError:
        print("Cost not a valid number. No transaction added")
        outfile.close()
        return

    
    outfile.write(f"{category}\n{value:.2f}\n")
    outfile.close()
    
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
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        print("Could not open file.")
        return

    total_cost = 0
    while True:
        category = infile.readline().strip()
        if category == "":
            break
        cost = infile.readline().strip()
        if cost == "":
            break
        try:
            value = float(cost)
        except ValueError:
            continue

        total_cost += value
    infile.close()
    print(f"total spent: ${total_cost:.2f}")


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
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        print("Could not open file.")
        return

    user_cat = input("Enter category you would like to total up: ")
    total_cost = 0
    while True:
        category = infile.readline().strip()
        if category == "":
            break
        if category != user_cat:
            continue
        cost = infile.readline().strip()
        if cost == "":
            break
        try:
            value = float(cost)
        except ValueError:
            continue

        total_cost += value
    infile.close()
    print(f"total spent on {user_cat}: ${total_cost:.2f}")


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
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        print("Could not open file.")

    user_cat = input("Enter category you would like to total up: ")
    with open(f"{user_cat}_transactions.txt", "w") as outfile:
        while True:
            category = infile.readline().strip()
            if category == "":
                break
            if category != user_cat:
                continue
            cost = infile.readline().strip()
            if cost == "":
                break
            try:
                value = float(cost)
            except ValueError:
                continue

            outfile.write(f"{value}\n")
    infile.close()


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

        if choice == 1:
            view_all_transactions(EXPENSES_FILE)
        elif choice == 2:
            add_transaction(EXPENSES_FILE)
        elif choice == 3:
            calculate_total_spending(EXPENSES_FILE)
        elif choice == 4:
            total_spending_by_category(EXPENSES_FILE)
        elif choice == 5:
            export_category_transactions(EXPENSES_FILE)
        else:
            break

main()