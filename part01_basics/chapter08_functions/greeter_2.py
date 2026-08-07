def get_formatted_name(firt_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = firt_name + " " + last_name
    return full_name.title()


# This is an infinite loop
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: thao dung
# Last name: le

# Hello, Thao Dung Le!

# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: khoa
# Last name: hoang

# Hello, Khoa Hoang!

# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: q
