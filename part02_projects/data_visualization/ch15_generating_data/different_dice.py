import pygal
from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = [x for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result."

hist.add("D6 + D10", frequencies)
hist.render_to_file("different_dice_visual.svg")
