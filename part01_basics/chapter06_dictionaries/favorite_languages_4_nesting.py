favorite_languages = {
    "jen": ["python", "ruby"],
    "khoa": "c",
    "dung": ["java", "go"],
    "Mr. bong bang": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are: ")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is: {languages.title()}")

# Jen's favorite languages are:
#         Python
#         Ruby

# Khoa's favorite language is: C

# Dung's favorite languages are:
#         Java
#         Go

# Mr. Bong Bang's favorite languages are:
#         Python
#         Haskell
