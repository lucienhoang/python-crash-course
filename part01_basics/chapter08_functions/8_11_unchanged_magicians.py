def make_great(names_list):
    """Adding the phrase Great to each magician's name"""
    great_magicians = []

    while names_list:
        magician = names_list.pop()
        great_magicians.append(f"{magician} the Great")

    great_magicians.reverse()
    return great_magicians


def show_magicians(names_list):
    """Print the names of the magicians"""
    print("List of Magician's names:")
    for name in names_list:
        print(f"{name}")


# Original list of magicians
magician_name = ["Luci", "Khoa", "Dung"]

# Call make_great() with a copy of the list using slice notation [:]
great_magicians_names = make_great(magician_name[:])

# Verify the original list is unchanged
print("Original List:")
show_magicians(magician_name)

# Verify the new list has 'the Great' added
print("\nGreat List:")
show_magicians(great_magicians_names)

# Original List:
# List of Magician's names:
# Luci
# Khoa
# Dung

# Great List:
# List of Magician's names:
# Luci the Great
# Khoa the Great
# Dung the Great
