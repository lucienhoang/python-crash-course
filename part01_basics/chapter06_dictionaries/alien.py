# A dictionary in Python is a collection of key-value pairs. Each key is connected
# to a value, and you can use a key to access the value associated with that key.

alien_0 = {"color": "green", "point": 5}

print(alien_0["color"])
# green
print(alien_0["point"])
# 5

# Accessing value in Dictionary
new_points = alien_0["point"]
print("You just earned " + str(new_points) + " points for shooting down the alien!")
# You just earned 5 points for shooting down the alien!

# Adding new key-value pairs
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
# {'color': 'green', 'point': 5, 'x_position': 0, 'y_position': 25}
