from pathlib import Path

file_name = Path(
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/file_text/happy.txt"
)

with open(file_name, encoding="utf-8") as obj_file:
    contents = obj_file.read()


print(contents.lower().count("the"))
