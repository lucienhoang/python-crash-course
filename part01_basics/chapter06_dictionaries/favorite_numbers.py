favorite_numbers = {"khoa": [13, 7, 10], "dung": [4, 2, 5], "laurence": [7, 9, 1]}

for index, (names, numbers) in enumerate(favorite_numbers.items(), start=1):
    print(f"{index}. {names.title()} favorite number ares:")
    for number in numbers:
        print(f"\t{number}")

# 1. Khoa favorite number ares:
#         13
#         7
#         10
# 2. Dung favorite number ares:
#         4
#         2
#         5
# 3. Laurence favorite number ares:
#         7
#         9
#         1
