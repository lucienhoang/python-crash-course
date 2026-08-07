def get_formatted_name(firt_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = firt_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("lucien", "hoang")
print(musician)

# Lucien Hoang
