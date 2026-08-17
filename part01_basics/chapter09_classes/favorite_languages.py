from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages["jen"] = "python"
favorite_languages["dung"] = "c"
favorite_languages["khoa"] = "java"
favorite_languages["Mr. bong bang"] = "ruby"


# Looping through all key-value pairs -> use medthod items() -> tuple
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is: " + language.title() + ".")

# Jen's favorite language is: Python.
# Khoa's favorite language is: C.
# Dung's favorite language is: Java.
# Mr. Bong Bang's favorite language is: Ruby.

# This is a great class to be aware of because it combines the main benefit
# of lists (retaining your original order) with the main feature of dictionaries
# (connecting pieces of information).
