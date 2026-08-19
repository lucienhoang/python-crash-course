import json

filename = "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/favorite_number.json"

try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)

except FileNotFoundError:
    prompt = "What is your favorite number? "
    favorite_number = input(prompt)

    with open(filename, "w") as f_obj:
        json.dump(favorite_number, f_obj)

else:
    print(f"I know your favorite number! It is {favorite_number}.")


# PS D:\python-crash-course> python -u "d:\python-crash-course\part01_basics\chapter10_file_and_exceptions\10_12_favorite_number_remembered.py"
# What is your favorite number? 7
# PS D:\python-crash-course> python -u "d:\python-crash-course\part01_basics\chapter10_file_and_exceptions\10_12_favorite_number_remembered.py"
# I know your favorite number! It is 7.
