favorite_numbers = {"khoa": 13, "dung": 4, "laurence": 7}

people = ["luci", "laurence", "dung", "Mr. Bong Bang"]

for person in people:
    if person in favorite_numbers:
        print(f"Thank you, {person.title()}, for responding!")
    else:
        print(f"{person.title()}, Would you like to take the poll?")

# Luci, Would you like to take the poll?
# Thank you, Laurence, for responding!
# Thank you, Dung, for responding!
# Mr. Bong Bang, Would you like to take the poll?
