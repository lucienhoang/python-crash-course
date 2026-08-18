# Count the occurrences of "the" in the file, ignoring case
from pathlib import Path

file_name = Path(
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/file_text/happy.txt"
)

with open(file_name, encoding="utf-8") as obj_file:
    contents = obj_file.read()

number = contents.lower().count("the")
print(f"The word 'the' appears {number} times in {file_name.name}.")

# The word 'the' appears 367 times in happy.txt.
