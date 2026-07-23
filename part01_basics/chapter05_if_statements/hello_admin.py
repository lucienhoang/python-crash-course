# users = ["luci", "admin", "khoa", "dung"]
users = []

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, are u still single?")
        else:
            print("Hi " + user.title() + "!")
else:
    print("We need to find some user.")

# We need to find some user.

current_users = ["luci", "admin", "khoa", "dung", "laurence"]
new_users = ["lucie", "thao", "vy", "dung", "boi"]

for new_user in new_users:
    if new_user in current_users:
        print(new_user.title() + " is already taken. You need to Enter a neew user!")
    else:
        print("The username " + new_user.title() + " is available")

# The username Lucie is available
# The username Thao is available
# The username Vy is available
# Dung is already taken. You need to Enter a neew user!
# The username Boi is available
