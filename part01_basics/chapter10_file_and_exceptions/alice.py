file_name = "alice.py"

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file {file_name} does not exist."
    print(msg)

# Sorry, the file alice.py does not exist.
