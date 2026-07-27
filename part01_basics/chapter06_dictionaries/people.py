person_0 = {"first_name": "Le", "last_name": "Dung", "age": 22, "city": "Ha Noi"}
person_1 = {
    "first_name": "Khoa",
    "last_name": "Hoang",
    "age": 27,
    "city": "Ho Chi Minh",
}
person_2 = {"first_name": "Luci", "last_name": "Liu", "age": 42, "city": "New York"}

people = [person_0, person_1, person_2]

for index, person in enumerate(people, start=1):
    print(f"{index}.")
    full_name = person["first_name"] + " " + person["last_name"]
    age = person["age"]
    city = person["city"]

    print(f"\t Fullname: {full_name}")
    print(f"\t Age: {age}")
    print(f"\t City: {city}")

# 1.
#          Fullname: Le Dung
#          Age: 22
#          City: Ha Noi
# 2.
#          Fullname: Khoa Hoang
#          Age: 27
#          City: Ho Chi Minh
# 3.
#          Fullname: Luci Liu
#          Age: 42
#          City: New York
