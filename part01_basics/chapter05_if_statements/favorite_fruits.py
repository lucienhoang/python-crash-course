favorite_fruits = ["banh beo", "banh xeo", "banh hoi"]

if "banh xeo" in favorite_fruits:
    print("I really like " + favorite_fruits[1].title() + "!")
if "banh beo" in favorite_fruits:
    print("I really like " + favorite_fruits[0].title() + "!")
if "banh canh" not in favorite_fruits:
    print("I don't really like banh canh!")
if "banh hoi" in favorite_fruits:
    print("I really like " + favorite_fruits[2].title() + "!")

# I really like Banh Xeo!
# I really like Banh Beo!
# I don't really like banh canh!
# I really like Banh Hoi!
