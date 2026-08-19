import json

filename = "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/favorite_number.json"

with open(filename) as f_obj:
    favorite_number = json.load(f_obj)

print(f"I know your favorite number! It is {favorite_number}.")

# I know your favorite number! It is 7.
