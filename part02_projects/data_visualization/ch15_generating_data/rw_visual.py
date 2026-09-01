import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    # Plot the points.
    point_numbers = list(range(rw.num_points))

    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, edgecolors="none", s=1)
    plt.plot(rw.x_values, rw.y_values, lw=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c="orange", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Remove the axes.
    # plt.axis("off")
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
