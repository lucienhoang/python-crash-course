# A Dictionary in a Dictionary
users = {
    "einstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# Username: einstein
#         Fullname: Albert Einstein
#         Location: Princeton

# Username: mcurie
#         Fullname: Marie Curie
#         Location: Paris
