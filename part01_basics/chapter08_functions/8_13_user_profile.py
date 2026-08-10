def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["fisrt_name"] = first
    profile["last_name"] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("lucien", "hoang", location="HCM", field="IT", age="27")

print(user_profile)

# {'fisrt_name': 'lucien', 'last_name': 'hoang', 'location': 'HCM', 'field': 'IT', 'age': '27'}
