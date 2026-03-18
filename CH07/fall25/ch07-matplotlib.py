import matplotlib.pyplot as plt

# Line Graphs
x_coords = [0,1,2,3,4]
y_coords = [0,2,4,6,8]

plt.plot(x_coords, y_coords)

plt.xlim(xmin = -3, xmax=15)
plt.ylim(ymin=-10, ymax=10)
plt.xticks(x_coords)
plt.yticks(y_coords, ["$0", "$2", "$4", "$6","$8"])

plt.title("dollars per hour")
plt.xlabel("hour")
plt.ylabel("sales")

plt.grid(True)

plt.show()

# Bar Graphs
bar_width = 0.5
plt.bar(x_coords, y_coords, bar_width, color = ("r", "g", "b", "k"))
plt.show()


# Pie Chart
values = [10, 40, 80]
slice_labels = ["donuts", "burgers", "milkshakes"]
plt.pie(values, labels=slice_labels, colors = ("r", "k", "b"))
plt.title("Purchases by Revenue")
plt.show()