class CoffeeOrder:

    def __init__(self, name, size, drink_type, milk_type=None, syrup_pumps=0, is_iced = False, shots = 0):
        self.name = name
        self.size = size
        self.drink_type = drink_type
        self.milk_type = milk_type
        self.syrup_pumps = syrup_pumps
        self.is_iced = is_iced
        self.shots = shots
        self.calculate_cost()
    
    def calculate_cost(self):
        """
        calculates the cost and updates the cost variable
        """
        cost = 0
        size_costs = {12:3, 16:3.75, 20: 4.50}
        # size cost
        cost += size_costs[self.size]
        if self.shots > 2:
            cost += (self.shots-2) * 0.75
        cost += self.syrup_pumps * 0.30
        milk_costs = {"oat": 0.50, "whole": 0, "almond": 0.50}
        cost += milk_costs[self.milk_type]

        if self.is_iced:
            cost += 0.25
        
        self.cost = cost
        
    def __str__(self):
        s = f"{self.name}: {self.size}oz"
        if self.is_iced:
            s += " iced"
        else:
            s += " hot"
        if self.milk_type:
            s += f" {self.milk_type} milk"
        
        if self.syrup_pumps > 0:
            s += f", {self.syrup_pumps} pumps syrup"
        
        if self.shots > 0:
            s += f", {self.shots} shots"
        
        s += f" -- ${self.cost:.2f}"

        return s

    def add_syrup(self):
        self.syrup_pumps += 1
        self.calculate_cost()
        

    def add_shot(self):
        self.shots += 1
        self.calculate_cost()

    def make_iced(self):
        self.is_iced = True
        self.calculate_cost()
    
    def make_hot(self):
        self.is_iced = False
        self.calculate_cost()

    def change_size(self, size):
        self.size = size
        self.calculate_cost()
    
    def change_milk(self, milk):
        self.milk_type = milk
        self.calculate_cost()


def main():
    name = input("Customer name: ")
    size = int(input("Size (12/16/20 oz): "))
    drink_type = input("Drink type: ").strip().lower()
    milk_type = input("Milk type: ").strip().lower()
    syrup_pumps = int(input("How many syrup pumps? "))
    is_iced = True if input("Iced? (yes/no): ").strip().lower() == "yes" else False
    shots = int(input("How many espresso shots? "))

    order = CoffeeOrder(name, size, drink_type, milk_type, syrup_pumps, is_iced, shots)

    choice = ""
    while choice != "8":
        print("\n1. View order")
        print("2. Add syrup")
        print("3. Add shot")
        print("4. Make iced")
        print("5. Make hot")
        print("6. Change size")
        print("7. Change milk")
        print("8. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(order)
        elif choice == "2":
            order.add_syrup()
        elif choice == "3":
            order.add_shot()
        elif choice == "4":
            order.make_iced()
        elif choice == "5":
            order.make_hot()
        elif choice == "6":
            size = int(input("Size (12/16/20 oz): "))
            order.change_size(size)
        elif choice == "7":
            milk_type = input("Milk type: ")
            order.change_milk(milk_type)
        elif choice == "8":
            print("Goodbye!")
            exit()
        else:
            print("Invalid option.")

main()