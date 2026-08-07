def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["luci", "hana", "margot"]
greet_users(usernames)

# Hello, Luci!
# Hello, Hana!
# Hello, Margot!
