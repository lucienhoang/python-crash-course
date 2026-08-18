file_name = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/guest.txt"
)

prompt = "Enter your name: "
name = input(prompt)

with open(file_name, "w") as object_file:
    object_file.write(name)
