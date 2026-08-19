import json

filename = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/username.json"
)

with open(filename) as f_obj:
    username = json.load(f_obj)
    print(f"Welcome back, {username}!")
