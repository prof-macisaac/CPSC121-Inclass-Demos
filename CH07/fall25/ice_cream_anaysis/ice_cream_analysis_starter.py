import matplotlib.pyplot as plt
def read_ic_per_month(filename):
    x = []
    y = []
    labels = []
    with open(filename, "r") as file:
        for item in file:
            record = item.rstrip().split(",")
            x.append(int(record[0]))
            labels.append(record[1])
            y.append(float(record[2]))

    return (x,y,labels)

def read_ic_per_year(filename):
    x = []
    y = []
    with open(filename, "r") as file:
        for item in file:
            record = item.rstrip().split(",")
            x.append(int(record[0]))
            y.append(float(record[1]))

    return (x,y)

def plot_line_graph():
    pass

def plot_bar_graph():
    pass

def plot_pie_graph():
    pass

def main():
    ic_per_month = read_ic_per_month("ice_cream_per_month.csv")
    print("Ice cream per month is made up of three lists: x values, y values, and labels for the x values. See each below")
    print("Note: Only printing first 3 elements of each list!")
    print(f"ic_per_month[0], x values, [int]: {ic_per_month[0][:3]}")
    print(f"ic_per_month[1], y values, [float]: {ic_per_month[1][:3]}")
    print(f"ic_per_month[2], label values, [str]: {ic_per_month[2][:3]}")
    print()

    ic_per_year = read_ic_per_year("ice_cream_per_year.csv")
    print("Ice cream per year is made up of two lists: x values (which also act as labels) and y values. See each below")
    print("Note: Only printing first 3 elements of each list!")
    print(f"ic_per_year[0], x values (also year labels), [int]: {ic_per_year[0][:3]}")
    print(f"ic_per_year[1], y values, [float]: {ic_per_year[1][:3]}")

if __name__== "__main__":
    main()