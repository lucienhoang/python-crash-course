rivers = {
    "serepok": "dak lak",
    "cuu long": "hcm",
    "hong": "ha noi",
}

for river, place in rivers.items():
    print(f"The {river.title()} runs through {place.title()}")

# The Serepok runs through Dak Lak
# The Cuu Long runs through Hcm
# The Hong runs through Ha Noi

for river in rivers:
    print(f"River name: {river}")

# River name: serepok
# River name: cuu long
# River name: hong

for i, place in enumerate(rivers.values(), start=1):
    print(f"{i}. Place name: {place}")

# 1. Place name: dak lak
# 2. Place name: hcm
# 3. Place name: ha noi

# enumerate() adds an index (number) to each item while looping.
# start=1 means the numbering begins at 1 instead of the default 0.
