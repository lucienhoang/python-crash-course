import json

prompt = "What is your favorite number? "
favorite_number = input(prompt)
#  favorite_number = int(input(prompt))

filename = "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/favorite_number.json"

with open(filename, "w") as f_obj:
    json.dump(favorite_number, f_obj)
