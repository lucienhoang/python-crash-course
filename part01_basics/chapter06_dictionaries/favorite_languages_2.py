# Looping through a Dictionary's key in order
favorite_languages = {
    "jen": "python",
    "khoa": "c",
    "dung": "java",
    "Mr. bong bang": "ruby",
}

for name in sorted(favorite_languages):
    print(name.title() + ", thank you for taking to the poll.")

# Mr. Bong Bang, thank you for taking to the poll.
# Dung, thank you for taking to the poll.
# Jen, thank you for taking to the poll.
# Khoa, thank you for taking to the poll.
