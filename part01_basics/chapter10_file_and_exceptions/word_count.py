from pathlib import Path


def count_words(filename):
    """Count the approximate number of words in the file"""
    try:
        file_name = Path(filename)
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


filenames = [
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/alice.txt",
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/siddhartha.txt",
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/moby_dick.txt",
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/little_women.txt",
]

for filename in filenames:
    count_words(filename)

# The file alice.txt has about 2093 words.
# Sorry, the file siddhartha.txt does not exist.
# The file moby_dick.txt has about 2190 words.
# The file little_women.txt has about 4099 words.
