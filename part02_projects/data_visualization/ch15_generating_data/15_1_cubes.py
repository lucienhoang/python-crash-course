import matplotlib.pyplot as plt

# Set chart title and axis labels.
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set tick label size.
plt.tick_params(axis="both", which="major", labelsize=14)

# Set value for the plot.
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Set the range for each axis.
plt.axis([0, 5100, 0, 130000000000])

# Draw the plot.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors="none", s=10)

plt.show()
