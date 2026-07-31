favorite_places = {
    "khoa": ["bed", "WC", "rooftop"],
    "dung": ["sapa", "phu quoc", "van ly truong thanh"],
    "laurence": ["buon ma thuot", "home", "da nang"],
}

# ver 1
# for index, person in enumerate(favorite_places, start=1):
#     print(f"{index}. {person.title()} favorite places are:")
#     if person == "khoa":
#         for place in favorite_places["khoa"]:
#             print(f"\t{place.title()}")
#     if person == "dung":
#         for place in favorite_places["dung"]:
#             print(f"\t{place.title()}")
#     if person == "laurence":
#         for place in favorite_places["laurence"]:
#             print(f"\t{place.title()}")

# ver 2
for index, (person, places) in enumerate(favorite_places.items(), start=1):
    print(f"{index}. {person.title()} favorite places are:")

    for place in places:
        print(f"\t{place.title()}")

# 1. Khoa favorite places are:
#         Bed
#         Wc
#         Rooftop
# 2. Dung favorite places are:
#         Sapa
#         Phu Quoc
#         Van Ly Truong Thanh
# 3. Laurence favorite places are:
#         Buon Ma Thuot
#         Home
#         Da Nang
