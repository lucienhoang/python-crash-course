file_name = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/programming.txt"
)

# with open(file_name, "w") as file_object:
#     file_object.write("I love programming!\n")
#     file_object.write("I love creating new games!\n")

with open(file_name, "a") as file_object:
    file_object.write(
        "I enjoy turning small everyday frustrations into simple software.\n"
    )
    file_object.write("Pray for me ^^\n")
