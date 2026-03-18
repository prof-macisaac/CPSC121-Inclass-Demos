import matplotlib.pyplot as plt

days = [0, 1, 2, 3, 4, 5, 6, 7]
mass = [0.2, 0.5, 1.2, 2.0, 3.2, 4.1, 4.8, 5.0]

plt.figure()
plt.plot(days, mass)

plt.title("Pumpkin Growth Over a Week")
plt.xlabel("Days")
plt.ylabel("Mass (kg)")
plt.grid(True)

plt.xlim(-0.5, 7.5)
plt.ylim(0, 5.5)

# Annotate max point
# max_idx = mass.index(max(mass))
# plt.annotate("Max", (days[max_idx], mass[max_idx]), xytext=(5.9, 5.25),
#              arrowprops=dict(arrowstyle="->"))
ticksy = []
for i in range(6):
    ticksy.append(i)
    ticksy.append(i + 0.5)
plt.yticks(ticksy)
plt.savefig("pumpkin_growth.jpg", dpi=150, bbox_inches="tight")
plt.close()


monsters = ['Ghost', 'Vampire', 'Zombie', 'Witch', 'Skeleton']
counts  = [12,       4,          6,        8,        10]

plt.figure()
plt.bar(monsters, counts, color = ('gray', 'purple', 'g', 'black','orange' ))

plt.title("Monster Sightings on Oct 31")
plt.ylabel("Count")
plt.xlabel("Monster Type")

plt.savefig("monster_bar.jpg", dpi=150, bbox_inches="tight")
plt.close()


labels = ["Snickers", "Fruit Snacks", "Reeses", "Kit Kat", "Nerds"]
sizes  = [40, 25, 10, 15, 10]

plt.figure()

plt.pie(sizes, labels=labels, colors = ("saddlebrown", "blue", "darkorange", "red", "hotpink"))
plt.title("Candy Haul by Type")

plt.savefig("candy_pie.jpg", dpi=150, bbox_inches="tight")
plt.close()
