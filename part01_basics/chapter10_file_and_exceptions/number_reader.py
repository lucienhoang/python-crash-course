# Using json.dump() and json.load()
import json

file_name = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/numbers.json"
)
with open(file_name) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# [2, 3, 5, 7, 11, 13]
