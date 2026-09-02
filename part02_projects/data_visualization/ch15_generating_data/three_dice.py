import pygal
from die import Die

# Create three D6.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a three D6 1000 times."
hist.x_labels = [x for x in range(3, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result."

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("three_dice.svg")
