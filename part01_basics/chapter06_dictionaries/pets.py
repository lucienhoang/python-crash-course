spike = {"name": "spike", "owner": "dung", "kind": "dog"}
tom = {"name": "tom", "owner": "khoa", "kind": "cat"}
jerry = {"name": "jerry", "owner": "laurence", "kind": "mouse"}

pets = [spike, tom, jerry]

for index, pet in enumerate(pets, start=1):
    print(
        f"{index}. {pet['name'].title()} is a {pet['kind']} living with {pet['owner'].title()}"
    )

# 1. Spike is a dog living with Dung
# 2. Tom is a cat living with Khoa
# 3. Jerry is a mouse living with Laurence
