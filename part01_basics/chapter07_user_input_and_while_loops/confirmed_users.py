unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:  # Run as long as the unconfirmed_users is not empty
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice

# The following users have been confirmed:
# Candace
# Brian
# Alice
