# alien_0 = {"color": "green", "point": 5}
# alien_1 = {"color": "yellow", "point": 10}
# alien_2 = {"color": "grereden", "point": 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# {'color': 'green', 'point': 5}
# {'color': 'yellow', 'point': 10}
# {'color': 'grereden', 'point': 15}

aliens = []

# Make 10 green aliens
for alien_number in range(10):
    new_alien = {"color": "green", "point": 5, "speed": "slow"}
    aliens.append(new_alien)

# Modify the first 3 aliens
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["point"] = 10
        alien["speed"] = "medium"
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["point"] = 15
        alien["speed"] = "fast"

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# {'color': 'yellow', 'point': 10, 'speed': 'medium'}
# {'color': 'yellow', 'point': 10, 'speed': 'medium'}
# {'color': 'yellow', 'point': 10, 'speed': 'medium'}
# {'color': 'green', 'point': 5, 'speed': 'slow'}
# {'color': 'green', 'point': 5, 'speed': 'slow'}
# ...
# Total number of aliens: 10
