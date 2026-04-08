import matplotlib.pyplot as plt

def main():
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    x = [1,2,3,4,5,6,7,8,9,10,11,12] 
    y = [120, 150, 180, 220, 300, 420, 480, 460, 380, 250, 180, 140]

    plt.figure(layout="constrained")
    plt.scatter(x,y, c="red")
    plt.plot(x, y)
    plt.title("Ice Cream Sales per Month")
    plt.xlabel("Months")
    plt.ylabel("Sales (Millions of Dollars)")
    # plt.grid(alpha=0.5)
    plt.xticks(x, month_labels)

    # plt.bar(x,y, color = ("blue", "red", "green", "yellow"))
    # plt.hist(y, 4)
    plt.savefig("test1.png")

    plt.figure()
    plt.pie(y, labels=month_labels, colors = ("blue","red", "darkgreen", "yellow", "purple"), autopct="%1.1f%%")
    # plt.show()
    plt.savefig("test.png")



main()