def build_person(first_name, last_name, age=""):
    """Return a dictionary of information about  a person"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("khoa", "hoang")
print(musician)
# {'first': 'khoa', 'last': 'hoang'}

musician = build_person("khoa", "hoang", age=27)
print(musician)
# {'first': 'khoa', 'last': 'hoang', 'age': 27}
