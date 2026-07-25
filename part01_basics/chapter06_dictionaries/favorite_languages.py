favorite_languages = {
    "jen": "python",
    "khoa": "c",
    "dung": "java",
    "Mr. bong bang": "ruby",
}

print("Jen favorite's language is " + favorite_languages["jen"].title() + ".")
# Jen favorite's language is Python.

# Looping through all key-value pairs -> use medthod items() -> tuple
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is: " + language.title() + ".")

# Jen's favorite language is: Python.
# Khoa's favorite language is: C.
# Dung's favorite language is: Java.
# Mr. Bong Bang's favorite language is: Ruby.

friends = ["khoa", "dung"]

# Looping through all the key in a Dictionary
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
