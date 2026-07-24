# Starting with ann Empty Dictionary
alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5


print(alien_0)
# {'color': 'green', 'points': 5}

# Modifying Values in a Dictionary
print("The alien is " + alien_0["color"] + ".")
# The alien is green.

alien_0["color"] = "yellow"

print("The alien is " + alien_0["color"] + ".")
# The alien is yellow.

alien_0 = {"x_position": 0, "y_position": 25, "speed": "fast"}
print("Original x_position: " + str(alien_0["x_position"]))
# Original x_position: 0

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x_position: " + str(alien_0["x_position"]))
# New x_position: 2
