# Making an Argument Optional
def get_formatted_name(firt_name, last_name, middle_name=""):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = firt_name + " " + middle_name + " " + last_name
    else:
        full_name = firt_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("khoa", "hoang")
print(musician)

musician = get_formatted_name("khoa", "hoang", "luci")
print(musician)

# Khoa Hoang
# Khoa Luci Hoang
