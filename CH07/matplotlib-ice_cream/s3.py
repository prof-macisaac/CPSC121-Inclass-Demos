import matplotlib.pyplot as plt

def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    x = [1,2,3,4,5,6,7,8,9,10,11,12] 
    y = [120, 150, 180, 220, 300, 420, 480, 460, 380, 250, 180, 140]
    
    plt.figure()
    plt.scatter(x,y, c="red", alpha = 0.2)
    plt.plot(x, y)

    

    plt.title("Ice Cream Sales per Month")

    plt.xlabel("Months")
    plt.ylabel("Sales (Millions of Dollars)")

    plt.xticks(x, months)
    plt.grid(alpha=0.5)

    plt.savefig("ice_cream_plot.png")

    plt.figure()
    plt.bar(x,y, color = ("blue", "green"))
    plt.xlabel("Months")
    plt.ylabel("Sales (Millions of Dollars)")

    

    plt.figure()
    plt.pie(y, labels=months, autopct="%1.1f%%", colors= ("blue", "green", "yellow", "red"))

    plt.show()


if __name__ == "__main__":
    main()