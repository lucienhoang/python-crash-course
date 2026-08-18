file_name = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/guest_book.txt"
)

prompt = "Enter your name (or press Enter to quit):"

while True:
    name = input(prompt)

    if name == "":
        break

    print(f"Hello {name.title()} ^^")
    with open(file_name, "a") as object_file:
        object_file.write(f"{name.title()} visited.\n")
