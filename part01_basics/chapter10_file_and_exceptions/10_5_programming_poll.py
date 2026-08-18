file_name = "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/programming_poll.txt"

prompt = "Enter your name (or press Enter to quit): "
prompt_reason = "Enter a reason why you like programming (or press Enter to quit): "

while True:
    name = input(prompt)

    if name == "":
        break

    reason = input(prompt_reason)

    if reason == "":
        break

    print(f"Hello {name.title()} ^^")
    with open(file_name, "a") as object_file:
        object_file.write(f"{name.title()}'s reason: {reason}\n")
