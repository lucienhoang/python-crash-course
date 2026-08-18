from pathlib import Path

file_name = Path(
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/alice.txt"
)

try:
    with open(file_name, encoding="utf-8") as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    msg = f"Sorry, the file {file_name.name} does not exist."
    print(msg)

else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_name.name} has about {num_words} words.")

# The file alice.txt has about 2093 words.
