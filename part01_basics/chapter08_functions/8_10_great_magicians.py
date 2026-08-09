def make_great(names_list):
    """Adding the phrase Great to each magician's name"""
    # for i in range(len(names_list)):
    #     magicians[i] = f"{magicians[i]} the Great"
    for i, name in enumerate(names_list):
        names_list[i] = name + " the Great"


def show_magicians(names_list):
    """Print the names of the magicians"""
    print("List of Magician's names:")
    for name in names_list:
        print(f"{name}")


# Original list of magicians
magician_name = ["Luci", "Khoa", "Dung"]

make_great(magician_name)

show_magicians(magician_name)

# List of Magician's names:
# Luci the Great
# Khoa the Great
# Dung the Great
