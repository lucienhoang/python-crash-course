def show_magicians(names_list):
    """Print the names of the magicians"""
    print("List of Magician's names:")
    for name in names_list:
        print(f"{name.title()}")


magician_name = ["luci", "khoa", "dung"]
show_magicians(magician_name)

# List of Magician's names:
# Luci
# Khoa
# Dung
