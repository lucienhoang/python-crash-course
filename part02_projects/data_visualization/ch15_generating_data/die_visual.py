import matplotlib.pyplot as plt
import pygal
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(1000)]

# Analyze the results.
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [x for x in range(1, die.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result."

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")

# Visualize the results with Matplotlib.
plt.figure(figsize=(10, 6))

# Prepare x label.
x_labels = [x for x in range(1, die.num_sides + 1)]

# Draw the plot.
plt.plot(x_labels, frequencies, marker="o", lw=2, color="steelblue")

# Set chart title and label axes.
plt.title("Results of rolling one D6 1000 times.", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis="both", labelsize=14)

# Set gridline.
plt.grid(True, linestyle="--", alpha=0.4)

# Set tick.
plt.xticks(x_labels)

# Set limit for y axes.
plt.ylim(0, max(frequencies) + 10)

plt.show()
