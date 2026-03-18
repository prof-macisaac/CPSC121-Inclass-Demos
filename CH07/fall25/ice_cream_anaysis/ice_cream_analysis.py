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

def plot_line_graph(x, y, labels, title, x_axis, y_axis):
    plt.plot(x, y)
    plt.title(title)
    plt.xticks(x, labels)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()

def plot_bar_graph(y,labels, title=""):
    plt.bar(labels,y)
    plt.title(title)
    plt.show()

def plot_pie_graph(y,labels, title=""):
    plt.pie(y, labels=labels)
    plt.title(title)
    plt.show()

def main():
    ic_per_month = read_ic_per_month("ice_cream_per_month.csv")
    print(ic_per_month[0])
    print(ic_per_month[1])
    print(ic_per_month[2])
    ic_per_month_title = "ice cream per month"
    plot_line_graph(ic_per_month[0],ic_per_month[1], ic_per_month[2], ic_per_month_title, "month", "sales")
    plot_bar_graph(ic_per_month[1], ic_per_month[2], ic_per_month_title)
    plot_pie_graph(ic_per_month[1], ic_per_month[2], ic_per_month_title)

    ic_per_year = read_ic_per_year("ice_cream_per_year.csv")
    ic_per_year_title = "ice cream per year"
    plot_line_graph(ic_per_year[0],ic_per_year[1], ic_per_year[0], ic_per_year_title, "month", "sales")
    plot_bar_graph(ic_per_year[1], ic_per_year[0], ic_per_year_title)
    plot_pie_graph(ic_per_year[1], ic_per_year[0], ic_per_year_title)

if __name__== "__main__":
    main()