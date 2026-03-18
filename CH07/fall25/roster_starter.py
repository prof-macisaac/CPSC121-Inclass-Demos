"""
Roster Manager - Starter Code (roster is local to main, no type hints)
You will implement ONLY the list-related parts marked with TODO.
Menu, input handling, and program loop are provided.

Features to implement:
    1) Create a list named `roster` (INSIDE main)
    2) Check if a student is on the roster
    3) Add a student to the roster
    4) Print the entire roster
"""

def normalize_name(raw):
    """Standardize how names are stored/compared."""
    return raw.strip().title()

def print_menu():
    print("\n=== Roster Menu ===")
    print("1) Check if a student is on the roster")
    print("2) Add a student to the roster")
    print("3) Print the entire roster")
    print("4) Remove a student by name  [remove]")
    print("5) Quit")

def check_student(roster):
    """Ask for a name and report whether it's in the roster."""
    name = normalize_name(input("Enter a student name to check: "))
    # ---------------------------
    # TODO: Use list membership (e.g., `in`) to check if name is present.
    # Print either:
    #   f"{name} is on the roster."
    # or
    #   f"{name} is NOT on the roster."
    # ---------------------------
    if name in roster:
        print(f"{name} is on the roster.")
    else:
        print(f"{name} is NOT on the roster.")


def add_student(roster):
    """Ask for a name and add it to the roster (avoid exact duplicates)."""
    name = normalize_name(input("Enter a student name to add: "))
    # ---------------------------
    # TODO: If the name is not already present, add it to the list (append).
    # If it is already present, print a message that it already exists.
    # ---------------------------
    if name not in roster:
        roster.append(name)
    else:
        print(f"{name} is already on the roster")


def print_roster(roster):
    """Print the entire roster (one name per line, numbered)."""
    # ---------------------------
    # TODO: Print the roster.
    # Requirements:
    #   - If empty, print: "Roster is empty."
    #   - Otherwise, print a numbered list:
    #         1) Alice
    #         2) Bob
    #   - Sort before printing for a consistent order
    #   - At end, print how many names are on the roster
    place = 1
    roster.sort()

    if len(roster) == 0:
        print("Roster is empty")
        return
    
    for name in roster:
        print(f"{place}) {name}")
        place += 1

    print(f"Roster has {len(roster)} names")


def remove_by_name(roster):
    name = normalize_name(input("Enter the name to remove: "))
    # TODO: remove name from roster. Handle case where name not found
    # Hint: if name not in roster, don't call remove; print a friendly message
    if name not in roster:
        print(f"{name} not on roster")
        return

    roster.remove(name)

def main():
    # ---------------------------
    # TODO: Create the roster list LOCALLY here (not global).
    # Start empty or seed with a few names for testing.
    # Example:
    # roster = []
    # ---------------------------
    roster = []
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            check_student(roster)
        elif choice == "2":
            add_student(roster)
        elif choice == "3":
            print_roster(roster)
        elif choice == "4":
            remove_by_name(roster)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
