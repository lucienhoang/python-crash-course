# Using Arbitrary Keyword Arguments

# The parameter **user_info cause Python to create an empty dictionary
# called user_info and pack whatever name-value pairs it receives into this dictionary.


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["fisrt_name"] = first
    profile["last_name"] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics", age="50"
)

print(user_profile)

# {'fisrt_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics', 'age': '50'}
