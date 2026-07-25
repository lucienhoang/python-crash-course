favorite_languages = {
    "jen": "python",
    "khoa": "c",
    "dung": "java",
    "Mr. bong bang": "ruby",
}

print("Jen favorite's language is " + favorite_languages["jen"].title() + ".")
# Jen favorite's language is Python.

friends = ["khoa", "dung"]

for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(
            " Hi "
            + name.title()
            + ", I see your favorite languages is "
            + favorite_languages[name].title()
            + "!"
        )

# Jen
# Khoa
#  Hi Khoa, I see your favorite languages is C.
# Dung
#  Hi Dung, I see your favorite languages is Java.
# Mr. Bong Bang

if "erin" not in favorite_languages.keys():
    print("\nErin, please take out the poll!")

# Erin, please take out the poll!
# favorite_languages.keys() return a list of all the keys
