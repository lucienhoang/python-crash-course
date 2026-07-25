# Looping through all value in a Dictionary
favorite_languages = {
    "jen": "python",
    "khoa": "c",
    "dung": "java",
    "Mr. bong bang": "python",
}

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())

# The following languages have been mentioned:
# Java
# C
# Python

# A set is similar to a list except that each item in the set must be unique
