import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.


def get_stored_username():
    """Get stored username if available."""
    filename = "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username


def verify_user():
    """Verify that the current user is the stored user."""
    correct_username = get_stored_username()

    if correct_username:
        prompt = f"Is '{correct_username}' your username? - (y/n) "
        answer = input(prompt)

        if answer == "y":
            return correct_username
    return get_new_username()


def greet_user():
    """Greet the user by name."""
    username = verify_user()
    if username:
        print(f"Welcome back, {username}!")


greet_user()

# What is your name? luci
# Welcome back, luci!

# Is 'luci' your username? - (y/n) n
# What is your name? khoa
# Welcome back, khoa!
