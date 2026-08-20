from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break

    last = input("Please give me a last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formmated name: {formatted_name}.")


# Please give me a first name: khoa
# Please give me a last name: luci

# Neatly formmated name: Khoa Luci.

# Please give me a first name: bao
# Please give me a last name: boi

# Neatly formmated name: Bao  Boi.

# Please give me a first name: dung
# Please give me a last name: laurence

# Neatly formmated name: Dung  Laurence.

# Please give me a first name: q
