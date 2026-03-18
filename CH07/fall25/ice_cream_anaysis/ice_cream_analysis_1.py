import matplotlib.pyplot as plt

def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    x = [1,2,3,4,5,6,7,8,9,10,11,12]  # Numeric x-axis for months
    y = [120, 150, 180, 220, 300, 420, 480, 460, 380, 250, 180, 140]  #
    plt.plot(x, y)
    plt.title("Ice Cream Sales Per Month")
    plt.xticks([0,5, 100])
    plt.xlabel("Month")
    plt.ylabel("Sales (Units)")


    plt.show()

if __name__== "__main__":
    main()