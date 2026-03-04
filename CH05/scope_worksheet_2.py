TAX_RATE = 0.10
total_sales = 0

def add_sale(amount):
    global total_sales
    total_sales = total_sales + amount
    print("Added sale:", amount)

def apply_tax(amount):
    tax = amount * TAX_RATE
    print("Tax:", tax)
    return tax

def print_summary():
    print("Total sales:", total_sales)

def discount():
    global sale1
    sale1 = sale1 - 10
    print("Discounted sale1:", sale1)

def main():
    sale1 = 100
    sale2 = 50

    add_sale(sale1)
    add_sale(sale2)

    tax1 = apply_tax(sale1)
    tax2 = apply_tax(sale2)

    print("Tax total:", tax1 + tax2)
    # discount()
    print_summary()

main()