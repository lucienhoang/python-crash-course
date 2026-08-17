from random import randint


class Die:
    """Model a Die game."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(f"Die: {x}")


six_sided_die = Die()
ten_sided_die = Die(10)


for index in range(1, 11):
    six_sided_die.roll_die()

print("---")

for index in range(1, 11):
    ten_sided_die.roll_die()

# Die: 2
# Die: 6
# Die: 2
# Die: 6
# Die: 3
# Die: 2
# Die: 6
# Die: 5
# Die: 6
# Die: 5
# ---
# Die: 5
# Die: 4
# Die: 8
# Die: 10
# Die: 2
# Die: 2
# Die: 7
# Die: 1
# Die: 9
# Die: 5
