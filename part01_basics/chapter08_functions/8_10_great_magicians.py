def make_great(names_list):
    """Adding the phrase Great to each magician's name"""
    # for i in range(len(names_list)):
    #     names_list[i] = "Great " + names_list[i]
    for i, name in enumerate(names_list):
        names_list[i] = "Great " + name


def show_magicians(names_list):
    """Print the names of the magicians"""
    print("List of Magician's names:")
    for name in names_list:
        print(f"{name.title()}")


magician_name = ["luci", "khoa", "dung"]
make_great(magician_name)
show_magicians(magician_name)

# List of Magician's names:
# Great Luci
# Great Khoa
# Great Dung
