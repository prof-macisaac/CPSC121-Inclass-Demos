import matplotlib.pyplot as plt

def main():
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    x = [1,2,3,4,5,6,7,8,9,10,11,12] 
    y = [120, 150, 180, 220, 300, 420, 480, 460, 380, 250, 180, 140]

    plt.plot(x, y)
    plt.title("Ice Cream Sales per Month")
    plt.xlabel("Months")
    plt.ylabel("Sales (Millions of Dollars)")
    plt.xticks(x, month_labels)
    plt.grid()
    plt.show()

    plt.bar(x,y,color = ("blue", "red", "green", "yellow") )
    plt.show()


    # plt.plot(x, y)

    # plt.show()

    # plt.xticks(x,month_labels)
    # plt.title("Ice Creams Sale per Month")
    # plt.xlabel("Months")
    # plt.ylabel("Sales (Thousands of Dollars)")
    # plt.bar(x, y, 1, color = ("blue", "red", "darkgreen"))
    # plt.title("Ice Cream Sales per Month")
    # plt.show()

    # plt.pie(y, labels= month_labels, colors=("blue", "red", "darkgreen"))
    # plt.title("Ice Cream Sales per Month")
    # plt.show()

    # plt.title("Ice Cream Sales per Month")
    # plt.xlabel("Months")
    # plt.ylabel("Sales")
    # plt.xticks(months, month_labels)

    # plt.show()

    # plt.bar(months,ice_cream_sales)
    # plt.title("Ice Cream Sales per Month")
    # plt.xticks(months, month_labels)
    # plt.show()

    # plt.pie(ice_cream_sales, labels=month_labels)
    # plt.title("Ice Cream Sales per Month")
    # plt.show()
if __name__== "__main__":
    main()