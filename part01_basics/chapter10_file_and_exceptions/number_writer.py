# Using json.dump() and json.load()

import json

numbers = [2, 3, 5, 7, 11, 13]

file_name = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/numbers.json"
)
with open(file_name, "w") as f_obj:
    json.dump(numbers, f_obj)
